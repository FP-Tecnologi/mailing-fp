# Revisa los mailings antes de enviarlos: imágenes que existan en assets/, alt/width, peso, baja y WhatsApp.
# Uso: python herramientas/verificar-mailing.py [archivo.html ...]   (sin argumentos revisa mailings/ y plantillas/)
import re, os, sys, glob
from urllib.parse import unquote

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
CDN = 'https://cdn.jsdelivr.net/gh/FP-Tecnologi/mailing-producto@main/assets/'

def revisar(html, nombre=''):
    errores = []
    if len(html.encode('utf-8')) > 100 * 1024: errores.append('pesa más de 100 KB (Gmail lo corta a los 102 KB)')
    if 'data:image' in html: errores.append('tiene imágenes en base64')
    if '[ENLACE_BAJA]' not in html and 'baja' not in html.lower(): errores.append('falta el enlace de baja')
    if not re.search(r'name="viewport"', html): errores.append('falta meta viewport')
    for img in re.findall(r'<img\b[^>]*>', html, re.S):
        src = (re.search(r'src="([^"]+)"', img) or [None, ''])[1]
        if 'alt=' not in img: errores.append('imagen sin alt: ' + src)
        if 'width=' not in img: errores.append('imagen sin width: ' + src)
        if re.search(r'\.(webp|svg)(\?|$)', src, re.I): errores.append('formato no compatible con Outlook: ' + src)
        if src.startswith(CDN):
            if not os.path.exists(os.path.join(root, 'assets', unquote(src[len(CDN):]))): errores.append('imagen no existe en assets/: ' + src)
        elif src and not src.startswith('['):
            errores.append('imagen fuera del repo (puede romperse): ' + src)
    for url in re.findall(r'href="(https://wa\.me/[^"]*)"', html):
        if not re.match(r'https://wa\.me/\d{11,15}(\?text=[^\s&"]+)?$', url): errores.append('enlace de WhatsApp mal formado: ' + url)
    return errores

if __name__ == '__main__':
    assert revisar('<meta name="viewport"><img src="x.webp">baja') == ['imagen sin alt: x.webp', 'imagen sin width: x.webp', 'formato no compatible con Outlook: x.webp', 'imagen fuera del repo (puede romperse): x.webp']
    assert revisar('<meta name="viewport">baja<a href="https://wa.me/51960951976?text=Hola%20a">') == []
    archivos = sys.argv[1:] or glob.glob(os.path.join(root, 'mailings', '*', '*.html')) + glob.glob(os.path.join(root, 'plantillas', '*.html'))
    total = 0
    for f in archivos:
        errores = revisar(open(f, encoding='utf-8').read())
        total += len(errores)
        print(('OK    ' if not errores else 'REVISAR ') + os.path.relpath(f, root))
        for e in errores: print('   - ' + e)
    sys.exit(1 if total else 0)

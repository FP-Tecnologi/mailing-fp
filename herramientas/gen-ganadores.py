# Genera los 4 correos de ganadores del sorteo (3 individuales + 1 conjunto) en mailings/2026-10-ganadores-sorteo/.
# Uso: python herramientas/gen-ganadores.py   (editar la lista W para cambiar ganadores)
import os
import urllib.parse as u

CDN = 'https://cdn.jsdelivr.net/gh/FP-Tecnologi/mailing-producto@main/assets/campanas/2026-10-ganadores-sorteo/'
W = [('Roosevelt Torres', 'roosevelt-torres'), ('Doris Prado Castañeda', 'doris-prado'), ('Romel Leyva', 'romel-leyva')]
BLUE, DARK = '#2181AF', '#155382'
STEPS = ['Responde a este correo para coordinar el recojo.', 'Te confirmaremos el lugar, la fecha y el horario de entrega.']


def btns(msg):
    wa = 'https://wa.me/51960951976?text=' + u.quote(msg)
    mail = 'mailto:marketing@fptecnologi.com?subject=' + u.quote('Recojo de mi mochila Dell')
    return f'''<table role="presentation" class="button-table" cellpadding="0" cellspacing="0" border="0" align="center"><tr>
<td align="center" bgcolor="#ffffff" style="background:#ffffff;border-radius:8px;mso-padding-alt:14px 26px;"><a href="{mail}" target="_blank" class="button" style="display:inline-block;padding:14px 26px;font-size:15px;line-height:18px;font-weight:700;color:{DARK};text-decoration:none;border-radius:8px;">Responder por correo</a></td>
<td width="12" class="gap">&nbsp;</td>
<td align="center" bgcolor="#25D366" style="background:#25D366;border-radius:8px;mso-padding-alt:14px 26px;"><a href="{wa}" target="_blank" class="button" style="display:inline-block;padding:14px 26px;font-size:15px;line-height:18px;font-weight:700;color:#0b3d1f;text-decoration:none;border-radius:8px;">Escribir por WhatsApp</a></td>
</tr></table>'''


def page(title, pre, headline, sub, prize, msg, winners=None):
    cards = ''
    if winners:
        rows = ''.join(
            f'<tr><td style="padding:5px 0;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#eaf4fa" style="background:#eaf4fa;border:1px solid #cfe3ef;border-radius:10px;border-collapse:separate;"><tr><td width="52" align="center" style="padding:14px 0 14px 14px;font-size:24px;font-weight:800;color:{BLUE};">{i}</td><td style="padding:14px 18px 14px 6px;font-size:19px;line-height:24px;font-weight:700;color:{DARK};">{n}</td></tr></table></td></tr>'
            for i, (n, _) in enumerate(winners, 1))
        cards = f'<tr><td class="pad" style="padding:6px 36px 4px 36px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{rows}</table></td></tr>'
    st = ''.join(
        f'<tr><td width="40" valign="top" style="padding:7px 0;"><table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr><td width="32" height="32" align="center" bgcolor="#ffffff" style="background:#ffffff;border-radius:16px;font-size:16px;font-weight:800;color:{BLUE};">{i}</td></tr></table></td><td valign="middle" style="padding:7px 0;font-size:15px;line-height:22px;color:#ffffff;">{t}</td></tr>'
        for i, t in enumerate(STEPS, 1))
    return f'''<!DOCTYPE html>
<html lang="es" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="x-apple-disable-message-reformatting">
<meta name="color-scheme" content="light only">
<meta name="supported-color-schemes" content="light only">
<title>{title}</title>
<!--[if mso]>
<style>* {{ font-family:Arial,Helvetica,sans-serif !important; }}</style>
<![endif]-->
<style>
  body {{ margin:0 !important; padding:0 !important; width:100% !important; background:#e8f1f7; font-family:Arial,Helvetica,sans-serif; color:#16324a; }}
  table {{ border-collapse:collapse; border-spacing:0; }}
  img {{ display:block; border:0; outline:none; text-decoration:none; }}
  a {{ text-decoration:none; }}
  @media only screen and (max-width:640px) {{
    .container {{ width:100% !important; }}
    .pad {{ padding-left:20px !important; padding-right:20px !important; }}
    .title {{ font-size:30px !important; line-height:36px !important; }}
    .button-table, .button-table td {{ width:100% !important; }}
    .button {{ display:block !important; }}
    .gap {{ display:block !important; height:10px !important; width:100% !important; }}
    .logo-fp {{ width:140px !important; height:auto !important; }}
    .logo-dell {{ width:130px !important; height:auto !important; }}
  }}
</style>
</head>
<body style="margin:0;padding:0;background:#e8f1f7;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#e8f1f7">
<tr><td align="center" style="padding:24px 12px;">
<table role="presentation" class="container" width="640" cellpadding="0" cellspacing="0" border="0" bgcolor="#ffffff" style="width:640px;max-width:640px;background:#ffffff;border-radius:16px;overflow:hidden;box-shadow:0 8px 30px rgba(21,83,130,.15);">

<tr><td style="display:none!important;visibility:hidden;opacity:0;color:transparent;height:0;width:0;overflow:hidden;mso-hide:all;font-size:1px;line-height:1px;">{pre}</td></tr>

<tr><td bgcolor="{BLUE}" style="height:8px;background:{BLUE};font-size:0;line-height:0;">&nbsp;</td></tr>

<!-- Logos -->
<tr><td class="pad" style="padding:22px 36px 6px 36px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
<td width="50%" align="center" valign="middle" style="padding-right:12px;border-right:1px solid #c9dbe8;"><img class="logo-fp" src="{CDN}logo-fp-color.png" width="230" alt="FP Tecnologi &amp; System" style="width:230px;height:auto;"></td>
<td width="50%" align="center" valign="middle" style="padding-left:12px;"><img class="logo-dell" src="{CDN}logo-dell-titanium.png" width="210" alt="Dell Technologies Titanium Partner" style="width:210px;height:auto;"></td>
</tr></table></td></tr>

<!-- Confeti -->
<tr><td style="font-size:0;line-height:0;"><img src="{CDN}confeti-arriba-v2.jpg" width="640" alt="" style="width:100%;max-width:640px;height:auto;"></td></tr>

<!-- Titular -->
<tr><td class="pad" align="center" style="padding:18px 36px 4px 36px;">
<div style="font-size:13px;font-weight:700;letter-spacing:2px;color:{BLUE};text-transform:uppercase;">&#127881; Resultado del sorteo &#127881;</div>
{headline}
<p style="margin:0;font-size:16px;line-height:24px;color:#4a6378;">{sub}</p>
</td></tr>
{cards}
<!-- Premio -->
<tr><td class="pad" align="center" style="padding:14px 36px 8px 36px;">
<div style="font-size:22px;line-height:28px;font-weight:800;color:{DARK};">{prize}</div>
<img src="{CDN}mochila-dell.jpg" width="300" alt="Mochila Dell EcoLoop Essential" style="width:300px;max-width:100%;height:auto;margin:10px auto 0 auto;">
</td></tr>

<!-- Cómo recoger -->
<tr><td class="pad" style="padding:10px 28px 8px 28px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{BLUE}" style="background:{BLUE};border-radius:16px;border-collapse:separate;">
<tr><td align="center" style="padding:24px 24px 6px 24px;font-size:22px;line-height:28px;font-weight:800;color:#ffffff;">¿Cómo recoger tu premio?</td></tr>
<tr><td style="padding:6px 28px 8px 28px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{st}</table></td></tr>
<tr><td align="center" style="padding:14px 24px 26px 24px;">{btns(msg)}</td></tr>
</table></td></tr>

<tr><td align="center" style="padding:20px 36px 26px 36px;font-size:16px;line-height:24px;font-weight:700;color:{DARK};">¡Gracias por ser parte de esta experiencia!</td></tr>

<tr><td style="font-size:0;line-height:0;"><img src="{CDN}confeti-abajo-v2.jpg" width="640" alt="" style="width:100%;max-width:640px;height:auto;"></td></tr>

<!-- Footer -->
<tr><td class="pad" align="center" bgcolor="{DARK}" style="padding:24px 36px 26px 36px;background:{DARK};">
<div style="font-size:15px;font-weight:700;color:#ffffff;">FP Tecnologi &amp; System S.A.C.</div>
<div style="font-size:12px;line-height:20px;color:#cfe3ef;margin-top:6px;">Gerencia de Marketing y Publicidad<br>
<a href="mailto:marketing@fptecnologi.com" style="color:#ffffff;">marketing@fptecnologi.com</a> &nbsp;|&nbsp;
<a href="https://wa.me/51960951976" style="color:#ffffff;">+51 960 951 976</a> &nbsp;|&nbsp;
<a href="https://www.fptecnologi.com" style="color:#ffffff;">www.fptecnologi.com</a></div>
<div style="font-size:11px;line-height:17px;color:#a9c8dc;margin-top:12px;">Si no deseas recibir más información, <a href="[ENLACE_BAJA]" style="color:#ffffff;text-decoration:underline;">solicita la baja aquí</a>.</div>
</td></tr>

</table></td></tr></table>
</body>
</html>
'''


out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'mailings', '2026-10-ganadores-sorteo')
os.makedirs(out, exist_ok=True)


def save(name, html):
    with open(os.path.join(out, name), 'w', encoding='utf-8') as f:
        f.write(html)


for n, slug in W:
    h = f'<h1 class="title" style="margin:10px 0 12px 0;font-size:38px;line-height:44px;color:#16324a;">¡Felicidades,<br><span style="color:{BLUE};">{n}</span>!</h1>'
    save(f'ganador-{slug}.html', page(
        f'¡Felicidades, {n}! Ganaste una mochila Dell | FP Tecnologi & System',
        'Gracias por participar en nuestro sorteo: ¡ganaste una mochila Dell! Responde este correo para coordinar el recojo.',
        h, 'Gracias por participar en nuestro sorteo.', '¡Ganaste una mochila Dell!',
        f'Hola, soy {n}, ganador(a) de la mochila Dell. Quiero coordinar el recojo.'))

h = f'<h1 class="title" style="margin:10px 0 12px 0;font-size:36px;line-height:42px;color:#16324a;">¡Felicidades a nuestros <span style="color:{BLUE};">3 ganadores</span>!</h1>'
save('ganadores-los-3.html', page(
    '¡Felicidades a los ganadores del sorteo! Mochila Dell | FP Tecnologi & System',
    'Roosevelt Torres, Doris Prado Castañeda y Romel Leyva ganaron una mochila Dell. Responde este correo para coordinar el recojo.',
    h, 'Gracias a todos por participar en nuestro sorteo. Estos son los ganadores:', 'Cada uno ganó una mochila Dell',
    'Hola, soy ganador(a) de la mochila Dell. Quiero coordinar el recojo.', W))

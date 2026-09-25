# Checklist antes de enviar un mailing

Revisar **cada mailing** con esta lista antes del envío masivo. Si un punto falla, no se envía.

## 1. Revisión automática

```bash
python herramientas/verificar-mailing.py mailings/<campaña>/<archivo>.html
```

Debe decir `OK`. Revisa que todas las imágenes existan en `assets/`, que tengan `alt` y `width`, que no haya base64, WebP ni SVG, que el HTML pese menos de 100 KB, que exista el enlace de baja y que los enlaces de WhatsApp estén bien escritos.

## 2. Imágenes que no se rompen

- [ ] Todas las imágenes salen de este repositorio: `https://cdn.jsdelivr.net/gh/FP-Tecnologi/mailing-producto@main/assets/...`. **Nunca** enlazar imágenes de otras webs (se borran o bloquean el enlace) ni de i.ibb.co u otros hostings gratuitos.
- [ ] El repositorio es público y el commit con las imágenes ya se subió (`git push`) **antes** de enviar la prueba.
- [ ] JPG para fotos, PNG para logos e íconos. Foto principal de 1280 px de ancho como máximo y menos de 250 KB.
- [ ] Cada `<img>` tiene `alt`, `width` y `height:auto`. Si la imagen no carga, el texto alternativo explica qué había.
- [ ] Las imágenes de fondo también llevan `bgcolor`, y el texto se lee sobre ese color (Outlook no muestra la imagen).
- [ ] No reemplazar una imagen ya enviada con el mismo nombre: usar `nombre-v2.jpg`.

## 3. Íconos

- [ ] Los íconos son **PNG** generados desde [Tabler Icons](https://tabler.io/icons) (librería pública, licencia MIT) con `herramientas/generar-iconos.js`.
- [ ] **No usar** fuentes de íconos (Font Awesome, Material Icons, Bootstrap Icons) ni SVG en línea: Gmail y Outlook los eliminan y el ícono sale vacío o como un cuadrado.
- [ ] El texto se entiende aunque los íconos no carguen (los íconos decorativos llevan `alt=""`).

## 4. Responsivo y compatible

- [ ] Ancho de 640 px; en celular las columnas con `class="stack"` pasan a una sola columna.
- [ ] Diseño con tablas `role="presentation"` y estilos en línea; fuente Arial.
- [ ] Botones hechos con una tabla que lleva `bgcolor` y `mso-padding-alt` (se ven en Outlook), con el enlace o número escrito debajo como respaldo.
- [ ] El diseño se ve bien sin esquinas redondeadas ni sombras (Outlook de escritorio no las muestra).
- [ ] Solo colores de la paleta FP: `#2181AF`, `#155382`, `#1C6587`, `#18778B`, `#208497`. Sin amarillo.

## 5. Enlaces y WhatsApp

- [ ] Formato: `https://wa.me/51XXXXXXXXX?text=<mensaje codificado>`. El número va con código de país, sin `+`, espacios ni guiones.
- [ ] El mensaje está codificado para URL (espacio `%20`, `&` `%26`, `á` `%C3%A1`, `¿` `%C2%BF`). Para codificarlo:
  `python -c "from urllib.parse import quote; print(quote('Hola Anthony, ...', safe=''))"`
- [ ] Se hizo clic en el botón desde la computadora **y** desde el celular: abre WhatsApp con el mensaje ya escrito.
- [ ] No quedan textos entre `[corchetes]` sin reemplazar (`[Nombre del contacto]`, `[ENLACE_BAJA]`, `[fecha]`…).
- [ ] El enlace de baja funciona.

## 6. Prueba real

Enviarse una prueba y revisarla en:

- [ ] Gmail web (computadora)
- [ ] Gmail app (Android o iPhone)
- [ ] Outlook de escritorio (Windows)
- [ ] Outlook web / Microsoft 365
- [ ] Apple Mail o Mail de iPhone, si hay destinatarios con iPhone

En cada uno: imágenes cargan, textos no se cortan, botones se pueden tocar con el dedo y abren el enlace correcto.

# Mailing FP Tecnologi & System

Repositorio central de los mailings (correos HTML) de FP Tecnologi & System, junto con las imágenes que usan.

## Estructura

```
assets/                     Imágenes públicas que cargan los correos
  marca/                    Logos y material de FP
  iconos/{blanco,cian,dorado}/
  eventos/<evento-año>/     Material de cada evento (logos, banners)
mailings/
  AAAA-MM-nombre-campana/   Una carpeta por campaña, con sus .html
plantillas/
  base.html                 Punto de partida para un mailing nuevo
```

## Crear un mailing nuevo

1. Copiar `plantillas/base.html` a `mailings/AAAA-MM-nombre-campana/nombre.html`.
2. Reemplazar los textos entre `[corchetes]`.
3. Subir las imágenes nuevas a `assets/` y enlazarlas con la URL del CDN (ver abajo).
4. Hacer commit y push a `main`.
5. Enviarse una prueba a Gmail y Outlook (computadora y celular) antes del envío masivo.

## Imágenes

Los correos cargan las imágenes desde este repositorio mediante jsDelivr:

```
https://cdn.jsdelivr.net/gh/FP-Tecnologi/mailing-producto@main/assets/<ruta>
```

Ejemplo: `https://cdn.jsdelivr.net/gh/FP-Tecnologi/mailing-producto@main/assets/marca/fp-logo-blanco.png`

Reglas:

- **El repositorio debe ser público**; si no, las imágenes no cargan en el correo.
- **Nunca incrustar imágenes en base64** (`data:image/...`): Gmail las bloquea y el correo supera los 102 KB, así que Gmail lo corta.
- **Formatos:** JPG para fotos y PNG para logos o íconos. No usar WebP ni SVG, porque Outlook no los muestra.
- **Tamaño:** imagen principal de 1280 px de ancho como máximo y menos de 250 KB. Siempre poner `alt`, `width` y `style="width:...;height:auto"`.
- **No reemplazar una imagen con el mismo nombre:** jsDelivr guarda en caché `@main` hasta 12 horas y los correos ya enviados cambiarían. Para una versión nueva, usar otro nombre (`banner-v2.jpg`).

## Reglas de HTML para correo

- Diseño con tablas (`role="presentation"`) y estilos en línea. El `<style>` del `<head>` es solo para los ajustes de celular.
- Ancho de 640 px. En celular se adapta con `@media (max-width:640px)`.
- Botones hechos con una tabla que lleva `bgcolor` y `mso-padding-alt`, para que se vean bien en Outlook.
- Fuente Arial. Debajo de cada botón importante, dejar el enlace escrito como respaldo.
- Outlook de escritorio no muestra esquinas redondeadas ni sombras; el diseño debe verse bien sin ellas.
- Mantener cada HTML por debajo de 100 KB.

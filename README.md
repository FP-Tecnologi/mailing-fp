# Mailing FP Tecnologi & System

Repositorio central de los mailings (correos HTML) de FP Tecnologi & System y de las imágenes que usan.

## Estructura

```
assets/                          Imágenes públicas que cargan los correos
  marca/                         Logos y material de FP
  iconos/lineal/{blanco,azul}/   Íconos de línea (Tabler, PNG 96 px)
  iconos/redes/                  LinkedIn, Facebook, Instagram, YouTube (blanco)
  iconos/{blanco,cian,dorado}/   Íconos de las propuestas de EXPOMINA
  eventos/<evento-año>/          Material de eventos
  campanas/<AAAA-MM-campana>/    Fotos de cada campaña
  plantillas/                    Imágenes de muestra con el tamaño recomendado
mailings/
  AAAA-MM-nombre-campana/        Una carpeta por campaña, con sus .html
plantillas/                      Modelos base, listos para copiar
herramientas/                    Scripts de apoyo (íconos)
```

## Plantillas

| Archivo | Para qué sirve |
|---|---|
| `01-invitacion-evento.html` | Ferias, congresos, desayunos, webinars: imagen principal, fecha, lugar, stand, 3 beneficios, 2 botones |
| `02-producto-promocion.html` | Lanzamientos y ofertas: producto con precio, 4 beneficios, ficha técnica, llamado a cotizar |
| `03-boletin-noticias.html` | Boletín mensual: noticia destacada, 2 noticias, agenda de eventos |
| `04-comunicado.html` | Avisos, políticas, saludos: texto, recuadro informativo y firma |
| `05-sorteo-dinamica.html` | Sorteos, encuestas y registros: premio, 3 pasos, botón, fecha |

Todas usan la paleta de FP, se adaptan a celular y tienen el mismo encabezado y pie de página.

## Paleta de marca

| Color | HEX | Pantone |
|---|---|---|
| Principal | `#2181AF` | 7468 C |
| Azul oscuro | `#155382` | 7692 C |
| Azul petróleo | `#1C6587` | 7698 C |
| Turquesa petróleo | `#18778B` | 7470 C |
| Azul turquesa claro | `#208497` | 7474 C |

## Crear un mailing nuevo

1. Copiar la plantilla adecuada a `mailings/AAAA-MM-nombre-campana/nombre.html`.
2. Reemplazar los textos entre `[corchetes]` y los enlaces (`[ENLACE]`, `[ENLACE_BAJA]`…).
3. Subir las fotos a `assets/campanas/AAAA-MM-nombre-campana/` y cambiar las URLs de las imágenes de muestra.
4. Hacer commit y push a `main`.
5. Enviarse una prueba a Gmail y Outlook (computadora y celular) antes del envío masivo.

## Imágenes

Los correos cargan las imágenes desde este repositorio mediante jsDelivr:

```
https://cdn.jsdelivr.net/gh/FP-Tecnologi/mailing-producto@main/assets/<ruta>
```

- **El repositorio debe ser público**; si no, las imágenes no cargan en el correo.
- **Nunca incrustar imágenes en base64** (`data:image/...`): Gmail las bloquea y corta los correos de más de 102 KB.
- **Formatos:** JPG para fotos y PNG para logos o íconos. No usar WebP ni SVG, porque Outlook no los muestra.
- **Tamaño:** foto principal de 1280 px de ancho como máximo y menos de 250 KB. Siempre poner `alt`, `width` y `height:auto`.
- **Después de enviar un correo, no reemplazar sus imágenes con el mismo nombre:** jsDelivr guarda en caché `@main` hasta 12 horas y los correos ya enviados cambiarían. Para una versión nueva, usar otro nombre (`banner-v2.jpg`).

## Íconos nuevos

Los íconos salen de [Tabler Icons](https://tabler.io/icons) (licencia MIT). Para agregar uno, busca su nombre en la web, agrégalo a la lista de `herramientas/generar-iconos.js` y ejecuta:

```bash
npm i sharp @tabler/icons
node herramientas/generar-iconos.js assets/iconos
```

## Vista previa local

Mientras una imagen todavía no está publicada, `python .preview/build.py` genera en `.preview/` copias con las imágenes incrustadas, solo para revisarlas en el navegador. Esa carpeta no se sube y **esas copias nunca se envían**.

## Reglas de HTML para correo

- Diseño con tablas (`role="presentation"`) y estilos en línea. El `<style>` del `<head>` es solo para los ajustes de celular (`.stack`, `.mobile-pad`, `.center-mobile`…).
- Ancho de 640 px. En celular, las columnas con `class="stack"` se ponen una debajo de otra.
- Botones hechos con una tabla que lleva `bgcolor` y `mso-padding-alt`, para que se vean bien en Outlook.
- Tablas con borde y esquinas redondeadas: agregar `border-collapse:separate`.
- Imágenes de fondo: poner también `bgcolor`, porque Outlook de escritorio solo muestra ese color.
- Fuente Arial. Debajo de cada botón importante, dejar el enlace escrito como respaldo.
- Outlook de escritorio no muestra esquinas redondeadas ni sombras; el diseño debe verse bien sin ellas.
- Incluir siempre el enlace de baja (`[ENLACE_BAJA]`).
- Mantener cada HTML por debajo de 100 KB.

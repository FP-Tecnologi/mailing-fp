// Renderiza íconos Tabler (MIT) a PNG para correo: 96 px (se muestran a 24–48 px).
const sharp = require('sharp'), fs = require('fs'), path = require('path');
const src = path.join(path.dirname(require.resolve('@tabler/icons/package.json')), 'icons');
const out = process.argv[2];
const lineal = ['device-desktop','hand-finger','camera','cpu','school','presentation','users-group',
  'presentation-analytics','settings','tool','users','chart-bar','calendar-event','chevron-right','devices','bulb','building-community'];
const colores = { blanco: '#ffffff', azul: '#2181AF' };
const redes = ['brand-linkedin','brand-facebook','brand-instagram','brand-youtube'];
(async () => {
  for (const [dir, hex] of Object.entries(colores)) {
    fs.mkdirSync(path.join(out, 'lineal', dir), { recursive: true });
    for (const n of lineal) {
      const svg = fs.readFileSync(path.join(src, 'outline', n + '.svg'), 'utf8').replace(/currentColor/g, hex).replace(/stroke-width="2"/, 'stroke-width="1.6"');
      await sharp(Buffer.from(svg), { density: 600 }).resize(96, 96).png().toFile(path.join(out, 'lineal', dir, n + '.png'));
    }
  }
  fs.mkdirSync(path.join(out, 'redes'), { recursive: true });
  for (const n of redes) {
    const svg = fs.readFileSync(path.join(src, 'filled', n + '.svg'), 'utf8').replace(/currentColor/g, '#ffffff');
    await sharp(Buffer.from(svg), { density: 600 }).resize(64, 64).png().toFile(path.join(out, 'redes', n.replace('brand-', '') + '.png'));
  }
})();

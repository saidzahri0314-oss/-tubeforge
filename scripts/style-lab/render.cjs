const { chromium } = require('playwright');
(async () => {
  const [,, svg, out, w, h, scale] = process.argv;
  const b = await chromium.launch();
  const p = await b.newPage({ viewport:{width:+w, height:+h}, deviceScaleFactor: +(scale||1) });
  await p.goto('file://' + svg);
  await p.screenshot({ path: out });
  await b.close();
})();

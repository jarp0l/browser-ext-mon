import puppeteer from 'puppeteer';
import path from 'path';

(async () => {
  const pathToExtension = path.join(process.cwd(), 'extensions', 'little-rat');
  const browser = await puppeteer.launch({
    headless: 'new',
    args: [
      `--disable-extensions-except=${pathToExtension}`,
      `--load-extension=${pathToExtension}`,
    ],
  });
  const backgroundPageTarget = await browser.waitForTarget(
    (target) => target.type() === 'background_page'
  );
  const backgroundPage = await backgroundPageTarget.page();
  const page = await browser.newPage();

  await page.goto('https://search.brave.com/');
  console.log('navigated to search.brave.com');

  await browser.close();
})();

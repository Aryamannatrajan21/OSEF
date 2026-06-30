import puppeteer from 'puppeteer';

(async () => {
  console.log('Launching browser...');
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();
  
  // Set a good viewport size
  await page.setViewport({ width: 1200, height: 800 });
  
  console.log('Navigating to OSEF Studio...');
  await page.goto('http://127.0.0.1:8000', { waitUntil: 'domcontentloaded' });
  
  // Click the Assistant tab
  console.log('Switching to Assistant tab...');
  // Assuming the tab is a button containing the text "Assistant"
  const tabs = await page.$$('button');
  for (const tab of tabs) {
    const text = await page.evaluate(el => el.textContent, tab);
    if (text && text.includes('Assistant')) {
      await tab.click();
      break;
    }
  }
  
  // Wait a moment for tab switch
  await new Promise(r => setTimeout(r, 1000));
  
  // Type a query in the chat input
  console.log('Typing query...');
  const input = await page.$('input[type="text"]');
  if (input) {
    await input.type('What are the main components of this architecture?');
    // Press Enter to send
    await input.press('Enter');
  }
  
  // Wait for the response (e.g. 10 seconds or until loading dot goes away)
  console.log('Waiting for response...');
  await new Promise(r => setTimeout(r, 15000));
  
  console.log('Taking screenshot...');
  await page.screenshot({ path: 'ai-assistant-screenshot.png' });
  
  await browser.close();
  console.log('Done!');
})();

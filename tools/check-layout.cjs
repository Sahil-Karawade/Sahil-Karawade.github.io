const {chromium} = require('C:/Users/Sahil Karawade/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async()=>{
 const browser = await chromium.launch({headless:true,channel:'msedge'});
 const page = await browser.newPage();
 const failures=[];
 for(const width of [1440,390]){
  await page.setViewportSize({width,height:1000});
  for(const route of ['/', '/about/','/research/','/projects/','/skills/','/businesses/','/articles/','/articles/your-mic-test-passed/','/contact/','/projects/n8n-job-notifier/','/Hartshorne-Solution.html','/primespectrum.html']){
   const response=await page.goto('http://127.0.0.1:4173'+route);
   if(response.status()!==200) failures.push(route+': '+response.status());
   const info=await page.evaluate(()=>({scroll:document.documentElement.scrollWidth,width:innerWidth,main:!!document.querySelector('main, .stackedit__html'),h1:document.querySelectorAll('h1').length}));
   if(info.scroll>info.width)failures.push(width+' '+route+': horizontal overflow '+info.scroll);
   if(route==='/')await page.screenshot({path:'tools/site-preview/home-'+width+'.png',fullPage:true});
   if(route==='/articles/your-mic-test-passed/'){
    await page.screenshot({path:'tools/site-preview/article-'+width+'.png',fullPage:true});
    if(await page.locator('.article-meta').innerText().then(text=>/Daniel|Krauss|Sahil/.test(text)))failures.push('Article author byline should be omitted');
    if(await page.locator('.article-body a[href="https://wavelocus.com/microphone-test"]').count()!==1)failures.push('Article contextual WaveLocus link missing');
   }
   if(['/','/research/'].includes(route)){
    if(await page.locator('a[href$="/folder/CV.pdf"]').count())failures.push('CV visible in production');
    if(/Master's Project|Course Catalog|Notes from Papers and Text/.test(await page.locator('#main').innerText()))failures.push('Removed section still visible');
   }
  }
 }
 await page.goto('http://127.0.0.1:4173/contact/');
 if(await page.locator('form#contact-form [required]').count()!==3)failures.push('Contact required fields');
 await browser.close();
 if(failures.length)throw Error(failures.join('\n'));
 console.log('PASS: 12 routes at desktop and mobile widths; hidden CV, removed sections, article byline and contextual link verified.');
})().catch(error=>{console.error(error.message);process.exitCode=1});

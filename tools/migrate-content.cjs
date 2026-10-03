const fs = require('fs');
const path = require('path');
const Module = require('module');
const source = 'C:/Users/Sahil Karawade/Personal-Website/interactive-torus-portfolio';
const sourceRequire = Module.createRequire(path.join(source, 'package.json'));
const ts = sourceRequire('typescript');
const React = sourceRequire('react');
const {renderToStaticMarkup} = sourceRequire('react-dom/server');
const targets = [
 ['about/page1.tsx', 'about', 'About Me'],
 ['contact/page2.tsx', 'contact', 'Contact'],
 ['skills/page7.tsx', 'skills', 'Skills & Expertise'],
 ['projects/chinese-chess-ai/page5.tsx', 'projects/chinese-chess-ai', 'Chinese Chess AI Engine'],
 ['projects/n8n-job-notifier/page6.tsx', 'projects/n8n-job-notifier', 'Automated Job Alert System'],
 ['projects/options-strategy/page8.tsx', 'projects/options-strategy', 'Options Strategy Classification'],
 ['projects/asset-allocation/page4.tsx', 'projects/asset-allocation', 'Quantitative Asset Allocation'],
];
fs.mkdirSync('tools/rendered', {recursive:true});
for (const [file, route, title] of targets) {
 const input = fs.readFileSync(path.join(source, 'app', file), 'utf8');
 const js = ts.transpileModule(input, {compilerOptions:{jsx:ts.JsxEmit.ReactJSX,module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2020}}).outputText;
 const mod = {exports:{}};
 const customRequire = id => id === 'next/navigation' ? {useRouter:()=>({push:()=>{}})} : sourceRequire(id);
 new Function('require','module','exports',js)(customRequire,mod,mod.exports);
 const html = renderToStaticMarkup(React.createElement(mod.exports.default));
 fs.writeFileSync('tools/rendered/'+route.replaceAll('/','--')+'.html', html);
}
const projectSource = fs.readFileSync(path.join(source,'app/projects/page3.tsx'),'utf8');
const data = new Function('return '+projectSource.match(/const projects = (\[[\s\S]*?\n\])/)[1])();
fs.writeFileSync('tools/rendered/projects.json',JSON.stringify(data,null,2));
console.log('Rendered all seven content pages and five project entries from original source.');

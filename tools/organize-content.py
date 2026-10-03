from pathlib import Path
import json, re, html
from bs4 import BeautifulSoup

root = Path(__file__).resolve().parent.parent
rendered = root / 'tools/rendered'
for source in rendered.glob('*.html'):
    route = source.stem.replace('--', '/')
    soup = BeautifulSoup(source.read_text(encoding='utf-8'), 'html.parser')
    title = soup.h1.get_text(' ', strip=True)
    original_text = soup.get_text(' ', strip=True)
    for el in soup.select('svg, style'):
        el.decompose()
    for el in list(soup.find_all(True)):
        classes = ' '.join(el.get('class', []))
        if 'fixed inset-0' in classes or 'absolute inset-0' in classes:
            el.decompose()
            continue
        if 'flex-wrap' in classes:
            el['class'] = 'skill-items'
        elif 'class' in el.attrs:
            del el['class']
        el.attrs.pop('style', None)
        el.attrs.pop('target', None)
    for button in list(soup.find_all('button')):
        if button.get_text(strip=True) == 'Back':
            button.decompose()
        elif button.get_text(strip=True) == 'Get in Touch':
            button.name = 'a'
            button['href'] = '/contact/'
    # Header taglines are intentionally omitted per the requested UI direction.
    for header in soup.find_all('header'):
        for p in header.find_all('p', recursive=False):
            p.decompose()
        for div in header.find_all('div', recursive=False):
            for p in div.find_all('p', recursive=False):
                p.decompose()
    soup.main.name = 'div'
    soup.div['class'] = 'migrated-content'
    if route == 'about':
        research_heading = soup.find('h2', string='Research Interests')
        if research_heading:
            research_heading.string = 'Additional Background'
    if route == 'contact':
        form = soup.find('input', {'id': 'name'}).parent.parent
        form.name = 'form'
        form['id'] = 'contact-form'
        form['action'] = 'mailto:sahilkarawade@outlook.com'
        form['method'] = 'post'
        form['enctype'] = 'text/plain'
        for name in ['name', 'email', 'message']:
            form.find(attrs={'name': name})['required'] = ''
        form.find('button')['type'] = 'submit'
        soup.append(BeautifulSoup('<script src="/assets/js/contact.js" defer></script>', 'html.parser'))
    output = root / (route + '.html')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text('---\nlayout: default\ntitle: '+json.dumps(title,ensure_ascii=False)+'\npermalink: /'+route+'/\n---\n'+str(soup)+'\n',encoding='utf-8')

projects = json.loads((rendered/'projects.json').read_text())
items = []
for project in projects:
    title = html.escape(project['title'])
    # The source has a Deutsch App entry but no detail page. Keep its text without a dead link.
    if project['id'] != 'deutsch-app':
        title = '<a href="/projects/'+project['id']+'/">'+title+'</a>'
    items.append('<li>'+title+'<p>'+html.escape(project['subtitle'])+'</p><p>'+html.escape(project['description'])+'</p></li>')
project_list = '<ul class="link-list project-list">\n'+'\n'.join(items)+'\n</ul>\n'
(root/'_includes/project-list.html').write_text(project_list,encoding='utf-8')
(root/'projects.html').write_text('---\ntitle: Projects\npermalink: /projects/\n---\n<h1>Projects</h1>\n{% include project-list.html %}\n',encoding='utf-8')

research = (root/'README.md').read_text(encoding='utf-8')
headings = {'List of Attended Conferences':'list-of-attended-conferences','Hartshorne Solution':'hartshorne-solution','Notes from Papers and Text':'notes-from-papers-and-text',"Master's Project":'masters-project','Course Catalog':'course-catalog'}
for heading, anchor in headings.items():
    research = re.sub(r'#### <ins>\s*'+re.escape(heading)+r'\s*</ins>', '<h2 id="'+anchor+'">'+heading+'</h2>', research)
research = research.split('<h2 id="masters-project">')[0].rstrip()+'\n'
research = research.replace('<h2 id="notes-from-papers-and-text">Notes from Papers and Text</h2>', '<span id="notes-from-papers-and-text" aria-hidden="true"></span>\n<h2 id="notes-from-papers">Notes from Papers</h2>')
research = research.replace('<ins> Here is my [CV](https://sahil-karawade.github.io/folder/CV.pdf) </ins>', '{% if site.show_cv %}\n<ins> Here is my [CV](https://sahil-karawade.github.io/folder/CV.pdf) </ins>\n{% endif %}')
(root/'research.md').write_text('---\ntitle: Mathematics\npermalink: /research/\n---\n# Mathematics\n\n'+research,encoding='utf-8')

for file in root.glob('*.html'):
    if file.name == 'google5b5d0f2081992c81.html' or file.read_text(encoding='utf-8').startswith('---'):
        continue
    text = file.read_text(encoding='utf-8')
    if file.name == 'primespectrum.html':
        text = re.sub(r'<head>[\s\S]*?</head>', '<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title> A Universe of Sorts </title><link rel="alternate" type="application/rss+xml" href="/feed.xml"><link rel="stylesheet" href="/assets/css/notes.css"></head>', text, count=1)
        file.write_text(text, encoding='utf-8')
    # Retain every existing article URL and all article content, including rendered mathematics.
    if '</head>' in text and '/assets/css/notes.css' not in text:
        text = text.replace('</head>', '<link rel="stylesheet" href="/assets/css/notes.css">\n</head>',1)
        text = re.sub(r'(<body[^>]*>)',r'\1\n<nav class="notes-nav" aria-label="Site navigation"><a href="/">Sahil Karawade</a><a href="/research/">Mathematics</a></nav>\n',text,count=1)
        file.write_text(text,encoding='utf-8')
print('Organized all migrated pages; original README retained; original note paths retained.')

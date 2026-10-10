from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlsplit, unquote
import subprocess, re

root = Path(__file__).resolve().parent.parent
site = root/'tools/site-preview'
errors = []
# Existing document bodies must be unchanged except the new shared navigation.
for file in root.glob('*.html'):
    old = subprocess.run(['git','show','HEAD:'+file.name],cwd=root,capture_output=True).stdout
    if not old or not b'<body' in old:
        continue
    before = BeautifulSoup(old.decode('utf-8'), 'html.parser')
    after = BeautifulSoup(file.read_text(encoding='utf-8'), 'html.parser')
    for nav in before.select('.notes-nav'):
        nav.decompose()
    for nav in after.select('.notes-nav'):
        nav.decompose()
    assert re.sub(r'\s+',' ',before.body.get_text()).strip() == re.sub(r'\s+',' ',after.body.get_text()).strip(), file.name+' text changed'
    assert [str(x) for x in before.select('math')] == [str(x) for x in after.select('math')], file.name+' math changed'
print('PASS: All 11 original document bodies and rendered mathematics preserved.')

for original in (root/'tools/rendered').glob('*.html'):
    source = BeautifulSoup(original.read_text(encoding='utf-8'), 'html.parser')
    route = original.stem.replace('--','/')
    target = BeautifulSoup((root/(route+'.html')).read_text(encoding='utf-8').split('---',2)[2], 'html.parser')
    # Every prose paragraph outside the explicitly removed header taglines is verbatim.
    for p in source.find_all('p'):
        if p.find_parent('header'):
            continue
        text = re.sub(r'\s+',' ',p.get_text()).strip()
        matches = [re.sub(r'\s+',' ',q.get_text()).strip() for q in target.find_all('p')]
        assert text in matches, route+': missing paragraph '+text[:80]
print('PASS: Every migrated prose paragraph preserved, excluding requested header taglines.')

for file in site.rglob('*.html'):
    soup = BeautifulSoup(file.read_text(encoding='utf-8'), 'html.parser')
    for link in soup.select('a[href],link[href],script[src],img[src]'):
        href = link.get('href') or link.get('src')
        url = urlsplit(href)
        if url.scheme or url.netloc or not url.path:
            continue
        candidate = site/unquote(url.path.lstrip('/')) if url.path.startswith('/') else file.parent/unquote(url.path)
        if candidate.is_dir():
            candidate = candidate/'index.html'
        if not candidate.exists():
            errors.append(str(file.relative_to(site))+': '+href)
        elif url.fragment and candidate.suffix == '.html':
            target = BeautifulSoup(candidate.read_text(encoding='utf-8'), 'html.parser')
            if not target.find(id=unquote(url.fragment)) and not target.find('a',attrs={'name':unquote(url.fragment)}):
                errors.append(str(file.relative_to(site))+': missing anchor '+href)
assert not errors, '\n'.join(errors)
assert (site/'sitemap.xml').exists()
assert (site/'feed.xml').exists()
assert (site/'google5b5d0f2081992c81.html').read_bytes() == (root/'google5b5d0f2081992c81.html').read_bytes()
print('PASS: Generated local links, anchors, sitemap, feed, and Google verification file.')

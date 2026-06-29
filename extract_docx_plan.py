import zipfile, re, os
from pathlib import Path

path = Path(r'c:/Work/Prj_33_Content_Factory/instagram_content_factory_no_api_architecture_v1_1.docx')
print('exists', path.exists())
with zipfile.ZipFile(path) as z:
    data = z.read('word/document.xml').decode('utf-8', errors='ignore')

text = re.sub(r'<[^>]+>', ' ', data)
text = re.sub(r'&[a-zA-Z]+;', ' ', text)
text = re.sub(r'\s+', ' ', text).strip()

for marker in ['план разработки', 'этапы', 'этап', 'roadmap', 'implementation', 'модуль', 'шаг']:
    idx = text.lower().find(marker.lower())
    if idx != -1:
        print('===', marker, '===')
        print(text[idx:idx+20000])
        break
else:
    print(text[:20000])

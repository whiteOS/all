from pathlib import Path
import json, requests

headers = {"userAgent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Mobile Safari/537.36 Edg/98.0.1108.50"}
cookies = Path('cookie.txt').read_text()
cookies = {x['name']: x['value'] for x in json.loads(cookies)}


r = requests.get(url = "http://yktfw.csust.edu.cn/PPage/ComePage", headers = headers, cookies = cookies)
print(r.text)
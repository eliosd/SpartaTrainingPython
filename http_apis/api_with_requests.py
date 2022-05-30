import requests
import json
from pprint import pprint

# pc_req = requests.get("https://api.postcodes.io/postcodes/SE12 0NB")
#
# print(pc_req, type(pc_req))
#
# if pc_req.status_code == 200:
#     # pprint(dict(pc_req.headers))
#     postcode = json.loads(pc_req.content)
#     result = postcode['result']
#     print(result["admin_district"])
#     print(result["eastings"], result["northings"])
#     print(result['codes']['nuts'])

headers = {'Content-Type': 'application/json'}
body = {'postcodes': ['SE12 0NB', 'E10 7BT']}

pc_req = requests.post(
    "https://api.postcodes.io/postcodes/",
    headers=headers,
    data=json.dumps(body)
)

# print(pc_req)
pcs = pc_req.json()['result']
pprint(pcs, sort_dicts=False)

for pc_data in pcs:
    result = pc_data['result']
    print('------',result["postcode"],'------')
    print(result["admin_ward"])
    print(result["eastings"], result["northings"])
    print(result['codes']['nuts'])


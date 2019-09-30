from collections import OrderedDict

import json

with open('data.json') as f:

  data = json.load(f)

print(json.dumps(data,indent=2))

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import sys 

```
test data:

[
  {
    "cpu": 16.52,
    "disk": 0,
    "id": "30",
    "instance": 22,
    "memory": 45056,
    "name": "backend"
  },
  {
    "cpu": 0.21,
    "disk": 0,
    "id": "57",
    "instance": 8,
    "memory": 8192,
    "name": "front"
  }
]
```

def main(filename):
  with open(filename, 'r') as f:
    data = json.loads(f.read())
    for item in data:
      print 'cpu: {}, memory: {}'.format(item['cpu'], item['memory'])

if __name__ == "__main__":
   main(sys.argv[1])

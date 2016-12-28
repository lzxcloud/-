#!/usr/bin/env python3
import json


with open('userdic2','r') as fp:
    udic = json.loads(fp.read())

for i in udic:
    print(udic[i])

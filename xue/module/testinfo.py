#!/usr/bin/env python3
import json
with open("userdic","r") as fb:
    a = json.loads(fb.read())



for i,j in enumerate(a) :
     print(i,a[j])


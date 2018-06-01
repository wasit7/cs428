# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 17:00:01 2014

@author: Wasit
"""

try:
    import json
except ImportError:
    import simplejson as json
import numpy as np
import base64

def Base64Encode(ndarray):
    return json.dumps([str(ndarray.dtype),base64.b64encode(ndarray),ndarray.shape])
def Base64Decode(jsonDump):
    loaded = json.loads(jsonDump)
    dtype = np.dtype(loaded[0])
    arr = np.frombuffer(base64.decodestring(loaded[1]),dtype)
    if len(loaded) > 2:
        return arr.reshape(loaded[2])
    return arr

a= np.random.random_sample((5, 7))

j1=json.dumps(Base64Encode(a))
f=open("data.json","w")
f.write(j1)
f.close()

f=open("data.json","r")

j2=json.loads(f.read())
f.close()
b=Base64Decode(j2)


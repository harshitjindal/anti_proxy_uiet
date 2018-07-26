# Train

import httplib, urllib, base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '135e49f7f9d24a2c808613544fd8ca3e',
}

params = urllib.urlencode({"largePersonGroupId": str(lpgi)})

data = {
    
}

try:
    conn = httplib.HTTPSConnection('centralindia.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/largepersongroups/{largePersonGroupId}/train?%s" % params, str(data), headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

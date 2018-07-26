#Add PersonID in LargePersonGroup ID

import httplib, urllib, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '135e49f7f9d24a2c808613544fd8ca3e',
}

params = urllib.urlencode({
    # Request parameters
    'largePersonGroupId': str(lpgi)),
    'personId': str(person_id),
})

#print(params)

data = {
    "url": "https://images-cdn.9gag.com/photo/6393392_700b.jpg"
}

try:
    conn = httplib.HTTPSConnection('centralindia.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/largepersongroups/{largePersonGroupId}/persons/{personId}/persistedfaces?%s" % params, str(data), headers)
    response = conn.getresponse()
    data = response.read()
    #print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

print

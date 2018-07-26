#Get name

import httplib, urllib, base64, json

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '135e49f7f9d24a2c808613544fd8ca3e',
}

params = urllib.urlencode({
    # Request parameters
    'largePersonGroupId': str(lpgi),
    'personId': str(person_id),
})

try:
    conn = httplib.HTTPSConnection('centralindia.api.cognitive.microsoft.com')
    conn.request("GET", "/face/v1.0/largepersongroups/{largePersonGroupId}/persons/{personId}?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    #print(data)
    persons_name = json.loads(data)
    person_name = persons_name["name"]
    print(person_name)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))


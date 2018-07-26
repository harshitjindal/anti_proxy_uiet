#create LargePersonGroup Person

import httplib, urllib, base64, json

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '135e49f7f9d24a2c808613544fd8ca3e',
}

params = urllib.urlencode({"largePersonGroupId": str(lpgi)})

data = {
    'name': raw_input("Please enter the name of the person you want to add: "),
    'userData': raw_input("Please enter the roll number of the respective person: ")
}


try:
    conn = httplib.HTTPSConnection('centralindia.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/largepersongroups/{largePersonGroupId}/persons?%s" % params, str(data), headers)
    response = conn.getresponse()
    data = response.read()
    #print(data)
    person_ID = json.loads(data)
    person_id = person_ID['personId']
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

print

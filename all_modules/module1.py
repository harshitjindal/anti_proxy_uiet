#create LargerPersonGroupID

import httplib, urllib, base64, json
lpgi = raw_input("Please enter the group ID: ")
headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '135e49f7f9d24a2c808613544fd8ca3e',
}

params = urllib.urlencode({"largePersonGroupId": str(lpgi)})

data = {
    'name': raw_input("Please enter the name of the group: "),
    'userData': raw_input("Please enter the batch: ")
}


try:
    conn = httplib.HTTPSConnection('centralindia.api.cognitive.microsoft.com')
    conn.request("PUT", "/face/v1.0/largepersongroups/{largePersonGroupId}?%s" % params, str(data), headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))


# Detect face

import httplib, urllib, base64, json

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '135e49f7f9d24a2c808613544fd8ca3e',
}

params = urllib.urlencode({
    # Request parameters
    'returnFaceId': 'true',
})



data = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/0/0a/ATC_Band.jpg"
}

face_id_arr = list()


try:
    conn = httplib.HTTPSConnection('centralindia.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/detect?%s" % params, str(data), headers)
    response = conn.getresponse()
    data = response.read()
    face_ID = json.loads(data)
    #print(face_ID)
    for j in face_ID:
        face_id_arr.append(j["faceId"])
        face_id = j["faceId"]
    #print(face_id_arr)
    #print(person_id)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
print

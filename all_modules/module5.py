# Detect face

import httplib, urllib, base64, json
lpgi = raw_input("Please enter the group ID: ")

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

#######################################################################

#Identify

import httplib, urllib, base64, json

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '135e49f7f9d24a2c808613544fd8ca3e',
}

params = urllib.urlencode({
})


faces = list()
for j in face_id_arr:
    faces.append(j)


data = {
    "largePersonGroupId": str(lpgi),
    "faceIds": [str(j) for j in faces],
    "maxNumOfCandidatesReturned": 10,
        "confidenceThreshold": 0.5}

try:
    conn = httplib.HTTPSConnection('centralindia.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/identify?%s" % params, str(data), headers)
    response = conn.getresponse()
    data = response.read()
    #print(data)
    identity = json.loads(data)
    #print(identity)
    for j in identity:
        ide_person = j["candidates"]
        #print(ide_person)
        if len(ide_person) > 0:
            identity_person = (ide_person[0]["personId"])
    #print(identity_person)
    #identity_person = identity['personId']
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

#######################################################################

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


#READ CSV ARCHIVE

import csv

array = []
array2 = []

with open('test.csv', 'rb') as File:
    reader = csv.DictReader(File)
    for row in reader:
        array.append(row['Tweet'])
        array2.append(row['Id'])

#CALL MEANINGCLOUD API - SENTIMENT

polarity_array = []
agreement_array = []
subjectivity_array = []
confidence_array = []
irony_array = []
error = []
key = "6b09f35eba67f4e3d406eae63cbe3c81"

import requests
import json

url = "https://api.meaningcloud.com/sentiment-2.1"
for x in range(0, 1500):

    try:
        payload = "key="+key+"&lang=auto&txt="+array[x]+"&txtf=plain&url=""&doc="""
        headers = {'content-type': 'application/x-www-form-urlencoded'}

        response = requests.request("POST", url, data=payload, headers=headers)

        decoded_json = json.loads(response.text)

        polarity_result = decoded_json["score_tag"]
        agreement_result = decoded_json["agreement"]
        subjectivity_result = decoded_json["subjectivity"]
        confidence_result = str(decoded_json["confidence"])
        irony_result = decoded_json["irony"]

        polarity_array.append(polarity_result)
        agreement_array.append(agreement_result)
        subjectivity_array.append(subjectivity_result)
        confidence_array.append(confidence_result)
        irony_array.append(irony_result)
        print "FINISH "+str(x)
    except KeyError:
        error.append(x)
        polarity_array.append("")
        agreement_array.append("")
        subjectivity_array.append("")
        confidence_array.append("")
        irony_array.append("")
        print "Not posible KEY_ERROR "+str(x)
    except UnicodeEncodeError:
        error.append(x)
        polarity_array.append("")
        agreement_array.append("")
        subjectivity_array.append("")
        confidence_array.append("")
        irony_array.append("")
        print "Not posible UNICODE_ENCODE_ERROR "+str(x)
    except ConnectionError:
        error.append(x)
        polarity_array.append("")
        agreement_array.append("")
        subjectivity_array.append("")
        confidence_array.append("")
        irony_array.append("")
        print "Not posible CONNECTION_ERROR "+str(x)

#WRITTE SENTIMENT ERROR TXT ARCHIVE

file = open("meaningcloud_errors.txt","w")

for a in error:
    file.write(str(a)+"\n")
file.close()

print("Writing 1 complete")
print(' ')
print(' ')

#CALL INDICO.IO EMOTION API

import indicoio
indicoio.config.api_key = 'ba420e48e2322e7e99b674c9d1d3a5d2'

anger_array = []
joy_array = []
fear_array = []
sadness_array = []
surprise_array = []
error2 = []

for y in range(0,1500):

    try:
        result = indicoio.emotion(array[y])

        data_string  = json.dumps(result)
        decoded_json = json.loads(data_string)

        anger_result = str(decoded_json["anger"]*100)
        joy_result = str(decoded_json["joy"]*100)
        fear_result = str(decoded_json["fear"]*100)
        sadness_result = str(decoded_json["sadness"]*100)
        surprise_result = str(decoded_json["surprise"]*100)

        anger_array.append(anger_result)
        joy_array.append(joy_result)
        fear_array.append(fear_result)
        sadness_array.append(sadness_result)
        surprise_array.append(surprise_result)
        print "FINISH "+str(y)

    except KeyError:
        error2.append(y)
        anger_array.append("")
        joy_array.append("")
        fear_array.append("")
        sadness_array.append("")
        surprise_array.append("")
        print "Not posible KEY_ERROR "+str(y)
    except UnicodeEncodeError:
        error2.append(y)
        anger_array.append("")
        joy_array.append("")
        fear_array.append("")
        sadness_array.append("")
        surprise_array.append("")
        print "Not posible UNICODE_ENCODE_ERROR "+str(y)
    except UnicodeDecodeError:
        error2.append(y)
        anger_array.append("")
        joy_array.append("")
        fear_array.append("")
        sadness_array.append("")
        surprise_array.append("")
        print "Not posible UNICODE_DECODE_ERROR "+str(y)
    except ConnectionError:
        error2.append(y)
        anger_array.append("")
        joy_array.append("")
        fear_array.append("")
        sadness_array.append("")
        surprise_array.append("")
        print "Not posible CONNECTION_ERROR "+str(y)

#WRITTE A FULL CSV ARCHIVE

with open('data.csv', 'wb') as csvfile:
    fieldnames = ['Tweet', 'Id', 'Polarity', 'Agreement', 'Subjectivity', 'Confidence', 'Irony', 'Anger', 'Joy', 'Fear', 'Sadness', 'Surprise']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for z in range(0, 1500):
        writer.writerow({'Tweet': array[z], 'Id': array2[z], 'Polarity':polarity_array[z], 'Agreement':agreement_array[z], 'Subjectivity':subjectivity_array[z], 'Confidence':confidence_array[z], 'Irony':irony_array[z], 'Anger': anger_array[z], 'Joy': joy_array[z], 'Fear': fear_array[z], 'Sadness': sadness_array[z], 'Surprise': surprise_array[z]})

#WRITTE INDICO.IO ERROR ARCHIVE

file = open("indico_errors.txt","w")

for b in error2:
    file.write(str(b)+"\n")
file.close()

print("Writing 2 complete")

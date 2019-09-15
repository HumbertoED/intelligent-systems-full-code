#READ CSV ARCHIVE

import csv

array = []
array2 = []
array3 = [] #polarity
array4 = [] #agreement
array5 = [] #subjectivity
array6 = [] #confidence
array7 = [] #irony
array8 = [] #anger
array9 = [] #joy
array10 = [] #fear
array11 = [] #sadness
array12 = [] #surprise

with open('test.csv', 'rb') as File:
    reader = csv.DictReader(File)
    for row in reader:
        array.append(row['Tweet'])
        array2.append(row['Id'])
        array3.append(row['Polarity'])
        array4.append(row['Agreement'])
        array5.append(row['Subjectivity'])
        array6.append(row['Confidence'])
        array7.append(row['Irony'])
        array8.append(row['Anger'])
        array9.append(row['Joy'])
        array10.append(row['Fear'])
        array11.append(row['Sadness'])
        array12.append(row['Surprise'])

import requests
import json

#CALL INDICO.IO EMOTION API

import indicoio
indicoio.config.api_key = 'ba420e48e2322e7e99b674c9d1d3a5d2'

extraversion_array = []
openness_array = []
agreeableness_array = []
conscientiousness_array = []
error2 = []

for y in range(0,1500):

    try:
        result = indicoio.personality(array[y])

        data_string  = json.dumps(result)
        decoded_json = json.loads(data_string)

        extraversion_result = str(decoded_json["extraversion"]*100)
        openness_result = str(decoded_json["openness"]*100)
        agreeableness_result = str(decoded_json["agreeableness"]*100)
        conscientiousness_result = str(decoded_json["conscientiousness"]*100)

        extraversion_array.append(extraversion_result)
        openness_array.append(openness_result)
        agreeableness_array.append(agreeableness_result)
        conscientiousness_array.append(conscientiousness_result)
        print "FINISH "+str(y)
    except KeyError:
        error2.append(y)
        extraversion_array.append("")
        openness_array.append("")
        agreeableness_array.append("")
        conscientiousness_array.append("")
        print "Not posible KEY_ERROR "+str(y)
    except UnicodeEncodeError:
        error2.append(y)
        extraversion_array.append("")
        openness_array.append("")
        agreeableness_array.append("")
        conscientiousness_array.append("")
        print "Not posible UNICODE_ENCODE_ERROR "+str(y)
    except UnicodeDecodeError:
        error2.append(y)
        extraversion_array.append("")
        openness_array.append("")
        agreeableness_array.append("")
        conscientiousness_array.append("")
        print "Not posible UNICODE_DECODE_ERROR "+str(y)
    except ConnectionError:
        error2.append(y)
        extraversion_array.append("")
        openness_array.append("")
        agreeableness_array.append("")
        conscientiousness_array.append("")
        print "Not posible CONNECTION_ERROR "+str(y)

#WRITTE A FULL CSV ARCHIVE

with open('data_test_analysis.csv', 'wb') as csvfile:
    fieldnames = ['Tweet', 'Id', 'Polarity', 'Agreement', 'Subjectivity', 'Confidence', 'Irony', 'Anger', 'Joy', 'Fear', 'Sadness', 'Surprise', 'Extraversion', 'Openness', 'Agreeableness', 'Conscientiousness']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for z in range(0, 1500):
        writer.writerow({'Tweet': array[z], 'Id': array2[z], 'Polarity':array3[z], 'Agreement':array4[z], 'Subjectivity':array5[z], 'Confidence':array6[z], 'Irony':array7[z], 'Anger': array8[z], 'Joy': array9[z], 'Fear': array10[z], 'Sadness': array11[z], 'Surprise': array12[z], 'Extraversion': extraversion_array[z], 'Openness': openness_array[z], 'Agreeableness': agreeableness_array[z], 'Conscientiousness': conscientiousness_array[z]})

print("New CSV File complete")

#WRITTE INDICO.IO ERROR ARCHIVE

file = open("indico_test_errors.txt","w")

for b in error2:
    file.write(str(b)+"\n")
file.close()

print("Writing 2 complete")
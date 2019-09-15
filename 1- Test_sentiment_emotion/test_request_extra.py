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

persistence_language_mistakes = []

with open('data.csv', 'rb') as File:
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

#CALL MEANINGCLOUD API - SENTIMENT

polarity_array = []
agreement_array = []
subjectivity_array = []
confidence_array = []
irony_array = []
key = "6b09f35eba67f4e3d406eae63cbe3c81"
count = 0

import requests
import json

url = "https://api.meaningcloud.com/sentiment-2.1"
f = open("meaningcloud_errors.txt", "r") #READ TXT ARCHIVE

for x in f:

    try:
        payload = "key="+key+"&lang=en&txt="+array[int(x)]+"&txtf=plain&url=""&doc="""
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

        array3[int(x)] = polarity_array[count]
        array4[int(x)] = agreement_array[count]
        array5[int(x)] = subjectivity_array[count]
        array6[int(x)] = confidence_array[count]
        array7[int(x)] = irony_array[count]

        count = count+1
        print "DONE ENGLISH "+str(x)
    except KeyError:
        try:
            payload = "key="+key+"&txt="+array[int(x)]+"&txtf=plain&url=""&doc="""
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

            array3[int(x)] = polarity_array[count]
            array4[int(x)] = agreement_array[count]
            array5[int(x)] = subjectivity_array[count]
            array6[int(x)] = confidence_array[count]
            array7[int(x)] = irony_array[count]

            count = count+1
            print "DONE SPANISH "+str(x)
        except KeyError:
            try:
                payload = "key="+key+"&lang=it&txt="+array[int(x)]+"&txtf=plain&url=""&doc="""
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

                array3[int(x)] = polarity_array[count]
                array4[int(x)] = agreement_array[count]
                array5[int(x)] = subjectivity_array[count]
                array6[int(x)] = confidence_array[count]
                array7[int(x)] = irony_array[count]

                count = count+1
                print "DONE ITALIAN "+str(x)
            except KeyError:
                try:
                    payload = "key="+key+"&lang=fr&txt="+array[int(x)]+"&txtf=plain&url=""&doc="""
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

                    array3[int(x)] = polarity_array[count]
                    array4[int(x)] = agreement_array[count]
                    array5[int(x)] = subjectivity_array[count]
                    array6[int(x)] = confidence_array[count]
                    array7[int(x)] = irony_array[count]

                    count = count+1
                    print "DONE FRENCH "+str(x)
                except KeyError:
                    try:
                        payload = "key="+key+"&lang=pt&txt="+array[int(x)]+"&txtf=plain&url=""&doc="""
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

                        array3[int(x)] = polarity_array[count]
                        array4[int(x)] = agreement_array[count]
                        array5[int(x)] = subjectivity_array[count]
                        array6[int(x)] = confidence_array[count]
                        array7[int(x)] = irony_array[count]

                        count = count+1
                        print "DONE PORTUGUESE "+str(x)
                    except KeyError:
                        try:
                            payload = "key="+key+"&lang=ca&txt="+array[int(x)]+"&txtf=plain&url=""&doc="""
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

                            array3[int(x)] = polarity_array[count]
                            array4[int(x)] = agreement_array[count]
                            array5[int(x)] = subjectivity_array[count]
                            array6[int(x)] = confidence_array[count]
                            array7[int(x)] = irony_array[count]

                            count = count+1
                            print "DONE CATALAN "+str(x)
                        except KeyError:
                            polarity_array.append("")
                            agreement_array.append("")
                            subjectivity_array.append("")
                            confidence_array.append("")
                            irony_array.append("")
                            persistence_language_mistakes.append(str(x))
                            count = count+1
                            print "FAIL KEY_ERROR NOT CATALAN "+str(x)
                        print "FAIL KEY_ERROR NOT PORTUGUESE "+str(x)
                    print "FAIL KEY_ERROR NOT FRENCH "+str(x)
                print "FAIL KEY_ERROR NOT ITALIAN "+str(x)
            print "FAIL KEY_ERROR NOT SPANISH "+str(x)
        print "FAIL KEY_ERROR NOT ENGLISH "+str(x)
    except requests.ConnectionError:
        polarity_array.append("")
        agreement_array.append("")
        subjectivity_array.append("")
        confidence_array.append("")
        irony_array.append("")
        persistence_language_mistakes.append(str(x))
        count = count+1
        print "FAIL CONNECTION_ERROR "+str(x)


#WRITTE SENTIMENT ERROR TXT ARCHIVE

file = open("meaningcloud_language_errors.txt","w")

for a in persistence_language_mistakes:
    file.write(str(a)+"\n")
file.close()

print("Correction complete")

#WRITTE A FULL CSV ARCHIVE

with open('data_sentiment_analysis.csv', 'wb') as csvfile:
    fieldnames = ['Tweet', 'Id', 'Polarity', 'Agreement', 'Subjectivity', 'Confidence', 'Irony', 'Anger', 'Joy', 'Fear', 'Sadness', 'Surprise']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for z in range(0, 1499):
        writer.writerow({'Tweet': array[z], 'Id': array2[z], 'Polarity':array3[z], 'Agreement':array4[z], 'Subjectivity':array5[z], 'Confidence':array6[z], 'Irony':array7[z], 'Anger': array8[z], 'Joy': array9[z], 'Fear': array10[z], 'Sadness': array11[z], 'Surprise': array12[z]})

print("New CSV File complete")

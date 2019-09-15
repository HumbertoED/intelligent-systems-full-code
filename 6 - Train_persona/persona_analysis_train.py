#READ CSV ARCHIVE

import csv

array = []
array2 = []

with open('train_original.csv', 'rb') as File:
    reader = csv.DictReader(File)
    for row in reader:
        array.append(row['Tweet'])
        array2.append(row['Class'])

import requests
import json

#CALL INDICO.IO EMOTION API

import indicoio
indicoio.config.api_key = 'b21e6a05e2dca170414dcda6cfcbef15'

advocate_array = []
debator_array = []
mediator_array = []
consul_array = []
error2 = []

for y in range(0,3000):

    try:
        result = indicoio.personas(array[y])

        print "This dictionary contains these keys: ", " ".join(result)

        advocate_result = (result["advocate"]*100)
        debator_result = (result["debater"]*100)
        mediator_result = (result["mediator"]*100)
        consul_result = (result["consul"]*100)

        advocate_array.append(advocate_result)
        debator_array.append(debator_result)
        mediator_array.append(mediator_result)
        consul_array.append(consul_result)
        print "FINISH "+str(y)
    except KeyError:
        error2.append(y)
        advocate_array.append("")
        debator_array.append("")
        mediator_array.append("")
        consul_array.append("")
        print "Not posible KEY_ERROR "+str(y)
    except UnicodeEncodeError:
        error2.append(y)
        advocate_array.append("")
        debator_array.append("")
        mediator_array.append("")
        consul_array.append("")
        print "Not posible UNICODE_ENCODE_ERROR "+str(y)
    except UnicodeDecodeError:
        error2.append(y)
        advocate_array.append("")
        debator_array.append("")
        mediator_array.append("")
        consul_array.append("")
        print "Not posible UNICODE_DECODE_ERROR "+str(y)
    except ConnectionError:
        error2.append(y)
        advocate_array.append("")
        debator_array.append("")
        mediator_array.append("")
        consul_array.append("")
        print "Not posible CONNECTION_ERROR "+str(y)

#WRITTE A FULL CSV ARCHIVE

with open('personas_train_analysis.csv', 'wb') as csvfile:
    fieldnames = ['Tweet', 'Class', 'Advocate', 'Debator', 'Mediator', 'Consul']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for z in range(0, 3000):
        writer.writerow({'Tweet': array[z], 'Class': array2[z], 'Advocate': advocate_array[z], 'Debator': debator_array[z], 'Mediator': mediator_array[z], 'Consul': consul_array[z]})

print("New CSV File complete")

#WRITTE INDICO.IO ERROR ARCHIVE

file = open("indico_train_errors.txt","w")

for b in error2:
    file.write(str(b)+"\n")
file.close()

print("Writing complete")

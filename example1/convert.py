#!/usr/bin/env python2

import csv
import json
from pprint import pprint

# load the file
with open('data.csv') as f:
	reader = csv.DictReader(f)
	rows = list(reader)

# make an empty list
json_data = []
for row in rows:

	# define how to translate the CSV to correct type of JSON
	item =  {
		"title": row['title'],
		"subtitle": row['subtitle'],
		"ranges": [
			float(row['range_min']),
			float(row['range_mid']),
			float(row['range_max'])],
		"measures": [
			float(row['measure_min']),
			float(row['measure_max'])],
		"markers": [float(row['markers'])]
	}
	# add to the empty list
	json_data.append(item)

# print it to the terminal
pprint(json_data)

# output to json
with open('output.json', 'w') as jsonfile:
	json.dump(json_data, jsonfile, indent=4)

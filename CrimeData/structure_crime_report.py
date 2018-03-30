#!/usr/local/bin/python

# this application is to conver unstructured raw crime data into csv structured format
# import dependencies here

import re
from pprint import pprint
import pandas as pd

f = open('./crime_raw_report.txt', 'r')
r = open('./crime_full_report.csv', 'a')

# various crime types
crime_types = ['Robbery', 'Violent Crime', 'Murder & Manslaughter', 'Forcible Rape', 'Aggravated Assault',
               'Property Crime', 'Burglary', 'Larceny & Theft', 'Motor Vehicle Theft', 'Arson', 'Total']

print(",".join(['Zip', 'City'] + crime_types))
r.write(f"{','.join(['Zip', 'City'] + crime_types)}\n")

for l in f.readlines():

    match = re.search(r'(Zip[0-9]+):', l)
    if match:
        zip = re.sub('Zip', '', match.group(0))
        zip = re.sub(':', '', zip)

    match = re.search(r'(Crime rates in.*):', l)
    if match:
        city = re.sub('Crime rates in ', '', match.group(0))
        city = re.sub(':', '', city)
        city = re.sub(',', '', city)

    report_count = []
    for crime_type in crime_types:
        match = re.search(rf'({crime_type}[0-9,]+)', l)
        if match:
            crime_type_count = "%s" % re.sub(f'{crime_type}', '', match.group(0))
            crime_type_count = re.sub(',', '', crime_type_count)
            report_count.append(crime_type_count)
        else:
            report_count.append(0)
    print(f"{zip},{city},{','.join(report_count)}")
    r.write(f"{zip},{city},{','.join(report_count)}\n")

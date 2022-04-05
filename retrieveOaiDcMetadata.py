
## FIX IDENTIFIERS!!!



# sickle is a OAI-PMH Python client library, more at https://pypi.org/project/Sickle/
# an alternative is https://pypi.org/project/pyoai/
# See https://xennis.org/wiki/Python_-_OAI-PMH for an example of both


from sickle import Sickle
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('repo', action='store', help='for example https://www.e-rara.ch/zut/oai')
parser.add_argument('id', action='store', help='for example 8965440')
args = parser.parse_args()

repo_url = args.repo
short_id = args.id


################ LIST RECORDS ################
'''
sickle = Sickle('https://www.e-rara.ch/zut/oai')
records = sickle.ListRecords(metadataPrefix='oai_dc')
print(records.next())
'''


################# GET RECORD #################
sickle = Sickle(repo_url)
record = sickle.GetRecord(identifier=short_id, metadataPrefix='oai_dc')

header = record.header
record_id = header.identifier
# print('id: {}'.format(header.identifier))

metadata = record.metadata
if 'title' in metadata:
    record_title = str(metadata['title'])[2:-2] # converting to string and slicing to remove the [''] for each list
else: record_title = "NO DATA"
if 'creator' in metadata:
    record_creator = str(metadata['creator'])[2:-2]
else: record_creator = "NO DATA"
if 'description' in metadata:
    record_description = str(metadata['description'])[2:-2]
else: record_description = "NO DATA"
if 'publisher' in metadata:
    record_publisher = str(metadata['publisher'])[2:-2]
else: record_publisher = "NO DATA"
if 'date' in metadata:
    record_date = str(metadata['date'])[2:-2]
else: record_date = "NO DATA"
if 'format' in metadata:
    record_format = str(metadata['format'])[2:-2]
else: record_format = "NO DATA"
if 'identifier' in metadata:
    record_identifier = str(metadata['identifier'])[2:-2]
else: record_identifier = "NO DATA"
if 'language' in metadata:
    record_language = str(metadata['language'])[2:-2]
else: record_language = "NO DATA"
if 'rights' in metadata:
    record_rights = str(metadata['rights'])[2:-2]
else: record_rights = "NO DATA"


# field names 
fields = ['ID', 'Title', 'Creator', 'Description', 'Publisher', 'Date', 'Format', 'Identifier', 'Language', 'Rights'] 
    
# data row of csv file 
row = [record_id, record_title, record_creator, record_description, record_publisher, record_date, record_format, record_identifier, record_language, record_rights] 
    
# name of csv file 
filename = "oaidc_" + short_id + ".csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerow(row)

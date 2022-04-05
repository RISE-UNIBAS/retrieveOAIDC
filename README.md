## Retrieve OAI DC

This script 
- retrieves OAI DC metadata from OAI-PMH data providers
- write them to a tabular format

Open a terminal and run the file `retrieveOaiDcMetadata.py` adding as arguments the data provider and the id of the resource, like this:

	python retrieveOaiDcMetadata.py REPO-URL ID

For example
	
	python retrieveOaiDcMetadata.py https://www.e-rara.ch/zut/oai 8965440
	
	python retrieveOaiDcMetadata.py https://digital.slub-dresden.de/oai oai:de:slub-dresden:db:id-372782140


___________________________________

Info about data providers (in progress):
- e-rara has rich OAI_DC metadata, almost as rich as METS;
- UB Augsburg has good OAI_DC supports (it does not support METS, but MARC21);
- SLUB Dresden has poor OAI_DC metadata, METS is more complete;
- Uni Halle does not support OAI_DC, only METS.

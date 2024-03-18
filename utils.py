import json

def create_vectara_document_from_file(filepath):
    with open(filepath, "r") as f:
        txt_file = f.read()
    
    # get metadata file
    with open(filepath[:-3] + "_metdata.json", "r") as f:
        metadata = json.load(f)

    document = {}
    document['document_id'] = metadata['title'] # using title as the id for now.
    document['title'] = metadata['title']

    document['metadata_json'] = json.dumps(metadata)

    document['section'] = [{"text": txt_file}]

    return document




    


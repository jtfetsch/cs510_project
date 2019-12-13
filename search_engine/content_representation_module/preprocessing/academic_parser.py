import json

class AcademicParser():
    def __init__(self, fname):
        self.academic_doc = []
        self.valid_docno = []
        self.document_id_to_num = {}
        # self.document_ids()
        self.load_files(fname)

    def document_ids(self):
        with open('../document_id_mapping.txt', 'r') as infile:
            for line in infile:
                doc_num, doc_id = line.strip().split(' ')
                self.document_id_to_num[doc_id] = int(doc_num)

    def load_files(self, fname):
        '''
        self.academic_doc is a dictionary with doc_num as keys.
        The value of each (key, value) pair is a json dictionary with keys: 
        ['keyPhrases', 'paperAbstract', 'numKeyReferences', 'title', 'venue', 'numCitedBy', 'numKeyCitations', 'docno', 'ana']]
        keyPhrases might be absent
        '''
        with open(fname, "r") as json_file:
            for line in json_file:
                f = json.loads(line)
                # doc_num = self.document_id_to_num[f["docno"]]
                if self.check_if_valid(f):
                    self.academic_doc.append(f)
                    self.valid_docno.append(f["docno"])

    def check_if_valid(self, doc):
        if len(doc["paperAbstract"][0]) > 0 and len(doc["title"][0]) > 0:
            return True

    def get_documents(self):
        return self.academic_doc

'''

def main():
    parser = AcademicParser("../train_data/Academic_papers/docs.json")
    docs = parser.get_documents()
    valid_count = 0
    for doc in docs:
        if len(doc["paperAbstract"][0]) > 0 and len(doc["title"][0]) > 0:
            valid_count += 1
        
    print("total datapoints: ", len(docs))
    print("total valid datapoints:", valid_count)

if __name__ == '__main__':  
    main()
'''
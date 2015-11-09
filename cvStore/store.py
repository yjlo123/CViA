__author__ = 'siwei'

import json
import os

class DataStore:

    def __init__(self):
        self.root_dir_path = os.path.dirname(os.path.abspath(__file__)) + '/data/'
        self.load()

    def save(self, d):
        with open(self.root_dir_path+'data.json', 'w') as f:
            f.write(unicode(json.dumps(d, ensure_ascii=False)))

    def load(self):
        with open(self.root_dir_path+'data.json', 'r') as f:
            self.data = json.loads(f.read())

    def printData(self):
        print(json.dumps(self.data))
        print self.data['cv'][0]['name']



if __name__ == "__main__":
    x = DataStore()
    """
    x.save( json.loads('''{
    "cv": [
        {
            "name": "siwei",
            "age": "23"
        },
        {
            "name": "jianghao",
            "age": "24"
        }
    ]
}'''))"""
    x.printData()
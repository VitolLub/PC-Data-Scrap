from pymongo import MongoClient
import json

def connect_to_db():
    db = MongoClient('mongodb+srv://vitol:vitol486070920@ebay.elcsu.mongodb.net/test?retryWrites=true&w=majority')
    db = db['pc_scrap_data']
    collections = db['pc_scrap_data']
    return collections


def load_json():
    collections = connect_to_db()
    # load all data by from collections, exclude _id
    data = collections.find({}, {'_id': False})
    print(type(data))
    for elem in data:
        print(elem)
        print(type(elem))
        with open('data.json', 'w') as f:
            json.dump(data, f)




if __name__ == '__main__':
    load_json()
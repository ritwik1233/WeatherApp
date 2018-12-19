import pymongo
from config.config import mongodbURL
def addReport(data):
    myclient = pymongo.MongoClient(mongodbURL)
    db = myclient.get_database()
    mycollection = db['reports']
    mycollection.insert_one(data)
    return mycollection


def viewReport():
    myclient = pymongo.MongoClient(mongodbURL)
    db = myclient.get_database()
    mycollection = db['reports']
    cursor = mycollection.find()
    result=[]
    for doc in cursor:
        result.append(doc)
    return result
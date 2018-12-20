import pymongo
from config.config import mongodbURL

# AUTHOR:Ritwik Sinha
# DATE CREATED:20/12/2018
# PURPOSE: This function is used to save city weekly report to Database
# PARAMETER: data containing a dictionary with date,location,humidity,temperature,pressure
# RETURN : return True or False depending on whether data is save

def add_report(data):
    try:
        myclient = pymongo.MongoClient(mongodbURL)
        db = myclient.get_database()
        mycollection = db['reports']
        cursor = mycollection.find({"$and": [{"date": data['date']}, {"location": data['location']}]}).count()
        if cursor == 0:
            mycollection.insert_one(data)
            myclient.close()
            return True
        else:
            myclient.close()
            return False
    except:
        myclient.close()
        return False


# AUTHOR:Ritwik Sinha
# DATE CREATED:20/12/2018
# PURPOSE: This function is used to get all reports from database
# PARAMETER:
# RETURN : return


def view_report():
    try:
        myclient = pymongo.MongoClient(mongodbURL)
        db = myclient.get_database()
        mycollection = db['reports']
        cursor = mycollection.find()
        result = []
        for doc in cursor:
            result.append(doc)
        myclient.close()
        return result
    except:
        myclient.close()
        return []
# AUTHOR:Ritwik Sinha
# DATE CREATED:20/12/2018
# PURPOSE: This function is used to delete a selected report from database
# PARAMETER:
# RETURN : return

def delete_report(data):
    try:
        myclient = pymongo.MongoClient(mongodbURL)
        db = myclient.get_database()
        mycollection = db['reports']
        cursor = mycollection.delete_one({"$and": [{"date": data['date']}, {"location": data['location']}]})
        myclient.close()
        return True
    except:
        myclient.close()
        return False



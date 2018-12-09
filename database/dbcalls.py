import pymongo;
from config.config import mongodbURL
favoriteCity = [
    {
        'location': 'Lucknow'
    },
]
# AUTHOR:Ritwik Sinha
# DATE CREATED:09/12/2018
# PURPOSE: This function is used to add a favorite city to the list of favourite city list
# PARAMETER: favoriteCity
# RETURN : return true if city is successfully added
def addfavorites(favoriteCity):
    myclient = pymongo.MongoClient(mongodbURL)
    db=myclient.get_database()
    cities = db['favoriteCity']
    cursor = cities.find({'location': favoriteCity[0]['location']})
    if not cursor.count()>=1:
        cities.insert_many(favoriteCity)
        myclient.close()
        return True
    else:
        myclient.close()
        return False
# AUTHOR:Ritwik Sinha
# DATE CREATED:09/12/2018
# PURPOSE: This function is used to get the list of favorite cities by performing a find query in the db
# PARAMETER: None
# RETURN : return the response i.e the list of favorite cities as a dictionary
def getfavorites():
    favoritecitiesDict = dict()
    myclient=pymongo.MongoClient(mongodbURL)
    db=myclient.get_database()
    cities=db['favoriteCity']
    cursor = cities.find()
    for db in cursor:
        favoritecitiesDict['location_'+str(db['_id'])]=db['location']
    myclient.close()
    return favoritecitiesDict
# AUTHOR:Ritwik Sinha
# DATE CREATED:09/12/2018
# PURPOSE: This function is used to delete  the return the response from the GET Web Service Call
# PARAMETER: city
# RETURN : return the true if successfull
def deletefavoritedata(location):
    myclient = pymongo.MongoClient(mongodbURL)
    db = myclient.get_database()
    cities = db['favoriteCity']
    cursor = cities.delete_one({'location':location})
    if(cursor.deleted_count==1):
        myclient.close()
        return True
    else:
        myclient.close()
        return False

print(addfavorites(favoriteCity))
print(deletefavoritedata('Lucknow'))
for key,value in getfavorites().items():
    print(value)

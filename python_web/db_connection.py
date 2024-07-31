import pymongo
import certifi
url= "mongodb+srv://nguyen:l5K9LyqcGPLCAuBx@cluster0.zwea0ao.mongodb.net/"
client =  pymongo.MongoClient(url, tlsCAFile=certifi.where())
db = client ['pythonweb']

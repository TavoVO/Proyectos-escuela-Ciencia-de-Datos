import pymongo

myclient = pymongo.MongoClient("mongodb+srv://TavoVO:<19120248>@cluster0.xyipa.mongodb.net/?retryWrites=true&w=majority")

mydb = myclient["mydatabase"]

dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")
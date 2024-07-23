from app.utils.database import get_database
import pymongo
import json
async def get_frequent_categories():
    db = get_database()
    collection = db.frequent_categorys
    query = {}
    found_documents = collection.find(query).sort('sup', pymongo.DESCENDING).limit(10)
    categories = []
    for i in found_documents:
        categories.append({"id":str(i["id"]),"name":i["name"],"url":i["url"],"img":i["img"],"sup":i["sup"]})
    return {"data":categories}

async def add_categories(file):
    content = await file.read()
    db = get_database()
    collection = db.frequent_categorys
    data = json.loads(content)
    for record in data:
        new_category = {"id":record["id"], "name":record["name"],"url":record["url"],"img":record["img"],"sup":0}
        collection.insert_one(new_category)
    return {"status":200,"message":"Success"}


async def get_all_categories(page, size):
    db = get_database()
    collection = db.frequent_categorys
    records = collection.find().sort('sup', pymongo.DESCENDING).skip(page*size).limit(size)
    categories = []
    for i in records:
        categories.append({"id":str(i["id"]),"name":i["name"],"url":i["url"],"img":i["img"],"sup":i["sup"]})
    return {"status":200,"data":categories}
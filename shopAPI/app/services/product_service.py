from app.utils.database import get_database
import pymongo
import json
async def get_frequent_products():
    db = get_database()
    collection = db.frequent_products
    query = {}
    found_documents = collection.find(query).sort('sup', pymongo.DESCENDING).limit(10)
    products = []
    for i in found_documents:
        products.append({"id":str(i["id"]),"name":i["name"],"url":i["url"],"img":i["img"],"sup":i["sup"]})
    return {"status":200,"data":products}

async def search_product(name: str):
    db = get_database()
    collection = db.frequent_products
    query = { 'name': { '$regex': name, '$options': 'i' } }
    found_documents = collection.find(query).sort('sup', pymongo.DESCENDING).limit(10)
    products = []
    for i in found_documents:
        products.append({"id":str(i["id"]),"name":i["name"],"url":i["url"],"img":i["img"],"sup":i["sup"]})
    return {"status":200,"data":products}

async def add_products(file):
    content = await file.read()
    db = get_database()
    collection = db.frequent_products
    data = json.loads(content)
    for record in data:
        new_product = {"id":record["id"], "idCate":record["idCate"],"name":record["name"],"url":record["url"],"img":record["img"],"price":record["price"],"sup":0}
        collection.insert_one(new_product)
    return {"status":200,"message":"Success"}

async def get_all_products(page,size):
    db = get_database()
    collection = db.frequent_products
    records = collection.find().sort('sup', pymongo.DESCENDING).skip(page*size).limit(size)
    products = []
    for i in records:
        products.append({"id":str(i["id"]),"name":i["name"],"url":i["url"],"img":i["img"],"sup":i["sup"]})
    return {"status":200,"data":products}

async def get_related_items(url: str):
    db = get_database()
    collection_categorys = db.frequent_categorys
    collection_category = db.frequent_category
    collection_itemsets = db.frequent_itemsets
    collection_products = db.frequent_products
    query = { 'url': url }
    c = collection_categorys.find_one(query)
    if c:
        categories = []
        queryTemp = {'categorys': c["id"]}
        cT = collection_category.find(queryTemp).sort('support', pymongo.DESCENDING)
        for cTi in cT:
            if len(cTi["categorys"]) > 1:
                for categoryId in cTi["categorys"]:
                    if categoryId != c["id"]:
                        queryTemp = {'id': categoryId}
                        cT = collection_categorys.find_one(queryTemp)
                        categories.append({"id":str(cT["id"]),"name":cT["name"],"url":cT["url"],"img":cT["img"],"sup":cT["sup"]})
        return {"status":200,"data":categories}
    
    split_string = url.split("/")
    new_url = ""
    index = 0
    for char in split_string:
        if(index == 0):
            new_url += char
        elif(index == 3):
            new_url += '//' + char
        else:
            new_url += '/' + char
        index += 1
    query = { 'url': new_url }
    p = collection_products.find_one(query)
    if p:
        products = []
        queryTemp = {'products': p["id"]}
        pT = collection_itemsets.find(queryTemp).sort('support', pymongo.DESCENDING)
        for pTi in pT:
            if len(pTi["products"]) > 1:
                for productId in pTi["products"]:
                    if productId != p["id"]:
                        queryTemp = {'id': productId}
                        pT = collection_products.find_one(queryTemp)
                        products.append({"id":str(pT["id"]),"name":pT["name"],"url":pT["url"],"img":pT["img"],"sup":pT["sup"]})
        return {"status":200,"data":products}
    return {"status":404,"data":""}

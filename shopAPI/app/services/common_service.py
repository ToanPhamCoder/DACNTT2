from app.utils.database import get_database
import pymongo
async def set_frequent():
    return {"data":"ngon"}
    # db = get_database()
    # collection = db.frequent_categorys
    # query = {}
    # found_documents = collection.find(query).sort('sup', pymongo.DESCENDING).limit(10)
    # categories = []
    # for i in found_documents:
    #     categories.append({"id":str(i["id"]),"name":i["name"],"url":i["url"],"img":i["img"],"sup":i["sup"]})
    # return {"data":categories}

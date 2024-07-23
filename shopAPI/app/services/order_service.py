from app.utils.database import get_database
import uuid
import ast
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
import json

async def get_Order(page,size):
    db = get_database()
    records = db.orders.find().skip(page*size).limit(size)
    orders = []
    for record in records:
        items = []
        for item in record["items"]:
            i = db.frequent_products.find_one({'id': item["productId"]})
            items.append({"id":str(i["id"]),"name":i["name"],"url":i["url"],"img":i["img"],"sup":i["sup"],"quan":item["quantity"]})
        orders.append({"orderId":record["orderId"],"userId":record["userId"],"items":items})
    return {"status":200,"data":orders}

async def add_Order(file):
    content = await file.read()
    db = get_database()
    collection = db.orders
    data = json.loads(content)
    for record in data:
        order_id = str(uuid.uuid4())
        new_order = {"orderId":order_id, "userId":record["userId"],"items":record["items"]}
        collection.insert_one(new_order)
    await refresh_sup()
    return {"status":200,"message":"Success"}

async def refresh_sup():
    db = get_database()
    collection = db.orders
    transactionsCat = []
    transactionsPro = []
    orders = collection.find({})
    for order in orders:
        itemsCat = []
        itemsPro = []
        for item in order["items"]:
            itemsCat.extend([item["categoryId"]])
            itemsPro.extend([item["productId"]])
        transactionsCat.append(itemsCat)
        transactionsPro.append(itemsPro)
    te = TransactionEncoder()
    te_ary_cat = te.fit(transactionsCat).transform(transactionsCat)
    df_cat = pd.DataFrame(te_ary_cat, columns=te.columns_)
    min_support_cat = 0.008
    frequent_itemsets_cat = apriori(df_cat, min_support=min_support_cat, use_colnames=True)
    collection = db.frequent_categorys
    db.frequent_category.delete_many({})
    for index, row in frequent_itemsets_cat.iterrows():
        s = str({row["itemsets"]})
        inner_str = s[len("frozenset("):-1]
        number_set = ast.literal_eval(inner_str)
        numbers = [str(num) for num in number_set]
        if(len(numbers) == 1):
            filter = {'id': numbers[0]}
            update = {'$set': {'sup': row["support"]}}
            collection.find_one_and_update(filter, update, return_document=True)
        else:
            db.frequent_category.insert_one({"id":str(uuid.uuid4()),"support":row["support"],"categorys":numbers})
    te = TransactionEncoder()
    te_ary_pro = te.fit(transactionsPro).transform(transactionsPro)
    df_pro = pd.DataFrame(te_ary_pro, columns=te.columns_)
    min_support_pro = 0.002
    frequent_itemsets_pro = apriori(df_pro, min_support=min_support_pro, use_colnames=True)
    collection = db.frequent_products
    db.frequent_itemsets.delete_many({})
    for index, row in frequent_itemsets_pro.iterrows():
        s = str({row["itemsets"]})
        inner_str = s[len("frozenset("):-1]
        number_set = ast.literal_eval(inner_str)
        numbers = [str(num) for num in number_set]
        if(len(numbers) == 1):
            filter = {'id': numbers[0]}
            update = {'$set': {'sup': row["support"]}}
            collection.find_one_and_update(filter, update, return_document=True)
        else:
            db.frequent_itemsets.insert_one({"id":str(uuid.uuid4()),"support":row["support"],"products":numbers})
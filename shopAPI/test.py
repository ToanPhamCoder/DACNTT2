import pymongo
from app.utils.database import get_database

db = get_database()
collection = db.frequent_categorys
# Xóa tất cả các bản ghi trong collection
result = collection.delete_many({})

# In số lượng bản ghi đã bị xóa
print(f"Đã xóa {result.deleted_count} bản ghi.")
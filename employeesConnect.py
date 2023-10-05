from pymongo import  MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client.company

collection = db.employees

new_document = {
    "name": "John Doe",
    "age": 33,
    "position": "Software Developer"
}
insert_result = collection.insert_one(new_document)
print("inserted document ID:", insert_result.inserted_id)

print("All documents in the collection:")
cursor = collection.find()
for document in cursor:
    print(document)

# update
update_query = {"name": "John Doe"}
update_data = {"$set": {"position": "Senior Developer"}}
update_result = collection.update_one(update_query, update_data)
print("Matched", update_result.matched_count,
      "documents and modified",update_result.modified_count, "documents")

print("All documents in the collection after update:")
cursor = collection.find()
for document in cursor:
    print(document)

# Delete

delete_query = {"name": "John Doe"}
delete_result = collection.delete_one(delete_query)
print("Deleted", delete_result.deleted_count, "document.")

print("All documents in the collection after delete:")
cursor = collection.find()
for document in cursor:
    print(document)

client.close()

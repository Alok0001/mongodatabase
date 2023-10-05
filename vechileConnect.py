from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017")

# Select the database (e.g., "Vehicle")
db = client.Vehicle


collection = db.Cars

# Insert a new car document
new_car = {
    "Model": "Lamborghini Aventador",
    "RegNo": "SUP001",
    "Category": "Supercar",
    "BrandName": "Lamborghini"
}
insert_result = collection.insert_one(new_car)
print("Inserted document ID:", insert_result.inserted_id)

# Find all car documents
print("All car documents in the collection:")
cursor = collection.find()
for document in cursor:
    print(document)

# Update a car document
update_query = {"Model": "Lamborghini Aventador"}
update_data = {"$set": {"Category": "Ultra Supercar"}}
update_result = collection.update_one(update_query, update_data)
print("Matched", update_result.matched_count,
      "documents and modified", update_result.modified_count, "documents")

# Find all car documents after the update
print("All car documents in the collection after update:")
cursor = collection.find()
for document in cursor:
    print(document)

# Delete a car document
delete_query = {"Model": "Lamborghini Aventador"}
delete_result = collection.delete_one(delete_query)
print("Deleted", delete_result.deleted_count, "document.")

# Find all car documents after the delete
print("All car documents in the collection after delete:")
cursor = collection.find()
for document in cursor:
    print(document)

# Close the MongoDB client connection
client.close()

async def insert_one(collection, document):
    result = await collection.insert_one(document)
    return result.inserted_id


async def insert_many(collection, documents):
    result = await collection.insert_many(documents)
    return result.inserted_ids


async def remove_one(collection, query):
    result = await collection.delete_one(query)
    return result.deleted_count


async def remove_many(collection, query):
    result = await collection.delete_many(query)
    return result.deleted_count


async def find_all(collection):
    cursor = collection.find({})
    documents = [document async for document in cursor]

    for document in documents:
        document["_id"] = str(document["_id"])
    
    return documents

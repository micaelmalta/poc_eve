import json

from bson import ObjectId
from pymongo import MongoClient

from app import app

client = app.test_client()

connection = MongoClient(app.config['MONGO_URI'])
db = connection.get_database()


def test_object_id_account():
    res = client.post("object_id_accounts", json={"name": "my_name"})
    val = json.loads(res.get_data().decode("utf-8"))
    _id = val["_id"]

    assert res.status_code == 201

    result = db["object_id_accounts_versions"].count_documents({"_id_document": ObjectId(_id)})
    assert result == 1

    res = client.patch(f"object_id_accounts/{_id}", json={"name": "my_name_modified"})
    assert res.status_code == 200

    result = db["object_id_accounts_versions"].count_documents({"_id_document": ObjectId(_id)})
    assert result == 2


def test_string_accounts():
    _id = str(ObjectId())

    res = client.post("string_id_accounts", json={"_id": _id, "name": "my_name"})
    val = json.loads(res.get_data().decode("utf-8"))

    assert _id == val["_id"]
    assert res.status_code == 201

    result = db["string_id_accounts_versions"].count_documents({"_id_document": _id})
    assert result == 1

    res = client.patch(f"string_id_accounts/{_id}", json={"name": "my_name_modified"})
    assert res.status_code == 200

    result = db["string_id_accounts_versions"].count_documents({"_id_document": _id})
    assert result == 2

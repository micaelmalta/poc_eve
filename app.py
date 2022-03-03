# -*- coding: utf-8 -*-
from eve import Eve

object_id_accounts = {
    "schema": {
        "name": {
            "type": "string",
        }
    },
    "versioning": True,
    "resource_methods": ["POST"],
    "item_methods": ["GET", "PATCH"],
}

string_id_accounts = {
    "schema": {
        "_id": {
            "type": "string",
            "regex": "^[0-9a-f]{24}$",
        },
        "name": {
            "type": "string",
        }
    },
    "query_objectid_as_string": True,
    "versioning": True,
    "resource_methods": ["POST"],
    "item_methods": ["GET", "PATCH"],
}


SETTINGS = {
    "MONGO_URI": "mongodb://mongo:27017/test",
    "IF_MATCH": False,
    "DOMAIN": {
        "object_id_accounts": object_id_accounts,
        "string_id_accounts": string_id_accounts
    }
}

app = Eve(auth=None, settings=SETTINGS)

if __name__ == "__main__":
    app.run()

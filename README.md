# Issue with query_objectid_as_string on Eve>=1.0.1

While migrating from Eve 1.0.0 to 1.0.1, we are seeing unexpected result with `query_objectid_as_string` and `versioning`


## How to test

```
$ docker-compose run --rm app_1_0_0
$ docker-compose run --rm app_1_0_1
```

### Expected results

```
$ docker-compose run --rm app_1_0_0
2 passed

$ docker-compose run --rm app_1_0_1
2 passed
```

### Current results

```
$ docker-compose run --rm app_1_0_0
2 passed

$ docker-compose run --rm app_1_0_1
FAILED test.py::test_string_accounts - assert 404 == 200
1 failed, 1 passed
```

### MONGODB INVESTIGATIONS

#### Expected result

```
{ find: "string_id_accounts", filter: { _id: 'xxx' }
```

#### With Eve==1.0.0

```
{ find: "string_id_accounts", filter: { _id: 'xxx' }
```

#### With Eve==1.0.1

```
{ find: "string_id_accounts", filter: { _id: ObjectId('xxx') }
```


import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/new_app")
mydb = client["new_app"]
users = mydb.users

# user = [{
#     "name": "John",
#     "age": 15,
#     "sex": "male",
#     "nationality": "USA"},
#     {
#     "name": "Lili",
#     "age": 25,
#     "sex": "female",
#     "nationality": "Paris"}
#     ]
#
# x = users.insert_many(user)

# for i in users.find():
#     print(i)

# for i in users.find({}, {"_id": 0, "name": 1, "nationality": 1}):
#     print(i)

# for i in users.find({"age": 25}):
#     print(i)

# Например, чтобы найти документы, в которых поле «адрес» начинается с буквы «S»
# или выше (в алфавитном порядке), используйте модификатор «больше чем» {"$gt": "S"}:

for i in users.find({"age": {"$gt": 16}}):
    print(i, "$gt----------")

# Чтобы найти только те документы, где поле «адрес» начинается с буквы «S»,
# используйте регулярное выражение {"$regex": "^S"}:

for i in users.find({"name": {"$regex": "^J"}}):
    print(i, "$regex--------")
# Сортировка

for i in users.find().sort("name"):
    print(i)

for i in users.find().limit(1):
    print(i, "lllliiiiiiiiiiiiiimit")

# user = {
#     "name": "Alex",
#     "age": 38,
#     "sex": "male",
#     "nationality": "Belarus"
# }
#
# users.insert_one(user)

# users.update_one({"name": "John"}, {"$set": {"nationality": "India"}})


# users.delete_one({"name": "Alex"})


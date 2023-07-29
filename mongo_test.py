import pymongo

client = pymongo.MongoClient(host='localhost', port=27017, username='admin', password='123456')
db = client.avIdol

collection = db['girl']

girl = [
    {"name": '波多野結衣', 'bwh': '{ "b": 90, "w": 59, "h": 85}' , 'age': 30},
    {"name": '吉泽明步', 'bwh': '{ "b": 86, "w": 58, "h": 86}' , 'age': 35},
    {"name": '桃乃木香奈', 'bwh': '{ "b": 80, "w": 54, "h": 80}' , 'age': 22},
    {"name": '西宫梦', 'bwh': '{ "b": 85, "w": 56, "h": 86}' , 'age': 22},
    {"name": '松下纱荣子', 'bwh': '{ "b": 88, "w": 57, "h": 86}' , 'age': 28}
]
result = collection.insert_many(girl)
print(result)

import pymongo

client = pymongo.MongoClient(host='localhost', port=27017, username='admin', password='123456')
db = client.avIdol

collection = db['girl']

girl = [
    {"name": '刘德华', 'bwh': '{ "b": 90, "w": 59, "h": 85}' , 'age': 30},
    {"name": '郭富城', 'bwh': '{ "b": 86, "w": 58, "h": 86}' , 'age': 35},
    {"name": '古天乐', 'bwh': '{ "b": 80, "w": 54, "h": 80}' , 'age': 22},
    {"name": '黎明', 'bwh': '{ "b": 85, "w": 56, "h": 86}' , 'age': 22},
    {"name": '梁朝伟', 'bwh': '{ "b": 88, "w": 57, "h": 86}' , 'age': 28}
]
result = collection.insert_many(girl)
print(result)

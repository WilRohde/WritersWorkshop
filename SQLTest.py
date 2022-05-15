import json
from json import JSONEncoder
from flask_app.models.Group import Group;
import datetime
# class Employee:
#     def __init__(self, name, salary, address):
#         self.name = name
#         self.salary = salary
#         self.address = address

# class Address:
#     def __init__(self, city, street, pin):
#         self.city = city
#         self.street = street
#         self.pin = pin

# subclass JSONEncoder
class CustomEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

data = {'id': 1,
        'name': 'Science Fiction Rangers', 
        'description': 'Outer space shit',
        'short_description': 'stuff blowing up',
        'created_at': str(datetime.datetime.now()),
        'updated_at': str(datetime.datetime.now()),
        'founding_date': str(datetime.datetime.now()),
        'Creator_id':'13',
        'Genre_id': '2',
        'GenreName': 'Science Fiction'}
group = Group(data)
# print("Printing to check how it will look like")
# print(CustomEncoder().encode(group))

# print("Encode Employee Object into JSON formatted Data using custom JSONEncoder")
# groupJSONData = json.dumps(group, indent=4, cls=CustomEncoder)
# print(groupJSONData)

# Let's load it using the load method to check if we can decode it or not.
# print("Decode JSON formatted Data")
# groupJSON = json.loads(groupJSONData)
# print(groupJSON)

print("Encode into JSON formatted Data")
groupJSONData = json.dumps(group.toJson(), indent=4)
print(groupJSONData)

# Let's load it using the load method to check if we can decode it or not.
print("Decode JSON formatted Data")
groupJSON = json.loads(groupJSONData)
print(groupJSON)
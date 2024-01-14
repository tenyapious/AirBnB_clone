#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)


print("-- Create a new BaseModel Object --")
my_model = BaseModel()
my_model.name = "Mr Money"
my_model.save()
print(my_model)

print("-- Create a new User Object --")
my_model = User()
my_model.save()
print(my_model)

print("-- Create a new City Object --")
my_model = City()
my_model.save()
print(my_model)

print("-- Create a new Place Object --")
my_model = Place()
my_model.save()
print(my_model)

print("-- Create a new Amenity Object --")
my_model = Amenity()
my_model.save()
print(my_model)

print("-- Create a new Review Object --")
my_model = Review()
my_model.save()
print(my_model)

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

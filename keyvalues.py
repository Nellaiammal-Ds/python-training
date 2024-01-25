                   # keyvalues or dictionary

# dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# dictionary items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# duplicates not allowed

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
print(len(thisdict))

# print the datatype of dictionary

print(type(thisdict))


# dict() constructor
dict1=dict(name="antony",age="24",country="india")
print(dict1)
# accessing the items
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

# get() method
x = thisdict.get("model")
print(x)

# get keys
x = thisdict.keys()
print(x)

# get values
x = thisdict.values()
print(x)
# if key exits
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

  # change items

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
  }
# change values
thisdict["year"] = 2018
print(thisdict)
thisdict.update({"year":2020})
print(thisdict)
#  remove items
thisdict.pop("model")
print(thisdict)
# popitem
thisdict.popitem()
print(thisdict)
# add items
thisdict["colour"] = "red"
print(thisdict)
# update items
thisdict.update({"model": "ford"})
print(thisdict)
# del item
del thisdict["model"]
print(thisdict)
# clear items
thisdict.clear()
print(thisdict)
# delete
del thisdict
print(thisdict)




import json

# load is used to extract the data from json to current file
with open("E:\Python-with-FreeCodeCamp\leacture 2\json\dump.json","r") as f:
    json_object = json.load(f)
    
print(json_object)

# when to use load or loads and dump or dumps

# in these keywords the s stands for the string
# we must use these s keywords thing when the data is in our file  
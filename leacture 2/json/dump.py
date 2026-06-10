import json

# dump is  used to create a file and add the data in that file
# where as dumps is used to store data as the json string format in the same file and sometime we also use that json format string to make our json file

my_dict = {
    "People": [
        {
            "name":"Rohan",
            "age":23,
            "height":5.5
        },
        
        {
            "name":"Alice",
            "age":27,
            "height":6
        },
        
        {
            "name":"Monty",
            "age":65,
            "height":5
        }
    ]
}

with open("E:\Python-with-FreeCodeCamp\leacture 2\json\dump.json","w") as f:
    json.dump(my_dict,f,indent=6)
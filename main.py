from driver import json_to_object 
dict_val = json_to_object('{"foo": [1, 2, {"bar": 2}]}')
print("Dict is",dict_val)
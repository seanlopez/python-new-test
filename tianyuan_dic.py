import json

name_list = ["tianqi_1", "tianqi_2"]
subnet_list = ["10.1.1.1/24", "20.1.1.1/24"]
count = 0
for i in name_list:
    str1 = '{"name": "' + i + '",' + '"value": "' + subnet_list[count] + '""overridable": False,"description": "Network obj 1","type": "Network"}'
    print(str1)
    json1 = json.dumps(str1)
    print(json1)
    count = count + 1

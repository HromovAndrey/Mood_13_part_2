# import json
# #Серіалізація Python обєкта в json рядок
# data = {"name":"John","age":30, "city":"New York"}
# json_string = json.dumps(data)
# print(json_string)
#
# #Десерелізація JSON рядка в Python обєкта
# json_string = '{"name": "Json", "age":30, "city": "new York"}'
# data = json.loads(json_string)
# print(data)

##Збереження та завантаження файлу
import json

#збереження обєкта в файл у форматі JSON
data = {"name":"John","age":30, "city":"New York"}
with open("data.json", "w") as file:
      json.dump(data, file)

#Завантаження обєкта з файлу у форматі JSON
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)


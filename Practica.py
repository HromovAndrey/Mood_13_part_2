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
import json

##Збереження та завантаження файлу
# import json
#
# #збереження обєкта в файл у форматі JSON
# data = {"name":"John","age":30, "city":"New York"}
# with open("data.json", "w") as file:
#       json.dump(data, file)
#
# #Завантаження обєкта з файлу у форматі JSON
# with open("data.json", "r") as file:
#     loaded_data = json.load(file)
#     print(loaded_data)

# import  json
# data = {"name": "John", "age":42, "info": {"city": "Krarkiv", "birthday": "2001"}}
# with open("data.json", "r") as file:
#     read_data = json.load(file)
# print(read_data)


# import json
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_info(self):
#          print(self.name, self.age)
#
# person = Person("Max", 16)
# with open("data.json", "w") as file:
#     json.dump(person, file)


#     ##Параметр indent для красивого відображення JSON
# data = {"name":"John","age":30, "city":"New York"}
# json_string = json.dumps(data, indent=4)
# print(json_string)
#
#    #Параметр sort_keys для сортування ключів у JSON
# data = {"name": "John", "age":30, "city": "new york", "address":{"street":"123 Main", "zip": "10001"}}
# json_string = json.dumps(data, indent=2, sort_keys=True)
# print(json_sting)
#
# import json
# class Person:
#     filename =
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def birthday(self):
#         self.age += 1
#     def print_info(self):
#         print(self.name, self.age)
#     @classmethod
#     def load_person(cls,):
#         with open(cls.filename, "r") as file:
#             dct = json.load(file)
#
#         return cls(name=dct["name"],
#                    age=dct["age"])
#
# person = Person("Max", 16)
# # person.birthday()
# # person.birthday()
# # person.birthday()
# # person.save()
# # person.load()
# # person.print_info()
#
#
#
# read_person = Person.load_person()
# read_person.print_info()

import json
import time

def save_timer_state(timer_state, filename):
    with open(filename, 'w') as f:
        json.dump(timer_state, f)

def load_timer_state(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def start_timer():
    try:

        timer_state = load_timer_state("timer_state.json")
        if timer_state:
            elapsed_time = timer_state.get("elapsed_time", 0)
            start_time = time.time() - elapsed_time
            print("Таймер відновлено.")
        else:
            start_time = time.time()
            print("Таймер почато.")


        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time
            print("Час: {:.2f} с".format(elapsed_time), end='\r')


            timer_state = {"elapsed_time": elapsed_time}
            save_timer_state(timer_state, "timer_state.json")

            time.sleep(1)
    except KeyboardInterrupt:
        print("\nТаймер зупинено.")

if __name__ == "__main__":
    start_timer()

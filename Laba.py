# Завдання 3
# До вже реалізованого класу «Дріб» додайте можливість стиснення та розпакування даних з
# використанням json та pickle.

import json
import pickle

class Дріб:
    def __init__(self, чисельник, знаменник):
        self.чисельник = чисельник
        self.знаменник = знаменник

    def стиснути_JSON(self, filename):
        with open(filename, 'w') as f:
            json.dump({"чисельник": self.чисельник, "знаменник": self.знаменник}, f)

    @classmethod
    def розпакувати_JSON(cls, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        return cls(data["чисельник"], data["знаменник"])

    def стиснути_pickle(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump((self.чисельник, self.знаменник), f)

    @classmethod
    def розпакувати_pickle(cls, filename):
        with open(filename, 'rb') as f:
            чисельник, знаменник = pickle.load(f)
        return cls(чисельник, знаменник)

    def __str__(self):
        return f"{self.чисельник}/{self.знаменник}"

if __name__ == "__main__":

    дріб1 = Дріб(3, 4)
    дріб1.стиснути_JSON("дріб1.json")

    дріб2 = Дріб.розпакувати_JSON("дріб1.json")
    print("Дріб 2 (збережений та завантажений з JSON):", дріб2)

    дріб3 = Дріб(5, 6)
    дріб3.стиснути_pickle("дріб3.pkl")

    дріб4 = Дріб.розпакувати_pickle("дріб3.pkl")
    print("Дріб 4 (збережений та завантажений з Pickle):", дріб4)

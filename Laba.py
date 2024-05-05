# Завдання 4
# До вже реалізованого класу «Годинник» додайте
# мож-ливість стиснення та розпакування даних з
# використан-ням json та pickle.
import json
import pickle

class Годинник:
    def __init__(self, години, хвилини, секунди):
        self.години = години
        self.хвилини = хвилини
        self.секунди = секунди

    def стиснути_JSON(self, filename):
        with open(filename, 'w') as f:
            json.dump({"години": self.години, "хвилини": self.хвилини, "секунди": self.секунди}, f)

    @classmethod
    def розпакувати_JSON(cls, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        return cls(data["години"], data["хвилини"], data["секунди"])

    def стиснути_pickle(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump((self.години, self.хвилини, self.секунди), f)

    @classmethod
    def розпакувати_pickle(cls, filename):
        with open(filename, 'rb') as f:
            години, хвилини, секунди = pickle.load(f)
        return cls(години, хвилини, секунди)

    def __str__(self):
        return f"{self.години:02}:{self.хвилини:02}:{self.секунди:02}"

if __name__ == "__main__":

    годинник1 = Годинник(12, 30, 45)
    годинник1.стиснути_JSON("годинник1.json")

    годинник2 = Годинник.розпакувати_JSON("годинник1.json")
    print("Годинник 2 (збережений та завантажений з JSON):", годинник2)

    годинник3 = Годинник(23, 59, 59)
    годинник3.стиснути_pickle("годинник3.pkl")

    годинник4 = Годинник.розпакувати_pickle("годинник3.pkl")
    print("Годинник 4 (збережений та завантажений з Pickle):", годинник4)

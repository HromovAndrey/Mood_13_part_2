# Завдання 1
# Розроблення програми з таймером, що підраховує
# час. Використати JSON для збереження стану таймера
# (наприклад, поточний час) у файлі. При перезапуску
# програми відновити час збереженого стану за
# допомогою завантаження даних з JSON-файлу.

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

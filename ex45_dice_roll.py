import random
import time

def roll():
    print("______________________________________________")
    input("Пожалуйста нажмите enter, чтобы бросить кубик")
    print("Кубик брошен...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    result = random.randint(1, 6)
    print(f"Итак, результат вашего броска... {result*'*'}!!")
    print("______________________________________________")
    return result



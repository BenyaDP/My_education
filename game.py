import numpy as np
number = np.random.randint (1, 101) # загадываем число
count_num = 0
while True:
    count_num += 1
    predict_number = int(input("Угадай число от 1 до 100\n"))
    
    if predict_number > number:
        print("Число должно быть меньше!")

    elif predict_number < number:
        print("Число должно быть больше!")

    else:
        print(f"Вы угадали число! Это число = {number}, за {count_num} попыток")
        break # конец игры, выход из цикла
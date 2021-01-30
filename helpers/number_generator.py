import numpy as np


NUM=5000
FILENAME_RANDOM_INTEGERS=f'random_integers_{NUM}'
FILENAME_RANDOM_DOUBLES=f'random_doubles_{NUM}'
FILENAME_RANDOM_INTEGERS_CPP=f'{FILENAME_RANDOM_INTEGERS}.cpp'
FILENAME_RANDOM_DOUBLES_CPP=f'{FILENAME_RANDOM_DOUBLES}.cpp'
END=".txt"

def gen_random_integers():
    arr = np.random.randint(0,NUM, NUM)
    cpp_array = "{"
    with open(file=f'{FILENAME_RANDOM_INTEGERS}{END}', mode="w", encoding="UTF-8") as file:
        for num in arr:
            cpp_array += f'{str(num)},'
            file.write(str(num)+"\n")

    cpp_array = cpp_array[:-1] + "}"
    print(cpp_array)
    with open(file=f'{FILENAME_RANDOM_INTEGERS_CPP}{END}', mode="w", encoding="UTF-8") as file:
        file.write(cpp_array)
    


def gen_random_doubles():
    arr = np.random.uniform(0,NUM, NUM)
    cpp_array = "{"
    with open(file=f'{FILENAME_RANDOM_DOUBLES}{END}', mode="w", encoding="UTF-8") as file:
        for num in arr:
            cpp_array += f'{str(num)},'
            file.write(str(num)+"\n")

    cpp_array = cpp_array[:-1] + "}"
    print(cpp_array)
    with open(file=f'{FILENAME_RANDOM_DOUBLES_CPP}{END}', mode="w", encoding="UTF-8") as file:
        file.write(cpp_array)

gen_random_integers()
gen_random_doubles()
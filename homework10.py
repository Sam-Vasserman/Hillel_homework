import random

def create_and_write(filename):
    with open(f"{filename}.txt", "w") as file:
        strings = []
        for _ in range(100):

            random_list = random.sample(range(100), 10)
            random_string = " ".join(map(str, random_list)) + '\n'
            strings.append(random_string)
        file.writelines(strings)

FILE_1 = 'text1'
FILE_2 = 'text2'
FILE_3 = 'text3'
FILE_4 = 'text4'
FILE_5 = 'text5'

create_and_write(FILE_1)
create_and_write(FILE_2)
create_and_write(FILE_3)
create_and_write(FILE_4)
create_and_write(FILE_5)

def read_and_append(filename):
    with open(f"{filename}.txt", "r+") as file:     
        my_list = file.readlines()
        for line in my_list:
            result = [int(value) ** 2 for value in line.split()]
            file.write(" ".join(map(str, result)) + '\n')

read_and_append(FILE_1)
read_and_append(FILE_2)
read_and_append(FILE_3)
read_and_append(FILE_4)
read_and_append(FILE_5)
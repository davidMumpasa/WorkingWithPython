numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
import random

# a = random.randint(1,9)
for i in numbers:
    random.shuffle(numbers)
    value = input('Please enter a number')
    num = int(value)
    print(num)
    if num == numbers[i]:
        print('passed')
    else:
        print(num, 'is incorrect you failed...')
        print('the machine guess is ',numbers[i])

        name = str
        price = int


    def dish(name, price):
        self.name = name
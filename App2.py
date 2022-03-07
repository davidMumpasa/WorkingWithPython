from Dish import Dish
from DishA import DishA
from DishB import DishB
from DishC import DishC


def getUserInput():
    print("Please select an option below", "\n"
          , "1 --> dishA", "\n"
          , "2 --> dishb", "\n"
          , "3 --> dishC", "\n"
          , "your choice: ")
    value = input()
    option = int(value)

    return option


def process():
    dish = Dish()
    option = getUserInput()

    value2 = input("Please enter the quantity")
    qty = int(value2)

    if option == 1:
        dish = DishA()
        dish.setName("Peperoni")
        dish.setPrice(67)
        dish.setQuantity(qty)
        print(dish.getName(""))

    elif option == 2:
        dish = DishB()
        dish.setName("makaroni")
        dish.setPrice(70)
        dish.setQuantity(qty)
    elif option == 3:
        dish = DishC()
        dish.setName("chips")
        dish.setPrice(90)
        dish.setQuantity(qty)
    else:
        print(option, ' is invalid please enter the right option')


def display():
    dish = Dish()
    print('name: ', dish.getName(""), "\n"
                                      'Price: ', dish.getPrice(""), "\n"
                                                                    'Quantity: ', dish.setQuantity(""))


process()
display()

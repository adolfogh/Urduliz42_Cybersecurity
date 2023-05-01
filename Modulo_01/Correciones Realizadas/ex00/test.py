# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dgerwig- <dgerwig-@student.42urduli>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/17 19:26:27 by dgerwig-          #+#    #+#              #
#    Updated: 2023/05/01 10:11:27 by dgerwig-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from book import Book
from recipe import Recipe

import time
import unittest


class Test(unittest.TestCase):
    
    def test_invalid_recipes_01_name_01(self):
        print("\n--------------------------")
        book3 = Book("Tester book")
        Recipe(123, 2, 42, ['flour', 'sugar', 'eggs'], "Sweet cake", "dessert")

    def test_invalid_recipes_02_name_02(self):
        print("\n--------------------------")
        book3 = Book("Tester book")
        Recipe("", 2, 42, ['flour', 'sugar', 'eggs'], "Sweet cake", "dessert")

    def test_invalid_recipes_03_level_01(self):
        print("\n--------------------------")
        book3 = Book("Tester book")
        Recipe("Cake", "a", 42, ['flour', 'sugar', 'eggs'], "Sweet cake", "dessert")

    def test_invalid_recipes_04_level_02(self):
        print("\n--------------------------")
        book3 = Book("Tester book")
        Recipe("Cake", 0, 42, ['flour', 'sugar', 'eggs'], "Sweet cake", "dessert")

    def test_invalid_recipes_05_level_03(self):
        print("\n--------------------------")
        book3 = Book("Tester book")
        Recipe("Cake", 7, 42, ['flour', 'sugar', 'eggs'], "Sweet cake", "dessert")

    def test_invalid_recipes_06_time_01(self):
        print("\n--------------------------")
        book3 = Book("Tester book")
        Recipe("Cake", 2, "A", ['flour', 'sugar', 'eggs'], "Sweet cake", "dessert")

    def test_invalid_recipes_07_time_02(self):
        print("\n--------------------------")
        book3 = Book("Tester book")
        Recipe("Cake", 2, -42, ['flour', 'sugar', 'eggs'], "Sweet cake", "dessert")

    def test_invalid_recipes_08_ingred_01(self):
        print("\n--------------------------")
        book3 = Book("Tester book")
        Recipe("Cake", 2, 42, 'flour', "Sweet cake", "dessert")

    def test_invalid_recipes_09_ingred_02(self):
        print("\n--------------------------")
        book3 = Book("Tester book")
        Recipe("Cake", 2, 42, [], "Sweet cake", "dessert")

    def test_invalid_recipes_10_descrip_01(self):
        print("\n--------------------------")
        book3 = Book("Tester book")
        Recipe("Cake", 2, 42, ['flour', 'sugar', 'eggs'], 123, "dessert")

    def test_invalid_recipes_11_rectype_01(self):
        print("\n--------------------------")
        book3 = Book("Tester book")
        Recipe("Cake", 2, 42, ['flour', 'sugar', 'eggs'], "Sweet cake", 123)

    def test_invalid_recipes_12_rectype_02(self):
        print("\n--------------------------")
        book3 = Book("Tester book")
        Recipe("Cake", 2, 42, ['flour', 'sugar', 'eggs'], "Sweet cake", "")

    def test_invalid_recipes_13_rectype_03(self):
        print("\n--------------------------")
        book3 = Book("Tester book")
        Recipe("Cake", 2, 42, ['flour', 'sugar', 'eggs'], "Sweet cake", "dinner")


if __name__ == '__main__':
    
    print("\n==========================\n")
    
    # Create Recipes
    cake = Recipe("Cake", 2, 42, ['flour', 'sugar', 'eggs'], "Sweet cake", "dessert")
    to_print = str(cake) 
    print(to_print)
    print("\n==========================\n")

    bread = Recipe("Bread", 3, 35, ['wheat flour', 'salt', 'water', 'yeast'], "White bread", "lunch")
    to_print = str(bread) 
    print(to_print)
    print("\n==========================\n")
    
    salad = Recipe("Salad", 1, 12, ['lettuce', 'tomatoes', 'salt', 'olive oil'], "Green salad", "starter")
    to_print = str(salad) 
    print(to_print)
    print("\n==========================\n")
    
    # Create Book 
    book1 = Book("The best recipe´s book")
    book2 = Book("The worst recipe´s book")


    ### Testing 
    # Add Recipe to Book
    book1.add_recipe(cake)
    book1.add_recipe(bread)
    time.sleep(1)
    book2.add_recipe(cake)
    book2.add_recipe(salad)


    # Find recipes in Book by type 
    Book.get_recipes_by_types(book1, 'lunch')
    print("\n==========================\n")
    
    Book.get_recipes_by_types(book1, '')
    print("\n==========================\n")
   

    # Print recipe from Book 
    print(bread)
    print("\n==========================\n")
   

    # Print all data from Book 
    print(book1)
    print("\n==========================\n")
    
    print(book2)
    print("\n==========================\n")


    # Force ERRORS 
    time.sleep(1)
    unittest.main()

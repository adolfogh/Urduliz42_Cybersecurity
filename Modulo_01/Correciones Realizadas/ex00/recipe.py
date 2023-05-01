# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dgerwig- <dgerwig-@student.42urduli>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/17 19:15:22 by dgerwig-          #+#    #+#              #
#    Updated: 2023/05/01 10:11:32 by dgerwig-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def valid_values(name, level, time, ingred, descrip, rectype):
    valid = 1
    
    if not isinstance(name, str):
        print("❌ Name is not a string.")
        valid = 0
    if len(name) == 0:
        print("❌ Name is empty.")
        valid = 0
    
    if not isinstance(level, int):
        print("❌ Cooking level is not an integer.")
        valid = 0
    if not 0 < level < 6:
        print("❌ Cooking level value is not valid.")
        valid = 0

    if not isinstance(time, int):
        print("❌ Cooking time is not an integer.")
        valid = 0
    if time <= 0:
        print("❌ Cooking time value is not valid.")
        valid = 0
    
    if not isinstance(ingred, list):
        print("❌ Ingredients is not a list.")
        valid = 0
    if len(ingred) == 0:
        print("❌ Ingredients list is empty.")
        valid = 0

    if not isinstance(descrip, str):
        print("❌ Description is not a string.")
        valid = 0

    if not isinstance(rectype, str):
        print("❌ Recipe type is not a string.")
        valid = 0
    if len(rectype) == 0:
        print("❌ Recipe type is empty.")
        valid = 0
    if rectype not in ('starter', 'lunch', 'dessert'):
        print("❌ Recipe type is not 'starter' / 'lunch' / 'dessert'.")
        valid = 0

    return valid


class Recipe:

    def __init__(self,  name, level, time, ingred, descrip, rectype):
        if valid_values(name, level, time, ingred, descrip, rectype):
            self.name = name
            self.cooking_lvl = level
            self.cooking_time = time
            self.ingredients = ingred
            self.description = descrip
            self.recipe_type = rectype
        else:
            sys.exit()

    def __str__(self):
        txt =  ( "Recipe :        " + self.name + "\n"
               + "Cooking level : " + str(self.cooking_lvl) + "\n"
               + "Cooking time :  " + str(self.cooking_time) + " minutes\n"
               + "Ingredients :   " + ', '.join(self.ingredients) + "\n"
               + "Description :   " + self.description + "\n"
               + "Recipe type :   " + self.recipe_type)
        return txt

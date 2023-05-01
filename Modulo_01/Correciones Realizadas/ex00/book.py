# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dgerwig- <dgerwig-@student.42urduli>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/17 19:15:33 by dgerwig-          #+#    #+#              #
#    Updated: 2023/04/17 21:47:37 by dgerwig-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from recipe import Recipe

from datetime import datetime


class Book:

    def __init__(self, name):
        self.name = name
        self.last_update = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        self.creation_date = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        self.recipes_list = {'starter': list(), 'lunch': list(), 'dessert': list()}

    def __str__(self):
        txt =  ( "Recipe book's name : " + self.name + "\n"
               + "Last update :        " + str(self.last_update) + "\n"
               + "Created at :         " + str(self.creation_date) + "\n"
               + "Starters :           " + str(', '.join(self.get_recipes_by_types('starter'))) + "\n"
               + "Lunches :            " + str(', '.join(self.get_recipes_by_types('lunch'))) + "\n"
               + "Desserts :           " + str(', '.join(self.get_recipes_by_types('dessert'))) + "\n") 
        return txt

    def get_recipe_by_name(self, name):
        if isinstance(name, str):
            for lst in self.recipes_list.values():
                for elem in lst:
                    if elem.name == name:
                        print(elem)
                        return elem
            print("Couldn't find the recipe you were looking for.")
        else:
            print("Error : Name isn't a string.")
        sys.exit()

    def get_recipes_by_types(self, recipe_type):
        if isinstance(recipe_type, str):
            if recipe_type in self.recipes_list:
                print("Recipes in " + recipe_type + " :")
                names = [recipe.name for recipe in self.recipes_list[recipe_type]]
                return names
            else:
                print("Error : Recipe type isn't starter, lunch or dessert.")
        else:
            print("Error : Recipe type isn't a string.")
            sys.exit()

    def add_recipe(self, recipe):
        if isinstance(recipe, Recipe):
            if recipe.recipe_type in self.recipes_list:
                self.recipes_list[recipe.recipe_type].append(recipe)
                self.last_update = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
            else:
                print("Error : Recipe type isn't starter, lunch or dessert.")
        else:
            print("Error : Recipe isn't an instance of the Recipe class.")
            sys.exit()

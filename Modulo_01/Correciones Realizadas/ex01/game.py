# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dgerwig- <dgerwig-@student.42urduli>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/19 19:07:56 by dgerwig-          #+#    #+#              #
#    Updated: 2023/05/01 10:12:56 by dgerwig-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class GotCharacter:

    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    '''
    A class representing the Stark family. Or when bad things happen to good people.
    '''

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False


if __name__ == '__main__':
    arya = Stark("arya")
    
    print("----\narya.__dict__ :")
    print(arya.__dict__)
    
    print("----\narya.is_alive :")
    print(arya.is_alive)
    
    print("----\narya.die & arya.is_alive :")
    arya.die()
    print(arya.is_alive)
    
    print("----\narya.__doc__ :")
    print(arya.__doc__)

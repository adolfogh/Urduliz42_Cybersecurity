# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dgerwig- <dgerwig-@student.42urduli>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/19 19:23:53 by dgerwig-          #+#    #+#              #
#    Updated: 2023/05/01 10:39:15 by dgerwig-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def is_type(elem):
    if not isinstance(elem, int) and not isinstance(elem, float):
        return False
    return True


def is_list(lst):
    if not isinstance(lst, list) or len(lst) == 0:
        return False
    for elem in lst:
        if not is_type(elem):
            return False
    return True


def is_list_list(lst):
    if not isinstance(lst, list) or len(lst) == 0:
        return False
    for elem in lst:
        if not is_list(elem):
            return False
    size = len(lst[0])
    for elem in lst:
        if len(elem) != size:
            return False
    return True


def is_range(tpl):
    if not isinstance(tpl, tuple) or len(tpl) != 2:
        return False
    if isinstance(tpl[0], int) and isinstance(tpl[1], int) and tpl[0] < tpl[1]:
        return True
    return False


class Vector:

    def __init__(self, values):
        self.values = []
        self.shape = ()
        if isinstance(values, list):
            if is_list(values):
                self.shape = (1, len(values))
                self.values.append(values)
            elif is_list_list(values):
                self.shape = (len(values), len(values[0]))
                for elem in values:
                    self.values.append(elem)
            else:
                raise ValueError("‼️  Invalid list for Vector")
        elif isinstance(values, int):
            self.shape = (values, 1)
            for i in range(values):
                self.values.append([float(i)])
        elif is_range(values):
            self.shape = (values[1] - values[0], 1)
            for i in range(values[0], values[1]):
                self.values.append([float(i)])
        else:
            raise ValueError("‼️  Invalid values for Vector")
    
    def __add__(self, original):
        modified = Vector(self.values)
        if isinstance(original, Vector) and self.shape == original.shape:
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    modified.values[i][j] += original.values[i][j]
        else:
            raise ValueError("‼️  Invalid type for addition")
        return modified

    def __radd__(self, original):
        return self.__add__(original)

    def __sub__(self, original):
        modified = Vector(self.values)
        if isinstance(original, Vector) and self.shape == original.shape:
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    modified.values[i][j] -= original.values[i][j]
        else:
            raise ValueError("‼️  Invalid type for substraction")
        return modified

    def __rsub__(self, original):
        return self.__sub__(original)

    def __truediv__(self, original):
        modified = Vector(self.values)
        if isinstance(original, int) or isinstance(original, float):
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    modified.values[i][j] /= original
        else:
            raise ValueError("‼️  Invalid type for division")
        return modified

    def __rtruediv__(self, original):
        raise ValueError("‼️  Can't divide by Vector")

    def __mul__(self, original):
        modified = Vector(self.values)
        if isinstance(original, int) or isinstance(original, float):
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    modified.values[i][j] *= original
        else:
            raise ValueError("‼️  Invalid type for multiplication")
        return modified

    def __rmul__(self, original):
        return self.__mul__(original)

    def __str__(self):
        txt = ("Vector values : " + str(self.values)
               + "\nShape : " + str(self.shape))
        return txt

    def __repr__(self):
        txt = ("Vector values : " + str(self.values)
               + "\nShape : " + str(self.shape))
        return txt

    def dot(self, vect):
        if self.shape[0] != vect.shape[0] and self.shape[1] != vect.shape[1]:
            raise ValueError("‼️  Dot product requires two vectors with the same shape")
        else:
            modified = 0
            for i in range(len(self.values)):
                for j in range(len(self.values[0])):
                    modified += self.values[i][j] * vect.values[i][j]
            return modified

    def T(self):
        values = [[0] * self.shape[0] for i in range(self.shape[1])]
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                values[j][i] = self.values[i][j]
        return Vector(values)

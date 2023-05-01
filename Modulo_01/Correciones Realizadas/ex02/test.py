# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dgerwig- <dgerwig-@student.42urduli>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/19 19:23:48 by dgerwig-          #+#    #+#              #
#    Updated: 2023/05/01 10:39:19 by dgerwig-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from vector import Vector

import time
import unittest

class Test(unittest.TestCase):

    def test_vector_errors_01(self):
        print("\n--------------------------")
        v_e1 = Vector([["a"], [2.0]])

    def test_vector_errors_02(self):
        print("\n--------------------------")
        v_e1 = Vector([ "" , 2.0])

    def test_vector_errors_03(self):
        print("\n--------------------------")
        v_e1 = Vector(['4', [2.0]])
    
    def test_vector_errors_04(self):
        print("\n--------------------------")
        v_e1 = Vector([[], [2.0]])

    def test_vector_errors_05(self):
        print("\n--------------------------")
        v_e1 = Vector([[1.0, 2.0], [2.0]])

    def test_vector_errors_06(self):
        print("\n--------------------------")
        v_e1 = Vector((10, 5))

    def test_vector_errors_07(self):
        print("\n--------------------------")
        v_e1 = Vector([[0.0, 1.0, 2.0, 3.0]])
        v_e2 = v_e1 / 0.0

    def test_vector_errors_08(self):
        print("\n--------------------------")
        v_e1 = Vector([[0.0, 1.0, 2.0, 3.0]])
        v_e2 = 2.0 / v_e1 

    def test_vector_errors_09(self):
        print("\n--------------------------")
        v_e1 = Vector([[0.0, 1.0, 2.0, 3.0]])
        v_e2 = v_e1 + "a"


if __name__ == '__main__':

    print("\n**** TEST 1 ****\n")
    v11 = Vector([[0.0], [1.0], [2.0], [3.0]])
    print(v11)
    v12 = v11 * 5
    print(v12)
    v13 = v11 / 2
    print(v13)
    
    print("\n**** TEST 2 ****\n")
    v21 = Vector([[0.0, 1.0, 2.0, 3.0]])
    print(v21)
    v22 = v21 * 5
    print(v22)
    v23 = v21 / 2
    print(v23)
   
    print("\n**** TEST 3 ****\n")
    print(Vector([[0.0], [1.0], [2.0], [3.0]]).shape)

    print("\n**** TEST 4 ****\n")
    print(Vector([[0.0], [1.0], [2.0], [3.0]]).values)
    
    print("\n**** TEST 5 ****\n")
    print(Vector([[0.0, 1.0, 2.0, 3.0]]).shape) 
    
    print("\n**** TEST 6 ****\n")
    print(Vector([[0.0, 1.0, 2.0, 3.0]]).values)
    
    print("\n**** TEST 7 ****\n")
    v31 = Vector([[0.0], [1.0], [2.0], [3.0]]) 
    print(v31)
    print(v31.shape)
    print(v31.T())
    print(v31.T().shape)
    
    print("\n**** TEST 8 ****\n")
    v32 = Vector([[0.0, 1.0, 2.0, 3.0]])
    print(v32)
    print(v32.shape)
    print(v32.T())
    print(v32.T().shape) 

    print("\n**** TEST 9 ****\n")
    v41 = Vector([[0.0], [1.0], [2.0], [3.0]]) 
    v42 = Vector([[2.0], [1.5], [2.25], [4.0]]) 
    print(v41)
    print(v42)
    print(v41.dot(v42))
    v43 = Vector([[1.0, 3.0]]) 
    v44 = Vector([[2.0, 4.0]]) 
    print(v43)
    print(v44)
    print(v43.dot(v44))
    v41
    print(v41)

    print("\n**** TEST 10 ****\n")
    v51 = Vector([[12.0, 4], [24.0, 6], [48.0, 8]])
    print(v51)
    v52 = v51 / 2
    print(v52)

    print("\n**** TEST 11 ****\n")
    v61 = Vector(5)
    print(v61)
    v62 = v61 + Vector([[0], [10], [20], [30], [40]])
    print(v62)

    print("\n**** TEST 12 ****\n")
    v71 = Vector((10, 15))
    print(v71)
    v72 = v71 - Vector([[6],[4], [12], [6], [8]])
    print(v72)

    print("\n**** TEST 13 ****\n")
    print(v72)
    print(v72.T())


    # Force ERRORS 
    time.sleep(1)
    print("\n**** TEST ERRORS ****\n")
    unittest.main()

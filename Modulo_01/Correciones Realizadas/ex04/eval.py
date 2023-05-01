# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    eval.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dgerwig- <dgerwig-@student.42urduli>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/25 18:45:09 by dgerwig-          #+#    #+#              #
#    Updated: 2023/05/01 11:01:06 by dgerwig-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class Evaluator:

    def zip_evaluate(self, coefs, words):
        if self.check_values(coefs, words):
            total = 0
            zipped = zip(coefs, words)
            for elem in zipped:
                total += elem[0] * len(elem[1])
            return total
        return -1

    def enumerate_evaluate(self, coefs, words):
        if self.check_values(coefs, words):
            total = 0
            for key, value in enumerate(words):
                total += coefs[key] * len(value)
            return total
        return -1

    def check_values(self, coefs, words):
        if not isinstance(coefs, list) or not isinstance(words, list):
            return False
        for elem in coefs:
            if not isinstance(elem, (int,float)):
                return False
        for elem in words:
            if not isinstance(elem, str):
                return False
        if len(coefs) != len(words):
            return False
        return True


def test_evaluator(coefs, words):
    evaluator = Evaluator()
    zip_result = evaluator.zip_evaluate(coefs, words)
    enum_result = evaluator.zip_evaluate(coefs, words)
    print(f"TEST Evaluator -> \n\
            words =               {words}\n\
            coefs =               {coefs}\n\
            zip_evaluate():       {zip_result}\n\
            enumerate_evaluate(): {enum_result}\n")


if __name__ == '__main__':
    test_evaluator([1.0, 2.0, 1.0, 4.0, 0.5], ["Le", "Lorem", "Ipsum", "est", "simple"])
    test_evaluator([0.0, -1.0, 1.0, -12.0, 0.5, 42.42], ["Le", "Lorem", "Ipsum", "n", "est", "pas", "simple"])
    test_evaluator([1, 2, 3], ["a", "b", "c"])
    test_evaluator(["a", "b", "c"], [1, 2,3])
    test_evaluator([1], ["one", "two"])
    test_evaluator([1, 2, 3], 42.0)
    test_evaluator([1, "two", 3], ["a", "b", "c"])
    test_evaluator([1, 2, 3], ["a", 2, "c"])

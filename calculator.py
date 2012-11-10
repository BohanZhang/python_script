# -*- coding: utf-8 -*-

# 正则表达式需要
from cmath import *
import re

class Calculator():
    """
    计算器类
    """

    VERSION = 0.1

    globals = {'__builtins__':None}
    
    locals = {'pi': pi, 'sin': sin}

    def calculation(self, data):
        """
        计算
        """
        pass

    def find_multiplication(self, formula):
        """
        查找算式中的乘法
        """
        pass

    def find_parentheses(self, formula): 
        """
        查找算式中的括号
        """
        start = formula.find('(')
        end = formula.find(')')
        if start == -1 and end == -1:
            pass
        elif start != -1 and end != -1:
            # sub formula
            sub_formula = formula[start + 1: end]
            formula_left = formula[:start]
            formula_right = formula[end + 1:]
            dic = {}
            dic['sub_formula'] = sub_formula
            dic['formula_left'] = formula_left
            dic['formula_right'] = formula_right
            return dic
        else:
            # raise an Exception
            raise FormulaFormatException

    def do_calc(self, formula):
        """
        做具体的计算，计算公式支持由locals提供
        """
        try:
            return eval(formula, self.globals, self.locals)
        except NameError:
            raise NameError()

class FormulaFormatException(Exception):
    """
    算式格式错误
    """
    pass

if __name__ == '__main__':
    formula = '1.2 + (2.3 - 4) * 3 % 5'
    c = Calculator()
    c.find_parentheses(formula)

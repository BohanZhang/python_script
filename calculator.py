# -*- coding: utf-8 -*-

# 正则表达式需要
import re

class Calculator():
    """
    计算器类
    """

    VERSION = 0.1

    def calculation(self, data):
        """
        利用递归完成计算
        """
        data = self.format_data(data)
        print 'data', data
        numbers = self.get_numbers(data)
        print 'numbers:', numbers
        operators = self.get_operator(numbers, data)
        print 'operators:', operators
        new_numbers = self.change_numbers_type(numbers)
        print 'new_numbers:', new_numbers

    def do_calc(self, numbers, operators):
        """
        完成计算
        1 + 2 * ? % 3 = 5
        3 * ? % 3 = 5
        1 * ? = 5
        ? = 5 % 1
        ? = 5
        """
        pass


    def format_data(self, data):
        """
        格式化数据：
            1. 如果结尾没有等号则在后面补全"=?"
            2. 如果结尾只有等号没有?且没有其它数字则补"?"
        """
        if data.find('=') == -1:
            data += '=?'
        elif data.find('?') == -1:
            data += '?'
        return data

    def get_numbers(self, data):
        """
        通过正则取得所有非操作符的列表
        """
        match = '[\+|\-|\*|\%|\=]'
        return re.split(match, data)

    def get_operator(self, numbers, data):
        """
        能过非操作符的列表及原始数据得到操作符列表
        """
        operators = []
        length = len(numbers)
        for index in range(length):
            if index + 1 != length:
                start = data.find(numbers[index]) + len(numbers[index])
                end = data.find(numbers[index + 1])
                operator = data[start: end]
                operators.append(operator)
                data = data[end:]
        return operators

    def change_numbers_type(self, numbers):
        """
        转换numbsers的类型
        """
        new_numbers = []
        for n in numbers:
            try:
                value = float(n.strip())
            except ValueError:
                value = n.strip()
            new_numbers.append(value)
        return new_numbers

if __name__ == '__main__':
    data = '1.2 + 2.3 - 4 * 3 % 5'
    c = Calculator()
    c.calculation(data)

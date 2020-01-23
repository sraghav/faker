# coding=utf-8

from __future__ import unicode_literals

from .. import BaseProvider

localized = False


# create new provider class. Note that the class name _must_ be ``Provider``.
class Provider(BaseProvider):

    def amount(self, digits=5, dec=2):
        if digits >= 1:
            num1 = str(self.generator.random_number(digits=digits, fix_len=False))
        else:
            num1 = '0'

        if dec == 0:
            num2 = ''
        else:
            num2 = '.' + str(self.generator.random_number(digits=dec, fix_len=True))

        # self.generator.numerify("#####.##")

        number = num1 + num2
        return number

    def f_interest_rate(self, digits=1, dec=4):
        num1 = ''

        if digits < 1:
            return ''
        elif digits == 1:
            num1 = str(self.generator.random_digit())
        else:
            num1 = str(self.generator.random_number(digits=digits, fix_len=False))

        if dec == 0:
            num2 = ''
        else:
            num2 = '.' + str(self.generator.random_number(digits=dec, fix_len=False))

        number = num1 + num2

        return number

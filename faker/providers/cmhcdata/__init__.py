# coding=utf-8

from __future__ import unicode_literals

from .. import BaseProvider

localized = False


# create new provider class. Note that the class name _must_ be ``Provider``.
class Provider(BaseProvider):

    def pool_number(self):
        return self.generator.bothify("########")

    def issuercode(self):
        return self.generator.bothify("??######").upper()

    def pool_type(self):
        return self.num(lb=1, ub=3)

    def pool_status(self):
        return self.num(lb=3, ub=3)
        # self.generator.bothify("#")

    def num(self, lb=1, ub=9):
        return self.generator.random.randint(lb, ub)

    def approval_date(self):
        pattern = '%Y-%m-%d'
        return self.generator.date_time_between().strftime(pattern)

    def approval_amount(self):
        return self.generator.amount()

    def interest_rate(self):
        return self.generator.f_interest_rate(1)

    def application_amount(self):
        return self.generator.amount(10, 0)

# coding=utf-8

from __future__ import unicode_literals

import csv

import six

from .. import BaseProvider

localized = False
csv.register_dialect('faker-csv', csv.excel, quoting=csv.QUOTE_ALL)


# create new provider class. Note that the class name _must_ be ``Provider``.
class Provider(BaseProvider):

    def cmhc_int(self):
        return self.num(lb=0, ub=10000)

    def cmhc_int(self, l=0, u=9):
        return self.num(lb=l, ub=u)

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

    # Raghav: Overriding row generating method to work with simpler schema/constraint input

    def gen_schema_data(self, schema, dialect='faker-csv', header=None,
                        num_rows=10, include_row_ids=False, **fmtparams):
        """
        Generic method that returns delimiter-separated values

        This method's signature is mostly the same as the signature of csv.writer with some
        additional keyword arguments for controlling data generation. Dialects and formatting
        parameters are passed to the csv.writer object during its instantiation.

        :param dialect: Name of a registered csv.Dialect subclass, defaults to 'faker-csv'
                        which is a subclass of csv.excel with full quoting enabled
        :param header: List of strings that will serve as the header row if supplied
        :param data_columns: List of string tokens that will be passed to the pystr_format
                             provider method during data generation
        :param num_rows: Number of rows of data to generate
        :param include_row_ids: True to include a sequential row ID column
        :param fmtparams: Formatting parameters expected by csv.writer
        :return: Delimiter-separated values, csv by default
        """

        if not schema.length() > 0:
            raise ValueError('`schema` must be defined ')
        if not isinstance(num_rows, int) or num_rows <= 0:
            raise ValueError('`num_rows` must be a positive integer')
        if not isinstance(data_columns, (list, tuple)):
            raise TypeError('`data_columns` must be a tuple or a list')
        if header is not None:
            if not isinstance(header, (list, tuple)):
                raise TypeError('`header` must be a tuple or a list')
            if len(header) != len(data_columns):
                raise ValueError('`header` and `data_columns` must have matching lengths')

        dsv_buffer = six.StringIO()
        writer = csv.writer(dsv_buffer, dialect=dialect, **fmtparams)

        if header:
            if include_row_ids:
                header = list(header)
                header.insert(0, 'ID')
            writer.writerow(header)

        for row_num in range(1, num_rows + 1):
            if six.PY2:
                row = [self.generator.pystr_format(column).encode('utf-8') for column in data_columns]
            else:
                row = [self.generator.pystr_format(column) for column in data_columns]
            if include_row_ids:
                row.insert(0, str(row_num))

            writer.writerow(row)

        dsv = dsv_buffer.getvalue()
        if six.PY2:
            return dsv.decode('utf-8')
        return dsv

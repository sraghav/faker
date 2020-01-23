from faker.factory import *

Faker = Factory.create

fake = Faker('en')
# fake.seed(42)

# print(fake.name())

# print(fake.age())

# def csv(self, header=None, data_columns=('{{name}}', '{{address}}'), num_rows=10, include_row_ids=False):

"""
 write a mapping piece for mapping semantic cols from business tables to equivalent faker types
 
 e.g pool number should map to int(8) or ########
 pool issuercode to XX####
 ppol type - #, range => (1,3)
 pool status - #, range => (3,3)
 approval date
 approval amount
 
 
 
"""
cols = (
    '{{issuercode}}',
    '{{pool_number}}',
    '{{pool_type}}',
    '{{pool_status}}',
    '{{approval_date}}',
    '{{approval_amount}}',
    '{{interest_rate}}',
    '{{application_amount}}'
)

d = fake.psv(header=cols, data_columns=cols, num_rows=500)
print(d)

# from faker import Faker
# fake = faker('en')


# c.seed(42)
#
# print(c.name())
#
# # 'Lucy Cechtelar'
#
#
# #c.age()

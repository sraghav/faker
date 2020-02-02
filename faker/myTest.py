from properties.p import Property

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

p = Property()
props = p.load_property_files('pool.schema')

# p.load(open('pool.schema'))
print(props)
print("===")
header = []
for key in props.keys():
    val = props.get(key)
    # print(key+"::"+val)
    header.append(key)

    # print(f"in {key} the val is {val}; found format at {val.find('format')}")
    if val.find('format') >= 0:
        f = val.split(":")
        # print("found format :: " + str(f))
        val2 = fake.bothify(f[1]).upper()
    elif val.find('range') >= 0:
        r = val.split(":")
        # print("range ::" + str(r[1]))
        r1 = r[1].split('(')
        r2 = r1[1].split(',')
        # print("r2 ::" +str(r2))
        lb = int(r2[0])
        ub = int(r2[1].rstrip(")"))

        # print(f"bounds of the range => {lb}, {ub}")
        val2 = fake.random_int(lb, ub)

    print(f"key = {key}, value = {val2}")

print(f"Header = {header}")

cols = (header)
#     '{{issuercode}}',
#     '{{pool_number}}',
#     '{{pool_type}}',
#     '{{pool_status}}',
#     '{{approval_date}}',
#     '{{approval_amount}}',
#     '{{interest_rate}}',
#     '{{application_amount}}'
# )
# print(type(header))
d = fake.psv(header=header, data_columns=header, num_rows=5)
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

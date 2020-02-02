from faker import utils
from faker.factory import *
from faker.utils import *

Faker = Factory.create

fake = Faker('en')
# fake.seed(42)

# print(fake.name())

# print(fake.age())

# def csv(self, header=None, data_columns=('{{name}}', '{{address}}'), num_rows=10, include_row_ids=False):

debug = False

"""
 write a mapping piece for mapping semantic cols from business tables to equivalent faker types
 
 e.g pool number should map to int(8) or ########
 pool issuercode to XX####
 ppol type - #, range => (1,3)
 pool status - #, range => (3,3)
 approval date
 approval amount
 
 
 
"""
debug = True


def log(msg, debug=debug):
    utils.log(msg, debug=debug)


p = getProperties("pool.schema", debug=False)

print(type(p))
header = []


def chkConstraint(constr):
    cons, consVal = '', ''
    for c in constraints:
        log(f"checking {constr} for {c}")
        if len(constr) > 1:
            cons = constr[1]
            log(f"cons is {cons}")
            if cons.find(c) >= 0:
                # cons = c
                val = cons.split("(")
                log("=========found constraint == " + val[0])
                log(f">>{val[1].strip(')')}<<")
                consVal = val[1].strip(')')
                cons = val[0]

                # exit(0)
    return cons, consVal


datatypes = ["boolean", "decimal", "amount", "int", "float", "double", "string", "date", "datetime", "timestamp"]

constraints = ["range", "format"]

TypeMapping = [["amount", "decimal"],
               ["format", "range"]]

for key in p.keys():
    val = p[key]
    log(key + "===" + val)
    header.append(key)
    log("Starting to parse the type/constraint")
    typ = val.split(":")

    if typ[0] not in datatypes:  # and len(typ) != 2:
        ErrMsg = f"Invalid data type : {typ}"
        log(ErrMsg)
        raise ValueError(ErrMsg)
    dtype = typ[0]
    log(f"Checking if there is a constraint for {key}. The type for this was {val}")
    cons, spec = chkConstraint(typ)

    log(f"constraint for {key} is {cons} with spec {spec}")
    #
    # log("typ 0 => "+ typ[0].strip())
    # if typ[0] in datatypes:
    #     dtype = typ[0]
    #     if len(typ[1].strip()) > 0:
    #         if typ[1] in constraints:
    #             cons = typ[1]
    # elif typ[0] in constraints:
    #     if typ[1].find("format")>0:
    #         dtype = "string"
    #         cons = typ[1][7:]
    #     elif typ[1].find("range") > 0:
    #         dtype = "number"
    #         cons=typ[1][6:]
    #
    #
    #
    # #constraint = typ[0]
    #
    # log(dtype)
    # log(cons)
    try:
        log(str(typ[1]))
    except:
        pass

    # log("data type =", str(typ[0]))
    # log("constraint =", str(typ[1]))

    log(f"header => {header}")

cols = (
    '{{cmhc_int}}',
    '{cmhc_int(1,9)}',
    '{{pool_number}}',
    '{{pool_type}}',
    '{{pool_status}}',
    '{{approval_date}}',
    '{{approval_amount}}',
    '{{interest_rate}}',
    '{{application_amount}}'
)
print(type(header))
d = fake.psv(header=header, data_columns=cols, num_rows=5)
print(d)

# print("===")
# header=[]
# for key in props.keys():
#     val = props.get(key)
#
#     print(key+"::"+val)
#     header.append(key)
#
#     val1,val2 ='',''
#     #print(f"in {key} the val is {val}; found format at {val.find('format')}")
#     if val.find('format') >= 0:
#         f = val.split(":")
#         #print("found format :: " + str(f))
#         val2 = fake.bothify(f[1]).upper()
#     elif val.find('range') >= 0:
#         r = val.split(":")
#         #print("range ::" + str(r[1]))
#         r1 = r[1].split('(')
#         r2 = r1[1].split(',')
#         #print("r2 ::" +str(r2))
#         lb = int(r2[0])
#         ub = int(r2[1].rstrip(")"))
#
#         #print(f"bounds of the range => {lb}, {ub}")
#         val2 = fake.random_int(lb, ub)
#
#     print(f"key = {key}, value = {val2}")
#
# # end for loop
# print(f"Header = {header}")
# cols = (header)
#
# # cols = (
# #     '{{issuercode}}',
# #     '{{pool_number}}',
# #     '{{pool_type}}',
# #     '{{pool_status}}',
# #     '{{approval_date}}',
# #     '{{approval_amount}}',
# #     '{{interest_rate}}',
# #     '{{application_amount}}'
# # )
# #print(type(header))
# d = fake.psv(header=cols, data_columns=cols, num_rows=5)
# print(d)

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

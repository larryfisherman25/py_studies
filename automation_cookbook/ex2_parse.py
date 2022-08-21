from parse import parse
from decimal import Decimal

def price(string):
    return Decimal(string)

LOG = '[2018-05-06T12:58:00.714611] - SALE - PRODUCT: 1345 - PRICE: $09.99'
FORMAT = '[{date:ti}] - SALE - PRODUCT: {product:d} - PRICE: ${price:price}'

result = parse(FORMAT, LOG, {'price':price})
print(result)
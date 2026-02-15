from decimal import Decimal, getcontext

getcontext().prec = 28
Decimal(10)

Decimal('3.14')

Decimal(3.14)

Decimal((0, (3, 1, 4), -2))

Decimal(str(2.0 ** 0.5))

Decimal(2) ** Decimal('0.5')

Decimal('NaN')

Decimal('-Infinity')
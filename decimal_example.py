from decimal import Decimal
a=input("Enter a decimal:")
b=input("Enter second decimal:")
sum_two_decimals=Decimal(a)+Decimal(b)
print("THIS IS THE SUM OF THE DECIMALS!:")
print(sum_two_decimals)

sum_two_mul=Decimal(a) * Decimal(b)
print("THIS IS THE MULTIPLICATION OF THE DECIMALS!:")
print(sum_two_mul)

sum_two_sub=Decimal(a) - Decimal(b)
print("THIS IS THE SUBTRACTION OF THE DECIMALS!:")
print(sum_two_sub)


sum_two_div=Decimal(a) / Decimal(b)
print("THIS IS THE DIVISON OF THE DECIMALS!:")
print(sum_two_div)

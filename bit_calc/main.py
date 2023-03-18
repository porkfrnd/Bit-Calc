from .Bitwise_operators import *


def add(a, b):
	while b != 0:
		carry = and_func(a,b)
		a = xor_func(a,b)
		b = carry << 1
	return a

def subtract(a, b):
	while b != 0:
		borrow = and_func(not_func(a),b)
		a = xor_func(a,b)
		b = borrow << 1
	return a

def multiply(a,b):
	x = b
	for i in range(a-1):
		b = add(b,x)
	return b

def power(a, b):
	x = a
	for i in range(b-1):
		a = multiply(a,x)
	return a

def divide(dividend, divisor):
	if divisor == 0:
		raise ZeroDivisionError("division by zero")
	quotient = 0
	sign = 1
	if (dividend < 0) != (divisor < 0):
		sign = -1
	dividend = abs(dividend)
	divisor = abs(divisor)
	while dividend >= divisor:
		dividend = subtract(dividend, divisor)
		quotient = add(quotient, 1)
	quotient =  multiply(quotient,sign)
	return quotient, dividend

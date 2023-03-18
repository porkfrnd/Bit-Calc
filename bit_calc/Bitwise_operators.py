def bin_func(a,b=None):
	if b:
		a_bin = "{0:b}".format(a)
		b_bin = "{0:b}".format(b)
		a_len = len(a_bin)
		b_len = len(b_bin)
		if a_len > b_len:
				req_len = a_len - b_len
				b_bin = f"{'0'*req_len}{b_bin}"
		elif b_len > a_len:
				req_len = b_len - a_len
				a_bin = f"{'0'*req_len}{a_bin}"
		return a_bin, b_bin
	else:
		a_bin = "{0:b}".format(a)
		return a_bin
	
def and_func(a,b):
	a_bin, b_bin = bin_func(a,b)
	result_bin = "0"
	for x, y in zip(a_bin,b_bin):
		if x == "1" and y == "1":
			result_bin += "1"
		else:
			result_bin += "0"
	result = int(result_bin,2)
	return result

def xor_func(a, b):
	a_bin, b_bin = bin_func(a,b)
	result_bin = "0"
	for x, y in zip(a_bin,b_bin):
		if x == "1" and y == "1":
			result_bin += "0"
		elif (x == "1" and y == "0") or (x == "0" and y == "1"):
			result_bin += "1"
		elif x == "0" and y == "0":
			result_bin += "0"
	result = int(result_bin,2)
	return result

def not_func(a):
	a_bin = bin_func(a)
	result_bin = ""
	for x in a_bin:
		if x == "0":
			result_bin += "1"
		elif x == "1":
			result_bin += "0"
	result = int(result_bin,2)
	return result
	
		

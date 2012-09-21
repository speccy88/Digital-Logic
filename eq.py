# -*- coding: latin-1 -*-

def getEquation():
	eq_raw = raw_input("Entrer l'équation:")
	eq_validated = validateEquation(eq_raw)
	return eq_validated

def evalEquation(eq,tail=None):
	table = {'a':True,'b':False,'c':True}
	finished = False
	while not finished:
		op, firstCase = getOp(eq)
		if firstCase:
			loc = eq.find(op)
			in1 = eq[0:loc]
			eq = eq[loc+1:]
			op2, tmp = getOp(eq)
			if len(eq)==1:
				in2=eq
			else:
				loc = eq.find(op2)
				in2 = eq[0:loc]
				eq = eq[loc:]
			if op == "|":
				res = table[in1] or table[in2]
			elif op == "&":
				res = table[in1] and table[in2]
			op = op2

		if len(eq) > 2:
			eq2 = eq[1:]
			op2, tmp = getOp(eq2)
			loc = eq2.find(op2)
			in3 = eq2[0:loc]
			eq = eq2[1:]

		else:
			in3 = eq[1:]
			if in3 == "":
				if tail==None:
					return res
				in3 = tail
				if op == "|":
					res = res or tail
				elif op == "&":
					res = res and tail
				return res
			finished = True

		if op == "|":
			res = res or table[in3]
		elif op == "&":
			res = res and table[in3]
		
	return res

def getOp(eq):	
	and_loc = eq.find("&")
	or_loc = eq.find("|")
	if or_loc == 0 or and_loc == 0:
		firstCase = False
	else:
		firstCase = True

	if and_loc == -1:
		op = "|"
	elif or_loc == -1:
		op = "&"
	elif or_loc > and_loc:
		op = "&"
	elif and_loc > or_loc:
		op = "|"
	else:
		raise Exception("Operator not recognized")
	return op, firstCase

def validateEquation(eq):
	global depth
	depth = eq.count("(")
	if depth != eq.count(")"):
		raise Exception("Bracket Error")
	if depth == 0:
		raise Exception("No Brackets")
	return eq

def separate(eq):
	b = eq.rfind("(")
	e = eq.find(")")
	content = eq[b+1:e]
	rest = eq[0:b]+eq[e+1:]
	if rest=="()":
		raise Exception("Unused Bracket")
	return content, rest

def test1():
	rest = getEquation()
	print rest
	print "dep",depth

	while rest!="":
		content, rest = separate(rest)
		print content
		print evalEquation(content)

test1()

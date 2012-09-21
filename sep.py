def separate(eq):
	ret = []
	nxt_eq = eq
	while True:
		d = 0
		e = nxt_eq.find(")")
		finished = False
		while not finished:
			b = nxt_eq.find("(")
			content = nxt_eq[b+1:e+1]
			print d,":", b,e
			print "c",content
			if b != -1:
				d=d+1
				if e > b:
					w = len(content)
					if content[0] == '(' and content[w-1] == ')':
						ret.append(content[1:-1])
						print "Appending", content
						nxt_eq = eq[e+1:]
						print nxt_eq
						e = nxt_eq.find(")")
					else:
						nxt_eq = content
				else:
					print "Not Appending"
					finished = True
			else:
				print "no more ("
				finished = True
			
		return ret
		break
			

table = {'a':True,'b':False,'c':True,'d':False}
eq = "(a|b|((d|c)|(a&b)))&(d|a)&c"

print eq
for i in separate(eq):	
	print "=======\n",i



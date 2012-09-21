#!/usr/bin/env python

class LogicFunc:
	def __init__(self, inputs, outputs=1, auto=True):
		self.inputs = inputs
		self.outputs = outputs
		self.i = []
		self.o = []
		if auto:
			self.autoName()
		else:
			self.promptName()

	def __str__(self):
		self.ret = []
		for i in range(self.outputs):
			self.ret.append(self.o[i]+"("+",".join(self.i)+")")
		return str(self.ret)

	def autoName(self):
		self.alpha = map(chr, range(97, 123))
		for name in range(self.inputs):
			self.i.append(self.alpha[name])
		
		for name in range(self.outputs):
			self.o.append("y"+str(name))
	
	def promptName(self):
		for name in range(self.inputs):
			self.i.append(raw_input("Enter name for input "+str(name)+":"))
		
		for name in range(self.outputs):
			self.o.append(raw_input("Enter name for output "+str(name)+":"))

	def setEquation(self):
		pass

	def createTable(self):
		pass

	def drawTable(self):
		self.w = 1
		for x in lf1.o:
			self.w=self.w+len(x)
			self.w=self.w+1
		for x in lf1.i:
			self.w=self.w+len(x)
			self.w=self.w+1
	
		print self.w*'='
		line = []
		line.append('|')
		line.append("|".join(self.i))
		line.append('|')
		line.append("|".join(self.o))
		line.append('|')
		linep = "".join(line)
		print str(linep)
			
		print self.w*'-'

		blank = []
		for x in linep:
			if x == "|":
				blank.append(x)
			else:
				blank.append(" ")
		blankp = "".join(blank)

		for x in range(2**len(self.i)):
			print blankp
		print self.w*'='
		

print("Logic function testing")
lf1 = LogicFunc(3,1,auto=True)
print lf1
lf1.drawTable()


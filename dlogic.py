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
			
print("Logic function test")
lf1 = LogicFunc(3,2,auto=True)
print lf1


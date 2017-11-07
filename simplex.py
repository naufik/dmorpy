import numpy

class LinearMapping:
	__cv = ()
	def __init__(self, coefficients):
		for item in coefficients:
			self.__cv = self.__cv + (item)

	def apply(self, vector):
		if len(self) != len(vector):
			print("Invalid Dimension")
			return None
		return sum([i*j for i,j in zip(__cv,vector)])

	def getDimensions(self):
		return len(self.__cv)

class LinearConstraint:
	__TYPEDICT = {"e": "=", "g": ">=", "l": "<="}
	__itype = 'e'
	__cv = ()
	__rhs = None
	def __init__(self, t, coefficients, rhs):
		if t in ('e', 'g', 'l'): 
			self.__itype = t
		for item in coefficients:
			self.__cv = self.__cv + (item)
		if type(rhs) in (int,float):
			this.__rhs = rhs

	def getVector(self):
		return self.__cv

	def getType(self):
		return self.__itype

	def print(self):
		return "+".join([i for i in self.__cv]) + self.__TYPEDICT[self.__t] + self.__rhs 

class LinearProgram:
	__mapping = None
	__constraints = []

	def __init__(self, f, *constraints):
		#First initialize the constraints and the things
		for c in constraints:
			if type(c) == LinearConstraint:
				self.__constraints.append(c)
		pass
		if type(f) == LinearMapping:
			self.__mapping = f

		#Now we normalize
		maxl = max([len(i.getVector()) for i in self.__constraints] + [self.__mapping.getDimensions()])
		self.__mapping.expand(maxl - self.__mapping.getDimensions())
		[i.expand(maxl - len(i.getVector())) for i in __constraints]

	def canonical(self):
		


def simplexSolve(program):

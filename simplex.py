import numpy

class LinearMapping:
	__cv = ()
	def __init__(self, *coefficients):
		for item in coefficients:
			self.__cv = self.__cv + (item,)
		return None

	def apply(self, vector):
		if len(self) != len(vector):
			print("Invalid Dimension")
			return None
		return sum([i*j for i,j in zip(__cv,vector)])

	def getVector(self):
		return self.__cv

	def getDimensions(self):
		return len(self.__cv)

	def expand(self, newdim):
		self.__cv = self.__cv + (0,) * (newdim - len(self.__cv))
		return None


class LinearConstraint:
	__TYPEDICT = {"e": "=", "g": ">=", "l": "<="}
	__itype = 'e'
	__cv = ()
	__rhs = None
	def __init__(self, t, coefficients, rhs):
		if t in ('e', 'g', 'l'): 
			self.__itype = t
		else:
			self.__itype = 'l'
		for item in coefficients:
			self.__cv = self.__cv + (item,)
		if type(rhs) in (int,float):
			self.__rhs = rhs
		return None

	def getVector(self):
		return self.__cv

	def getType(self):
		return self.__itype

	def setType(self, newtype):
		if newtype in ("e","g","l"):
			self.__itype = newtype

	def print(self):
		print(" + ".join([str(self.__cv[i]) + "x_{0}".format(i) for i in range(len(self.__cv))]) + " " + self.__TYPEDICT[self.__itype] + " " + str(self.__rhs))

	def expand(self, newdim):
		self.__cv = self.__cv + (0,) * (newdim - len(self.__cv))
		return None

	def addSlack(self, index, numconst):
		self.__cv = self.__cv + tuple([1 if i == index else 0 for i in range(numconst)])
		return None

class LinearProgram:
	__mapping = None
	__canon = False
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
		[i.expand(maxl - len(i.getVector())) for i in self.__constraints]

	def canonical(self):
		for k in self.__constraints:
			self.__makeCanonical(k);
	
	def __makeCanonical(self,const):
		numconst = len(self.__constraints)
		for i in range(numconst):
			self.__constraints[i].addSlack(i,numconst)
			self.__constraints[i].setType("e")

	def printProg(self):
		print(self.__mapping.getVector())
		for c in self.__constraints:
			c.print()

x = LinearProgram(LinearMapping(4,-2,0,1),LinearConstraint("l",(0,1,0,0),32),LinearConstraint("l",(0,9,2,3),44))
x.printProg()
x.canonical()
x.printProg()
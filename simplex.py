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
		sgn = -1 if self.__itype == "g" else 1
		self.__cv = self.__cv + tuple([sgn if i == index else 0 for i in range(numconst)])
		return None
	def getRHS(self):
		return self.__rhs

class LinearProgram:
	__mapping = None
	__canon = False
	__constraints = []
	__slacks = ()
	__artificials = ()

	def __init__(self, f, *constraints):
		#First initialize the constraints and the things
		for c in constraints:
			if type(c) == LinearConstraint:
				self.__constraints.append(c)
		pass
		if type(f) == LinearMapping:
			self.__mapping = f
		self.normalize()

	def normalize(self):
		maxl = max([len(i.getVector()) for i in self.__constraints] + [self.__mapping.getDimensions()])
		self.__mapping.expand(maxl)
		[i.expand(maxl - len(i.getVector())) for i in self.__constraints]

	def canonical(self):
		numconst = len(self.__constraints)
		for i in range(numconst):
			self.__constraints[i].addSlack(i,numconst)
			self.__constraints[i].setType("e")
		self.__canon = True
		self.normalize()

	def isCanonical(self):
		return self.__canon

	def printProg(self):
		print("max z = " + " + ".join([str(i) for i in self.__mapping.getVector()]))
		for c in self.__constraints:
			c.print()

	def getMapping(self):
		return self.__mapping

	def getConstraints(self):
		return [k for k in self.__constraints]



def simplex(program):
	def pivot(co, cost, rhs, fxc):
		pass
	if not program.isCanonical():
		program.canonical()
	flattenedConstraints = [a for a in [list(c.getVector()) for c in program.getConstraints()]]

	#initialization of the important matrices
	coefficients = numpy.matrix(flattenedConstraints)
	cost = -numpy.matrix(list(program.getMapping().getVector()))
	rhs = numpy.matrix([c.getRHS() for c in program.getConstraints()]).transpose()
	fxc = 0

	#start pivoting
	if numpy.argwhere(cost < 0).shape != (0,0):
		col = numpy.argwhere(cost == min(cost.A[0]))[0][1]
		#do the ratio test
		for i in range(len(s.A[0]):

			rats = (rhs / coefficients[:,col]

		print(rhs)

l = LinearProgram(LinearMapping(1/4,5/4),LinearConstraint("l",(1,1), 4),LinearConstraint("l",(1,0),0.5))
simplex(l)

from PySide import QtGui, QtCore

class QDoubleValidator(QtGui.QDoubleValidator):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDoubleValidator,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def bottom(self):
		"""
		This property holds the validators minimum acceptable value.
		By default, this property contains a value of -infinity.
		"""
		res = super(QDoubleValidator,self).bottom()
		isinstance(res,QtCore.double)
		return res
	#----------------------------------------------------------------------
	def decimals(self):
		"""
		This property holds the validators maximum number of digits after the decimal point.
		By default, this property contains a value of 1000.
		"""
		res = super(QDoubleValidator,self).decimals()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def notation(self):
		"""
		This property holds the notation of how a string can describe a number.
		By default, this property is set to ScientificNotation .
		"""
		res = super(QDoubleValidator,self).notation()
		isinstance(res,QtGui.QDoubleValidator.Notation)
		return res
	#----------------------------------------------------------------------
	def top(self):
		"""
		This property holds the validators maximum acceptable value.
		By default, this property contains a value of infinity.
		"""
		res = super(QDoubleValidator,self).top()
		isinstance(res,QtCore.double)
		return res
	#----------------------------------------------------------------------
	def setBottom(self,arg__1):
		"""
		setBottom(arg__1)
			arg__1=QtCore.double

		This property holds the validators minimum acceptable value.
		By default, this property contains a value of -infinity.
		"""
		res = super(QDoubleValidator,self).setBottom(arg__1)
		return res
	#----------------------------------------------------------------------
	def setDecimals(self,arg__1):
		"""
		setDecimals(arg__1)
			arg__1=QtCore.int

		This property holds the validators maximum number of digits after the decimal point.
		By default, this property contains a value of 1000.
		"""
		res = super(QDoubleValidator,self).setDecimals(arg__1)
		return res
	#----------------------------------------------------------------------
	def setNotation(self,arg__1):
		"""
		setNotation(arg__1)
			arg__1=QtGui.QDoubleValidator.Notation

		This property holds the notation of how a string can describe a number.
		By default, this property is set to ScientificNotation .
		"""
		res = super(QDoubleValidator,self).setNotation(arg__1)
		return res
	#----------------------------------------------------------------------
	def setRange(self,bottom,top,decimals=None):
		"""
		setRange(bottom,top,decimals=None)
			bottom=QtCore.double
			top=QtCore.double
			decimals=QtCore.int

		Sets the validator to accept doubles from minimum to maximum inclusive, with at most decimals digits after the decimal point.
		"""
		res = super(QDoubleValidator,self).setRange(bottom,top,decimals)
		return res
	#----------------------------------------------------------------------
	def setTop(self,arg__1):
		"""
		setTop(arg__1)
			arg__1=QtCore.double

		This property holds the validators maximum acceptable value.
		By default, this property contains a value of infinity.
		"""
		res = super(QDoubleValidator,self).setTop(arg__1)
		return res

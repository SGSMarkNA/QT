from PySide import QtGui, QtCore

class QIntValidator(QtGui.QIntValidator):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QIntValidator,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def bottom(self):
		"""
		This property holds the validators lowest acceptable value.
		By default, this propertys value is derived from the lowest signed integer available (typically -2147483647).
		"""
		res = super(QIntValidator,self).bottom()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def top(self):
		"""
		This property holds the validators highest acceptable value.
		By default, this propertys value is derived from the highest signed integer available (typically 2147483647).
		"""
		res = super(QIntValidator,self).top()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def setBottom(self,arg__1):
		"""
		setBottom(arg__1)
			arg__1=QtCore.int

		This property holds the validators lowest acceptable value.
		By default, this propertys value is derived from the lowest signed integer available (typically -2147483647).
		"""
		res = super(QIntValidator,self).setBottom(arg__1)
		return res
	#----------------------------------------------------------------------
	def setRange(self,bottom,top):
		"""
		setRange(bottom,top)
			bottom=QtCore.int
			top=QtCore.int

		Sets the range of the validator to only accept integers between bottom and top inclusive.
		"""
		res = super(QIntValidator,self).setRange(bottom,top)
		return res
	#----------------------------------------------------------------------
	def setTop(self,arg__1):
		"""
		setTop(arg__1)
			arg__1=QtCore.int

		This property holds the validators highest acceptable value.
		By default, this propertys value is derived from the highest signed integer available (typically 2147483647).
		"""
		res = super(QIntValidator,self).setTop(arg__1)
		return res

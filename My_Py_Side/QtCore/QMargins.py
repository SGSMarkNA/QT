from PySide import QtGui, QtCore

class QMargins(QtCore.QMargins):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QMargins,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def bottom(self):
		"""
		Returns the bottom margin.
		"""
		res = super(QMargins,self).bottom()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if all margins are is 0; otherwise returns false.
		"""
		res = super(QMargins,self).isNull()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def left(self):
		"""
		Returns the left margin.
		"""
		res = super(QMargins,self).left()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def right(self):
		"""
		Returns the right margin.
		"""
		res = super(QMargins,self).right()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def top(self):
		"""
		Returns the top margin.
		"""
		res = super(QMargins,self).top()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,m2):
		"""
		__ne__(m2)
			m2=QtCore.QMargins


		"""
		res = super(QMargins,self).__ne__(m2)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,m2):
		"""
		__eq__(m2)
			m2=QtCore.QMargins


		"""
		res = super(QMargins,self).__eq__(m2)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def setBottom(self,bottom):
		"""
		setBottom(bottom)
			bottom=QtCore.int

		Sets the bottom margin to bottom .
		"""
		res = super(QMargins,self).setBottom(bottom)
		return res
	#----------------------------------------------------------------------
	def setLeft(self,left):
		"""
		setLeft(left)
			left=QtCore.int

		Sets the left margin to left .
		"""
		res = super(QMargins,self).setLeft(left)
		return res
	#----------------------------------------------------------------------
	def setRight(self,right):
		"""
		setRight(right)
			right=QtCore.int

		Sets the right margin to right .
		"""
		res = super(QMargins,self).setRight(right)
		return res
	#----------------------------------------------------------------------
	def setTop(self,top):
		"""
		setTop(top)
			top=QtCore.int

		Sets the Top margin to Top .
		"""
		res = super(QMargins,self).setTop(top)
		return res

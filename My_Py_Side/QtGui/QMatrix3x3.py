from PySide import QtGui, QtCore

class QMatrix3x3(QtGui.QMatrix3x3):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QMatrix3x3,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __reduce__(self):
		"""

		"""
		res = super(QMatrix3x3,self).__reduce__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __repr__(self):
		"""

		"""
		res = super(QMatrix3x3,self).__repr__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def data(self):
		"""

		"""
		res = super(QMatrix3x3,self).data()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def transposed(self):
		"""

		"""
		res = super(QMatrix3x3,self).transposed()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def fill(self,arg__1):
		"""
		fill(arg__1)
			arg__1=Object


		"""
		res = super(QMatrix3x3,self).fill(arg__1)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,arg__1):
		"""
		__ne__(arg__1)
			arg__1=QtGui.QMatrix3x3


		"""
		res = super(QMatrix3x3,self).__ne__(arg__1)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __imul__(self,arg__1):
		"""
		__imul__(arg__1)
			arg__1=QtCore.qreal


		"""
		res = super(QMatrix3x3,self).__imul__(arg__1)
		isinstance(res,QtGui.QMatrix3x3)
		return res
	#----------------------------------------------------------------------
	def __iadd__(self,arg__1):
		"""
		__iadd__(arg__1)
			arg__1=QtGui.QMatrix3x3


		"""
		res = super(QMatrix3x3,self).__iadd__(arg__1)
		isinstance(res,QtGui.QMatrix3x3)
		return res
	#----------------------------------------------------------------------
	def __isub__(self,arg__1):
		"""
		__isub__(arg__1)
			arg__1=QtGui.QMatrix3x3


		"""
		res = super(QMatrix3x3,self).__isub__(arg__1)
		isinstance(res,QtGui.QMatrix3x3)
		return res
	#----------------------------------------------------------------------
	def __idiv__(self,arg__1):
		"""
		__idiv__(arg__1)
			arg__1=QtCore.qreal


		"""
		res = super(QMatrix3x3,self).__idiv__(arg__1)
		isinstance(res,QtGui.QMatrix3x3)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,arg__1):
		"""
		__eq__(arg__1)
			arg__1=QtGui.QMatrix3x3


		"""
		res = super(QMatrix3x3,self).__eq__(arg__1)
		isinstance(res,QtCore.bool)
		return res
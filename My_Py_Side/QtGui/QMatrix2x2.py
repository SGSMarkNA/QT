from PySide import QtGui, QtCore

class QMatrix2x2(QtGui.QMatrix2x2):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QMatrix2x2,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __reduce__(self):
		"""

		"""
		res = super(QMatrix2x2,self).__reduce__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __repr__(self):
		"""

		"""
		res = super(QMatrix2x2,self).__repr__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def data(self):
		"""

		"""
		res = super(QMatrix2x2,self).data()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def transposed(self):
		"""

		"""
		res = super(QMatrix2x2,self).transposed()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def fill(self,arg__1):
		"""
		fill(arg__1)
			arg__1=Object


		"""
		res = super(QMatrix2x2,self).fill(arg__1)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,arg__1):
		"""
		__ne__(arg__1)
			arg__1=QtGui.QMatrix2x2


		"""
		res = super(QMatrix2x2,self).__ne__(arg__1)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __imul__(self,arg__1):
		"""
		__imul__(arg__1)
			arg__1=QtCore.qreal


		"""
		res = super(QMatrix2x2,self).__imul__(arg__1)
		isinstance(res,QtGui.QMatrix2x2)
		return res
	#----------------------------------------------------------------------
	def __iadd__(self,arg__1):
		"""
		__iadd__(arg__1)
			arg__1=QtGui.QMatrix2x2


		"""
		res = super(QMatrix2x2,self).__iadd__(arg__1)
		isinstance(res,QtGui.QMatrix2x2)
		return res
	#----------------------------------------------------------------------
	def __isub__(self,arg__1):
		"""
		__isub__(arg__1)
			arg__1=QtGui.QMatrix2x2


		"""
		res = super(QMatrix2x2,self).__isub__(arg__1)
		isinstance(res,QtGui.QMatrix2x2)
		return res
	#----------------------------------------------------------------------
	def __idiv__(self,arg__1):
		"""
		__idiv__(arg__1)
			arg__1=QtCore.qreal


		"""
		res = super(QMatrix2x2,self).__idiv__(arg__1)
		isinstance(res,QtGui.QMatrix2x2)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,arg__1):
		"""
		__eq__(arg__1)
			arg__1=QtGui.QMatrix2x2


		"""
		res = super(QMatrix2x2,self).__eq__(arg__1)
		isinstance(res,QtCore.bool)
		return res

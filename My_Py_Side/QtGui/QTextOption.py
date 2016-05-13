from PySide import QtGui, QtCore

class QTextOption(QtGui.QTextOption):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextOption,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtGui.QTextOption::Tab

		Returns true if tab other is not equal to this tab; otherwise returns false.
		"""
		res = super(QTextOption,self).__ne__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtGui.QTextOption::Tab

		Returns true if tab other is equal to this tab; otherwise returns false.
		"""
		res = super(QTextOption,self).__eq__(other)
		isinstance(res,QtCore.bool)
		return res

from PySide import QtGui, QtCore

class QGenericArgument(QtCore.QGenericArgument):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGenericArgument,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def data(self):
		"""
		Returns the data set in the constructor.
		"""
		res = super(QGenericArgument,self).data()
		isinstance(res,void)
		return res
	#----------------------------------------------------------------------
	def name(self):
		"""
		Returns the name set in the constructor.
		"""
		res = super(QGenericArgument,self).name()
		return res

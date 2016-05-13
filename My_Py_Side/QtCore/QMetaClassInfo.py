from PySide import QtGui, QtCore

class QMetaClassInfo(QtCore.QMetaClassInfo):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QMetaClassInfo,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def name(self):
		"""
		Returns the name of this item.
		"""
		res = super(QMetaClassInfo,self).name()
		return res
	#----------------------------------------------------------------------
	def value(self):
		"""
		Returns the value of this item.
		"""
		res = super(QMetaClassInfo,self).value()
		return res

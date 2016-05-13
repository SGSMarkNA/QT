from PySide import QtGui, QtCore

class QDynamicPropertyChangeEvent(QtCore.QDynamicPropertyChangeEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDynamicPropertyChangeEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def propertyName(self):
		"""
		Returns the name of the dynamic property that was added, changed or removed.
		"""
		res = super(QDynamicPropertyChangeEvent,self).propertyName()
		isinstance(res,QtCore.QByteArray)
		return res

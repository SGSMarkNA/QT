from PySide import QtGui, QtCore

class QAccessibleEvent(QtGui.QAccessibleEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QAccessibleEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def child(self):
		"""
		Returns the (1-based) index of the child to which the request applies
		If the child is 0, the request is for the widget itself.
		"""
		res = super(QAccessibleEvent,self).child()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def value(self):
		"""
		Returns the text set using PySide.QtGui.QAccessibleEvent.setValue() .
		"""
		res = super(QAccessibleEvent,self).value()
		return res
	#----------------------------------------------------------------------
	def setValue(self,aText):
		"""
		setValue(aText)
			aText=unicode

		Set the description or help text for the given PySide.QtGui.QAccessibleEvent.child() to text , thereby answering the request.
		"""
		res = super(QAccessibleEvent,self).setValue(aText)
		return res

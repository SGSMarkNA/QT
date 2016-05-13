from PySide import QtGui, QtCore

class QFocusEvent(QtGui.QFocusEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QFocusEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def gotFocus(self):
		"""
		Returns true if PySide.QtCore.QEvent.type() is QEvent.FocusIn ; otherwise returns false.
		"""
		res = super(QFocusEvent,self).gotFocus()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def lostFocus(self):
		"""
		Returns true if PySide.QtCore.QEvent.type() is QEvent.FocusOut ; otherwise returns false.
		"""
		res = super(QFocusEvent,self).lostFocus()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def reason(self):
		"""
		Returns the reason for this focus event.
		"""
		res = super(QFocusEvent,self).reason()
		isinstance(res,QtCore.Qt.FocusReason)
		return res

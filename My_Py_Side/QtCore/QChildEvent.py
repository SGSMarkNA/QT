from PySide import QtGui, QtCore

class QChildEvent(QtCore.QChildEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QChildEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def added(self):
		"""
		Returns true if PySide.QtCore.QEvent.type() is QEvent.ChildAdded ; otherwise returns false.
		"""
		res = super(QChildEvent,self).added()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def child(self):
		"""
		Returns the child object that was added or removed.
		"""
		res = super(QChildEvent,self).child()
		isinstance(res,QtCore.QObject)
		return res
	#----------------------------------------------------------------------
	def polished(self):
		"""
		Returns true if PySide.QtCore.QEvent.type() is QEvent.ChildPolished ; otherwise returns false.
		"""
		res = super(QChildEvent,self).polished()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def removed(self):
		"""
		Returns true if PySide.QtCore.QEvent.type() is QEvent.ChildRemoved ; otherwise returns false.
		"""
		res = super(QChildEvent,self).removed()
		isinstance(res,bool)
		return res

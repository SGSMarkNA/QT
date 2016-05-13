from PySide import QtGui, QtCore

class QDragMoveEvent(QtGui.QDragMoveEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDragMoveEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def answerRect(self):
		"""
		Returns the rectangle in the widget where the drop will occur if accepted
		You can use this information to restrict drops to certain places on the widget.
		"""
		res = super(QDragMoveEvent,self).answerRect()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def accept(self,r):
		"""
		accept(r)
			r=QtCore.QRect

		The same as PySide.QtGui.QDragMoveEvent.accept() , but also notifies that future moves will also be acceptable if they remain within the rectangle given on the widget
		This can improve performance, but may also be ignored by the underlying system.
		If the rectangle is empty, drag move events will be sent continuously
		This is useful if the source is scrolling in a timer event.
		"""
		res = super(QDragMoveEvent,self).accept(r)
		return res
	#----------------------------------------------------------------------
	def ignore(self,r):
		"""
		ignore(r)
			r=QtCore.QRect

		The opposite of the accept(const PySide.QtCore.QRect &) function
		Moves within the rectangle are not acceptable, and will be ignored.
		"""
		res = super(QDragMoveEvent,self).ignore(r)
		return res

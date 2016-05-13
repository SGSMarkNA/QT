from PySide import QtGui, QtCore

class QDropEvent(QtGui.QDropEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDropEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def acceptProposedAction(self):
		"""
		Sets the drop action to be the proposed action.
		"""
		res = super(QDropEvent,self).acceptProposedAction()
		return res
	#----------------------------------------------------------------------
	def dropAction(self):
		"""
		Returns the action to be performed on the data by the target
		This may be different from the action supplied in PySide.QtGui.QDropEvent.proposedAction() if you have called PySide.QtGui.QDropEvent.setDropAction() to explicitly choose a drop action.
		"""
		res = super(QDropEvent,self).dropAction()
		isinstance(res,QtCore.Qt.DropAction)
		return res
	#----------------------------------------------------------------------
	def keyboardModifiers(self):
		"""
		Returns the modifier keys that are pressed.
		"""
		res = super(QDropEvent,self).keyboardModifiers()
		isinstance(res,QtCore.Qt.KeyboardModifiers)
		return res
	#----------------------------------------------------------------------
	def mimeData(self):
		"""
		Returns the data that was dropped on the widget and its associated MIME type information.
		"""
		res = super(QDropEvent,self).mimeData()
		isinstance(res,QtCore.QMimeData)
		return res
	#----------------------------------------------------------------------
	def mouseButtons(self):
		"""
		Returns the mouse buttons that are pressed..
		"""
		res = super(QDropEvent,self).mouseButtons()
		isinstance(res,QtCore.Qt.MouseButtons)
		return res
	#----------------------------------------------------------------------
	def pos(self):
		"""
		Returns the position where the drop was made.
		"""
		res = super(QDropEvent,self).pos()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def possibleActions(self):
		"""
		Returns an OR-combination of possible drop actions.
		"""
		res = super(QDropEvent,self).possibleActions()
		isinstance(res,QtCore.Qt.DropActions)
		return res
	#----------------------------------------------------------------------
	def proposedAction(self):
		"""
		Returns the proposed drop action.
		"""
		res = super(QDropEvent,self).proposedAction()
		isinstance(res,QtCore.Qt.DropAction)
		return res
	#----------------------------------------------------------------------
	def source(self):
		"""
		If the source of the drag operation is a widget in this application, this function returns that source; otherwise it returns 0
		The source of the operation is the first parameter to the PySide.QtGui.QDrag object used instantiate the drag.
		This is useful if your widget needs special behavior when dragging to itself.
		"""
		res = super(QDropEvent,self).source()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def setDropAction(self,action):
		"""
		setDropAction(action)
			action=QtCore.Qt.DropAction


		"""
		res = super(QDropEvent,self).setDropAction(action)
		return res

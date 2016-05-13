from PySide import QtGui, QtCore

class QUndoView(QtGui.QUndoView):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QUndoView,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def cleanIcon(self):
		"""
		This property holds the icon used to represent the clean state..
		A stack may have a clean state set with QUndoStack.setClean()
		This is usually the state of the document at the point it was saved
		PySide.QtGui.QUndoView can display an icon in the list of commands to show the clean state
		If this property is a null icon, no icon is shown
		The default value is the null icon.
		"""
		res = super(QUndoView,self).cleanIcon()
		isinstance(res,QtGui.QIcon)
		return res
	#----------------------------------------------------------------------
	def emptyLabel(self):
		"""
		This property holds the label used for the empty state..
		The empty label is the topmost element in the list of commands, which represents the state of the document before any commands were pushed on the stack
		The default is the string <empty>.
		"""
		res = super(QUndoView,self).emptyLabel()
		return res
	#----------------------------------------------------------------------
	def group(self):
		"""
		Returns the group displayed by this view.
		If the view is not looking at group, this function returns 0.
		"""
		res = super(QUndoView,self).group()
		isinstance(res,QtGui.QUndoGroup)
		return res
	#----------------------------------------------------------------------
	def stack(self):
		"""
		Returns the stack currently displayed by this view
		If the view is looking at a PySide.QtGui.QUndoGroup , this the groups active stack.
		"""
		res = super(QUndoView,self).stack()
		isinstance(res,QtGui.QUndoStack)
		return res
	#----------------------------------------------------------------------
	def setCleanIcon(self,icon):
		"""
		setCleanIcon(icon)
			icon=QtGui.QIcon

		This property holds the icon used to represent the clean state..
		A stack may have a clean state set with QUndoStack.setClean()
		This is usually the state of the document at the point it was saved
		PySide.QtGui.QUndoView can display an icon in the list of commands to show the clean state
		If this property is a null icon, no icon is shown
		The default value is the null icon.
		"""
		res = super(QUndoView,self).setCleanIcon(icon)
		return res
	#----------------------------------------------------------------------
	def setEmptyLabel(self,label):
		"""
		setEmptyLabel(label)
			label=unicode

		This property holds the label used for the empty state..
		The empty label is the topmost element in the list of commands, which represents the state of the document before any commands were pushed on the stack
		The default is the string <empty>.
		"""
		res = super(QUndoView,self).setEmptyLabel(label)
		return res

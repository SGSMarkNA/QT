from PySide import QtGui, QtCore

class QUndoGroup(QtGui.QUndoGroup):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QUndoGroup,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def activeStack(self):
		"""
		Returns the active stack of this group.
		If none of the stacks are active, or if the group is empty, this function returns 0.
		"""
		res = super(QUndoGroup,self).activeStack()
		isinstance(res,QtGui.QUndoStack)
		return res
	#----------------------------------------------------------------------
	def canRedo(self):
		"""
		Returns the value of the active stacks QUndoStack.canRedo() .
		If none of the stacks are active, or if the group is empty, this function returns false.
		"""
		res = super(QUndoGroup,self).canRedo()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def canUndo(self):
		"""
		Returns the value of the active stacks QUndoStack.canUndo() .
		If none of the stacks are active, or if the group is empty, this function returns false.
		"""
		res = super(QUndoGroup,self).canUndo()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isClean(self):
		"""
		Returns the value of the active stacks QUndoStack.isClean() .
		If none of the stacks are active, or if the group is empty, this function returns true.
		"""
		res = super(QUndoGroup,self).isClean()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def redoText(self):
		"""
		Returns the value of the active stacks QUndoStack.redoText() .
		If none of the stacks are active, or if the group is empty, this function returns an empty string.
		"""
		res = super(QUndoGroup,self).redoText()
		return res
	#----------------------------------------------------------------------
	def stacks(self):
		"""
		Returns a list of stacks in this group.
		"""
		res = super(QUndoGroup,self).stacks()
		return res
	#----------------------------------------------------------------------
	def undoText(self):
		"""
		Returns the value of the active stacks QUndoStack.undoText() .
		If none of the stacks are active, or if the group is empty, this function returns an empty string.
		"""
		res = super(QUndoGroup,self).undoText()
		return res
	#----------------------------------------------------------------------
	def addStack(self,stack):
		"""
		addStack(stack)
			stack=QtGui.QUndoStack

		Adds stack to this group
		The group does not take ownership of the stack
		Another way of adding a stack to a group is by specifying the group as the stacks parent PySide.QtCore.QObject in QUndoStack.QUndoStack()
		In this case, the stack is deleted when the group is deleted, in the usual manner of QObjects .
		"""
		res = super(QUndoGroup,self).addStack(stack)
		return res
	#----------------------------------------------------------------------
	def createRedoAction(self,parent,prefix=None):
		"""
		createRedoAction(parent,prefix=None)
			parent=QtCore.QObject
			prefix=unicode

		Creates an redo PySide.QtGui.QAction object with parent parent .
		Triggering this action will cause a call to QUndoStack.redo() on the active stack
		The text of this action will always be the text of the command which will be redone in the next call to PySide.QtGui.QUndoGroup.redo() , prefixed by prefix
		If there is no command available for redo, if the group is empty or if none of the stacks are active, this action will be disabled.
		If prefix is empty, the default prefix Undo is used.
		"""
		res = super(QUndoGroup,self).createRedoAction(parent,prefix)
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def createUndoAction(self,parent,prefix=None):
		"""
		createUndoAction(parent,prefix=None)
			parent=QtCore.QObject
			prefix=unicode

		Creates an undo PySide.QtGui.QAction object with parent parent .
		Triggering this action will cause a call to QUndoStack.undo() on the active stack
		The text of this action will always be the text of the command which will be undone in the next call to PySide.QtGui.QUndoGroup.undo() , prefixed by prefix
		If there is no command available for undo, if the group is empty or if none of the stacks are active, this action will be disabled.
		If prefix is empty, the default prefix Undo is used.
		"""
		res = super(QUndoGroup,self).createUndoAction(parent,prefix)
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def removeStack(self,stack):
		"""
		removeStack(stack)
			stack=QtGui.QUndoStack

		Removes stack from this group
		If the stack was the active stack in the group, the active stack becomes 0.
		"""
		res = super(QUndoGroup,self).removeStack(stack)
		return res

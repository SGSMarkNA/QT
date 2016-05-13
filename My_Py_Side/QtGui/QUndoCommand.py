from PySide import QtGui, QtCore

class QUndoCommand(QtGui.QUndoCommand):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QUndoCommand,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def childCount(self):
		"""
		Returns the number of child commands in this command.
		"""
		res = super(QUndoCommand,self).childCount()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def id(self):
		"""
		Returns the ID of this command.
		A command ID is used in command compression
		It must be an integer unique to this commands class, or -1 if the command doesnt support compression.
		If the command supports compression this function must be overridden in the derived class to return the correct ID
		The base implementation returns -1.
		QUndoStack.push() will only try to merge two commands if they have the same ID, and the ID is not -1.
		"""
		res = super(QUndoCommand,self).id()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def redo(self):
		"""
		Applies a change to the document
		This function must be implemented in the derived class
		Calling QUndoStack.push() , QUndoStack.undo() or QUndoStack.redo() from this function leads to undefined beahavior.
		The default implementation calls PySide.QtGui.QUndoCommand.redo() on all child commands.
		"""
		res = super(QUndoCommand,self).redo()
		return res
	#----------------------------------------------------------------------
	def text(self):
		"""
		Returns a short text string describing what this command does; for example, insert text.
		The text is used when the text properties of the stacks undo and redo actions are updated.
		"""
		res = super(QUndoCommand,self).text()
		return res
	#----------------------------------------------------------------------
	def undo(self):
		"""
		Reverts a change to the document
		After PySide.QtGui.QUndoCommand.undo() is called, the state of the document should be the same as before PySide.QtGui.QUndoCommand.redo() was called
		This function must be implemented in the derived class
		Calling QUndoStack.push() , QUndoStack.undo() or QUndoStack.redo() from this function leads to undefined beahavior.
		The default implementation calls PySide.QtGui.QUndoCommand.undo() on all child commands in reverse order.
		"""
		res = super(QUndoCommand,self).undo()
		return res
	#----------------------------------------------------------------------
	def child(self,index):
		"""
		child(index)
			index=QtCore.int

		Returns the child command at index .
		"""
		res = super(QUndoCommand,self).child(index)
		isinstance(res,QtGui.QUndoCommand)
		return res
	#----------------------------------------------------------------------
	def mergeWith(self,other):
		"""
		mergeWith(other)
			other=QtGui.QUndoCommand

		Attempts to merge this command with command
		Returns true on success; otherwise returns false.
		If this function returns true, calling this commands PySide.QtGui.QUndoCommand.redo() must have the same effect as redoing both this command and command
		Similarly, calling this commands PySide.QtGui.QUndoCommand.undo() must have the same effect as undoing command and this command.
		PySide.QtGui.QUndoStack will only try to merge two commands if they have the same id, and the id is not -1.
		The default implementation returns false.
		"""
		res = super(QUndoCommand,self).mergeWith(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def setText(self,text):
		"""
		setText(text)
			text=unicode

		Sets the commands text to be the text specified.
		The specified text should be a short user-readable string describing what this command does.
		"""
		res = super(QUndoCommand,self).setText(text)
		return res

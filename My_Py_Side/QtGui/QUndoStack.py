from PySide import QtGui, QtCore

class QUndoStack(QtGui.QUndoStack):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QUndoStack,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def canRedo(self):
		"""
		Returns true if there is a command available for redo; otherwise returns false.
		This function returns false if the stack is empty or if the top command on the stack has already been redone.
		Synonymous with PySide.QtGui.QUndoStack.index() == PySide.QtGui.QUndoStack.count() .
		"""
		res = super(QUndoStack,self).canRedo()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def canUndo(self):
		"""
		Returns true if there is a command available for undo; otherwise returns false.
		This function returns false if the stack is empty, or if the bottom command on the stack has already been undone.
		Synonymous with PySide.QtGui.QUndoStack.index() == 0.
		"""
		res = super(QUndoStack,self).canUndo()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def cleanIndex(self):
		"""
		Returns the clean index
		This is the index at which PySide.QtGui.QUndoStack.setClean() was called.
		A stack may not have a clean index
		This happens if a document is saved, some commands are undone, then a new command is pushed
		Since PySide.QtGui.QUndoStack.push() deletes all the undone commands before pushing the new command, the stack cant return to the clean state again
		In this case, this function returns -1.
		"""
		res = super(QUndoStack,self).cleanIndex()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Clears the command stack by deleting all commands on it, and returns the stack to the clean state.
		Commands are not undone or redone; the state of the edited object remains unchanged.
		This function is usually used when the contents of the document are abandoned.
		"""
		res = super(QUndoStack,self).clear()
		return res
	#----------------------------------------------------------------------
	def count(self):
		"""
		Returns the number of commands on the stack
		Macro commands are counted as one command.
		"""
		res = super(QUndoStack,self).count()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def endMacro(self):
		"""
		Ends composition of a macro command.
		If this is the outermost macro in a set nested macros, this function emits PySide.QtGui.QUndoStack.indexChanged() once for the entire macro command.
		"""
		res = super(QUndoStack,self).endMacro()
		return res
	#----------------------------------------------------------------------
	def index(self):
		"""
		Returns the index of the current command
		This is the command that will be executed on the next call to PySide.QtGui.QUndoStack.redo()
		It is not always the top-most command on the stack, since a number of commands may have been undone.
		"""
		res = super(QUndoStack,self).index()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def isActive(self):
		"""
		This property holds the active status of this stack..
		An application often has multiple undo stacks, one for each opened document
		The active stack is the one associated with the currently active document
		If the stack belongs to a PySide.QtGui.QUndoGroup , calls to QUndoGroup.undo() or QUndoGroup.redo() will be forwarded to this stack when it is active
		If the PySide.QtGui.QUndoGroup is watched by a PySide.QtGui.QUndoView , the view will display the contents of this stack when it is active
		If the stack does not belong to a PySide.QtGui.QUndoGroup , making it active has no effect.
		It is the programmers responsibility to specify which stack is active by calling PySide.QtGui.QUndoStack.setActive() , usually when the associated document window receives focus.
		"""
		res = super(QUndoStack,self).isActive()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isClean(self):
		"""
		If the stack is in the clean state, returns true; otherwise returns false.
		"""
		res = super(QUndoStack,self).isClean()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def redoText(self):
		"""
		Returns the text of the command which will be redone in the next call to PySide.QtGui.QUndoStack.redo() .
		"""
		res = super(QUndoStack,self).redoText()
		return res
	#----------------------------------------------------------------------
	def undoLimit(self):
		"""
		This property holds the maximum number of commands on this stack..
		When the number of commands on a stack exceedes the stacks PySide.QtGui.QUndoStack.undoLimit() , commands are deleted from the bottom of the stack
		Macro commands (commands with child commands) are treated as one command
		The default value is 0, which means that there is no limit.
		This property may only be set when the undo stack is empty, since setting it on a non-empty stack might delete the command at the current index
		Calling PySide.QtGui.QUndoStack.setUndoLimit() on a non-empty stack prints a warning and does nothing.
		"""
		res = super(QUndoStack,self).undoLimit()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def undoText(self):
		"""
		Returns the text of the command which will be undone in the next call to PySide.QtGui.QUndoStack.undo() .
		"""
		res = super(QUndoStack,self).undoText()
		return res
	#----------------------------------------------------------------------
	def beginMacro(self,text):
		"""
		beginMacro(text)
			text=unicode

		Begins composition of a macro command with the given text description.
		An empty command described by the specified text is pushed on the stack
		Any subsequent commands pushed on the stack will be appended to the empty commands children until PySide.QtGui.QUndoStack.endMacro() is called.
		Calls to PySide.QtGui.QUndoStack.beginMacro() and PySide.QtGui.QUndoStack.endMacro() may be nested, but every call to PySide.QtGui.QUndoStack.beginMacro() must have a matching call to PySide.QtGui.QUndoStack.endMacro() .
		While a macro is composed, the stack is disabled
		This means that:
		The stack becomes enabled and appropriate signals are emitted when PySide.QtGui.QUndoStack.endMacro() is called for the outermost macro.
		This code is equivalent to:
		"""
		res = super(QUndoStack,self).beginMacro(text)
		return res
	#----------------------------------------------------------------------
	def command(self,index):
		"""
		command(index)
			index=QtCore.int

		Returns a const pointer to the command at index .
		This function returns a const pointer, because modifying a command, once it has been pushed onto the stack and executed, almost always causes corruption of the state of the document, if the command is later undone or redone.
		"""
		res = super(QUndoStack,self).command(index)
		isinstance(res,QtGui.QUndoCommand)
		return res
	#----------------------------------------------------------------------
	def createRedoAction(self,parent,prefix=None):
		"""
		createRedoAction(parent,prefix=None)
			parent=QtCore.QObject
			prefix=unicode

		Creates an redo PySide.QtGui.QAction object with the given parent .
		Triggering this action will cause a call to PySide.QtGui.QUndoStack.redo()
		The text of this action is the text of the command which will be redone in the next call to PySide.QtGui.QUndoStack.redo() , prefixed by the specified prefix
		If there is no command available for redo, this action will be disabled.
		If prefix is empty, the default prefix Redo is used.
		"""
		res = super(QUndoStack,self).createRedoAction(parent,prefix)
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def createUndoAction(self,parent,prefix=None):
		"""
		createUndoAction(parent,prefix=None)
			parent=QtCore.QObject
			prefix=unicode

		Creates an undo PySide.QtGui.QAction object with the given parent .
		Triggering this action will cause a call to PySide.QtGui.QUndoStack.undo()
		The text of this action is the text of the command which will be undone in the next call to PySide.QtGui.QUndoStack.undo() , prefixed by the specified prefix
		If there is no command available for undo, this action will be disabled.
		If prefix is empty, the default prefix Undo is used.
		"""
		res = super(QUndoStack,self).createUndoAction(parent,prefix)
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def push(self,cmd):
		"""
		push(cmd)
			cmd=QtGui.QUndoCommand

		Pushes cmd on the stack or merges it with the most recently executed command
		In either case, executes cmd by calling its PySide.QtGui.QUndoStack.redo() function.
		If cmd s id is not -1, and if the id is the same as that of the most recently executed command, PySide.QtGui.QUndoStack will attempt to merge the two commands by calling QUndoCommand.mergeWith() on the most recently executed command
		If QUndoCommand.mergeWith() returns true, cmd is deleted.
		In all other cases cmd is simply pushed on the stack.
		If commands were undone before cmd was pushed, the current command and all commands above it are deleted
		Hence cmd always ends up being the top-most on the stack.
		Once a command is pushed, the stack takes ownership of it
		There are no getters to return the command, since modifying it after it has been executed will almost always lead to corruption of the documents state.
		"""
		res = super(QUndoStack,self).push(cmd)
		return res
	#----------------------------------------------------------------------
	def setUndoLimit(self,limit):
		"""
		setUndoLimit(limit)
			limit=QtCore.int

		This property holds the maximum number of commands on this stack..
		When the number of commands on a stack exceedes the stacks PySide.QtGui.QUndoStack.undoLimit() , commands are deleted from the bottom of the stack
		Macro commands (commands with child commands) are treated as one command
		The default value is 0, which means that there is no limit.
		This property may only be set when the undo stack is empty, since setting it on a non-empty stack might delete the command at the current index
		Calling PySide.QtGui.QUndoStack.setUndoLimit() on a non-empty stack prints a warning and does nothing.
		"""
		res = super(QUndoStack,self).setUndoLimit(limit)
		return res
	#----------------------------------------------------------------------
	def text(self,idx):
		"""
		text(idx)
			idx=QtCore.int

		Returns the text of the command at index idx .
		"""
		res = super(QUndoStack,self).text(idx)
		return res

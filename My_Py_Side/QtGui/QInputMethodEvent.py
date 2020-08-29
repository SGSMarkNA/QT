from PySide import QtGui, QtCore

class QInputMethodEvent(QtGui.QInputMethodEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QInputMethodEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def attributes(self):
		"""
		Returns the list of attributes passed to the PySide.QtGui.QInputMethodEvent constructor
		The attributes control the visual appearance of the preedit string (the visual appearance of text outside the preedit string is controlled by the widget only).
		"""
		res = super(QInputMethodEvent,self).attributes()
		return res
	#----------------------------------------------------------------------
	def commitString(self):
		"""
		Returns the text that should get added to (or replace parts of) the text of the editor widget
		It usually is a result of the input operations and has to be inserted to the widgets text directly before the preedit string.
		"""
		res = super(QInputMethodEvent,self).commitString()
		return res
	#----------------------------------------------------------------------
	def preeditString(self):
		"""
		Returns the preedit text, i.e
		the text before the user started editing it.
		"""
		res = super(QInputMethodEvent,self).preeditString()
		return res
	#----------------------------------------------------------------------
	def replacementLength(self):
		"""
		Returns the number of characters to be replaced in the preedit string.
		"""
		res = super(QInputMethodEvent,self).replacementLength()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def replacementStart(self):
		"""
		Returns the position at which characters are to be replaced relative from the start of the preedit string.
		"""
		res = super(QInputMethodEvent,self).replacementStart()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def setCommitString(self,commitString,replaceFrom=None,replaceLength=None):
		"""
		setCommitString(commitString,replaceFrom=None,replaceLength=None)
			commitString=unicode
			replaceFrom=QtCore.int
			replaceLength=QtCore.int

		Sets the commit string to commitString .
		The commit string is the text that should get added to (or replace parts of) the text of the editor widget
		It usually is a result of the input operations and has to be inserted to the widgets text directly before the preedit string.
		If the commit string should replace parts of the of the text in the editor, replaceLength specifies the number of characters to be replaced
		replaceFrom specifies the position at which characters are to be replaced relative from the start of the preedit string.
		"""
		res = super(QInputMethodEvent,self).setCommitString(commitString,replaceFrom,replaceLength)
		return res

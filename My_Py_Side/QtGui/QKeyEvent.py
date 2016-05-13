from PySide import QtGui, QtCore

class QKeyEvent(QtGui.QKeyEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QKeyEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def count(self):
		"""
		Returns the number of keys involved in this event
		If PySide.QtGui.QKeyEvent.text() is not empty, this is simply the length of the string.
		"""
		res = super(QKeyEvent,self).count()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def hasExtendedInfo(self):
		"""

		"""
		res = super(QKeyEvent,self).hasExtendedInfo()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isAutoRepeat(self):
		"""
		Returns true if this event comes from an auto-repeating key; returns false if it comes from an initial key press.
		Note that if the event is a multiple-key compressed event that is partly due to auto-repeat, this function could return either true or false indeterminately.
		"""
		res = super(QKeyEvent,self).isAutoRepeat()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def key(self):
		"""
		Returns the code of the key that was pressed or released.
		See Qt.Key for the list of keyboard codes
		These codes are independent of the underlying window system
		Note that this function does not distinguish between capital and non-capital letters, use the PySide.QtGui.QKeyEvent.text() function (returning the Unicode text the key generated) for this purpose.
		A value of either 0 or Qt.Key_unknown means that the event is not the result of a known key; for example, it may be the result of a compose sequence, a keyboard macro, or due to key event compression.
		"""
		res = super(QKeyEvent,self).key()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def nativeModifiers(self):
		"""
		Returns the native modifiers of a key event
		If the key event does not contain this data 0 is returned.
		Note: The native modifiers may be 0, even if the key event contains extended information.
		"""
		res = super(QKeyEvent,self).nativeModifiers()
		isinstance(res,QtCore.quint32)
		return res
	#----------------------------------------------------------------------
	def nativeScanCode(self):
		"""
		Returns the native scan code of the key event
		If the key event does not contain this data 0 is returned.
		Note: The native scan code may be 0, even if the key event contains extended information.
		Note: On Mac OS/X, this function is not useful, because there is no way to get the scan code from Carbon or Cocoa
		The function always returns 1 (or 0 in the case explained above).
		"""
		res = super(QKeyEvent,self).nativeScanCode()
		isinstance(res,QtCore.quint32)
		return res
	#----------------------------------------------------------------------
	def nativeVirtualKey(self):
		"""
		Returns the native virtual key, or key sym of the key event
		If the key event does not contain this data 0 is returned.
		Note: The native virtual key may be 0, even if the key event contains extended information.
		"""
		res = super(QKeyEvent,self).nativeVirtualKey()
		isinstance(res,QtCore.quint32)
		return res
	#----------------------------------------------------------------------
	def text(self):
		"""
		Returns the Unicode text that this key generated
		The text returned can be an empty string in cases where modifier keys, such as Shift, Control, Alt, and Meta, are being pressed or released
		In such cases PySide.QtGui.QKeyEvent.key() will contain a valid value.
		"""
		res = super(QKeyEvent,self).text()
		return res
	#----------------------------------------------------------------------
	def matches(self,key):
		"""
		matches(key)
			key=QtGui.QKeySequence.StandardKey


		"""
		res = super(QKeyEvent,self).matches(key)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,arg__1):
		"""
		__ne__(arg__1)
			arg__1=QtGui.QKeySequence.StandardKey


		"""
		res = super(QKeyEvent,self).__ne__(arg__1)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,*args,**kwargs):
		"""
		__eq__(key)
			key=QtGui.QKeySequence.StandardKey

		__eq__(key)
			key=QtGui.QKeySequence.StandardKey


		"""
		res = super(QKeyEvent,self).__eq__(*args,**kwargs)
		isinstance(res,QtCore.bool)
		return res

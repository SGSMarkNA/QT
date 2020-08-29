from PySide import QtGui, QtCore

class QKeySequence(QtGui.QKeySequence):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QKeySequence,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __getitem__(self):
		"""

		"""
		res = super(QKeySequence,self).__getitem__()
		return res
	#----------------------------------------------------------------------
	def __reduce__(self):
		"""

		"""
		res = super(QKeySequence,self).__reduce__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __repr__(self):
		"""

		"""
		res = super(QKeySequence,self).__repr__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def count(self):
		"""
		Returns the number of keys in the key sequence
		The maximum is 4.
		"""
		res = super(QKeySequence,self).count()
		isinstance(res,QtCore.uint)
		return res
	#----------------------------------------------------------------------
	def isEmpty(self):
		"""
		Returns true if the key sequence is empty; otherwise returns false.
		"""
		res = super(QKeySequence,self).isEmpty()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def assign(self,*args,**kwargs):
		"""
		assign(str)
			str=unicode

		assign(str,format)
			str=unicode
			format=QtGui.QKeySequence.SequenceFormat


		"""
		res = super(QKeySequence,self).assign(*args,**kwargs)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def matches(self,seq):
		"""
		matches(seq)
			seq=QtGui.QKeySequence

		Matches the sequence with seq
		Returns ExactMatch if successful, PartialMatch if seq matches incompletely, and NoMatch if the sequences have nothing in common
		Returns NoMatch if seq is shorter.
		"""
		res = super(QKeySequence,self).matches(seq)
		isinstance(res,QtGui.QKeySequence.SequenceMatch)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtGui.QKeySequence

		Returns true if this key sequence is not equal to the other key sequence; otherwise returns false.
		"""
		res = super(QKeySequence,self).__ne__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __lt__(self,ks):
		"""
		__lt__(ks)
			ks=QtGui.QKeySequence

		Provides an arbitrary comparison of this key sequence and other key sequence
		All that is guaranteed is that the operator returns false if both key sequences are equal and that (ks1 < ks2) == !( ks2 < ks1) if the key sequences are not equal.
		This function is useful in some circumstances, for example if you want to use PySide.QtGui.QKeySequence objects as keys in a QMap .
		"""
		res = super(QKeySequence,self).__lt__(ks)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __le__(self,other):
		"""
		__le__(other)
			other=QtGui.QKeySequence

		Returns true if this key sequence is smaller or equal to the other key sequence; otherwise returns false.
		"""
		res = super(QKeySequence,self).__le__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtGui.QKeySequence

		Returns true if this key sequence is equal to the other key sequence; otherwise returns false.
		"""
		res = super(QKeySequence,self).__eq__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __gt__(self,other):
		"""
		__gt__(other)
			other=QtGui.QKeySequence

		Returns true if this key sequence is larger than the other key sequence; otherwise returns false.
		"""
		res = super(QKeySequence,self).__gt__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __ge__(self,other):
		"""
		__ge__(other)
			other=QtGui.QKeySequence

		Returns true if this key sequence is larger or equal to the other key sequence; otherwise returns false.
		"""
		res = super(QKeySequence,self).__ge__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setKey(self,key,index):
		"""
		setKey(key,index)
			key=QtCore.int
			index=QtCore.int


		"""
		res = super(QKeySequence,self).setKey(key,index)
		return res
	#----------------------------------------------------------------------
	def toString(self,format=None):
		"""
		toString(format=None)
			format=QtGui.QKeySequence.SequenceFormat

		Return a string representation of the key sequence, based on format .
		For example, the value Qt.CTRL + Qt.Key_O results in Ctrl+O
		If the key sequence has multiple key codes, each is separated by commas in the string returned, such as Alt+X, Ctrl+Y, Z
		The strings, Ctrl, Shift, etc
		are translated using QObject.tr() in the  PySide.QtGui.QShortcut  context.
		If the key sequence has no keys, an empty string is returned.
		On Mac OS X, the string returned resembles the sequence that is shown in the menu bar.
		"""
		res = super(QKeySequence,self).toString(format)
		return res

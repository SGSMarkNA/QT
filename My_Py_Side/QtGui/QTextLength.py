from PySide import QtGui, QtCore

class QTextLength(QtGui.QTextLength):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextLength,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def rawValue(self):
		"""
		Returns the constraint value that is specific for the type of the length
		If the length is QTextLength.PercentageLength then the raw value is in percent, in the range of 0 to 100
		If the length is QTextLength.FixedLength then that fixed amount is returned
		For variable lengths, zero is returned.
		"""
		res = super(QTextLength,self).rawValue()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def type(self):
		"""
		Returns the type of this length object.
		"""
		res = super(QTextLength,self).type()
		isinstance(res,QtGui.QTextLength.Type)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtGui.QTextLength

		Returns true if this text length is different from the other text length.
		"""
		res = super(QTextLength,self).__ne__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtGui.QTextLength

		Returns true if this text length is the same as the other text length.
		"""
		res = super(QTextLength,self).__eq__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def value(self,maximumLength):
		"""
		value(maximumLength)
			maximumLength=QtCore.qreal

		Returns the effective length, constrained by the type of the length object and the specified maximumLength .
		"""
		res = super(QTextLength,self).value(maximumLength)
		isinstance(res,QtCore.qreal)
		return res

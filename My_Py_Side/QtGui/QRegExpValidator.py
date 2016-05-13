from PySide import QtGui, QtCore

class QRegExpValidator(QtGui.QRegExpValidator):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QRegExpValidator,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def regExp(self):
		"""
		This property holds the regular expression used for validation.
		By default, this property contains a regular expression with the pattern .* that matches any string.
		"""
		res = super(QRegExpValidator,self).regExp()
		isinstance(res,QtCore.QRegExp)
		return res
	#----------------------------------------------------------------------
	def setRegExp(self,rx):
		"""
		setRegExp(rx)
			rx=QtCore.QRegExp

		This property holds the regular expression used for validation.
		By default, this property contains a regular expression with the pattern .* that matches any string.
		"""
		res = super(QRegExpValidator,self).setRegExp(rx)
		return res

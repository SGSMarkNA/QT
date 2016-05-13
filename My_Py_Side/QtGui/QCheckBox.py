from PySide import QtGui, QtCore

class QCheckBox(QtGui.QCheckBox):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QCheckBox,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def checkState(self):
		"""
		Returns the check boxs check state
		If you do not need tristate support, you can also use QAbstractButton.isChecked() which returns a boolean.
		"""
		res = super(QCheckBox,self).checkState()
		isinstance(res,QtCore.Qt.CheckState)
		return res
	#----------------------------------------------------------------------
	def isTristate(self):
		"""
		This property holds whether the checkbox is a tri-state checkbox.
		The default is false; i.e
		the checkbox has only two states.
		"""
		res = super(QCheckBox,self).isTristate()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def initStyleOption(self,option):
		"""
		initStyleOption(option)
			option=QtGui.QStyleOptionButton

		Initializes option with the values from this PySide.QtGui.QCheckBox
		This method is useful for subclasses that require a PySide.QtGui.QStyleOptionButton , but do not want to fill in all the information themselves.
		"""
		res = super(QCheckBox,self).initStyleOption(option)
		return res
	#----------------------------------------------------------------------
	def setCheckState(self,state):
		"""
		setCheckState(state)
			state=QtCore.Qt.CheckState


		"""
		res = super(QCheckBox,self).setCheckState(state)
		return res
	#----------------------------------------------------------------------
	def setTristate(self,y=None):
		"""
		setTristate(y=None)
			y=QtCore.bool

		This property holds whether the checkbox is a tri-state checkbox.
		The default is false; i.e
		the checkbox has only two states.
		"""
		res = super(QCheckBox,self).setTristate(y)
		return res

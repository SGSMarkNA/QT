from PySide import QtGui, QtCore

class QInputDialog(QtGui.QInputDialog):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QInputDialog,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def cancelButtonText(self):
		"""

		"""
		res = super(QInputDialog,self).cancelButtonText()
		return res
	#----------------------------------------------------------------------
	def comboBoxItems(self):
		"""

		"""
		res = super(QInputDialog,self).comboBoxItems()
		return res
	#----------------------------------------------------------------------
	def doubleDecimals(self):
		"""

		"""
		res = super(QInputDialog,self).doubleDecimals()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def doubleMaximum(self):
		"""

		"""
		res = super(QInputDialog,self).doubleMaximum()
		isinstance(res,QtCore.double)
		return res
	#----------------------------------------------------------------------
	def doubleMinimum(self):
		"""

		"""
		res = super(QInputDialog,self).doubleMinimum()
		isinstance(res,QtCore.double)
		return res
	#----------------------------------------------------------------------
	def doubleValue(self):
		"""

		"""
		res = super(QInputDialog,self).doubleValue()
		isinstance(res,QtCore.double)
		return res
	#----------------------------------------------------------------------
	def inputMode(self):
		"""

		"""
		res = super(QInputDialog,self).inputMode()
		isinstance(res,QtGui.QInputDialog.InputMode)
		return res
	#----------------------------------------------------------------------
	def intMaximum(self):
		"""

		"""
		res = super(QInputDialog,self).intMaximum()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def intMinimum(self):
		"""

		"""
		res = super(QInputDialog,self).intMinimum()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def intStep(self):
		"""

		"""
		res = super(QInputDialog,self).intStep()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def intValue(self):
		"""

		"""
		res = super(QInputDialog,self).intValue()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def isComboBoxEditable(self):
		"""

		"""
		res = super(QInputDialog,self).isComboBoxEditable()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def labelText(self):
		"""

		"""
		res = super(QInputDialog,self).labelText()
		return res
	#----------------------------------------------------------------------
	def okButtonText(self):
		"""

		"""
		res = super(QInputDialog,self).okButtonText()
		return res
	#----------------------------------------------------------------------
	def textEchoMode(self):
		"""

		"""
		res = super(QInputDialog,self).textEchoMode()
		isinstance(res,QtGui.QLineEdit.EchoMode)
		return res
	#----------------------------------------------------------------------
	def textValue(self):
		"""

		"""
		res = super(QInputDialog,self).textValue()
		return res
	#----------------------------------------------------------------------
	def open(self,receiver,member):
		"""
		open(receiver,member)
			receiver=QtCore.QObject
			member=str

		This is an overloaded function.
		This function connects one of its signals to the slot specified by receiver and member
		The specific signal depends on the arguments that are specified in member
		These are:
		The signal will be disconnected from the slot when the dialog is closed.
		"""
		res = super(QInputDialog,self).open(receiver,member)
		return res
	#----------------------------------------------------------------------
	def setCancelButtonText(self,text):
		"""
		setCancelButtonText(text)
			text=unicode


		"""
		res = super(QInputDialog,self).setCancelButtonText(text)
		return res
	#----------------------------------------------------------------------
	def setComboBoxEditable(self,editable):
		"""
		setComboBoxEditable(editable)
			editable=QtCore.bool


		"""
		res = super(QInputDialog,self).setComboBoxEditable(editable)
		return res
	#----------------------------------------------------------------------
	def setComboBoxItems(self,items):
		"""
		setComboBoxItems(items)
			items=list


		"""
		res = super(QInputDialog,self).setComboBoxItems(items)
		return res
	#----------------------------------------------------------------------
	def setDoubleDecimals(self,decimals):
		"""
		setDoubleDecimals(decimals)
			decimals=QtCore.int


		"""
		res = super(QInputDialog,self).setDoubleDecimals(decimals)
		return res
	#----------------------------------------------------------------------
	def setDoubleMaximum(self,max):
		"""
		setDoubleMaximum(max)
			max=QtCore.double


		"""
		res = super(QInputDialog,self).setDoubleMaximum(max)
		return res
	#----------------------------------------------------------------------
	def setDoubleMinimum(self,min):
		"""
		setDoubleMinimum(min)
			min=QtCore.double


		"""
		res = super(QInputDialog,self).setDoubleMinimum(min)
		return res
	#----------------------------------------------------------------------
	def setDoubleRange(self,min,max):
		"""
		setDoubleRange(min,max)
			min=QtCore.double
			max=QtCore.double

		Sets the range of double precision floating point values accepted by the dialog when used in DoubleInput mode, with minimum and maximum values specified by min and max respectively.
		"""
		res = super(QInputDialog,self).setDoubleRange(min,max)
		return res
	#----------------------------------------------------------------------
	def setDoubleValue(self,value):
		"""
		setDoubleValue(value)
			value=QtCore.double


		"""
		res = super(QInputDialog,self).setDoubleValue(value)
		return res
	#----------------------------------------------------------------------
	def setInputMode(self,mode):
		"""
		setInputMode(mode)
			mode=QtGui.QInputDialog.InputMode


		"""
		res = super(QInputDialog,self).setInputMode(mode)
		return res
	#----------------------------------------------------------------------
	def setIntMaximum(self,max):
		"""
		setIntMaximum(max)
			max=QtCore.int


		"""
		res = super(QInputDialog,self).setIntMaximum(max)
		return res
	#----------------------------------------------------------------------
	def setIntMinimum(self,min):
		"""
		setIntMinimum(min)
			min=QtCore.int


		"""
		res = super(QInputDialog,self).setIntMinimum(min)
		return res
	#----------------------------------------------------------------------
	def setIntRange(self,min,max):
		"""
		setIntRange(min,max)
			min=QtCore.int
			max=QtCore.int

		Sets the range of integer values accepted by the dialog when used in IntInput mode, with minimum and maximum values specified by min and max respectively.
		"""
		res = super(QInputDialog,self).setIntRange(min,max)
		return res
	#----------------------------------------------------------------------
	def setIntStep(self,step):
		"""
		setIntStep(step)
			step=QtCore.int


		"""
		res = super(QInputDialog,self).setIntStep(step)
		return res
	#----------------------------------------------------------------------
	def setIntValue(self,value):
		"""
		setIntValue(value)
			value=QtCore.int


		"""
		res = super(QInputDialog,self).setIntValue(value)
		return res
	#----------------------------------------------------------------------
	def setLabelText(self,text):
		"""
		setLabelText(text)
			text=unicode


		"""
		res = super(QInputDialog,self).setLabelText(text)
		return res
	#----------------------------------------------------------------------
	def setOkButtonText(self,text):
		"""
		setOkButtonText(text)
			text=unicode


		"""
		res = super(QInputDialog,self).setOkButtonText(text)
		return res
	#----------------------------------------------------------------------
	def setOption(self,option,on=None):
		"""
		setOption(option,on=None)
			option=QtGui.QInputDialog.InputDialogOption
			on=QtCore.bool

		Sets the given option to be enabled if on is true; otherwise, clears the given option .
		"""
		res = super(QInputDialog,self).setOption(option,on)
		return res
	#----------------------------------------------------------------------
	def setTextEchoMode(self,mode):
		"""
		setTextEchoMode(mode)
			mode=QtGui.QLineEdit.EchoMode


		"""
		res = super(QInputDialog,self).setTextEchoMode(mode)
		return res
	#----------------------------------------------------------------------
	def setTextValue(self,text):
		"""
		setTextValue(text)
			text=unicode


		"""
		res = super(QInputDialog,self).setTextValue(text)
		return res
	#----------------------------------------------------------------------
	def testOption(self,option):
		"""
		testOption(option)
			option=QtGui.QInputDialog.InputDialogOption

		Returns true if the given option is enabled; otherwise, returns false.
		"""
		res = super(QInputDialog,self).testOption(option)
		isinstance(res,QtCore.bool)
		return res

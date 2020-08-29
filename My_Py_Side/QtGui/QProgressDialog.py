from PySide import QtGui, QtCore

class QProgressDialog(QtGui.QProgressDialog):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QProgressDialog,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def autoClose(self):
		"""
		This property holds whether the dialog gets hidden by PySide.QtGui.QProgressDialog.reset() .
		The default is true.
		"""
		res = super(QProgressDialog,self).autoClose()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def autoReset(self):
		"""
		This property holds whether the progress dialog calls PySide.QtGui.QProgressDialog.reset() as soon as PySide.QtGui.QProgressDialog.value() equals PySide.QtGui.QProgressDialog.maximum() .
		The default is true.
		"""
		res = super(QProgressDialog,self).autoReset()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def canceled(self):
		"""

		"""
		res = super(QProgressDialog,self).canceled()
		return res
	#----------------------------------------------------------------------
	def labelText(self):
		"""
		This property holds the labels text.
		The default text is an empty string.
		"""
		res = super(QProgressDialog,self).labelText()
		return res
	#----------------------------------------------------------------------
	def maximum(self):
		"""
		This property holds the highest value represented by the progress bar.
		The default is 0.
		"""
		res = super(QProgressDialog,self).maximum()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def minimum(self):
		"""
		This property holds the lowest value represented by the progress bar.
		The default is 0.
		"""
		res = super(QProgressDialog,self).minimum()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def minimumDuration(self):
		"""
		This property holds the time that must pass before the dialog appears.
		If the expected duration of the task is less than the PySide.QtGui.QProgressDialog.minimumDuration() , the dialog will not appear at all
		This prevents the dialog popping up for tasks that are quickly over
		For tasks that are expected to exceed the PySide.QtGui.QProgressDialog.minimumDuration() , the dialog will pop up after the PySide.QtGui.QProgressDialog.minimumDuration() time or as soon as any progress is set.
		If set to 0, the dialog is always shown as soon as any progress is set
		The default is 4000 milliseconds.
		"""
		res = super(QProgressDialog,self).minimumDuration()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def value(self):
		"""
		This property holds the current amount of progress made..
		For the progress dialog to work as expected, you should initially set this property to 0 and finally set it to QProgressDialog.maximum() ; you can call PySide.QtGui.QProgressDialog.setValue() any number of times in-between.
		"""
		res = super(QProgressDialog,self).value()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def wasCanceled(self):
		"""
		This property holds whether the dialog was canceled.
		"""
		res = super(QProgressDialog,self).wasCanceled()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def open(self,receiver,member):
		"""
		open(receiver,member)
			receiver=QtCore.QObject
			member=str

		This is an overloaded function.
		Opens the dialog and connects its PySide.QtGui.QDialog.accepted() signal to the slot specified by receiver and member .
		The signal will be disconnected from the slot when the dialog is closed.
		"""
		res = super(QProgressDialog,self).open(receiver,member)
		return res
	#----------------------------------------------------------------------
	def setAutoClose(self,close):
		"""
		setAutoClose(close)
			close=QtCore.bool

		This property holds whether the dialog gets hidden by PySide.QtGui.QProgressDialog.reset() .
		The default is true.
		"""
		res = super(QProgressDialog,self).setAutoClose(close)
		return res
	#----------------------------------------------------------------------
	def setAutoReset(self,reset):
		"""
		setAutoReset(reset)
			reset=QtCore.bool

		This property holds whether the progress dialog calls PySide.QtGui.QProgressDialog.reset() as soon as PySide.QtGui.QProgressDialog.value() equals PySide.QtGui.QProgressDialog.maximum() .
		The default is true.
		"""
		res = super(QProgressDialog,self).setAutoReset(reset)
		return res
	#----------------------------------------------------------------------
	def setBar(self,bar):
		"""
		setBar(bar)
			bar=QtGui.QProgressBar

		Sets the progress bar widget to bar
		The progress dialog resizes to fit
		The progress dialog takes ownership of the progress bar which will be deleted when necessary, so do not use a progress bar allocated on the stack.
		"""
		res = super(QProgressDialog,self).setBar(bar)
		return res
	#----------------------------------------------------------------------
	def setCancelButton(self,button):
		"""
		setCancelButton(button)
			button=QtGui.QPushButton

		Sets the cancel button to the push button, cancelButton
		The progress dialog takes ownership of this button which will be deleted when necessary, so do not pass the address of an object that is on the stack, i.e
		use new() to create the button
		If 0 is passed then no cancel button will be shown.
		"""
		res = super(QProgressDialog,self).setCancelButton(button)
		return res
	#----------------------------------------------------------------------
	def setLabel(self,label):
		"""
		setLabel(label)
			label=QtGui.QLabel

		Sets the label to label
		The progress dialog resizes to fit
		The label becomes owned by the progress dialog and will be deleted when necessary, so do not pass the address of an object on the stack.
		"""
		res = super(QProgressDialog,self).setLabel(label)
		return res

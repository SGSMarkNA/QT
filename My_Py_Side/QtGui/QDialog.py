from PySide import QtGui, QtCore

class QDialog(QtGui.QDialog):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDialog,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def accept(self):
		"""
		Hides the modal dialog and sets the result code to Accepted .
		"""
		res = super(QDialog,self).accept()
		return res
	#----------------------------------------------------------------------
	def accepted(self):
		"""

		"""
		res = super(QDialog,self).accepted()
		return res
	#----------------------------------------------------------------------
	def isSizeGripEnabled(self):
		"""
		This property holds whether the size grip is enabled.
		A PySide.QtGui.QSizeGrip is placed in the bottom-right corner of the dialog when this property is enabled
		By default, the size grip is disabled.
		"""
		res = super(QDialog,self).isSizeGripEnabled()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def reject(self):
		"""
		Hides the modal dialog and sets the result code to Rejected .
		"""
		res = super(QDialog,self).reject()
		return res
	#----------------------------------------------------------------------
	def rejected(self):
		"""

		"""
		res = super(QDialog,self).rejected()
		return res
	#----------------------------------------------------------------------
	def result(self):
		"""
		Returns the modal dialogs result code, Accepted or Rejected .
		Do not call this function if the dialog was constructed with the Qt.WA_DeleteOnClose attribute.
		"""
		res = super(QDialog,self).result()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def adjustPosition(self,arg__1):
		"""
		adjustPosition(arg__1)
			arg__1=QtGui.QWidget


		"""
		res = super(QDialog,self).adjustPosition(arg__1)
		return res
	#----------------------------------------------------------------------
	def done(self,arg__1):
		"""
		done(arg__1)
			arg__1=QtCore.int

		Closes the dialog and sets its result code to r
		If this dialog is shown with exec() , PySide.QtGui.QDialog.done() causes the local event loop to finish, and exec() to return r .
		As with QWidget.close() , PySide.QtGui.QDialog.done() deletes the dialog if the Qt.WA_DeleteOnClose flag is set
		If the dialog is the applications main widget, the application terminates
		If the dialog is the last window closed, the QApplication.lastWindowClosed() signal is emitted.
		"""
		res = super(QDialog,self).done(arg__1)
		return res
	#----------------------------------------------------------------------
	def setModal(self,modal):
		"""
		setModal(modal)
			modal=QtCore.bool

		This property holds whether PySide.QtGui.QWidget.show() should pop up the dialog as modal or modeless.
		By default, this property is false and PySide.QtGui.QWidget.show() pops up the dialog as modeless
		Setting his property to true is equivalent to setting QWidget.windowModality to Qt.ApplicationModal .
		exec() ignores the value of this property and always pops up the dialog as modal.
		"""
		res = super(QDialog,self).setModal(modal)
		return res
	#----------------------------------------------------------------------
	def setResult(self,r):
		"""
		setResult(r)
			r=QtCore.int

		Sets the modal dialogs result code to i .
		"""
		res = super(QDialog,self).setResult(r)
		return res
	#----------------------------------------------------------------------
	def setSizeGripEnabled(self,arg__1):
		"""
		setSizeGripEnabled(arg__1)
			arg__1=QtCore.bool

		This property holds whether the size grip is enabled.
		A PySide.QtGui.QSizeGrip is placed in the bottom-right corner of the dialog when this property is enabled
		By default, the size grip is disabled.
		"""
		res = super(QDialog,self).setSizeGripEnabled(arg__1)
		return res

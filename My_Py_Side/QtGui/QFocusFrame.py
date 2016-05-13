from PySide import QtGui, QtCore

class QFocusFrame(QtGui.QFocusFrame):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QFocusFrame,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def widget(self):
		"""
		Returns the currently monitored widget for automatically resize and update.
		"""
		res = super(QFocusFrame,self).widget()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def initStyleOption(self,option):
		"""
		initStyleOption(option)
			option=QtGui.QStyleOption

		Initialize option with the values from this PySide.QtGui.QFocusFrame
		This method is useful for subclasses when they need a PySide.QtGui.QStyleOption , but dont want to fill in all the information themselves.
		"""
		res = super(QFocusFrame,self).initStyleOption(option)
		return res
	#----------------------------------------------------------------------
	def setWidget(self,widget):
		"""
		setWidget(widget)
			widget=QtGui.QWidget

		PySide.QtGui.QFocusFrame will track changes to widget and resize itself automatically
		If the monitored widgets parent changes, PySide.QtGui.QFocusFrame will follow the widget and place itself around the widget automatically
		If the monitored widget is deleted, PySide.QtGui.QFocusFrame will set it to zero.
		"""
		res = super(QFocusFrame,self).setWidget(widget)
		return res

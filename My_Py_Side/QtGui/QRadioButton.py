from PySide import QtGui, QtCore

class QRadioButton(QtGui.QRadioButton):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QRadioButton,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def initStyleOption(self,button):
		"""
		initStyleOption(button)
			button=QtGui.QStyleOptionButton

		Initialize option with the values from this PySide.QtGui.QRadioButton
		This method is useful for subclasses when they need a PySide.QtGui.QStyleOptionButton , but dont want to fill in all the information themselves.
		"""
		res = super(QRadioButton,self).initStyleOption(button)
		return res

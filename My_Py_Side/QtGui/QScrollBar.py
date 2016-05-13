from PySide import QtGui, QtCore

class QScrollBar(QtGui.QScrollBar):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QScrollBar,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def initStyleOption(self,option):
		"""
		initStyleOption(option)
			option=QtGui.QStyleOptionSlider

		Initialize option with the values from this PySide.QtGui.QScrollBar
		This method is useful for subclasses when they need a PySide.QtGui.QStyleOptionSlider , but dont want to fill in all the information themselves.
		"""
		res = super(QScrollBar,self).initStyleOption(option)
		return res

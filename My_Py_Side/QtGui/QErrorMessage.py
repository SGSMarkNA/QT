from PySide import QtGui, QtCore

class QErrorMessage(QtGui.QErrorMessage):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QErrorMessage,self).__init__(*args,**kwargs)

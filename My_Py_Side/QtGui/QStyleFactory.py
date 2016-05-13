from PySide import QtGui, QtCore

class QStyleFactory(QtGui.QStyleFactory):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QStyleFactory,self).__init__(*args,**kwargs)

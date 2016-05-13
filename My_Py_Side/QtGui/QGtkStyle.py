from PySide import QtGui, QtCore

class QGtkStyle(QtGui.QGtkStyle):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGtkStyle,self).__init__(*args,**kwargs)

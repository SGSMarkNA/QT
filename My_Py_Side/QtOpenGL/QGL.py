from PySide import QtGui, QtCore

class QGL(QtOpenGL.QGL):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGL,self).__init__(*args,**kwargs)

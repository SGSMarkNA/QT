from PySide import QtGui, QtCore

class Signal(QtCore.Signal):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(Signal,self).__init__(*args,**kwargs)

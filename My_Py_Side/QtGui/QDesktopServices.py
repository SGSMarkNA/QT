from PySide import QtGui, QtCore

class QDesktopServices(QtGui.QDesktopServices):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDesktopServices,self).__init__(*args,**kwargs)

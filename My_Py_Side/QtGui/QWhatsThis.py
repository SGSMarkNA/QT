from PySide import QtGui, QtCore

class QWhatsThis(QtGui.QWhatsThis):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QWhatsThis,self).__init__(*args,**kwargs)

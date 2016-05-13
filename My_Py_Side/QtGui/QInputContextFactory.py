from PySide import QtGui, QtCore

class QInputContextFactory(QtGui.QInputContextFactory):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QInputContextFactory,self).__init__(*args,**kwargs)

from PySide import QtGui, QtCore

class QLibraryInfo(QtCore.QLibraryInfo):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QLibraryInfo,self).__init__(*args,**kwargs)

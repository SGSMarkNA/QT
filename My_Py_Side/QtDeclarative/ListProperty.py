from PySide import QtGui, QtCore

class ListProperty(QtDeclarative.ListProperty):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(ListProperty,self).__init__(*args,**kwargs)

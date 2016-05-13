from PySide import QtGui, QtCore

class QStringListModel(QtGui.QStringListModel):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QStringListModel,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def stringList(self):
		"""
		Returns the string list used by the model to store data.
		"""
		res = super(QStringListModel,self).stringList()
		return res
	#----------------------------------------------------------------------
	def setStringList(self,strings):
		"""
		setStringList(strings)
			strings=list

		Sets the models internal string list to strings
		The model will notify any attached views that its underlying data has changed.
		"""
		res = super(QStringListModel,self).setStringList(strings)
		return res

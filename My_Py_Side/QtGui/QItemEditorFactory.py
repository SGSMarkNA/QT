from PySide import QtGui, QtCore

class QItemEditorFactory(QtGui.QItemEditorFactory):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QItemEditorFactory,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def createEditor(self,type,parent):
		"""
		createEditor(type,parent)
			type=QtCore.QVariant::Type
			parent=QtGui.QWidget


		"""
		res = super(QItemEditorFactory,self).createEditor(type,parent)
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def registerEditor(self,type,creator):
		"""
		registerEditor(type,creator)
			type=QtCore.QVariant::Type
			creator=QtGui.QItemEditorCreatorBase


		"""
		res = super(QItemEditorFactory,self).registerEditor(type,creator)
		return res
	#----------------------------------------------------------------------
	def valuePropertyName(self,type):
		"""
		valuePropertyName(type)
			type=QtCore.QVariant::Type


		"""
		res = super(QItemEditorFactory,self).valuePropertyName(type)
		isinstance(res,QtCore.QByteArray)
		return res

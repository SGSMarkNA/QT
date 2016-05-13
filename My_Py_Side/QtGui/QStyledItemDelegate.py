from PySide import QtGui, QtCore

class QStyledItemDelegate(QtGui.QStyledItemDelegate):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QStyledItemDelegate,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def itemEditorFactory(self):
		"""
		Returns the editor factory used by the item delegate
		If no editor factory is set, the function will return null.
		"""
		res = super(QStyledItemDelegate,self).itemEditorFactory()
		isinstance(res,QtGui.QItemEditorFactory)
		return res
	#----------------------------------------------------------------------
	def displayText(self,value,locale):
		"""
		displayText(value,locale)
			value=object
			locale=QtCore.QLocale

		This function returns the string that the delegate will use to display the Qt.DisplayRole of the model in locale
		value is the value of the Qt.DisplayRole provided by the model.
		The default implementation uses the QLocale::toString to convert value into a PySide.QtCore.QString .
		"""
		res = super(QStyledItemDelegate,self).displayText(value,locale)
		return res
	#----------------------------------------------------------------------
	def initStyleOption(self,option,index):
		"""
		initStyleOption(option,index)
			option=QtGui.QStyleOptionViewItem
			index=QtCore.QModelIndex

		Initialize option with the values using the index index
		This method is useful for subclasses when they need a PySide.QtGui.QStyleOptionViewItem , but dont want to fill in all the information themselves
		This function will check the version of the PySide.QtGui.QStyleOptionViewItem and fill in the additional values for a PySide.QtGui.QStyleOptionViewItemV2 , PySide.QtGui.QStyleOptionViewItemV3 and PySide.QtGui.QStyleOptionViewItemV4 .
		"""
		res = super(QStyledItemDelegate,self).initStyleOption(option,index)
		return res
	#----------------------------------------------------------------------
	def setItemEditorFactory(self,factory):
		"""
		setItemEditorFactory(factory)
			factory=QtGui.QItemEditorFactory

		Sets the editor factory to be used by the item delegate to be the factory specified
		If no editor factory is set, the item delegate will use the default editor factory.
		"""
		res = super(QStyledItemDelegate,self).setItemEditorFactory(factory)
		return res

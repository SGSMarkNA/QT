from PySide import QtGui, QtCore

class QDataWidgetMapper(QtGui.QDataWidgetMapper):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDataWidgetMapper,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def clearMapping(self):
		"""
		Clears all mappings.
		"""
		res = super(QDataWidgetMapper,self).clearMapping()
		return res
	#----------------------------------------------------------------------
	def currentIndex(self):
		"""
		This property holds the current row or column.
		The widgets are populated with with data from the row at index if the orientation is horizontal (the default), otherwise with data from the column at index .
		"""
		res = super(QDataWidgetMapper,self).currentIndex()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def itemDelegate(self):
		"""
		Returns the current item delegate.
		"""
		res = super(QDataWidgetMapper,self).itemDelegate()
		isinstance(res,QtGui.QAbstractItemDelegate)
		return res
	#----------------------------------------------------------------------
	def model(self):
		"""
		Returns the current model.
		"""
		res = super(QDataWidgetMapper,self).model()
		isinstance(res,QtCore.QAbstractItemModel)
		return res
	#----------------------------------------------------------------------
	def orientation(self):
		"""
		This property holds the orientation of the model.
		If the orientation is Qt.Horizontal (the default), a widget is mapped to a column of a data model
		The widget will be populated with the models data from its mapped column and the row that PySide.QtGui.QDataWidgetMapper.currentIndex() points at.
		Use Qt.Horizontal for tabular data that looks like this:
		If the orientation is set to Qt.Vertical , a widget is mapped to a row
		Calling PySide.QtGui.QDataWidgetMapper.setCurrentIndex() will change the current column
		The widget will be populates with the models data from its mapped row and the column that PySide.QtGui.QDataWidgetMapper.currentIndex() points at.
		Use Qt.Vertical for tabular data that looks like this:
		Changing the orientation clears all existing mappings.
		"""
		res = super(QDataWidgetMapper,self).orientation()
		isinstance(res,QtCore.Qt.Orientation)
		return res
	#----------------------------------------------------------------------
	def rootIndex(self):
		"""
		Returns the current root index.
		"""
		res = super(QDataWidgetMapper,self).rootIndex()
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def submitPolicy(self):
		"""
		This property holds the current submit policy.
		Changing the current submit policy will revert all widgets to the current data from the model.
		"""
		res = super(QDataWidgetMapper,self).submitPolicy()
		isinstance(res,QtGui.QDataWidgetMapper.SubmitPolicy)
		return res
	#----------------------------------------------------------------------
	def addMapping(self,*args,**kwargs):
		"""
		addMapping(widget,section)
			widget=QtGui.QWidget
			section=QtCore.int

		addMapping(widget,section,propertyName)
			widget=QtGui.QWidget
			section=QtCore.int
			propertyName=QtCore.QByteArray

		Adds a mapping between a widget and a section from the model
		The section is a column in the model if the orientation is horizontal (the default), otherwise a row.
		For the following example, we assume a model myModel that has two columns: the first one contains the names of people in a group, and the second column contains their ages
		The first column is mapped to the PySide.QtGui.QLineEdit nameLineEdit , and the second is mapped to the PySide.QtGui.QSpinBox ageSpinBox :
		Notes:
		"""
		res = super(QDataWidgetMapper,self).addMapping(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def mappedPropertyName(self,widget):
		"""
		mappedPropertyName(widget)
			widget=QtGui.QWidget

		Returns the name of the property that is used when mapping data to the given widget .
		"""
		res = super(QDataWidgetMapper,self).mappedPropertyName(widget)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def mappedSection(self,widget):
		"""
		mappedSection(widget)
			widget=QtGui.QWidget

		Returns the section the widget is mapped to or -1 if the widget is not mapped.
		"""
		res = super(QDataWidgetMapper,self).mappedSection(widget)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def mappedWidgetAt(self,section):
		"""
		mappedWidgetAt(section)
			section=QtCore.int

		Returns the widget that is mapped at section , or 0 if no widget is mapped at that section.
		"""
		res = super(QDataWidgetMapper,self).mappedWidgetAt(section)
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def removeMapping(self,widget):
		"""
		removeMapping(widget)
			widget=QtGui.QWidget

		Removes the mapping for the given widget .
		"""
		res = super(QDataWidgetMapper,self).removeMapping(widget)
		return res
	#----------------------------------------------------------------------
	def setCurrentIndex(self,index):
		"""
		setCurrentIndex(index)
			index=QtCore.int

		This property holds the current row or column.
		The widgets are populated with with data from the row at index if the orientation is horizontal (the default), otherwise with data from the column at index .
		"""
		res = super(QDataWidgetMapper,self).setCurrentIndex(index)
		return res
	#----------------------------------------------------------------------
	def setItemDelegate(self,delegate):
		"""
		setItemDelegate(delegate)
			delegate=QtGui.QAbstractItemDelegate

		Sets the item delegate to delegate
		The delegate will be used to write data from the model into the widget and from the widget to the model, using QAbstractItemDelegate.setEditorData() and QAbstractItemDelegate.setModelData() .
		The delegate also decides when to apply data and when to change the editor, using QAbstractItemDelegate.commitData() and QAbstractItemDelegate.closeEditor() .
		"""
		res = super(QDataWidgetMapper,self).setItemDelegate(delegate)
		return res
	#----------------------------------------------------------------------
	def setModel(self,model):
		"""
		setModel(model)
			model=QtCore.QAbstractItemModel

		Sets the current model to model
		If another model was set, all mappings to that old model are cleared.
		"""
		res = super(QDataWidgetMapper,self).setModel(model)
		return res
	#----------------------------------------------------------------------
	def setOrientation(self,aOrientation):
		"""
		setOrientation(aOrientation)
			aOrientation=QtCore.Qt.Orientation

		This property holds the orientation of the model.
		If the orientation is Qt.Horizontal (the default), a widget is mapped to a column of a data model
		The widget will be populated with the models data from its mapped column and the row that PySide.QtGui.QDataWidgetMapper.currentIndex() points at.
		Use Qt.Horizontal for tabular data that looks like this:
		If the orientation is set to Qt.Vertical , a widget is mapped to a row
		Calling PySide.QtGui.QDataWidgetMapper.setCurrentIndex() will change the current column
		The widget will be populates with the models data from its mapped row and the column that PySide.QtGui.QDataWidgetMapper.currentIndex() points at.
		Use Qt.Vertical for tabular data that looks like this:
		Changing the orientation clears all existing mappings.
		"""
		res = super(QDataWidgetMapper,self).setOrientation(aOrientation)
		return res
	#----------------------------------------------------------------------
	def setRootIndex(self,index):
		"""
		setRootIndex(index)
			index=QtCore.QModelIndex

		Sets the root item to index
		This can be used to display a branch of a tree
		Pass an invalid model index to display the top-most branch.
		"""
		res = super(QDataWidgetMapper,self).setRootIndex(index)
		return res
	#----------------------------------------------------------------------
	def setSubmitPolicy(self,policy):
		"""
		setSubmitPolicy(policy)
			policy=QtGui.QDataWidgetMapper.SubmitPolicy

		This property holds the current submit policy.
		Changing the current submit policy will revert all widgets to the current data from the model.
		"""
		res = super(QDataWidgetMapper,self).setSubmitPolicy(policy)
		return res

from PySide import QtGui, QtCore

class QColumnView(QtGui.QColumnView):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QColumnView,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def columnWidths(self):
		"""
		Returns a list of the width of all the columns in this view.
		"""
		res = super(QColumnView,self).columnWidths()
		return res
	#----------------------------------------------------------------------
	def previewWidget(self):
		"""
		Returns the preview widget, or 0 if there is none.
		"""
		res = super(QColumnView,self).previewWidget()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def resizeGripsVisible(self):
		"""
		This property holds the way to specify if the list views gets resize grips or not.
		By default, visible is set to true
		"""
		res = super(QColumnView,self).resizeGripsVisible()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def createColumn(self,rootIndex):
		"""
		createColumn(rootIndex)
			rootIndex=QtCore.QModelIndex

		To use a custom widget for the final column when you select an item overload this function and return a widget
		index is the root index that will be assigned to the view.
		Return the new view
		PySide.QtGui.QColumnView will automatically take ownership of the widget.
		"""
		res = super(QColumnView,self).createColumn(rootIndex)
		isinstance(res,QtGui.QAbstractItemView)
		return res
	#----------------------------------------------------------------------
	def initializeColumn(self,column):
		"""
		initializeColumn(column)
			column=QtGui.QAbstractItemView

		Copies the behavior and options of the column view and applies them to the column such as the PySide.QtGui.QAbstractItemView.iconSize() , PySide.QtGui.QAbstractItemView.textElideMode() and PySide.QtGui.QAbstractItemView.alternatingRowColors()
		This can be useful when reimplementing PySide.QtGui.QColumnView.createColumn() .
		"""
		res = super(QColumnView,self).initializeColumn(column)
		return res
	#----------------------------------------------------------------------
	def setColumnWidths(self,list):
		"""
		setColumnWidths(list)
			list=unKnown


		"""
		res = super(QColumnView,self).setColumnWidths(list)
		return res
	#----------------------------------------------------------------------
	def setPreviewWidget(self,widget):
		"""
		setPreviewWidget(widget)
			widget=QtGui.QWidget

		Sets the preview widget .
		The widget becomes a child of the column view, and will be destroyed when the column area is deleted or when a new widget is set.
		"""
		res = super(QColumnView,self).setPreviewWidget(widget)
		return res
	#----------------------------------------------------------------------
	def setResizeGripsVisible(self,visible):
		"""
		setResizeGripsVisible(visible)
			visible=QtCore.bool

		This property holds the way to specify if the list views gets resize grips or not.
		By default, visible is set to true
		"""
		res = super(QColumnView,self).setResizeGripsVisible(visible)
		return res

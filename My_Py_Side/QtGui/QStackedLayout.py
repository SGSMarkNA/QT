from PySide import QtGui, QtCore

class QStackedLayout(QtGui.QStackedLayout):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QStackedLayout,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def currentIndex(self):
		"""
		This property holds the index position of the widget that is visible.
		The current index is -1 if there is no current widget.
		"""
		res = super(QStackedLayout,self).currentIndex()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def currentWidget(self):
		"""
		Returns the current widget, or 0 if there are no widgets in this layout.
		"""
		res = super(QStackedLayout,self).currentWidget()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def stackingMode(self):
		"""
		This property determines the way visibility of child widgets are handled..
		The default value is StackOne
		Setting the property to StackAll allows you to make use of the layout for overlay widgets that do additional drawing on top of other widgets, for example, graphical editors.
		"""
		res = super(QStackedLayout,self).stackingMode()
		isinstance(res,QtGui.QStackedLayout.StackingMode)
		return res
	#----------------------------------------------------------------------
	def insertWidget(self,index,w):
		"""
		insertWidget(index,w)
			index=QtCore.int
			w=QtGui.QWidget

		Inserts the given widget at the given index in this PySide.QtGui.QStackedLayout
		If index is out of range, the widget is appended (in which case it is the actual index of the widget that is returned).
		If the PySide.QtGui.QStackedLayout is empty before this function is called, the given widget becomes the current widget.
		Inserting a new widget at an index less than or equal to the current index will increment the current index, but keep the current widget.
		"""
		res = super(QStackedLayout,self).insertWidget(index,w)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def setStackingMode(self,stackingMode):
		"""
		setStackingMode(stackingMode)
			stackingMode=QtGui.QStackedLayout.StackingMode

		This property determines the way visibility of child widgets are handled..
		The default value is StackOne
		Setting the property to StackAll allows you to make use of the layout for overlay widgets that do additional drawing on top of other widgets, for example, graphical editors.
		"""
		res = super(QStackedLayout,self).setStackingMode(stackingMode)
		return res
	#----------------------------------------------------------------------
	def widget(self,arg__1):
		"""
		widget(arg__1)
			arg__1=QtCore.int

		Returns the widget at the given index , or 0 if there is no widget at the given position.
		"""
		res = super(QStackedLayout,self).widget(arg__1)
		isinstance(res,QtGui.QWidget)
		return res

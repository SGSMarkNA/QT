from PySide import QtGui, QtCore

class QStackedWidget(QtGui.QStackedWidget):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QStackedWidget,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def count(self):
		"""
		This property holds the number of widgets contained by this stacked widget.
		By default, this property contains a value of 0.
		"""
		res = super(QStackedWidget,self).count()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def currentIndex(self):
		"""
		This property holds the index position of the widget that is visible.
		The current index is -1 if there is no current widget.
		By default, this property contains a value of -1 because the stack is initially empty.
		"""
		res = super(QStackedWidget,self).currentIndex()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def currentWidget(self):
		"""
		Returns the current widget, or 0 if there are no child widgets.
		"""
		res = super(QStackedWidget,self).currentWidget()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def addWidget(self,w):
		"""
		addWidget(w)
			w=QtGui.QWidget

		Appends the given widget to the PySide.QtGui.QStackedWidget and returns the index position
		Ownership of widget is passed on to the PySide.QtGui.QStackedWidget .
		If the PySide.QtGui.QStackedWidget is empty before this function is called, widget becomes the current widget.
		"""
		res = super(QStackedWidget,self).addWidget(w)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def indexOf(self,arg__1):
		"""
		indexOf(arg__1)
			arg__1=QtGui.QWidget

		Returns the index of the given widget , or -1 if the given widget is not a child of the PySide.QtGui.QStackedWidget .
		"""
		res = super(QStackedWidget,self).indexOf(arg__1)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def insertWidget(self,index,w):
		"""
		insertWidget(index,w)
			index=QtCore.int
			w=QtGui.QWidget

		Inserts the given widget at the given index in the PySide.QtGui.QStackedWidget
		Ownership of widget is passed on to the PySide.QtGui.QStackedWidget
		If index is out of range, the widget is appended (in which case it is the actual index of the widget that is returned).
		If the PySide.QtGui.QStackedWidget was empty before this function is called, the given widget becomes the current widget.
		Inserting a new widget at an index less than or equal to the current index will increment the current index, but keep the current widget.
		"""
		res = super(QStackedWidget,self).insertWidget(index,w)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def removeWidget(self,w):
		"""
		removeWidget(w)
			w=QtGui.QWidget

		Removes widget from the PySide.QtGui.QStackedWidget
		i.e., widget is not deleted but simply removed from the stacked layout, causing it to be hidden.
		"""
		res = super(QStackedWidget,self).removeWidget(w)
		return res
	#----------------------------------------------------------------------
	def widget(self,arg__1):
		"""
		widget(arg__1)
			arg__1=QtCore.int

		Returns the widget at the given index , or 0 if there is no such widget.
		"""
		res = super(QStackedWidget,self).widget(arg__1)
		isinstance(res,QtGui.QWidget)
		return res

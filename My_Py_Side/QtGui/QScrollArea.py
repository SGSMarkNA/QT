from PySide import QtGui, QtCore

class QScrollArea(QtGui.QScrollArea):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QScrollArea,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def alignment(self):
		"""
		This property holds the alignment of the scroll areas widget.
		By default, the widget stays rooted to the top-left corner of the scroll area.
		"""
		res = super(QScrollArea,self).alignment()
		isinstance(res,QtCore.Qt.Alignment)
		return res
	#----------------------------------------------------------------------
	def takeWidget(self):
		"""
		Removes the scroll areas widget, and passes ownership of the widget to the caller.
		"""
		res = super(QScrollArea,self).takeWidget()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def widget(self):
		"""
		Returns the scroll areas widget, or 0 if there is none.
		"""
		res = super(QScrollArea,self).widget()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def widgetResizable(self):
		"""
		This property holds whether the scroll area should resize the view widget.
		If this property is set to false (the default), the scroll area honors the size of its widget
		Regardless of this property, you can programmatically resize the widget using PySide.QtGui.QScrollArea.widget() -> PySide.QtGui.QWidget.resize() , and the scroll area will automatically adjust itself to the new size.
		If this property is set to true, the scroll area will automatically resize the widget in order to avoid scroll bars where they can be avoided, or to take advantage of extra space.
		"""
		res = super(QScrollArea,self).widgetResizable()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def ensureVisible(self,x,y,xmargin=None,ymargin=None):
		"""
		ensureVisible(x,y,xmargin=None,ymargin=None)
			x=QtCore.int
			y=QtCore.int
			xmargin=QtCore.int
			ymargin=QtCore.int

		Scrolls the contents of the scroll area so that the point (x , y ) is visible inside the region of the viewport with margins specified in pixels by xmargin and ymargin
		If the specified point cannot be reached, the contents are scrolled to the nearest valid position
		The default value for both margins is 50 pixels.
		"""
		res = super(QScrollArea,self).ensureVisible(x,y,xmargin,ymargin)
		return res
	#----------------------------------------------------------------------
	def ensureWidgetVisible(self,childWidget,xmargin=None,ymargin=None):
		"""
		ensureWidgetVisible(childWidget,xmargin=None,ymargin=None)
			childWidget=QtGui.QWidget
			xmargin=QtCore.int
			ymargin=QtCore.int

		Scrolls the contents of the scroll area so that the childWidget of QScrollArea.widget() is visible inside the viewport with margins specified in pixels by xmargin and ymargin
		If the specified point cannot be reached, the contents are scrolled to the nearest valid position
		The default value for both margins is 50 pixels.
		"""
		res = super(QScrollArea,self).ensureWidgetVisible(childWidget,xmargin,ymargin)
		return res
	#----------------------------------------------------------------------
	def setAlignment(self,arg__1):
		"""
		setAlignment(arg__1)
			arg__1=QtCore.Qt.Alignment

		This property holds the alignment of the scroll areas widget.
		By default, the widget stays rooted to the top-left corner of the scroll area.
		"""
		res = super(QScrollArea,self).setAlignment(arg__1)
		return res
	#----------------------------------------------------------------------
	def setWidget(self,widget):
		"""
		setWidget(widget)
			widget=QtGui.QWidget

		Sets the scroll areas widget .
		The widget becomes a child of the scroll area, and will be destroyed when the scroll area is deleted or when a new widget is set.
		The widgets autoFillBackground property will be set to true .
		If the scroll area is visible when the widget is added, you must PySide.QtGui.QWidget.show() it explicitly.
		Note that You must add the layout of widget before you call this function; if you add it later, the widget will not be visible - regardless of when you PySide.QtGui.QWidget.show() the scroll area
		In this case, you can also not PySide.QtGui.QWidget.show() the widget later.
		"""
		res = super(QScrollArea,self).setWidget(widget)
		return res
	#----------------------------------------------------------------------
	def setWidgetResizable(self,resizable):
		"""
		setWidgetResizable(resizable)
			resizable=QtCore.bool

		This property holds whether the scroll area should resize the view widget.
		If this property is set to false (the default), the scroll area honors the size of its widget
		Regardless of this property, you can programmatically resize the widget using PySide.QtGui.QScrollArea.widget() -> PySide.QtGui.QWidget.resize() , and the scroll area will automatically adjust itself to the new size.
		If this property is set to true, the scroll area will automatically resize the widget in order to avoid scroll bars where they can be avoided, or to take advantage of extra space.
		"""
		res = super(QScrollArea,self).setWidgetResizable(resizable)
		return res

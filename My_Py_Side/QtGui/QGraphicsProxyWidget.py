from PySide import QtGui, QtCore

class QGraphicsProxyWidget(QtGui.QGraphicsProxyWidget):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsProxyWidget,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def widget(self):
		"""
		Returns a pointer to the embedded widget.
		"""
		res = super(QGraphicsProxyWidget,self).widget()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def createProxyForChildWidget(self,child):
		"""
		createProxyForChildWidget(child)
			child=QtGui.QWidget

		Creates a proxy widget for the given child of the widget contained in this proxy.
		This function makes it possible to acquire proxies for non top-level widgets
		For instance, you can embed a dialog, and then transform only one of its widgets.
		If the widget is already embedded, return the existing proxy widget.
		"""
		res = super(QGraphicsProxyWidget,self).createProxyForChildWidget(child)
		isinstance(res,QtGui.QGraphicsProxyWidget)
		return res
	#----------------------------------------------------------------------
	def setWidget(self,widget):
		"""
		setWidget(widget)
			widget=QtGui.QWidget

		Embeds widget into this proxy widget
		The embedded widget must reside exclusively either inside or outside of Graphics View
		You cannot embed a widget as long as it is is visible elsewhere in the UI, at the same time.
		widget must be a top-level widget whose parent is 0.
		When the widget is embedded, its state (e.g., visible, enabled, geometry, size hints) is copied into the proxy widget
		If the embedded widget is explicitly hidden or disabled, the proxy widget will become explicitly hidden or disabled after embedding is complete
		The class documentation has a full overview over the shared state.
		PySide.QtGui.QGraphicsProxyWidget s window flags determine whether the widget, after embedding, will be given window decorations or not.
		After this function returns, PySide.QtGui.QGraphicsProxyWidget will keep its state synchronized with that of widget whenever possible.
		If a widget is already embedded by this proxy when this function is called, that widget will first be automatically unembedded
		Passing 0 for the widget argument will only unembed the widget, and the ownership of the currently embedded widget will be passed on to the caller
		Every child widget that are embedded will also be embedded and their proxy widget destroyed.
		Note that widgets with the Qt.WA_PaintOnScreen widget attribute set and widgets that wrap an external application or controller cannot be embedded
		Examples are PySide.QtOpenGL.QGLWidget and QAxWidget .
		"""
		res = super(QGraphicsProxyWidget,self).setWidget(widget)
		return res
	#----------------------------------------------------------------------
	def subWidgetRect(self,widget):
		"""
		subWidgetRect(widget)
			widget=QtGui.QWidget

		Returns the rectangle for widget , which must be a descendant of PySide.QtGui.QGraphicsProxyWidget.widget() , or PySide.QtGui.QGraphicsProxyWidget.widget() itself, in this proxy items local coordinates.
		If no widget is embedded, widget is 0, or widget is not a descendant of the embedded widget, this function returns an empty PySide.QtCore.QRectF .
		"""
		res = super(QGraphicsProxyWidget,self).subWidgetRect(widget)
		isinstance(res,QtCore.QRectF)
		return res

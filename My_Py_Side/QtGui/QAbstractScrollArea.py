from PySide import QtGui, QtCore
from QFrame import QFrame
class QAbstractScrollArea(QtGui.QAbstractScrollArea, QFrame):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QAbstractScrollArea,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def cornerWidget(self):
		"""
		Returns the widget in the corner between the two scroll bars.
		By default, no corner widget is present.
		"""
		res = super(QAbstractScrollArea,self).cornerWidget()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def horizontalScrollBar(self):
		"""
		Returns the horizontal scroll bar.
		"""
		res = super(QAbstractScrollArea,self).horizontalScrollBar()
		isinstance(res,QtGui.QScrollBar)
		return res
	#----------------------------------------------------------------------
	def horizontalScrollBarPolicy(self):
		"""
		This property holds the policy for the horizontal scroll bar.
		The default policy is Qt.ScrollBarAsNeeded .
		"""
		res = super(QAbstractScrollArea,self).horizontalScrollBarPolicy()
		isinstance(res,QtCore.Qt.ScrollBarPolicy)
		return res
	#----------------------------------------------------------------------
	def maximumViewportSize(self):
		"""
		Returns the size of the viewport as if the scroll bars had no valid scrolling range.
		"""
		res = super(QAbstractScrollArea,self).maximumViewportSize()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def verticalScrollBar(self):
		"""
		Returns the vertical scroll bar.
		"""
		res = super(QAbstractScrollArea,self).verticalScrollBar()
		isinstance(res,QtGui.QScrollBar)
		return res
	#----------------------------------------------------------------------
	def verticalScrollBarPolicy(self):
		"""
		This property holds the policy for the vertical scroll bar.
		The default policy is Qt.ScrollBarAsNeeded .
		"""
		res = super(QAbstractScrollArea,self).verticalScrollBarPolicy()
		isinstance(res,QtCore.Qt.ScrollBarPolicy)
		return res
	#----------------------------------------------------------------------
	def viewport(self):
		"""
		Returns the viewport widget.
		Use the QScrollArea.widget() function to retrieve the contents of the viewport widget.
		"""
		res = super(QAbstractScrollArea,self).viewport()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def addScrollBarWidget(self,widget,alignment):
		"""
		addScrollBarWidget(widget,alignment)
			widget=QtGui.QWidget
			alignment=QtCore.Qt.Alignment


		"""
		res = super(QAbstractScrollArea,self).addScrollBarWidget(widget,alignment)
		return res
	#----------------------------------------------------------------------
	def scrollBarWidgets(self,alignment):
		"""
		scrollBarWidgets(alignment)
			alignment=QtCore.Qt.Alignment


		"""
		res = super(QAbstractScrollArea,self).scrollBarWidgets(alignment)
		return res
	#----------------------------------------------------------------------
	def scrollContentsBy(self,dx,dy):
		"""
		scrollContentsBy(dx,dy)
			dx=QtCore.int
			dy=QtCore.int

		This virtual handler is called when the scroll bars are moved by dx , dy , and consequently the viewports contents should be scrolled accordingly.
		The default implementation simply calls PySide.QtGui.QWidget.update() on the entire PySide.QtGui.QAbstractScrollArea.viewport() , subclasses can reimplement this handler for optimization purposes, or - like PySide.QtGui.QScrollArea - to move a contents widget
		The parameters dx and dy are there for convenience, so that the class knows how much should be scrolled (useful e.g
		when doing pixel-shifts)
		You may just as well ignore these values and scroll directly to the position the scroll bars indicate.
		Calling this function in order to scroll programmatically is an error, use the scroll bars instead (e.g
		by calling QScrollBar.setValue() directly).
		"""
		res = super(QAbstractScrollArea,self).scrollContentsBy(dx,dy)
		return res
	#----------------------------------------------------------------------
	def setCornerWidget(self,widget):
		"""
		setCornerWidget(widget)
			widget=QtGui.QWidget

		Sets the widget in the corner between the two scroll bars to be widget .
		You will probably also want to set at least one of the scroll bar modes to AlwaysOn .
		Passing 0 shows no widget in the corner.
		Any previous corner widget is hidden.
		You may call PySide.QtGui.QAbstractScrollArea.setCornerWidget() with the same widget at different times.
		All widgets set here will be deleted by the scroll area when it is destroyed unless you separately reparent the widget after setting some other corner widget (or 0).
		Any newly set widget should have no current parent.
		By default, no corner widget is present.
		"""
		res = super(QAbstractScrollArea,self).setCornerWidget(widget)
		return res
	#----------------------------------------------------------------------
	def setHorizontalScrollBar(self,scrollbar):
		"""
		setHorizontalScrollBar(scrollbar)
			scrollbar=QtGui.QScrollBar

		Replaces the existing horizontal scroll bar with scrollBar , and sets all the former scroll bars slider properties on the new scroll bar
		The former scroll bar is then deleted.
		PySide.QtGui.QAbstractScrollArea already provides horizontal and vertical scroll bars by default
		You can call this function to replace the default horizontal scroll bar with your own custom scroll bar.
		"""
		res = super(QAbstractScrollArea,self).setHorizontalScrollBar(scrollbar)
		return res
	#----------------------------------------------------------------------
	def setHorizontalScrollBarPolicy(self,arg__1):
		"""
		setHorizontalScrollBarPolicy(arg__1)
			arg__1=QtCore.Qt.ScrollBarPolicy

		This property holds the policy for the horizontal scroll bar.
		The default policy is Qt.ScrollBarAsNeeded .
		"""
		res = super(QAbstractScrollArea,self).setHorizontalScrollBarPolicy(arg__1)
		return res
	#----------------------------------------------------------------------
	def setVerticalScrollBar(self,scrollbar):
		"""
		setVerticalScrollBar(scrollbar)
			scrollbar=QtGui.QScrollBar

		Replaces the existing vertical scroll bar with scrollBar , and sets all the former scroll bars slider properties on the new scroll bar
		The former scroll bar is then deleted.
		PySide.QtGui.QAbstractScrollArea already provides vertical and horizontal scroll bars by default
		You can call this function to replace the default vertical scroll bar with your own custom scroll bar.
		"""
		res = super(QAbstractScrollArea,self).setVerticalScrollBar(scrollbar)
		return res
	#----------------------------------------------------------------------
	def setVerticalScrollBarPolicy(self,arg__1):
		"""
		setVerticalScrollBarPolicy(arg__1)
			arg__1=QtCore.Qt.ScrollBarPolicy

		This property holds the policy for the vertical scroll bar.
		The default policy is Qt.ScrollBarAsNeeded .
		"""
		res = super(QAbstractScrollArea,self).setVerticalScrollBarPolicy(arg__1)
		return res
	#----------------------------------------------------------------------
	def setViewport(self,widget):
		"""
		setViewport(widget)
			widget=QtGui.QWidget

		Sets the viewport to be the given widget
		The PySide.QtGui.QAbstractScrollArea will take ownership of the given widget .
		If widget is 0, PySide.QtGui.QAbstractScrollArea will assign a new PySide.QtGui.QWidget instance for the viewport.
		"""
		res = super(QAbstractScrollArea,self).setViewport(widget)
		return res
	#----------------------------------------------------------------------
	def setViewportMargins(self,*args,**kwargs):
		"""
		setViewportMargins(left,top,right,bottom)
			left=QtCore.int
			top=QtCore.int
			right=QtCore.int
			bottom=QtCore.int

		setViewportMargins(margins)
			margins=QtCore.QMargins

		Sets the margins around the scrolling area to left , top , right and bottom
		This is useful for applications such as spreadsheets with locked rows and columns
		The marginal space is is left blank; put widgets in the unused area.
		Note that this function is frequently called by PySide.QtGui.QTreeView and PySide.QtGui.QTableView , so margins must be implemented by PySide.QtGui.QAbstractScrollArea subclasses
		Also, if the subclasses are to be used in item views, they should not call this function.
		By default all margins are zero.
		"""
		res = super(QAbstractScrollArea,self).setViewportMargins(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def viewportEvent(self,arg__1):
		"""
		viewportEvent(arg__1)
			arg__1=QtCore.QEvent

		The main event handler for the scrolling area (the PySide.QtGui.QAbstractScrollArea.viewport() widget)
		It handles the event specified, and can be called by subclasses to provide reasonable default behavior.
		Returns true to indicate to the event system that the event has been handled, and needs no further processing; otherwise returns false to indicate that the event should be propagated further.
		You can reimplement this function in a subclass, but we recommend using one of the specialized event handlers instead.
		Specialized handlers for viewport events are: PySide.QtGui.QAbstractScrollArea.paintEvent() , PySide.QtGui.QAbstractScrollArea.mousePressEvent() , PySide.QtGui.QAbstractScrollArea.mouseReleaseEvent() , PySide.QtGui.QAbstractScrollArea.mouseDoubleClickEvent() , PySide.QtGui.QAbstractScrollArea.mouseMoveEvent() , PySide.QtGui.QAbstractScrollArea.wheelEvent() , PySide.QtGui.QAbstractScrollArea.dragEnterEvent() , PySide.QtGui.QAbstractScrollArea.dragMoveEvent() , PySide.QtGui.QAbstractScrollArea.dragLeaveEvent() , PySide.QtGui.QAbstractScrollArea.dropEvent() , PySide.QtGui.QAbstractScrollArea.contextMenuEvent() , and PySide.QtGui.QAbstractScrollArea.resizeEvent() .
		"""
		res = super(QAbstractScrollArea,self).viewportEvent(arg__1)
		return res

	CornerWidget              = property(cornerWidget)
	HorizontalScrollBar       = property(horizontalScrollBar)
	HorizontalScrollBarPolicy = property(horizontalScrollBarPolicy)
	MaximumViewportSize       = property(maximumViewportSize)
	VerticalScrollBar         = property(verticalScrollBar)
	VerticalScrollBarPolicy   = property(verticalScrollBarPolicy)
	Viewport                  = property(viewport)

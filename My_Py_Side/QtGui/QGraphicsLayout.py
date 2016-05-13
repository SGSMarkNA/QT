from PySide import QtGui, QtCore

class QGraphicsLayout(QtGui.QGraphicsLayout):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsLayout,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def activate(self):
		"""
		Activates the layout, causing all items in the layout to be immediately rearranged
		This function is based on calling PySide.QtGui.QGraphicsLayout.count() and PySide.QtGui.QGraphicsLayout.itemAt() , and then calling PySide.QtGui.QGraphicsLayoutItem.setGeometry() on all items sequentially
		When activated, the layout will adjust its geometry to its parents PySide.QtGui.QGraphicsLayoutItem.contentsRect()
		The parent will then invalidate any layout of its own.
		If called in sequence or recursively, e.g., by one of the arranged items in response to being resized, this function will do nothing.
		Note that the layout is free to use geometry caching to optimize this process
		To forcefully invalidate any such cache, you can call PySide.QtGui.QGraphicsLayout.invalidate() before calling PySide.QtGui.QGraphicsLayout.activate() .
		"""
		res = super(QGraphicsLayout,self).activate()
		return res
	#----------------------------------------------------------------------
	def count(self):
		"""
		This pure virtual function must be reimplemented in a subclass of PySide.QtGui.QGraphicsLayout to return the number of items in the layout.
		The subclass is free to decide how to store the items.
		"""
		res = super(QGraphicsLayout,self).count()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def invalidate(self):
		"""
		Clears any cached geometry and size hint information in the layout, and posts a LayoutRequest event to the managed parent PySide.QtGui.QGraphicsLayoutItem .
		"""
		res = super(QGraphicsLayout,self).invalidate()
		return res
	#----------------------------------------------------------------------
	def isActivated(self):
		"""
		Returns true if the layout is currently being activated; otherwise, returns false
		If the layout is being activated, this means that it is currently in the process of rearranging its items (i.e., the PySide.QtGui.QGraphicsLayout.activate() function has been called, and has not yet returned).
		"""
		res = super(QGraphicsLayout,self).isActivated()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def addChildLayoutItem(self,layoutItem):
		"""
		addChildLayoutItem(layoutItem)
			layoutItem=QtGui.QGraphicsLayoutItem

		This function is a convenience function provided for custom layouts, and will go through all items in the layout and reparent their graphics items to the closest PySide.QtGui.QGraphicsWidget ancestor of the layout.
		If layoutItem is already in a different layout, it will be removed from that layout.
		If custom layouts want special behaviour they can ignore to use this function, and implement their own behaviour.
		"""
		res = super(QGraphicsLayout,self).addChildLayoutItem(layoutItem)
		return res
	#----------------------------------------------------------------------
	def itemAt(self,i):
		"""
		itemAt(i)
			i=QtCore.int

		This pure virtual function must be reimplemented in a subclass of PySide.QtGui.QGraphicsLayout to return a pointer to the item at index i
		The reimplementation can assume that i is valid (i.e., it respects the value of PySide.QtGui.QGraphicsLayout.count() )
		Together with PySide.QtGui.QGraphicsLayout.count() , it is provided as a means of iterating over all items in a layout.
		The subclass is free to decide how to store the items, and the visual arrangement does not have to be reflected through this function.
		"""
		res = super(QGraphicsLayout,self).itemAt(i)
		isinstance(res,QtGui.QGraphicsLayoutItem)
		return res
	#----------------------------------------------------------------------
	def removeAt(self,index):
		"""
		removeAt(index)
			index=QtCore.int

		This pure virtual function must be reimplemented in a subclass of PySide.QtGui.QGraphicsLayout to remove the item at index
		The reimplementation can assume that index is valid (i.e., it respects the value of PySide.QtGui.QGraphicsLayout.count() ).
		The implementation must ensure that the PySide.QtGui.QGraphicsLayoutItem.parentLayoutItem() of the removed item does not point to this layout, since the item is considered to be removed from the layout hierarchy.
		If the layout is to be reused between applications, we recommend that the layout deletes the item, but the graphics view framework does not depend on this.
		The subclass is free to decide how to store the items.
		"""
		res = super(QGraphicsLayout,self).removeAt(index)
		return res
	#----------------------------------------------------------------------
	def setContentsMargins(self,left,top,right,bottom):
		"""
		setContentsMargins(left,top,right,bottom)
			left=QtCore.qreal
			top=QtCore.qreal
			right=QtCore.qreal
			bottom=QtCore.qreal

		Sets the contents margins to left , top , right and bottom
		The default contents margins for toplevel layouts are style dependent (by querying the pixelMetric for QStyle.PM_LayoutLeftMargin , QStyle.PM_LayoutTopMargin , QStyle.PM_LayoutRightMargin and QStyle.PM_LayoutBottomMargin ).
		For sublayouts the default margins are 0.
		Changing the contents margins automatically invalidates the layout.
		"""
		res = super(QGraphicsLayout,self).setContentsMargins(left,top,right,bottom)
		return res
	#----------------------------------------------------------------------
	def widgetEvent(self,e):
		"""
		widgetEvent(e)
			e=QtCore.QEvent

		This virtual event handler receives all events for the managed widget
		PySide.QtGui.QGraphicsLayout uses this event handler to listen for layout related events such as geometry changes, layout changes or layout direction changes.
		e is a pointer to the event.
		You can reimplement this event handler to track similar events for your own custom layout.
		"""
		res = super(QGraphicsLayout,self).widgetEvent(e)
		return res

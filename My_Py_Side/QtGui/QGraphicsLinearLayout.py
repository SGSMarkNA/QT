from PySide import QtGui, QtCore

class QGraphicsLinearLayout(QtGui.QGraphicsLinearLayout):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsLinearLayout,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def orientation(self):
		"""
		Returns the layout orientation.
		"""
		res = super(QGraphicsLinearLayout,self).orientation()
		isinstance(res,QtCore.Qt.Orientation)
		return res
	#----------------------------------------------------------------------
	def spacing(self):
		"""
		Returns the layouts spacing
		Spacing refers to the vertical and horizontal distances between items.
		"""
		res = super(QGraphicsLinearLayout,self).spacing()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def addItem(self,item):
		"""
		addItem(item)
			item=QtGui.QGraphicsLayoutItem

		This convenience function is equivalent to calling insertItem(-1, item ).
		"""
		res = super(QGraphicsLinearLayout,self).addItem(item)
		return res
	#----------------------------------------------------------------------
	def addStretch(self,stretch=None):
		"""
		addStretch(stretch=None)
			stretch=QtCore.int

		This convenience function is equivalent to calling insertStretch(-1, stretch ).
		"""
		res = super(QGraphicsLinearLayout,self).addStretch(stretch)
		return res
	#----------------------------------------------------------------------
	def alignment(self,item):
		"""
		alignment(item)
			item=QtGui.QGraphicsLayoutItem

		Returns the alignment for item
		The default alignment is Qt.AlignTop | Qt.AlignLeft .
		The alignment decides how the item is positioned within its assigned space in the case where theres more space available in the layout than the widgets can occupy.
		"""
		res = super(QGraphicsLinearLayout,self).alignment(item)
		isinstance(res,QtCore.Qt.Alignment)
		return res
	#----------------------------------------------------------------------
	def dump(self,indent=None):
		"""
		dump(indent=None)
			indent=QtCore.int


		"""
		res = super(QGraphicsLinearLayout,self).dump(indent)
		return res
	#----------------------------------------------------------------------
	def insertItem(self,index,item):
		"""
		insertItem(index,item)
			index=QtCore.int
			item=QtGui.QGraphicsLayoutItem

		Inserts item into the layout at index , or before any item that is currently at index .
		"""
		res = super(QGraphicsLinearLayout,self).insertItem(index,item)
		return res
	#----------------------------------------------------------------------
	def insertStretch(self,index,stretch=None):
		"""
		insertStretch(index,stretch=None)
			index=QtCore.int
			stretch=QtCore.int

		Inserts a stretch of stretch at index , or before any item that is currently at index .
		"""
		res = super(QGraphicsLinearLayout,self).insertStretch(index,stretch)
		return res
	#----------------------------------------------------------------------
	def itemSpacing(self,index):
		"""
		itemSpacing(index)
			index=QtCore.int

		Returns the spacing after item at index .
		"""
		res = super(QGraphicsLinearLayout,self).itemSpacing(index)
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def removeItem(self,item):
		"""
		removeItem(item)
			item=QtGui.QGraphicsLayoutItem

		Removes item from the layout without destroying it
		Ownership of item is transferred to the caller.
		"""
		res = super(QGraphicsLinearLayout,self).removeItem(item)
		return res
	#----------------------------------------------------------------------
	def setAlignment(self,item,alignment):
		"""
		setAlignment(item,alignment)
			item=QtGui.QGraphicsLayoutItem
			alignment=QtCore.Qt.Alignment


		"""
		res = super(QGraphicsLinearLayout,self).setAlignment(item,alignment)
		return res
	#----------------------------------------------------------------------
	def setItemSpacing(self,index,spacing):
		"""
		setItemSpacing(index,spacing)
			index=QtCore.int
			spacing=QtCore.qreal

		Sets the spacing after item at index to spacing .
		"""
		res = super(QGraphicsLinearLayout,self).setItemSpacing(index,spacing)
		return res
	#----------------------------------------------------------------------
	def setOrientation(self,orientation):
		"""
		setOrientation(orientation)
			orientation=QtCore.Qt.Orientation


		"""
		res = super(QGraphicsLinearLayout,self).setOrientation(orientation)
		return res
	#----------------------------------------------------------------------
	def setSpacing(self,spacing):
		"""
		setSpacing(spacing)
			spacing=QtCore.qreal

		Sets the layouts spacing to spacing
		Spacing refers to the vertical and horizontal distances between items.
		"""
		res = super(QGraphicsLinearLayout,self).setSpacing(spacing)
		return res
	#----------------------------------------------------------------------
	def setStretchFactor(self,item,stretch):
		"""
		setStretchFactor(item,stretch)
			item=QtGui.QGraphicsLayoutItem
			stretch=QtCore.int

		Sets the stretch factor for item to stretch
		If an items stretch factor changes, this function will invalidate the layout.
		Setting stretch to 0 removes the stretch factor from the item, and is effectively equivalent to setting stretch to 1.
		"""
		res = super(QGraphicsLinearLayout,self).setStretchFactor(item,stretch)
		return res
	#----------------------------------------------------------------------
	def stretchFactor(self,item):
		"""
		stretchFactor(item)
			item=QtGui.QGraphicsLayoutItem

		Returns the stretch factor for item
		The default stretch factor is 0, meaning that the item has no assigned stretch factor.
		"""
		res = super(QGraphicsLinearLayout,self).stretchFactor(item)
		isinstance(res,QtCore.int)
		return res

from PySide import QtGui, QtCore

class QGraphicsAnchorLayout(QtGui.QGraphicsAnchorLayout):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsAnchorLayout,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def horizontalSpacing(self):
		"""
		Returns the default horizontal spacing for the anchor layout.
		"""
		res = super(QGraphicsAnchorLayout,self).horizontalSpacing()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def verticalSpacing(self):
		"""
		Returns the default vertical spacing for the anchor layout.
		"""
		res = super(QGraphicsAnchorLayout,self).verticalSpacing()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def addAnchor(self,firstItem,firstEdge,secondItem,secondEdge):
		"""
		addAnchor(firstItem,firstEdge,secondItem,secondEdge)
			firstItem=QtGui.QGraphicsLayoutItem
			firstEdge=QtCore.Qt.AnchorPoint
			secondItem=QtGui.QGraphicsLayoutItem
			secondEdge=QtCore.Qt.AnchorPoint


		"""
		res = super(QGraphicsAnchorLayout,self).addAnchor(firstItem,firstEdge,secondItem,secondEdge)
		isinstance(res,QtGui.QGraphicsAnchor)
		return res
	#----------------------------------------------------------------------
	def addAnchors(self,firstItem,secondItem,orientations=None):
		"""
		addAnchors(firstItem,secondItem,orientations=None)
			firstItem=QtGui.QGraphicsLayoutItem
			secondItem=QtGui.QGraphicsLayoutItem
			orientations=QtCore.Qt.Orientations


		"""
		res = super(QGraphicsAnchorLayout,self).addAnchors(firstItem,secondItem,orientations)
		return res
	#----------------------------------------------------------------------
	def addCornerAnchors(self,firstItem,firstCorner,secondItem,secondCorner):
		"""
		addCornerAnchors(firstItem,firstCorner,secondItem,secondCorner)
			firstItem=QtGui.QGraphicsLayoutItem
			firstCorner=QtCore.Qt.Corner
			secondItem=QtGui.QGraphicsLayoutItem
			secondCorner=QtCore.Qt.Corner


		"""
		res = super(QGraphicsAnchorLayout,self).addCornerAnchors(firstItem,firstCorner,secondItem,secondCorner)
		return res
	#----------------------------------------------------------------------
	def anchor(self,firstItem,firstEdge,secondItem,secondEdge):
		"""
		anchor(firstItem,firstEdge,secondItem,secondEdge)
			firstItem=QtGui.QGraphicsLayoutItem
			firstEdge=QtCore.Qt.AnchorPoint
			secondItem=QtGui.QGraphicsLayoutItem
			secondEdge=QtCore.Qt.AnchorPoint


		"""
		res = super(QGraphicsAnchorLayout,self).anchor(firstItem,firstEdge,secondItem,secondEdge)
		isinstance(res,QtGui.QGraphicsAnchor)
		return res
	#----------------------------------------------------------------------
	def setHorizontalSpacing(self,spacing):
		"""
		setHorizontalSpacing(spacing)
			spacing=QtCore.qreal

		Sets the default horizontal spacing for the anchor layout to spacing .
		"""
		res = super(QGraphicsAnchorLayout,self).setHorizontalSpacing(spacing)
		return res
	#----------------------------------------------------------------------
	def setSpacing(self,spacing):
		"""
		setSpacing(spacing)
			spacing=QtCore.qreal

		Sets the default horizontal and the default vertical spacing for the anchor layout to spacing .
		If an item is anchored with no spacing associated with the anchor, it will use the default spacing.
		PySide.QtGui.QGraphicsAnchorLayout does not support negative spacings
		Setting a negative value will unset the previous spacing and make the layout use the spacing provided by the current widget style.
		"""
		res = super(QGraphicsAnchorLayout,self).setSpacing(spacing)
		return res
	#----------------------------------------------------------------------
	def setVerticalSpacing(self,spacing):
		"""
		setVerticalSpacing(spacing)
			spacing=QtCore.qreal

		Sets the default vertical spacing for the anchor layout to spacing .
		"""
		res = super(QGraphicsAnchorLayout,self).setVerticalSpacing(spacing)
		return res

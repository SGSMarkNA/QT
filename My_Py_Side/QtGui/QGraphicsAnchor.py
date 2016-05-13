from PySide import QtGui, QtCore

class QGraphicsAnchor(QtGui.QGraphicsAnchor):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsAnchor,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def sizePolicy(self):
		"""
		This property holds the size policy for the PySide.QtGui.QGraphicsAnchor ..
		By setting the size policy on an anchor you can configure how the anchor can resize itself from its preferred spacing
		For instance, if the anchor has the size policy QSizePolicy.Minimum , the spacing is the minimum size of the anchor
		However, its size can grow up to the anchors maximum size
		If the default size policy is QSizePolicy.Fixed , the anchor can neither grow or shrink, which means that the only size the anchor can have is the spacing
		QSizePolicy.Fixed is the default size policy
		PySide.QtGui.QGraphicsAnchor always has a minimum spacing of 0 and a very large maximum spacing.
		"""
		res = super(QGraphicsAnchor,self).sizePolicy()
		isinstance(res,QtGui.QSizePolicy.Policy)
		return res
	#----------------------------------------------------------------------
	def spacing(self):
		"""
		This property holds the preferred space between items in the PySide.QtGui.QGraphicsAnchorLayout ..
		Depending on the anchor type, the default spacing is either 0 or a value returned from the style.
		"""
		res = super(QGraphicsAnchor,self).spacing()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def unsetSpacing(self):
		"""
		This property holds the preferred space between items in the PySide.QtGui.QGraphicsAnchorLayout ..
		Depending on the anchor type, the default spacing is either 0 or a value returned from the style.
		"""
		res = super(QGraphicsAnchor,self).unsetSpacing()
		return res
	#----------------------------------------------------------------------
	def setSizePolicy(self,policy):
		"""
		setSizePolicy(policy)
			policy=QtGui.QSizePolicy.Policy

		This property holds the size policy for the PySide.QtGui.QGraphicsAnchor ..
		By setting the size policy on an anchor you can configure how the anchor can resize itself from its preferred spacing
		For instance, if the anchor has the size policy QSizePolicy.Minimum , the spacing is the minimum size of the anchor
		However, its size can grow up to the anchors maximum size
		If the default size policy is QSizePolicy.Fixed , the anchor can neither grow or shrink, which means that the only size the anchor can have is the spacing
		QSizePolicy.Fixed is the default size policy
		PySide.QtGui.QGraphicsAnchor always has a minimum spacing of 0 and a very large maximum spacing.
		"""
		res = super(QGraphicsAnchor,self).setSizePolicy(policy)
		return res
	#----------------------------------------------------------------------
	def setSpacing(self,spacing):
		"""
		setSpacing(spacing)
			spacing=QtCore.qreal

		This property holds the preferred space between items in the PySide.QtGui.QGraphicsAnchorLayout ..
		Depending on the anchor type, the default spacing is either 0 or a value returned from the style.
		"""
		res = super(QGraphicsAnchor,self).setSpacing(spacing)
		return res

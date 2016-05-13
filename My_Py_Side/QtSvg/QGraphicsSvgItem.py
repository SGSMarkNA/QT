from PySide import QtGui, QtCore

class QGraphicsSvgItem(QtSvg.QGraphicsSvgItem):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsSvgItem,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def elementId(self):
		"""
		This property holds the elements XML ID.
		"""
		res = super(QGraphicsSvgItem,self).elementId()
		return res
	#----------------------------------------------------------------------
	def isCachingEnabled(self):
		"""
		Use QGraphicsItem.cacheMode() instead.
		"""
		res = super(QGraphicsSvgItem,self).isCachingEnabled()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def maximumCacheSize(self):
		"""
		This property holds the maximum size of the device coordinate cache for this item.
		"""
		res = super(QGraphicsSvgItem,self).maximumCacheSize()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def renderer(self):
		"""
		Returns the currently use PySide.QtSvg.QSvgRenderer .
		"""
		res = super(QGraphicsSvgItem,self).renderer()
		isinstance(res,QtSvg.QSvgRenderer)
		return res
	#----------------------------------------------------------------------
	def setCachingEnabled(self,arg__1):
		"""
		setCachingEnabled(arg__1)
			arg__1=QtCore.bool

		Use QGraphicsItem.setCacheMode() instead
		Passing true to this function is equivalent to QGraphicsItem::setCacheMode( QGraphicsItem.DeviceCoordinateCache ).
		"""
		res = super(QGraphicsSvgItem,self).setCachingEnabled(arg__1)
		return res
	#----------------------------------------------------------------------
	def setElementId(self,id):
		"""
		setElementId(id)
			id=unicode

		This property holds the elements XML ID.
		"""
		res = super(QGraphicsSvgItem,self).setElementId(id)
		return res
	#----------------------------------------------------------------------
	def setMaximumCacheSize(self,size):
		"""
		setMaximumCacheSize(size)
			size=QtCore.QSize

		This property holds the maximum size of the device coordinate cache for this item.
		"""
		res = super(QGraphicsSvgItem,self).setMaximumCacheSize(size)
		return res
	#----------------------------------------------------------------------
	def setSharedRenderer(self,renderer):
		"""
		setSharedRenderer(renderer)
			renderer=QtSvg.QSvgRenderer

		Sets renderer to be a shared PySide.QtSvg.QSvgRenderer on the item
		By using this method one can share the same PySide.QtSvg.QSvgRenderer on a number of items
		This means that the SVG file will be parsed only once
		PySide.QtSvg.QSvgRenderer passed to this method has to exist for as long as this item is used.
		"""
		res = super(QGraphicsSvgItem,self).setSharedRenderer(renderer)
		return res

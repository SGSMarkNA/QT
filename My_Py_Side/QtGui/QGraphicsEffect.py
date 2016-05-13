from PySide import QtGui, QtCore

class QGraphicsEffect(QtGui.QGraphicsEffect):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsEffect,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def boundingRect(self):
		"""
		Returns the effective bounding rectangle for this effect, i.e., the bounding rectangle of the source in device coordinates, adjusted by any margins applied by the effect itself.
		"""
		res = super(QGraphicsEffect,self).boundingRect()
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def isEnabled(self):
		"""
		This property holds whether the effect is enabled or not..
		If an effect is disabled, the source will be rendered with as normal, with no interference from the effect
		If the effect is enabled, the source will be rendered with the effect applied.
		This property is enabled by default.
		Using this property, you can disable certain effects on slow platforms, in order to ensure that the user interface is responsive.
		"""
		res = super(QGraphicsEffect,self).isEnabled()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def sourceIsPixmap(self):
		"""
		Returns true if the source effectively is a pixmap, e.g., a PySide.QtGui.QGraphicsPixmapItem .
		This function is useful for optimization purposes
		For instance, theres no point in drawing the source in device coordinates to avoid pixmap scaling if this function returns true - the source pixmap will be scaled anyways.
		"""
		res = super(QGraphicsEffect,self).sourceIsPixmap()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def updateBoundingRect(self):
		"""
		This function notifies the effect framework when the effects bounding rectangle has changed
		As a custom effect author, you must call this function whenever you change any parameters that will cause the virtual PySide.QtGui.QGraphicsEffect.boundingRectFor() function to return a different value.
		This function will call PySide.QtGui.QGraphicsEffect.update() if this is necessary.
		"""
		res = super(QGraphicsEffect,self).updateBoundingRect()
		return res
	#----------------------------------------------------------------------
	def boundingRectFor(self,sourceRect):
		"""
		boundingRectFor(sourceRect)
			sourceRect=QtCore.QRectF

		Returns the effective bounding rectangle for this effect, given the provided rect in the device coordinates
		When writing you own custom effect, you must call PySide.QtGui.QGraphicsEffect.updateBoundingRect() whenever any parameters are changed that may cause this this function to return a different value.
		"""
		res = super(QGraphicsEffect,self).boundingRectFor(sourceRect)
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def draw(self,painter):
		"""
		draw(painter)
			painter=QtGui.QPainter

		This pure virtual function draws the effect and is called whenever the source needs to be drawn.
		Reimplement this function in a PySide.QtGui.QGraphicsEffect subclass to provide the effects drawing implementation, using painter .
		For example:
		This function should not be called explicitly by the user, since it is meant for reimplementation purposes only.
		"""
		res = super(QGraphicsEffect,self).draw(painter)
		return res
	#----------------------------------------------------------------------
	def drawSource(self,painter):
		"""
		drawSource(painter)
			painter=QtGui.QPainter

		Draws the source directly using the given painter .
		This function should only be called from QGraphicsEffect.draw() .
		For example:
		"""
		res = super(QGraphicsEffect,self).drawSource(painter)
		return res
	#----------------------------------------------------------------------
	def sourceBoundingRect(self,system=None):
		"""
		sourceBoundingRect(system=None)
			system=QtCore.Qt.CoordinateSystem


		"""
		res = super(QGraphicsEffect,self).sourceBoundingRect(system)
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def sourceChanged(self,flags):
		"""
		sourceChanged(flags)
			flags=QtGui.QGraphicsEffect.ChangeFlags


		"""
		res = super(QGraphicsEffect,self).sourceChanged(flags)
		return res
	#----------------------------------------------------------------------
	def sourcePixmap(self,system=None,offset=None,mode=None):
		"""
		sourcePixmap(system=None,offset=None,mode=None)
			system=QtCore.Qt.CoordinateSystem
			offset=QtCore.QPoint
			mode=QtGui.QGraphicsEffect.PixmapPadMode


		"""
		res = super(QGraphicsEffect,self).sourcePixmap(system,offset,mode)
		isinstance(res,QtGui.QPixmap)
		return res

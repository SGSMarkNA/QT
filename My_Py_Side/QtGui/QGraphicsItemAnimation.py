from PySide import QtGui, QtCore

class QGraphicsItemAnimation(QtGui.QGraphicsItemAnimation):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsItemAnimation,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Clears the scheduled transformations used for the animation, but retains the item and timeline.
		"""
		res = super(QGraphicsItemAnimation,self).clear()
		return res
	#----------------------------------------------------------------------
	def item(self):
		"""
		Returns the item on which the animation object operates.
		"""
		res = super(QGraphicsItemAnimation,self).item()
		isinstance(res,QtGui.QGraphicsItem)
		return res
	#----------------------------------------------------------------------
	def posList(self):
		"""
		Returns all explicitly inserted positions.
		"""
		res = super(QGraphicsItemAnimation,self).posList()
		return res
	#----------------------------------------------------------------------
	def rotationList(self):
		"""
		Returns all explicitly inserted rotations.
		"""
		res = super(QGraphicsItemAnimation,self).rotationList()
		return res
	#----------------------------------------------------------------------
	def scaleList(self):
		"""
		Returns all explicitly inserted scales.
		"""
		res = super(QGraphicsItemAnimation,self).scaleList()
		return res
	#----------------------------------------------------------------------
	def shearList(self):
		"""
		Returns all explicitly inserted shears.
		"""
		res = super(QGraphicsItemAnimation,self).shearList()
		return res
	#----------------------------------------------------------------------
	def timeLine(self):
		"""
		Returns the timeline object used to control the rate at which the animation occurs.
		"""
		res = super(QGraphicsItemAnimation,self).timeLine()
		isinstance(res,QtCore.QTimeLine)
		return res
	#----------------------------------------------------------------------
	def translationList(self):
		"""
		Returns all explicitly inserted translations.
		"""
		res = super(QGraphicsItemAnimation,self).translationList()
		return res
	#----------------------------------------------------------------------
	def afterAnimationStep(self,step):
		"""
		afterAnimationStep(step)
			step=QtCore.qreal

		This method is meant to be overridden in subclasses that need to execute additional code after a new step has taken place
		The animation step is provided for use in cases where the action depends on its value.
		"""
		res = super(QGraphicsItemAnimation,self).afterAnimationStep(step)
		return res
	#----------------------------------------------------------------------
	def beforeAnimationStep(self,step):
		"""
		beforeAnimationStep(step)
			step=QtCore.qreal

		This method is meant to be overridden by subclassed that needs to execute additional code before a new step takes place
		The animation step is provided for use in cases where the action depends on its value.
		"""
		res = super(QGraphicsItemAnimation,self).beforeAnimationStep(step)
		return res
	#----------------------------------------------------------------------
	def horizontalScaleAt(self,step):
		"""
		horizontalScaleAt(step)
			step=QtCore.qreal

		Returns the horizontal scale for the item at the specified step value.
		"""
		res = super(QGraphicsItemAnimation,self).horizontalScaleAt(step)
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def horizontalShearAt(self,step):
		"""
		horizontalShearAt(step)
			step=QtCore.qreal

		Returns the horizontal shear for the item at the specified step value.
		"""
		res = super(QGraphicsItemAnimation,self).horizontalShearAt(step)
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def matrixAt(self,step):
		"""
		matrixAt(step)
			step=QtCore.qreal

		Returns the matrix used to transform the item at the specified step value.
		"""
		res = super(QGraphicsItemAnimation,self).matrixAt(step)
		isinstance(res,QtGui.QMatrix)
		return res
	#----------------------------------------------------------------------
	def posAt(self,step):
		"""
		posAt(step)
			step=QtCore.qreal

		Returns the position of the item at the given step value.
		"""
		res = super(QGraphicsItemAnimation,self).posAt(step)
		isinstance(res,QtCore.QPointF)
		return res
	#----------------------------------------------------------------------
	def rotationAt(self,step):
		"""
		rotationAt(step)
			step=QtCore.qreal

		Returns the angle at which the item is rotated at the specified step value.
		"""
		res = super(QGraphicsItemAnimation,self).rotationAt(step)
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def setItem(self,item):
		"""
		setItem(item)
			item=QtGui.QGraphicsItem

		Sets the specified item to be used in the animation.
		"""
		res = super(QGraphicsItemAnimation,self).setItem(item)
		return res
	#----------------------------------------------------------------------
	def setPosAt(self,step,pos):
		"""
		setPosAt(step,pos)
			step=QtCore.qreal
			pos=QtCore.QPointF

		Sets the position of the item at the given step value to the point specified.
		"""
		res = super(QGraphicsItemAnimation,self).setPosAt(step,pos)
		return res
	#----------------------------------------------------------------------
	def setRotationAt(self,step,angle):
		"""
		setRotationAt(step,angle)
			step=QtCore.qreal
			angle=QtCore.qreal

		Sets the rotation of the item at the given step value to the angle specified.
		"""
		res = super(QGraphicsItemAnimation,self).setRotationAt(step,angle)
		return res
	#----------------------------------------------------------------------
	def setScaleAt(self,step,sx,sy):
		"""
		setScaleAt(step,sx,sy)
			step=QtCore.qreal
			sx=QtCore.qreal
			sy=QtCore.qreal

		Sets the scale of the item at the given step value using the horizontal and vertical scale factors specified by sx and sy .
		"""
		res = super(QGraphicsItemAnimation,self).setScaleAt(step,sx,sy)
		return res
	#----------------------------------------------------------------------
	def setShearAt(self,step,sh,sv):
		"""
		setShearAt(step,sh,sv)
			step=QtCore.qreal
			sh=QtCore.qreal
			sv=QtCore.qreal

		Sets the shear of the item at the given step value using the horizontal and vertical shear factors specified by sh and sv .
		"""
		res = super(QGraphicsItemAnimation,self).setShearAt(step,sh,sv)
		return res
	#----------------------------------------------------------------------
	def setTimeLine(self,timeLine):
		"""
		setTimeLine(timeLine)
			timeLine=QtCore.QTimeLine

		Sets the timeline object used to control the rate of animation to the timeLine specified.
		"""
		res = super(QGraphicsItemAnimation,self).setTimeLine(timeLine)
		return res
	#----------------------------------------------------------------------
	def setTranslationAt(self,step,dx,dy):
		"""
		setTranslationAt(step,dx,dy)
			step=QtCore.qreal
			dx=QtCore.qreal
			dy=QtCore.qreal

		Sets the translation of the item at the given step value using the horizontal and vertical coordinates specified by dx and dy .
		"""
		res = super(QGraphicsItemAnimation,self).setTranslationAt(step,dx,dy)
		return res
	#----------------------------------------------------------------------
	def verticalScaleAt(self,step):
		"""
		verticalScaleAt(step)
			step=QtCore.qreal

		Returns the vertical scale for the item at the specified step value.
		"""
		res = super(QGraphicsItemAnimation,self).verticalScaleAt(step)
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def verticalShearAt(self,step):
		"""
		verticalShearAt(step)
			step=QtCore.qreal

		Returns the vertical shear for the item at the specified step value.
		"""
		res = super(QGraphicsItemAnimation,self).verticalShearAt(step)
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def xTranslationAt(self,step):
		"""
		xTranslationAt(step)
			step=QtCore.qreal

		Returns the horizontal translation of the item at the specified step value.
		"""
		res = super(QGraphicsItemAnimation,self).xTranslationAt(step)
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def yTranslationAt(self,step):
		"""
		yTranslationAt(step)
			step=QtCore.qreal

		Returns the vertical translation of the item at the specified step value.
		"""
		res = super(QGraphicsItemAnimation,self).yTranslationAt(step)
		isinstance(res,QtCore.qreal)
		return res

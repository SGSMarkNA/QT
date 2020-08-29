from PySide import QtGui, QtCore

class QSvgRenderer(QtSvg.QSvgRenderer):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSvgRenderer,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def animated(self):
		"""
		Returns true if the current document contains animated elements; otherwise returns false.
		"""
		res = super(QSvgRenderer,self).animated()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def animationDuration(self):
		"""
		Returns the number of frames in the animation, or 0 if the current document is not animated.
		"""
		res = super(QSvgRenderer,self).animationDuration()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def currentFrame(self):
		"""
		This property holds the current frame of the documents animation, or 0 if the document is not animated.
		"""
		res = super(QSvgRenderer,self).currentFrame()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def defaultSize(self):
		"""
		Returns the default size of the document contents.
		"""
		res = super(QSvgRenderer,self).defaultSize()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def framesPerSecond(self):
		"""
		This property holds the number of frames per second to be shown.
		The number of frames per second is 0 if the current document is not animated.
		"""
		res = super(QSvgRenderer,self).framesPerSecond()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if there is a valid current document; otherwise returns false.
		"""
		res = super(QSvgRenderer,self).isValid()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def repaintNeeded(self):
		"""

		"""
		res = super(QSvgRenderer,self).repaintNeeded()
		return res
	#----------------------------------------------------------------------
	def viewBox(self):
		"""
		Returns PySide.QtSvg.QSvgRenderer.viewBoxF()
		toRect() .
		"""
		res = super(QSvgRenderer,self).viewBox()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def viewBoxF(self):
		"""
		This property holds the rectangle specifying the visible area of the document in logical coordinates.
		"""
		res = super(QSvgRenderer,self).viewBoxF()
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def boundsOnElement(self,id):
		"""
		boundsOnElement(id)
			id=unicode

		Returns bounding rectangle of the item with the given id
		The transformation matrix of parent elements is not affecting the bounds of the element.
		"""
		res = super(QSvgRenderer,self).boundsOnElement(id)
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def elementExists(self,id):
		"""
		elementExists(id)
			id=unicode

		Returns true if the element with the given id exists in the currently parsed SVG file and is a renderable element.
		Note: this method returns true only for elements that can be rendered
		Which implies that elements that are considered part of the fill/stroke style properties, e.g
		radialGradients even tough marked with id attributes will not be found by this method.
		"""
		res = super(QSvgRenderer,self).elementExists(id)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def matrixForElement(self,id):
		"""
		matrixForElement(id)
			id=unicode

		Returns the transformation matrix for the element with the given id
		The matrix is a product of the transformation of the elements parents
		The transformation of the element itself is not included.
		To find the bounding rectangle of the element in logical coordinates, you can apply the matrix on the rectangle returned from PySide.QtSvg.QSvgRenderer.boundsOnElement() .
		"""
		res = super(QSvgRenderer,self).matrixForElement(id)
		isinstance(res,QtGui.QMatrix)
		return res
	#----------------------------------------------------------------------
	def setCurrentFrame(self,arg__1):
		"""
		setCurrentFrame(arg__1)
			arg__1=QtCore.int

		This property holds the current frame of the documents animation, or 0 if the document is not animated.
		"""
		res = super(QSvgRenderer,self).setCurrentFrame(arg__1)
		return res
	#----------------------------------------------------------------------
	def setFramesPerSecond(self,num):
		"""
		setFramesPerSecond(num)
			num=QtCore.int

		This property holds the number of frames per second to be shown.
		The number of frames per second is 0 if the current document is not animated.
		"""
		res = super(QSvgRenderer,self).setFramesPerSecond(num)
		return res
	#----------------------------------------------------------------------
	def setViewBox(self,*args,**kwargs):
		"""
		setViewBox(viewbox)
			viewbox=QtCore.QRectF

		setViewBox(viewbox)
			viewbox=QtCore.QRect

		This property holds the rectangle specifying the visible area of the document in logical coordinates.
		"""
		res = super(QSvgRenderer,self).setViewBox(*args,**kwargs)
		return res

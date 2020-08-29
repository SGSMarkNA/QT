from PySide import QtGui, QtCore

class QBrush(QtGui.QBrush):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QBrush,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def color(self):
		"""
		Returns the brush color.
		"""
		res = super(QBrush,self).color()
		isinstance(res,QtGui.QColor)
		return res
	#----------------------------------------------------------------------
	def gradient(self):
		"""
		Returns the gradient describing this brush.
		"""
		res = super(QBrush,self).gradient()
		isinstance(res,QtGui.QGradient)
		return res
	#----------------------------------------------------------------------
	def isOpaque(self):
		"""
		Returns true if the brush is fully opaque otherwise false
		A brush is considered opaque if:
		"""
		res = super(QBrush,self).isOpaque()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def matrix(self):
		"""
		Returns the current transformation matrix for the brush.
		"""
		res = super(QBrush,self).matrix()
		isinstance(res,QtGui.QMatrix)
		return res
	#----------------------------------------------------------------------
	def style(self):
		"""
		Returns the brush style.
		"""
		res = super(QBrush,self).style()
		isinstance(res,QtCore.Qt.BrushStyle)
		return res
	#----------------------------------------------------------------------
	def texture(self):
		"""
		Returns the custom brush pattern, or a null pixmap if no custom brush pattern has been set.
		"""
		res = super(QBrush,self).texture()
		isinstance(res,QtGui.QPixmap)
		return res
	#----------------------------------------------------------------------
	def textureImage(self):
		"""
		Returns the custom brush pattern, or a null image if no custom brush pattern has been set.
		If the texture was set as a PySide.QtGui.QPixmap it will be converted to a PySide.QtGui.QImage .
		"""
		res = super(QBrush,self).textureImage()
		isinstance(res,QtGui.QImage)
		return res
	#----------------------------------------------------------------------
	def transform(self):
		"""
		Returns the current transformation matrix for the brush.
		"""
		res = super(QBrush,self).transform()
		isinstance(res,QtGui.QTransform)
		return res
	#----------------------------------------------------------------------
	def init(self,color,bs):
		"""
		init(color,bs)
			color=QtGui.QColor
			bs=QtCore.Qt.BrushStyle


		"""
		res = super(QBrush,self).init(color,bs)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,b):
		"""
		__ne__(b)
			b=QtGui.QBrush

		Returns true if the brush is different from the given brush ; otherwise returns false.
		Two brushes are different if they have different styles, colors or transforms or different pixmaps or gradients depending on the style.
		"""
		res = super(QBrush,self).__ne__(b)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,b):
		"""
		__eq__(b)
			b=QtGui.QBrush

		Returns true if the brush is equal to the given brush ; otherwise returns false.
		Two brushes are equal if they have equal styles, colors and transforms and equal pixmaps or gradients depending on the style.
		"""
		res = super(QBrush,self).__eq__(b)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setColor(self,*args,**kwargs):
		"""
		setColor(color)
			color=QtGui.QColor

		setColor(color)
			color=QtCore.Qt.GlobalColor

		Sets the brush color to the given color .
		Note that calling PySide.QtGui.QBrush.setColor() will not make a difference if the style is a gradient
		The same is the case if the style is Qt.TexturePattern style unless the current texture is a PySide.QtGui.QBitmap .
		"""
		res = super(QBrush,self).setColor(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setMatrix(self,mat):
		"""
		setMatrix(mat)
			mat=QtGui.QMatrix

		Sets matrix as an explicit transformation matrix on the current brush
		The brush transformation matrix is merged with PySide.QtGui.QPainter transformation matrix to produce the final result.
		"""
		res = super(QBrush,self).setMatrix(mat)
		return res
	#----------------------------------------------------------------------
	def setStyle(self,arg__1):
		"""
		setStyle(arg__1)
			arg__1=QtCore.Qt.BrushStyle


		"""
		res = super(QBrush,self).setStyle(arg__1)
		return res
	#----------------------------------------------------------------------
	def setTexture(self,pixmap):
		"""
		setTexture(pixmap)
			pixmap=QtGui.QPixmap

		Sets the brush pixmap to pixmap
		The style is set to Qt.TexturePattern .
		The current brush color will only have an effect for monochrome pixmaps, i.e
		for QPixmap.depth() == 1 ( QBitmaps ).
		"""
		res = super(QBrush,self).setTexture(pixmap)
		return res
	#----------------------------------------------------------------------
	def setTextureImage(self,image):
		"""
		setTextureImage(image)
			image=QtGui.QImage

		Sets the brush image to image
		The style is set to Qt.TexturePattern .
		Note the current brush color will not have any affect on monochrome images, as opposed to calling PySide.QtGui.QBrush.setTexture() with a PySide.QtGui.QBitmap
		If you want to change the color of monochrome image brushes, either convert the image to PySide.QtGui.QBitmap with QBitmap::fromImage() and set the resulting PySide.QtGui.QBitmap as a texture, or change the entries in the color table for the image.
		"""
		res = super(QBrush,self).setTextureImage(image)
		return res
	#----------------------------------------------------------------------
	def setTransform(self,arg__1):
		"""
		setTransform(arg__1)
			arg__1=QtGui.QTransform

		Sets matrix as an explicit transformation matrix on the current brush
		The brush transformation matrix is merged with PySide.QtGui.QPainter transformation matrix to produce the final result.
		"""
		res = super(QBrush,self).setTransform(arg__1)
		return res

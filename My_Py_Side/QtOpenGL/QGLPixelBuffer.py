from PySide import QtGui, QtCore

class QGLPixelBuffer(QtOpenGL.QGLPixelBuffer):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGLPixelBuffer,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def doneCurrent(self):
		"""
		Makes no context the current OpenGL context
		Returns true on success; otherwise returns false.
		"""
		res = super(QGLPixelBuffer,self).doneCurrent()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def format(self):
		"""
		Returns the format of the pbuffer
		The format may be different from the one that was requested.
		"""
		res = super(QGLPixelBuffer,self).format()
		isinstance(res,QtOpenGL.QGLFormat)
		return res
	#----------------------------------------------------------------------
	def generateDynamicTexture(self):
		"""

		"""
		res = super(QGLPixelBuffer,self).generateDynamicTexture()
		return res
	#----------------------------------------------------------------------
	def handle(self):
		"""
		Returns the native pbuffer handle.
		"""
		res = super(QGLPixelBuffer,self).handle()
		isinstance(res,QtCore.Qt::HANDLE)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if this pbuffer is valid; otherwise returns false.
		"""
		res = super(QGLPixelBuffer,self).isValid()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def makeCurrent(self):
		"""
		Makes this pbuffer the current OpenGL rendering context
		Returns true on success; otherwise returns false.
		"""
		res = super(QGLPixelBuffer,self).makeCurrent()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def releaseFromDynamicTexture(self):
		"""
		Releases the pbuffer from any previously bound texture.
		"""
		res = super(QGLPixelBuffer,self).releaseFromDynamicTexture()
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""
		Returns the size of the pbuffer.
		"""
		res = super(QGLPixelBuffer,self).size()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def toImage(self):
		"""
		Returns the contents of the pbuffer as a PySide.QtGui.QImage .
		"""
		res = super(QGLPixelBuffer,self).toImage()
		isinstance(res,QtGui.QImage)
		return res
	#----------------------------------------------------------------------
	def bindTexture(self,*args,**kwargs):
		"""
		bindTexture(fileName)
			fileName=unicode

		bindTexture(pixmap,target=None)
			pixmap=QtGui.QPixmap
			target=long

		bindTexture(image,target=None)
			image=QtGui.QImage
			target=long

		This is an overloaded function.
		Reads the DirectDrawSurface (DDS) compressed file fileName and generates a 2D GL texture from it.
		Equivalent to calling QGLContext.bindTexture() .
		"""
		res = super(QGLPixelBuffer,self).bindTexture(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def bindToDynamicTexture(self,texture):
		"""
		bindToDynamicTexture(texture)
			texture=long


		"""
		res = super(QGLPixelBuffer,self).bindToDynamicTexture(texture)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def deleteTexture(self,texture_id):
		"""
		deleteTexture(texture_id)
			texture_id=long


		"""
		res = super(QGLPixelBuffer,self).deleteTexture(texture_id)
		return res
	#----------------------------------------------------------------------
	def drawTexture(self,*args,**kwargs):
		"""
		drawTexture(point,textureId,textureTarget=None)
			point=QtCore.QPointF
			textureId=long
			textureTarget=long

		drawTexture(target,textureId,textureTarget=None)
			target=QtCore.QRectF
			textureId=long
			textureTarget=long


		"""
		res = super(QGLPixelBuffer,self).drawTexture(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def updateDynamicTexture(self,texture_id):
		"""
		updateDynamicTexture(texture_id)
			texture_id=long


		"""
		res = super(QGLPixelBuffer,self).updateDynamicTexture(texture_id)
		return res

from PySide import QtGui, QtCore

class QGLFramebufferObject(QtOpenGL.QGLFramebufferObject):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGLFramebufferObject,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def attachment(self):
		"""
		Returns the status of the depth and stencil buffers attached to this framebuffer object.
		"""
		res = super(QGLFramebufferObject,self).attachment()
		isinstance(res,QtOpenGL.QGLFramebufferObject.Attachment)
		return res
	#----------------------------------------------------------------------
	def bind(self):
		"""
		Switches rendering from the default, windowing system provided framebuffer to this framebuffer object
		Returns true upon success, false otherwise.
		"""
		res = super(QGLFramebufferObject,self).bind()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def format(self):
		"""
		Returns the format of this framebuffer object.
		"""
		res = super(QGLFramebufferObject,self).format()
		isinstance(res,QtOpenGL.QGLFramebufferObjectFormat)
		return res
	#----------------------------------------------------------------------
	def handle(self):
		"""
		Returns the GL framebuffer object handle for this framebuffer object (returned by the glGenFrameBuffersEXT() function)
		This handle can be used to attach new images or buffers to the framebuffer
		The user is responsible for cleaning up and destroying these objects.
		"""
		res = super(QGLFramebufferObject,self).handle()
		return res
	#----------------------------------------------------------------------
	def isBound(self):
		"""
		Returns true if the framebuffer object is currently bound to a context, otherwise false is returned.
		"""
		res = super(QGLFramebufferObject,self).isBound()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if the framebuffer object is valid.
		The framebuffer can become invalid if the initialization process fails, the user attaches an invalid buffer to the framebuffer object, or a non-power of two width/height is specified as the texture size if the texture target is GL_TEXTURE_2D
		The non-power of two limitation does not apply if the OpenGL version is 2.0 or higher, or if the GL_ARB_texture_non_power_of_two extension is present.
		The framebuffer can also become invalid if the PySide.QtOpenGL.QGLContext that the framebuffer was created within is destroyed and there are no other shared contexts that can take over ownership of the framebuffer.
		"""
		res = super(QGLFramebufferObject,self).isValid()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def release(self):
		"""
		Switches rendering back to the default, windowing system provided framebuffer
		Returns true upon success, false otherwise.
		"""
		res = super(QGLFramebufferObject,self).release()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""
		Returns the size of the texture attached to this framebuffer object.
		"""
		res = super(QGLFramebufferObject,self).size()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def texture(self):
		"""
		Returns the texture id for the texture attached as the default rendering target in this framebuffer object
		This texture id can be bound as a normal texture in your own GL code.
		If a multisample framebuffer object is used then the value returned from this function will be invalid.
		"""
		res = super(QGLFramebufferObject,self).texture()
		return res
	#----------------------------------------------------------------------
	def toImage(self):
		"""
		Returns the contents of this framebuffer object as a PySide.QtGui.QImage .
		"""
		res = super(QGLFramebufferObject,self).toImage()
		isinstance(res,QtGui.QImage)
		return res
	#----------------------------------------------------------------------
	def drawTexture(self,*args,**kwargs):
		"""
		drawTexture(target,textureId,textureTarget=None)
			target=QtCore.QRectF
			textureId=long
			textureTarget=long

		drawTexture(point,textureId,textureTarget=None)
			point=QtCore.QPointF
			textureId=long
			textureTarget=long


		"""
		res = super(QGLFramebufferObject,self).drawTexture(*args,**kwargs)
		return res

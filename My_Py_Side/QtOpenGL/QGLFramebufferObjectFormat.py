from PySide import QtGui, QtCore

class QGLFramebufferObjectFormat(QtOpenGL.QGLFramebufferObjectFormat):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGLFramebufferObjectFormat,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def attachment(self):
		"""
		Returns the configuration of the depth and stencil buffers attached to a framebuffer object
		The default is QGLFramebufferObject.NoAttachment .
		"""
		res = super(QGLFramebufferObjectFormat,self).attachment()
		isinstance(res,QtOpenGL.QGLFramebufferObject.Attachment)
		return res
	#----------------------------------------------------------------------
	def internalTextureFormat(self):
		"""
		Returns the internal format of a framebuffer objects texture or multisample framebuffer objects color buffer
		The default is GL_RGBA8 on desktop OpenGL systems, and GL_RGBA on OpenGL/ES systems.
		"""
		res = super(QGLFramebufferObjectFormat,self).internalTextureFormat()
		return res
	#----------------------------------------------------------------------
	def samples(self):
		"""
		Returns the number of samples per pixel if a framebuffer object is a multisample framebuffer object
		Otherwise, returns 0
		The default value is 0.
		"""
		res = super(QGLFramebufferObjectFormat,self).samples()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def textureTarget(self):
		"""
		Returns the texture target of the texture attached to a framebuffer object
		Ignored for multisample framebuffer objects
		The default is GL_TEXTURE_2D .
		"""
		res = super(QGLFramebufferObjectFormat,self).textureTarget()
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtOpenGL.QGLFramebufferObjectFormat

		Returns false if all the options of this framebuffer object format are the same as other ; otherwise returns true.
		"""
		res = super(QGLFramebufferObjectFormat,self).__ne__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtOpenGL.QGLFramebufferObjectFormat

		Returns true if all the options of this framebuffer object format are the same as other ; otherwise returns false.
		"""
		res = super(QGLFramebufferObjectFormat,self).__eq__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def setAttachment(self,attachment):
		"""
		setAttachment(attachment)
			attachment=QtOpenGL.QGLFramebufferObject.Attachment


		"""
		res = super(QGLFramebufferObjectFormat,self).setAttachment(attachment)
		return res
	#----------------------------------------------------------------------
	def setInternalTextureFormat(self,internalTextureFormat):
		"""
		setInternalTextureFormat(internalTextureFormat)
			internalTextureFormat=long


		"""
		res = super(QGLFramebufferObjectFormat,self).setInternalTextureFormat(internalTextureFormat)
		return res
	#----------------------------------------------------------------------
	def setSamples(self,samples):
		"""
		setSamples(samples)
			samples=QtCore.int

		Sets the number of samples per pixel for a multisample framebuffer object to samples
		The default sample count of 0 represents a regular non-multisample framebuffer object.
		If the desired amount of samples per pixel is not supported by the hardware then the maximum number of samples per pixel will be used
		Note that multisample framebuffer objects can not be bound as textures
		Also, the GL_EXT_framebuffer_multisample extension is required to create a framebuffer with more than one sample per pixel.
		"""
		res = super(QGLFramebufferObjectFormat,self).setSamples(samples)
		return res
	#----------------------------------------------------------------------
	def setTextureTarget(self,target):
		"""
		setTextureTarget(target)
			target=long


		"""
		res = super(QGLFramebufferObjectFormat,self).setTextureTarget(target)
		return res

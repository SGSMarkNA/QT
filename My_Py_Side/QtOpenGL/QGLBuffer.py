from PySide import QtGui, QtCore

class QGLBuffer(QtOpenGL.QGLBuffer):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGLBuffer,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def bind(self):
		"""
		Binds the buffer associated with this object to the current GL context
		Returns false if binding was not possible, usually because PySide.QtOpenGL.QGLBuffer.type() is not supported on this GL implementation.
		The buffer must be bound to the same PySide.QtOpenGL.QGLContext current when PySide.QtOpenGL.QGLBuffer.create() was called, or to another PySide.QtOpenGL.QGLContext that is sharing with it
		Otherwise, false will be returned from this function.
		"""
		res = super(QGLBuffer,self).bind()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def bufferId(self):
		"""
		Returns the GL identifier associated with this buffer; zero if the buffer has not been created.
		"""
		res = super(QGLBuffer,self).bufferId()
		return res
	#----------------------------------------------------------------------
	def create(self):
		"""
		Creates the buffer object in the GL server
		Returns true if the object was created; false otherwise.
		This function must be called with a current PySide.QtOpenGL.QGLContext
		The buffer will be bound to and can only be used in that context (or any other context that is shared with it).
		This function will return false if the GL implementation does not support buffers, or there is no current PySide.QtOpenGL.QGLContext .
		"""
		res = super(QGLBuffer,self).create()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def destroy(self):
		"""
		Destroys this buffer object, including the storage being used in the GL server
		All references to the buffer will become invalid.
		"""
		res = super(QGLBuffer,self).destroy()
		return res
	#----------------------------------------------------------------------
	def isCreated(self):
		"""
		Returns true if this buffer has been created; false otherwise.
		"""
		res = super(QGLBuffer,self).isCreated()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def release(self):
		"""
		Releases the buffer associated with this object from the current GL context.
		This function must be called with the same PySide.QtOpenGL.QGLContext current as when PySide.QtOpenGL.QGLBuffer.bind() was called on the buffer.
		"""
		res = super(QGLBuffer,self).release()
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""
		Returns the size of the data in this buffer, for reading operations
		Returns -1 if fetching the buffer size is not supported, or the buffer has not been created.
		It is assumed that this buffer has been bound to the current context.
		"""
		res = super(QGLBuffer,self).size()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def type(self):
		"""
		Returns the type of buffer represented by this object.
		"""
		res = super(QGLBuffer,self).type()
		isinstance(res,QtOpenGL.QGLBuffer.Type)
		return res
	#----------------------------------------------------------------------
	def unmap(self):
		"""
		Unmaps the buffer after it was mapped into the applications memory space with a previous call to PySide.QtOpenGL.QGLBuffer.map()
		Returns true if the unmap succeeded; false otherwise.
		It is assumed that this buffer has been bound to the current context, and that it was previously mapped with PySide.QtOpenGL.QGLBuffer.map() .
		This function is only supported under OpenGL/ES if the GL_OES_mapbuffer extension is present.
		"""
		res = super(QGLBuffer,self).unmap()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def usagePattern(self):
		"""
		Returns the usage pattern for this buffer object
		The default value is StaticDraw .
		"""
		res = super(QGLBuffer,self).usagePattern()
		isinstance(res,QtOpenGL.QGLBuffer.UsagePattern)
		return res
	#----------------------------------------------------------------------
	def allocate(self,*args,**kwargs):
		"""
		allocate(data,count=None)
			data=void
			count=QtCore.int

		allocate(count)
			count=QtCore.int

		Allocates count bytes of space to the buffer, initialized to the contents of data
		Any previous contents will be removed.
		It is assumed that PySide.QtOpenGL.QGLBuffer.create() has been called on this buffer and that it has been bound to the current context.
		"""
		res = super(QGLBuffer,self).allocate(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def map(self,access):
		"""
		map(access)
			access=QtOpenGL.QGLBuffer.Access


		"""
		res = super(QGLBuffer,self).map(access)
		isinstance(res,void)
		return res
	#----------------------------------------------------------------------
	def read(self,offset,count):
		"""
		read(offset,count)
			offset=QtCore.int
			count=QtCore.int

		Reads the count bytes in this buffer starting at offset into data
		Returns true on success; false if reading from the buffer is not supported
		Buffer reading is not supported under OpenGL/ES.
		It is assumed that this buffer has been bound to the current context.
		"""
		res = super(QGLBuffer,self).read(offset,count)
		return res
	#----------------------------------------------------------------------
	def setUsagePattern(self,value):
		"""
		setUsagePattern(value)
			value=QtOpenGL.QGLBuffer.UsagePattern


		"""
		res = super(QGLBuffer,self).setUsagePattern(value)
		return res
	#----------------------------------------------------------------------
	def write(self,offset,data,count=None):
		"""
		write(offset,data,count=None)
			offset=QtCore.int
			data=void
			count=QtCore.int

		Replaces the count bytes of this buffer starting at offset with the contents of data
		Any other bytes in the buffer will be left unmodified.
		It is assumed that PySide.QtOpenGL.QGLBuffer.create() has been called on this buffer and that it has been bound to the current context.
		"""
		res = super(QGLBuffer,self).write(offset,data,count)
		return res

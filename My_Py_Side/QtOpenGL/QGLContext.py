from PySide import QtGui, QtCore

class QGLContext(QtOpenGL.QGLContext):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGLContext,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def chooseVisual(self):
		"""
		X11 only: This virtual function tries to find a visual that matches the format, reducing the demands if the original request cannot be met.
		The algorithm for reducing the demands of the format is quite simple-minded, so override this method in your subclass if your application has spcific requirements on visual selection.
		"""
		res = super(QGLContext,self).chooseVisual()
		isinstance(res,void)
		return res
	#----------------------------------------------------------------------
	def device(self):
		"""
		Returns the paint device set for this context.
		"""
		res = super(QGLContext,self).device()
		isinstance(res,QtGui.QPaintDevice)
		return res
	#----------------------------------------------------------------------
	def deviceIsPixmap(self):
		"""
		Returns true if the paint device of this context is a pixmap; otherwise returns false.
		"""
		res = super(QGLContext,self).deviceIsPixmap()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def doneCurrent(self):
		"""
		Makes no GL context the current context
		Normally, you do not need to call this function; PySide.QtOpenGL.QGLContext calls it as necessary.
		"""
		res = super(QGLContext,self).doneCurrent()
		return res
	#----------------------------------------------------------------------
	def format(self):
		"""
		Returns the frame buffer format that was obtained (this may be a subset of what was requested).
		"""
		res = super(QGLContext,self).format()
		isinstance(res,QtOpenGL.QGLFormat)
		return res
	#----------------------------------------------------------------------
	def initialized(self):
		"""
		Returns true if this context has been initialized, i.e
		if QGLWidget.initializeGL() has been performed on it; otherwise returns false.
		"""
		res = super(QGLContext,self).initialized()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isSharing(self):
		"""
		Returns true if this context is sharing its GL context with another PySide.QtOpenGL.QGLContext , otherwise false is returned
		Note that context sharing might not be supported between contexts with different formats.
		"""
		res = super(QGLContext,self).isSharing()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if a GL rendering context has been successfully created; otherwise returns false.
		"""
		res = super(QGLContext,self).isValid()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def makeCurrent(self):
		"""
		Makes this context the current OpenGL rendering context
		All GL functions you call operate on this context until another context is made current.
		In some very rare cases the underlying call may fail
		If this occurs an error message is output to stderr.
		"""
		res = super(QGLContext,self).makeCurrent()
		return res
	#----------------------------------------------------------------------
	def overlayTransparentColor(self):
		"""
		If this context is a valid context in an overlay plane, returns the planes transparent color
		Otherwise returns an invalid color.
		The returned colors PySide.QtGui.QColor.pixel() value is the index of the transparent color in the colormap of the overlay plane
		(Naturally, the colors RGB values are meaningless.)
		The returned PySide.QtGui.QColor object will generally work as expected only when passed as the argument to QGLWidget.qglColor() or QGLWidget.qglClearColor()
		Under certain circumstances it can also be used to draw transparent graphics with a PySide.QtGui.QPainter
		See the examples/opengl/overlay_x11 example for details.
		"""
		res = super(QGLContext,self).overlayTransparentColor()
		isinstance(res,QtGui.QColor)
		return res
	#----------------------------------------------------------------------
	def requestedFormat(self):
		"""
		Returns the frame buffer format that was originally requested in the constructor or PySide.QtOpenGL.QGLContext.setFormat() .
		"""
		res = super(QGLContext,self).requestedFormat()
		isinstance(res,QtOpenGL.QGLFormat)
		return res
	#----------------------------------------------------------------------
	def reset(self):
		"""
		Resets the context and makes it invalid.
		"""
		res = super(QGLContext,self).reset()
		return res
	#----------------------------------------------------------------------
	def swapBuffers(self):
		"""
		Swaps the screen contents with an off-screen buffer
		Only works if the context is in double buffer mode.
		"""
		res = super(QGLContext,self).swapBuffers()
		return res
	#----------------------------------------------------------------------
	def windowCreated(self):
		"""
		Returns true if a window has been created for this context; otherwise returns false.
		"""
		res = super(QGLContext,self).windowCreated()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def bindTexture(self,*args,**kwargs):
		"""
		bindTexture(fileName)
			fileName=unicode

		bindTexture(pixmap,target,format,options)
			pixmap=QtGui.QPixmap
			target=long
			format=QtCore.int
			options=QtOpenGL.QGLContext.BindOptions

		bindTexture(image,target,format,options)
			image=QtGui.QImage
			target=long
			format=QtCore.int
			options=QtOpenGL.QGLContext.BindOptions

		bindTexture(pixmap,target=None,format=None)
			pixmap=QtGui.QPixmap
			target=long
			format=QtCore.int

		bindTexture(image,target=None,format=None)
			image=QtGui.QImage
			target=long
			format=QtCore.int

		This is an overloaded function.
		Reads the compressed texture file fileName and generates a 2D GL texture from it.
		This function can load DirectDrawSurface (DDS) textures in the DXT1, DXT3 and DXT5 DDS formats if the GL_ARB_texture_compression and GL_EXT_texture_compression_s3tc extensions are supported.
		Since 4.6.1, textures in the ETC1 format can be loaded if the GL_OES_compressed_ETC1_RGB8_texture extension is supported and the ETC1 texture has been encapsulated in the PVR container format
		Also, textures in the PVRTC2 and PVRTC4 formats can be loaded if the GL_IMG_texture_compression_pvrtc extension is supported.
		"""
		res = super(QGLContext,self).bindTexture(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def chooseContext(self,shareContext=None):
		"""
		chooseContext(shareContext=None)
			shareContext=QtOpenGL.QGLContext

		This semi-internal function is called by PySide.QtOpenGL.QGLContext.create()
		It creates a system-dependent OpenGL handle that matches the PySide.QtOpenGL.QGLContext.format() of shareContext as closely as possible, returning true if successful or false if a suitable handle could not be found.
		On Windows, it calls the virtual function choosePixelFormat() , which finds a matching pixel format identifier
		On X11, it calls the virtual function PySide.QtOpenGL.QGLContext.chooseVisual() which finds an appropriate X visual
		On other platforms it may work differently.
		"""
		res = super(QGLContext,self).chooseContext(shareContext)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def colorIndex(self,c):
		"""
		colorIndex(c)
			c=QtGui.QColor

		Returns a colormap index for the color c, in ColorIndex mode
		Used by qglColor() and qglClearColor().
		"""
		res = super(QGLContext,self).colorIndex(c)
		isinstance(res,QtCore.uint)
		return res
	#----------------------------------------------------------------------
	def create(self,shareContext=None):
		"""
		create(shareContext=None)
			shareContext=QtOpenGL.QGLContext

		Creates the GL context
		Returns true if it was successful in creating a valid GL rendering context on the paint device specified in the constructor; otherwise returns false (i.e
		the context is invalid).
		After successful creation, PySide.QtOpenGL.QGLContext.format() returns the set of features of the created GL rendering context.
		If shareContext points to a valid PySide.QtOpenGL.QGLContext , this method will try to establish OpenGL display list and texture object sharing between this context and the shareContext
		Note that this may fail if the two contexts have different formats
		Use PySide.QtOpenGL.QGLContext.isSharing() to see if sharing is in effect.
		"""
		res = super(QGLContext,self).create(shareContext)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def deleteTexture(self,tx_id):
		"""
		deleteTexture(tx_id)
			tx_id=long


		"""
		res = super(QGLContext,self).deleteTexture(tx_id)
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
		res = super(QGLContext,self).drawTexture(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def getProcAddress(self,proc):
		"""
		getProcAddress(proc)
			proc=unicode

		Returns a function pointer to the GL extension function passed in proc
		0 is returned if a pointer to the function could not be obtained.
		"""
		res = super(QGLContext,self).getProcAddress(proc)
		isinstance(res,void)
		return res
	#----------------------------------------------------------------------
	def setDevice(self,pDev):
		"""
		setDevice(pDev)
			pDev=QtGui.QPaintDevice


		"""
		res = super(QGLContext,self).setDevice(pDev)
		return res
	#----------------------------------------------------------------------
	def setFormat(self,format):
		"""
		setFormat(format)
			format=QtOpenGL.QGLFormat

		Sets a format for this context
		The context is PySide.QtOpenGL.QGLContext.reset() .
		Call PySide.QtOpenGL.QGLContext.create() to create a new GL context that tries to match the new format.
		"""
		res = super(QGLContext,self).setFormat(format)
		return res
	#----------------------------------------------------------------------
	def setInitialized(self,on):
		"""
		setInitialized(on)
			on=QtCore.bool

		If on is true the context has been initialized, i.e
		QGLContext.setInitialized() has been called on it
		If on is false the context has not been initialized.
		"""
		res = super(QGLContext,self).setInitialized(on)
		return res
	#----------------------------------------------------------------------
	def setValid(self,valid):
		"""
		setValid(valid)
			valid=QtCore.bool

		Forces the GL rendering context to be valid.
		"""
		res = super(QGLContext,self).setValid(valid)
		return res
	#----------------------------------------------------------------------
	def setWindowCreated(self,on):
		"""
		setWindowCreated(on)
			on=QtCore.bool

		If on is true the context has had a window created for it
		If on is false no window has been created for the context.
		"""
		res = super(QGLContext,self).setWindowCreated(on)
		return res
	#----------------------------------------------------------------------
	def tryVisual(self,f,bufDepth=None):
		"""
		tryVisual(f,bufDepth=None)
			f=QtOpenGL.QGLFormat
			bufDepth=QtCore.int

		X11 only: This virtual function chooses a visual that matches the OpenGL PySide.QtOpenGL.QGLContext.format()
		Reimplement this function in a subclass if you need a custom visual.
		"""
		res = super(QGLContext,self).tryVisual(f,bufDepth)
		isinstance(res,void)
		return res

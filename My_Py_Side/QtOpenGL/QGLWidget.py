from PySide import QtGui, QtCore

class QGLWidget(QtOpenGL.QGLWidget):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGLWidget,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def autoBufferSwap(self):
		"""
		Returns true if the widget is doing automatic GL buffer swapping; otherwise returns false.
		"""
		res = super(QGLWidget,self).autoBufferSwap()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def colormap(self):
		"""
		Returns the colormap for this widget.
		Usually it is only top-level widgets that can have different colormaps installed
		Asking for the colormap of a child widget will return the colormap for the childs top-level widget.
		If no colormap has been set for this widget, the PySide.QtOpenGL.QGLColormap returned will be empty.
		"""
		res = super(QGLWidget,self).colormap()
		isinstance(res,QtOpenGL.QGLColormap)
		return res
	#----------------------------------------------------------------------
	def context(self):
		"""
		Returns the context of this widget.
		It is possible that the context is not valid (see PySide.QtOpenGL.QGLWidget.isValid() ), for example, if the underlying hardware does not support the format attributes that were requested.
		"""
		res = super(QGLWidget,self).context()
		isinstance(res,QtOpenGL.QGLContext)
		return res
	#----------------------------------------------------------------------
	def doneCurrent(self):
		"""
		Makes no GL context the current context
		Normally, you do not need to call this function; PySide.QtOpenGL.QGLContext calls it as necessary
		However, it may be useful in multithreaded environments.
		"""
		res = super(QGLWidget,self).doneCurrent()
		return res
	#----------------------------------------------------------------------
	def doubleBuffer(self):
		"""
		Returns true if the contained GL rendering context has double buffering; otherwise returns false.
		"""
		res = super(QGLWidget,self).doubleBuffer()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def format(self):
		"""
		Returns the format of the contained GL rendering context.
		"""
		res = super(QGLWidget,self).format()
		isinstance(res,QtOpenGL.QGLFormat)
		return res
	#----------------------------------------------------------------------
	def glDraw(self):
		"""
		Executes the virtual function PySide.QtOpenGL.QGLWidget.paintGL() .
		The widgets rendering context will become the current context and PySide.QtOpenGL.QGLWidget.initializeGL() will be called if it hasnt already been called.
		"""
		res = super(QGLWidget,self).glDraw()
		return res
	#----------------------------------------------------------------------
	def glInit(self):
		"""
		Initializes OpenGL for this widgets context
		Calls the virtual function PySide.QtOpenGL.QGLWidget.initializeGL() .
		"""
		res = super(QGLWidget,self).glInit()
		return res
	#----------------------------------------------------------------------
	def initializeGL(self):
		"""
		This virtual function is called once before the first call to PySide.QtOpenGL.QGLWidget.paintGL() or PySide.QtOpenGL.QGLWidget.resizeGL() , and then once whenever the widget has been assigned a new PySide.QtOpenGL.QGLContext
		Reimplement it in a subclass.
		This function should set up any required OpenGL context rendering flags, defining display lists, etc.
		There is no need to call PySide.QtOpenGL.QGLWidget.makeCurrent() because this has already been done when this function is called.
		"""
		res = super(QGLWidget,self).initializeGL()
		return res
	#----------------------------------------------------------------------
	def initializeOverlayGL(self):
		"""
		This virtual function is used in the same manner as PySide.QtOpenGL.QGLWidget.initializeGL() except that it operates on the widgets overlay context instead of the widgets main context
		This means that PySide.QtOpenGL.QGLWidget.initializeOverlayGL() is called once before the first call to PySide.QtOpenGL.QGLWidget.paintOverlayGL() or PySide.QtOpenGL.QGLWidget.resizeOverlayGL()
		Reimplement it in a subclass.
		This function should set up any required OpenGL context rendering flags, defining display lists, etc
		for the overlay context.
		There is no need to call PySide.QtOpenGL.QGLWidget.makeOverlayCurrent() because this has already been done when this function is called.
		"""
		res = super(QGLWidget,self).initializeOverlayGL()
		return res
	#----------------------------------------------------------------------
	def isSharing(self):
		"""
		Returns true if this widgets GL context is shared with another GL context, otherwise false is returned
		Context sharing might not be possible if the widgets use different formats.
		"""
		res = super(QGLWidget,self).isSharing()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if the widget has a valid GL rendering context; otherwise returns false
		A widget will be invalid if the system has no OpenGL support .
		"""
		res = super(QGLWidget,self).isValid()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def makeCurrent(self):
		"""
		Makes this widget the current widget for OpenGL operations, i.e
		makes the widgets rendering context the current OpenGL rendering context.
		"""
		res = super(QGLWidget,self).makeCurrent()
		return res
	#----------------------------------------------------------------------
	def makeOverlayCurrent(self):
		"""
		Makes the overlay context of this widget current
		Use this if you need to issue OpenGL commands to the overlay context outside of PySide.QtOpenGL.QGLWidget.initializeOverlayGL() , PySide.QtOpenGL.QGLWidget.resizeOverlayGL() , and PySide.QtOpenGL.QGLWidget.paintOverlayGL() .
		Does nothing if this widget has no overlay.
		"""
		res = super(QGLWidget,self).makeOverlayCurrent()
		return res
	#----------------------------------------------------------------------
	def overlayContext(self):
		"""
		Returns the overlay context of this widget, or 0 if this widget has no overlay.
		"""
		res = super(QGLWidget,self).overlayContext()
		isinstance(res,QtOpenGL.QGLContext)
		return res
	#----------------------------------------------------------------------
	def paintGL(self):
		"""
		This virtual function is called whenever the widget needs to be painted
		Reimplement it in a subclass.
		There is no need to call PySide.QtOpenGL.QGLWidget.makeCurrent() because this has already been done when this function is called.
		"""
		res = super(QGLWidget,self).paintGL()
		return res
	#----------------------------------------------------------------------
	def paintOverlayGL(self):
		"""
		This virtual function is used in the same manner as PySide.QtOpenGL.QGLWidget.paintGL() except that it operates on the widgets overlay context instead of the widgets main context
		This means that PySide.QtOpenGL.QGLWidget.paintOverlayGL() is called whenever the widgets overlay needs to be painted
		Reimplement it in a subclass.
		There is no need to call PySide.QtOpenGL.QGLWidget.makeOverlayCurrent() because this has already been done when this function is called.
		"""
		res = super(QGLWidget,self).paintOverlayGL()
		return res
	#----------------------------------------------------------------------
	def swapBuffers(self):
		"""
		Swaps the screen contents with an off-screen buffer
		This only works if the widgets format specifies double buffer mode.
		Normally, there is no need to explicitly call this function because it is done automatically after each widget repaint, i.e
		each time after PySide.QtOpenGL.QGLWidget.paintGL() has been executed.
		"""
		res = super(QGLWidget,self).swapBuffers()
		return res
	#----------------------------------------------------------------------
	def updateGL(self):
		"""
		Updates the widget by calling PySide.QtOpenGL.QGLWidget.glDraw() .
		"""
		res = super(QGLWidget,self).updateGL()
		return res
	#----------------------------------------------------------------------
	def updateOverlayGL(self):
		"""
		Updates the widgets overlay (if any)
		Will cause the virtual function PySide.QtOpenGL.QGLWidget.paintOverlayGL() to be executed.
		The widgets rendering context will become the current context and PySide.QtOpenGL.QGLWidget.initializeGL() will be called if it hasnt already been called.
		"""
		res = super(QGLWidget,self).updateOverlayGL()
		return res
	#----------------------------------------------------------------------
	def bindTexture(self,*args,**kwargs):
		"""
		bindTexture(pixmap,target,format,options)
			pixmap=QtGui.QPixmap
			target=long
			format=QtCore.int
			options=QtOpenGL.QGLContext.BindOptions

		bindTexture(pixmap,target=None,format=None)
			pixmap=QtGui.QPixmap
			target=long
			format=QtCore.int

		bindTexture(fileName)
			fileName=unicode

		bindTexture(image,target,format,options)
			image=QtGui.QImage
			target=long
			format=QtCore.int
			options=QtOpenGL.QGLContext.BindOptions

		bindTexture(image,target=None,format=None)
			image=QtGui.QImage
			target=long
			format=QtCore.int


		"""
		res = super(QGLWidget,self).bindTexture(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def deleteTexture(self,tx_id):
		"""
		deleteTexture(tx_id)
			tx_id=long


		"""
		res = super(QGLWidget,self).deleteTexture(tx_id)
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
		res = super(QGLWidget,self).drawTexture(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def grabFrameBuffer(self,withAlpha=None):
		"""
		grabFrameBuffer(withAlpha=None)
			withAlpha=QtCore.bool

		Returns an image of the frame buffer
		If withAlpha is true the alpha channel is included.
		Depending on your hardware, you can explicitly select which color buffer to grab with a glReadBuffer() call before calling this function.
		"""
		res = super(QGLWidget,self).grabFrameBuffer(withAlpha)
		isinstance(res,QtGui.QImage)
		return res
	#----------------------------------------------------------------------
	def qglClearColor(self,c):
		"""
		qglClearColor(c)
			c=QtGui.QColor

		Convenience function for specifying the clearing color to OpenGL
		Calls glClearColor (in RGBA mode) or glClearIndex (in color-index mode) with the color c
		Applies to this widgets GL context.
		"""
		res = super(QGLWidget,self).qglClearColor(c)
		return res
	#----------------------------------------------------------------------
	def qglColor(self,c):
		"""
		qglColor(c)
			c=QtGui.QColor

		Convenience function for specifying a drawing color to OpenGL
		Calls glColor4 (in RGBA mode) or glIndex (in color-index mode) with the color c
		Applies to this widgets GL context.
		"""
		res = super(QGLWidget,self).qglColor(c)
		return res
	#----------------------------------------------------------------------
	def renderPixmap(self,w=None,h=None,useContext=None):
		"""
		renderPixmap(w=None,h=None,useContext=None)
			w=QtCore.int
			h=QtCore.int
			useContext=QtCore.bool

		Renders the current scene on a pixmap and returns the pixmap.
		You can use this method on both visible and invisible PySide.QtOpenGL.QGLWidget objects.
		This method will create a pixmap and a temporary PySide.QtOpenGL.QGLContext to render on the pixmap
		It will then call PySide.QtOpenGL.QGLWidget.initializeGL() , PySide.QtOpenGL.QGLWidget.resizeGL() , and PySide.QtOpenGL.QGLWidget.paintGL() on this context
		Finally, the widgets original GL context is restored.
		The size of the pixmap will be w pixels wide and h pixels high unless one of these parameters is 0 (the default), in which case the pixmap will have the same size as the widget.
		If useContext is true, this method will try to be more efficient by using the existing GL context to render the pixmap
		The default is false
		Only use true if you understand the risks
		Note that under Windows a temporary context has to be created and usage of the useContext parameter is not supported.
		Overlays are not rendered onto the pixmap.
		If the GL rendering context and the desktop have different bit depths, the result will most likely look surprising.
		Note that the creation of display lists, modifications of the view frustum etc
		should be done from within PySide.QtOpenGL.QGLWidget.initializeGL()
		If this is not done, the temporary PySide.QtOpenGL.QGLContext will not be initialized properly, and the rendered pixmap may be incomplete/corrupted.
		"""
		res = super(QGLWidget,self).renderPixmap(w,h,useContext)
		isinstance(res,QtGui.QPixmap)
		return res
	#----------------------------------------------------------------------
	def renderText(self,*args,**kwargs):
		"""
		renderText(x,y,str,fnt=None,listBase=None)
			x=QtCore.int
			y=QtCore.int
			str=unicode
			fnt=QtGui.QFont
			listBase=QtCore.int

		renderText(x,y,z,str,fnt=None,listBase=None)
			x=QtCore.double
			y=QtCore.double
			z=QtCore.double
			str=unicode
			fnt=QtGui.QFont
			listBase=QtCore.int

		Renders the string str into the GL context of this widget.
		x and y are specified in window coordinates, with the origin in the upper left-hand corner of the window
		If font is not specified, the currently set application font will be used to render the string
		To change the color of the rendered text you can use the glColor() call (or the PySide.QtOpenGL.QGLWidget.qglColor() convenience function), just before the PySide.QtOpenGL.QGLWidget.renderText() call.
		The listBase parameter is obsolete and will be removed in a future version of Qt.
		Overpaint with QPainter.drawText() instead.
		"""
		res = super(QGLWidget,self).renderText(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def resizeGL(self,w,h):
		"""
		resizeGL(w,h)
			w=QtCore.int
			h=QtCore.int

		This virtual function is called whenever the widget has been resized
		The new size is passed in width and height
		Reimplement it in a subclass.
		There is no need to call PySide.QtOpenGL.QGLWidget.makeCurrent() because this has already been done when this function is called.
		"""
		res = super(QGLWidget,self).resizeGL(w,h)
		return res
	#----------------------------------------------------------------------
	def resizeOverlayGL(self,w,h):
		"""
		resizeOverlayGL(w,h)
			w=QtCore.int
			h=QtCore.int

		This virtual function is used in the same manner as PySide.QtOpenGL.QGLWidget.paintGL() except that it operates on the widgets overlay context instead of the widgets main context
		This means that PySide.QtOpenGL.QGLWidget.resizeOverlayGL() is called whenever the widget has been resized
		The new size is passed in width and height
		Reimplement it in a subclass.
		There is no need to call PySide.QtOpenGL.QGLWidget.makeOverlayCurrent() because this has already been done when this function is called.
		"""
		res = super(QGLWidget,self).resizeOverlayGL(w,h)
		return res
	#----------------------------------------------------------------------
	def setAutoBufferSwap(self,on):
		"""
		setAutoBufferSwap(on)
			on=QtCore.bool

		If on is true automatic GL buffer swapping is switched on; otherwise it is switched off.
		If on is true and the widget is using a double-buffered format, the background and foreground GL buffers will automatically be swapped after each PySide.QtOpenGL.QGLWidget.paintGL() call.
		The buffer auto-swapping is on by default.
		"""
		res = super(QGLWidget,self).setAutoBufferSwap(on)
		return res
	#----------------------------------------------------------------------
	def setColormap(self,map):
		"""
		setColormap(map)
			map=QtOpenGL.QGLColormap

		Set the colormap for this widget to cmap
		Usually it is only top-level widgets that can have colormaps installed.
		"""
		res = super(QGLWidget,self).setColormap(map)
		return res

from PySide import QtGui, QtCore

class QGLFormat(QtOpenGL.QGLFormat):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGLFormat,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def accum(self):
		"""
		Returns true if the accumulation buffer is enabled; otherwise returns false
		The accumulation buffer is disabled by default.
		"""
		res = super(QGLFormat,self).accum()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def accumBufferSize(self):
		"""
		Returns the accumulation buffer size.
		"""
		res = super(QGLFormat,self).accumBufferSize()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def alpha(self):
		"""
		Returns true if the alpha buffer in the framebuffer is enabled; otherwise returns false
		The alpha buffer is disabled by default.
		"""
		res = super(QGLFormat,self).alpha()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def alphaBufferSize(self):
		"""
		Returns the alpha buffer size.
		"""
		res = super(QGLFormat,self).alphaBufferSize()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def blueBufferSize(self):
		"""
		Returns the blue buffer size.
		"""
		res = super(QGLFormat,self).blueBufferSize()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def depth(self):
		"""
		Returns true if the depth buffer is enabled; otherwise returns false
		The depth buffer is enabled by default.
		"""
		res = super(QGLFormat,self).depth()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def depthBufferSize(self):
		"""
		Returns the depth buffer size.
		"""
		res = super(QGLFormat,self).depthBufferSize()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def directRendering(self):
		"""
		Returns true if direct rendering is enabled; otherwise returns false.
		Direct rendering is enabled by default.
		"""
		res = super(QGLFormat,self).directRendering()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def doubleBuffer(self):
		"""
		Returns true if double buffering is enabled; otherwise returns false
		Double buffering is enabled by default.
		"""
		res = super(QGLFormat,self).doubleBuffer()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def greenBufferSize(self):
		"""
		Returns the green buffer size.
		"""
		res = super(QGLFormat,self).greenBufferSize()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def hasOverlay(self):
		"""
		Returns true if overlay plane is enabled; otherwise returns false.
		Overlay is disabled by default.
		"""
		res = super(QGLFormat,self).hasOverlay()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def majorVersion(self):
		"""
		Returns the OpenGL major version.
		"""
		res = super(QGLFormat,self).majorVersion()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def minorVersion(self):
		"""
		Returns the OpenGL minor version.
		"""
		res = super(QGLFormat,self).minorVersion()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def plane(self):
		"""
		Returns the plane of this format
		The default for normal formats is 0, which means the normal plane
		The default for overlay formats is 1, which is the first overlay plane.
		"""
		res = super(QGLFormat,self).plane()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def profile(self):
		"""
		Returns the OpenGL context profile.
		"""
		res = super(QGLFormat,self).profile()
		isinstance(res,QtOpenGL.QGLFormat.OpenGLContextProfile)
		return res
	#----------------------------------------------------------------------
	def redBufferSize(self):
		"""
		Returns the red buffer size.
		"""
		res = super(QGLFormat,self).redBufferSize()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def rgba(self):
		"""
		Returns true if RGBA color mode is set
		Returns false if color index mode is set
		The default color mode is RGBA.
		"""
		res = super(QGLFormat,self).rgba()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def sampleBuffers(self):
		"""
		Returns true if multisample buffer support is enabled; otherwise returns false.
		The multisample buffer is disabled by default.
		"""
		res = super(QGLFormat,self).sampleBuffers()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def samples(self):
		"""
		Returns the number of samples per pixel when multisampling is enabled
		By default, the highest number of samples that is available is used.
		"""
		res = super(QGLFormat,self).samples()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def stencil(self):
		"""
		Returns true if the stencil buffer is enabled; otherwise returns false
		The stencil buffer is enabled by default.
		"""
		res = super(QGLFormat,self).stencil()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def stencilBufferSize(self):
		"""
		Returns the stencil buffer size.
		"""
		res = super(QGLFormat,self).stencilBufferSize()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def stereo(self):
		"""
		Returns true if stereo buffering is enabled; otherwise returns false
		Stereo buffering is disabled by default.
		"""
		res = super(QGLFormat,self).stereo()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def swapInterval(self):
		"""
		Returns the currently set swap interval
		-1 is returned if setting the swap interval isnt supported in the system GL implementation.
		"""
		res = super(QGLFormat,self).swapInterval()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,arg__2):
		"""
		__ne__(arg__2)
			arg__2=QtOpenGL.QGLFormat


		"""
		res = super(QGLFormat,self).__ne__(arg__2)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,arg__2):
		"""
		__eq__(arg__2)
			arg__2=QtOpenGL.QGLFormat


		"""
		res = super(QGLFormat,self).__eq__(arg__2)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setAccum(self,enable):
		"""
		setAccum(enable)
			enable=QtCore.bool

		If enable is true enables the accumulation buffer; otherwise disables the accumulation buffer.
		The accumulation buffer is disabled by default.
		The accumulation buffer is used to create blur effects and multiple exposures.
		"""
		res = super(QGLFormat,self).setAccum(enable)
		return res
	#----------------------------------------------------------------------
	def setAccumBufferSize(self,size):
		"""
		setAccumBufferSize(size)
			size=QtCore.int

		Set the preferred accumulation buffer size, where size is the bit depth for each RGBA component.
		"""
		res = super(QGLFormat,self).setAccumBufferSize(size)
		return res
	#----------------------------------------------------------------------
	def setAlpha(self,enable):
		"""
		setAlpha(enable)
			enable=QtCore.bool

		If enable is true enables the alpha buffer; otherwise disables the alpha buffer.
		The alpha buffer is disabled by default.
		The alpha buffer is typically used for implementing transparency or translucency
		The A in RGBA specifies the transparency of a pixel.
		"""
		res = super(QGLFormat,self).setAlpha(enable)
		return res
	#----------------------------------------------------------------------
	def setAlphaBufferSize(self,size):
		"""
		setAlphaBufferSize(size)
			size=QtCore.int

		Set the preferred alpha buffer size to size
		This function implicitly enables the alpha channel.
		"""
		res = super(QGLFormat,self).setAlphaBufferSize(size)
		return res
	#----------------------------------------------------------------------
	def setBlueBufferSize(self,size):
		"""
		setBlueBufferSize(size)
			size=QtCore.int

		Set the preferred blue buffer size to size .
		"""
		res = super(QGLFormat,self).setBlueBufferSize(size)
		return res
	#----------------------------------------------------------------------
	def setDepth(self,enable):
		"""
		setDepth(enable)
			enable=QtCore.bool

		If enable is true enables the depth buffer; otherwise disables the depth buffer.
		The depth buffer is enabled by default.
		The purpose of a depth buffer (or Z-buffering) is to remove hidden surfaces
		Pixels are assigned Z values based on the distance to the viewer
		A pixel with a high Z value is closer to the viewer than a pixel with a low Z value
		This information is used to decide whether to draw a pixel or not.
		"""
		res = super(QGLFormat,self).setDepth(enable)
		return res
	#----------------------------------------------------------------------
	def setDepthBufferSize(self,size):
		"""
		setDepthBufferSize(size)
			size=QtCore.int

		Set the minimum depth buffer size to size .
		"""
		res = super(QGLFormat,self).setDepthBufferSize(size)
		return res
	#----------------------------------------------------------------------
	def setDirectRendering(self,enable):
		"""
		setDirectRendering(enable)
			enable=QtCore.bool

		If enable is true enables direct rendering; otherwise disables direct rendering.
		Direct rendering is enabled by default.
		Enabling this option will make OpenGL bypass the underlying window system and render directly from hardware to the screen, if this is supported by the system.
		"""
		res = super(QGLFormat,self).setDirectRendering(enable)
		return res
	#----------------------------------------------------------------------
	def setDoubleBuffer(self,enable):
		"""
		setDoubleBuffer(enable)
			enable=QtCore.bool

		If enable is true sets double buffering; otherwise sets single buffering.
		Double buffering is enabled by default.
		Double buffering is a technique where graphics are rendered on an off-screen buffer and not directly to the screen
		When the drawing has been completed, the program calls a swapBuffers() function to exchange the screen contents with the buffer
		The result is flicker-free drawing and often better performance.
		Note that single buffered contexts are currently not supported with EGL.
		"""
		res = super(QGLFormat,self).setDoubleBuffer(enable)
		return res
	#----------------------------------------------------------------------
	def setGreenBufferSize(self,size):
		"""
		setGreenBufferSize(size)
			size=QtCore.int

		Set the preferred green buffer size to size .
		"""
		res = super(QGLFormat,self).setGreenBufferSize(size)
		return res
	#----------------------------------------------------------------------
	def setOption(self,opt):
		"""
		setOption(opt)
			opt=QtOpenGL.QGL.FormatOptions


		"""
		res = super(QGLFormat,self).setOption(opt)
		return res
	#----------------------------------------------------------------------
	def setOverlay(self,enable):
		"""
		setOverlay(enable)
			enable=QtCore.bool

		If enable is true enables an overlay plane; otherwise disables the overlay plane.
		Enabling the overlay plane will cause PySide.QtOpenGL.QGLWidget to create an additional context in an overlay plane
		See the PySide.QtOpenGL.QGLWidget documentation for further information.
		"""
		res = super(QGLFormat,self).setOverlay(enable)
		return res
	#----------------------------------------------------------------------
	def setPlane(self,plane):
		"""
		setPlane(plane)
			plane=QtCore.int

		Sets the requested plane to plane
		0 is the normal plane, 1 is the first overlay plane, 2 is the second overlay plane, etc.; -1, -2, etc
		are underlay planes.
		Note that in contrast to other format specifications, the plane specifications will be matched exactly
		This means that if you specify a plane that the underlying OpenGL system cannot provide, an invalid PySide.QtOpenGL.QGLWidget will be created.
		"""
		res = super(QGLFormat,self).setPlane(plane)
		return res
	#----------------------------------------------------------------------
	def setProfile(self,profile):
		"""
		setProfile(profile)
			profile=QtOpenGL.QGLFormat.OpenGLContextProfile

		Set the OpenGL context profile to profile
		The profile is ignored if the requested OpenGL version is less than 3.2.
		"""
		res = super(QGLFormat,self).setProfile(profile)
		return res
	#----------------------------------------------------------------------
	def setRedBufferSize(self,size):
		"""
		setRedBufferSize(size)
			size=QtCore.int

		Set the preferred red buffer size to size .
		"""
		res = super(QGLFormat,self).setRedBufferSize(size)
		return res
	#----------------------------------------------------------------------
	def setRgba(self,enable):
		"""
		setRgba(enable)
			enable=QtCore.bool

		If enable is true sets RGBA mode
		If enable is false sets color index mode.
		The default color mode is RGBA.
		RGBA is the preferred mode for most OpenGL applications
		In RGBA color mode you specify colors as red + green + blue + alpha quadruplets.
		In color index mode you specify an index into a color lookup table.
		"""
		res = super(QGLFormat,self).setRgba(enable)
		return res
	#----------------------------------------------------------------------
	def setSampleBuffers(self,enable):
		"""
		setSampleBuffers(enable)
			enable=QtCore.bool

		If enable is true, a GL context with multisample buffer support is picked; otherwise ignored.
		"""
		res = super(QGLFormat,self).setSampleBuffers(enable)
		return res
	#----------------------------------------------------------------------
	def setSamples(self,numSamples):
		"""
		setSamples(numSamples)
			numSamples=QtCore.int

		Set the preferred number of samples per pixel when multisampling is enabled to numSamples
		By default, the highest number of samples available is used.
		"""
		res = super(QGLFormat,self).setSamples(numSamples)
		return res
	#----------------------------------------------------------------------
	def setStencil(self,enable):
		"""
		setStencil(enable)
			enable=QtCore.bool

		If enable is true enables the stencil buffer; otherwise disables the stencil buffer.
		The stencil buffer is enabled by default.
		The stencil buffer masks certain parts of the drawing area so that masked parts are not drawn on.
		"""
		res = super(QGLFormat,self).setStencil(enable)
		return res
	#----------------------------------------------------------------------
	def setStencilBufferSize(self,size):
		"""
		setStencilBufferSize(size)
			size=QtCore.int

		Set the preferred stencil buffer size to size .
		"""
		res = super(QGLFormat,self).setStencilBufferSize(size)
		return res
	#----------------------------------------------------------------------
	def setStereo(self,enable):
		"""
		setStereo(enable)
			enable=QtCore.bool

		If enable is true enables stereo buffering; otherwise disables stereo buffering.
		Stereo buffering is disabled by default.
		Stereo buffering provides extra color buffers to generate left-eye and right-eye images.
		"""
		res = super(QGLFormat,self).setStereo(enable)
		return res
	#----------------------------------------------------------------------
	def setSwapInterval(self,interval):
		"""
		setSwapInterval(interval)
			interval=QtCore.int

		Set the preferred swap interval
		This can be used to sync the GL drawing into a system window to the vertical refresh of the screen
		Setting an interval value of 0 will turn the vertical refresh syncing off, any value higher than 0 will turn the vertical syncing on.
		Under Windows and under X11, where the WGL_EXT_swap_control and GLX_SGI_video_sync extensions are used, the interval parameter can be used to set the minimum number of video frames that are displayed before a buffer swap will occur
		In effect, setting the interval to 10, means there will be 10 vertical retraces between every buffer swap.
		Under Windows the WGL_EXT_swap_control extension has to be present, and under X11 the GLX_SGI_video_sync extension has to be present.
		"""
		res = super(QGLFormat,self).setSwapInterval(interval)
		return res
	#----------------------------------------------------------------------
	def setVersion(self,major,minor):
		"""
		setVersion(major,minor)
			major=QtCore.int
			minor=QtCore.int

		Set the OpenGL version to the major and minor numbers
		If a context compatible with the requested OpenGL version cannot be created, a context compatible with version 1.x is created instead.
		"""
		res = super(QGLFormat,self).setVersion(major,minor)
		return res
	#----------------------------------------------------------------------
	def testOption(self,opt):
		"""
		testOption(opt)
			opt=QtOpenGL.QGL.FormatOptions


		"""
		res = super(QGLFormat,self).testOption(opt)
		isinstance(res,bool)
		return res

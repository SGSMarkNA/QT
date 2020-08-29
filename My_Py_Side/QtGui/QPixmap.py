from PySide import QtGui, QtCore

class QPixmap(QtGui.QPixmap):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QPixmap,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def alphaChannel(self):
		"""
		Returns the alpha channel of the pixmap as a new grayscale PySide.QtGui.QPixmap in which each pixels red, green, and blue values are given the alpha value of the original pixmap
		The color depth of the returned pixmap is the system depth on X11 and 8-bit on Windows and Mac OS X.
		You can use this function while debugging to get a visible image of the alpha channel
		If the pixmap doesnt have an alpha channel, i.e., the alpha channels value for all pixels equals 0xff), a null pixmap is returned
		You can check this with the isNull() function.
		We show an example:
		"""
		res = super(QPixmap,self).alphaChannel()
		isinstance(res,QtGui.QPixmap)
		return res
	#----------------------------------------------------------------------
	def cacheKey(self):
		"""
		Returns a number that identifies this PySide.QtGui.QPixmap
		Distinct PySide.QtGui.QPixmap objects can only have the same cache key if they refer to the same contents.
		The PySide.QtGui.QPixmap.cacheKey() will change when the pixmap is altered.
		"""
		res = super(QPixmap,self).cacheKey()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def deref(self):
		"""

		"""
		res = super(QPixmap,self).deref()
		return res
	#----------------------------------------------------------------------
	def handle(self):
		"""
		Returns the pixmaps handle to the device context.
		Note that, since PySide.QtGui.QPixmap make use of implicit data sharing , the detach() function must be called explicitly to ensure that only this pixmaps data is modified if the pixmap data is shared.
		"""
		res = super(QPixmap,self).handle()
		isinstance(res,QtCore.Qt::HANDLE)
		return res
	#----------------------------------------------------------------------
	def hasAlpha(self):
		"""
		Returns true if this pixmap has an alpha channel, or has a mask, otherwise returns false.
		"""
		res = super(QPixmap,self).hasAlpha()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def hasAlphaChannel(self):
		"""
		Returns true if the pixmap has a format that respects the alpha channel, otherwise returns false.
		"""
		res = super(QPixmap,self).hasAlphaChannel()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if this is a null pixmap; otherwise returns false.
		A null pixmap has zero width, zero height and no contents
		You cannot draw in a null pixmap.
		"""
		res = super(QPixmap,self).isNull()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isQBitmap(self):
		"""
		Returns true if this is a PySide.QtGui.QBitmap ; otherwise returns false.
		"""
		res = super(QPixmap,self).isQBitmap()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def mask(self):
		"""
		Extracts a bitmap mask from the pixmaps alpha channel.
		"""
		res = super(QPixmap,self).mask()
		isinstance(res,QtGui.QBitmap)
		return res
	#----------------------------------------------------------------------
	def rect(self):
		"""
		Returns the pixmaps enclosing rectangle.
		"""
		res = super(QPixmap,self).rect()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""
		Returns the size of the pixmap.
		"""
		res = super(QPixmap,self).size()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def toImage(self):
		"""
		Converts the pixmap to a PySide.QtGui.QImage
		Returns a null image if the conversion fails.
		If the pixmap has 1-bit depth, the returned image will also be 1 bit deep
		Images with more bits will be returned in a format closely represents the underlying system
		Usually this will be QImage.Format_ARGB32_Premultiplied for pixmaps with an alpha and QImage.Format_RGB32 or QImage.Format_RGB16 for pixmaps without alpha.
		Note that for the moment, alpha masks on monochrome images are ignored.
		"""
		res = super(QPixmap,self).toImage()
		isinstance(res,QtGui.QImage)
		return res
	#----------------------------------------------------------------------
	def x11Info(self):
		"""
		X11 only: Returns information about the configuration of the X display used by the screen to which the pixmap currently belongs.
		"""
		res = super(QPixmap,self).x11Info()
		isinstance(res,QtGui.QX11Info)
		return res
	#----------------------------------------------------------------------
	def x11PictureHandle(self):
		"""
		X11 only: Returns the X11 Picture handle of the pixmap for XRender support.
		This function will return 0 if XRender support is not compiled into Qt, if the XRender extension is not supported on the X11 display, or if the handle could not be created
		Use of this function is not portable.
		"""
		res = super(QPixmap,self).x11PictureHandle()
		isinstance(res,QtCore.Qt::HANDLE)
		return res
	#----------------------------------------------------------------------
	def convertFromImage(self,img,flags=None):
		"""
		convertFromImage(img,flags=None)
			img=QtGui.QImage
			flags=QtCore.Qt.ImageConversionFlags


		"""
		res = super(QPixmap,self).convertFromImage(img,flags)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def copy(self,*args,**kwargs):
		"""
		copy(x,y,width,height)
			x=QtCore.int
			y=QtCore.int
			width=QtCore.int
			height=QtCore.int

		copy(rect=None)
			rect=QtCore.QRect

		This is an overloaded function.
		Returns a deep copy of the subset of the pixmap that is specified by the rectangle PySide.QtCore.QRect ( x , y , width , height ).
		"""
		res = super(QPixmap,self).copy(*args,**kwargs)
		isinstance(res,QtGui.QPixmap)
		return res
	#----------------------------------------------------------------------
	def createHeuristicMask(self,clipTight=None):
		"""
		createHeuristicMask(clipTight=None)
			clipTight=QtCore.bool

		Creates and returns a heuristic mask for this pixmap.
		The function works by selecting a color from one of the corners and then chipping away pixels of that color, starting at all the edges
		If clipTight is true (the default) the mask is just large enough to cover the pixels; otherwise, the mask is larger than the data pixels.
		The mask may not be perfect but it should be reasonable, so you can do things such as the following:
		This function is slow because it involves converting to/from a PySide.QtGui.QImage , and non-trivial computations.
		"""
		res = super(QPixmap,self).createHeuristicMask(clipTight)
		isinstance(res,QtGui.QBitmap)
		return res
	#----------------------------------------------------------------------
	def createMaskFromColor(self,*args,**kwargs):
		"""
		createMaskFromColor(maskColor,mode)
			maskColor=QtGui.QColor
			mode=QtCore.Qt.MaskMode

		createMaskFromColor(maskColor)
			maskColor=QtGui.QColor


		"""
		res = super(QPixmap,self).createMaskFromColor(*args,**kwargs)
		isinstance(res,QtGui.QBitmap)
		return res
	#----------------------------------------------------------------------
	def doImageIO(self,io,quality):
		"""
		doImageIO(io,quality)
			io=QtGui.QImageWriter
			quality=QtCore.int


		"""
		res = super(QPixmap,self).doImageIO(io,quality)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def fill(self,*args,**kwargs):
		"""
		fill(widget,xofs,yofs)
			widget=QtGui.QWidget
			xofs=QtCore.int
			yofs=QtCore.int

		fill(widget,ofs)
			widget=QtGui.QWidget
			ofs=QtCore.QPoint

		fill(fillColor=None)
			fillColor=QtGui.QColor

		This is an overloaded function.
		Fills the pixmap with the widget s background color or pixmap
		The given point, (x , y ), defines an offset in widget coordinates to which the pixmaps top-left pixel will be mapped to.
		"""
		res = super(QPixmap,self).fill(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def init(self,*args,**kwargs):
		"""
		init(arg__1,arg__2,arg__3=None)
			arg__1=QtCore.int
			arg__2=QtCore.int
			arg__3=QPixmap.Type

		init(arg__1,arg__2,arg__3)
			arg__1=QtCore.int
			arg__2=QtCore.int
			arg__3=QtCore.int


		"""
		res = super(QPixmap,self).init(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def load(self,fileName,format=None,flags=None):
		"""
		load(fileName,format=None,flags=None)
			fileName=unicode
			format=str
			flags=QtCore.Qt.ImageConversionFlags


		"""
		res = super(QPixmap,self).load(fileName,format,flags)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def loadFromData(self,*args,**kwargs):
		"""
		loadFromData(data,format=None,flags=None)
			data=QtCore.QByteArray
			format=str
			flags=QtCore.Qt.ImageConversionFlags

		loadFromData(buf,format=None,flags=None)
			buf=QtCore.uchar
			format=str
			flags=QtCore.Qt.ImageConversionFlags


		"""
		res = super(QPixmap,self).loadFromData(*args,**kwargs)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def save(self,*args,**kwargs):
		"""
		save(device,format=None,quality=None)
			device=QtCore.QIODevice
			format=str
			quality=QtCore.int

		save(fileName,format=None,quality=None)
			fileName=unicode
			format=str
			quality=QtCore.int

		This is an overloaded function.
		This function writes a PySide.QtGui.QPixmap to the given device using the specified image file format and quality factor
		This can be used, for example, to save a pixmap directly into a PySide.QtCore.QByteArray :
		"""
		res = super(QPixmap,self).save(*args,**kwargs)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def scaled(self,*args,**kwargs):
		"""
		scaled(s,aspectMode=None,mode=None)
			s=QtCore.QSize
			aspectMode=QtCore.Qt.AspectRatioMode
			mode=QtCore.Qt.TransformationMode

		scaled(w,h,aspectMode=None,mode=None)
			w=QtCore.int
			h=QtCore.int
			aspectMode=QtCore.Qt.AspectRatioMode
			mode=QtCore.Qt.TransformationMode


		"""
		res = super(QPixmap,self).scaled(*args,**kwargs)
		isinstance(res,QtGui.QPixmap)
		return res
	#----------------------------------------------------------------------
	def scaledToHeight(self,h,mode=None):
		"""
		scaledToHeight(h,mode=None)
			h=QtCore.int
			mode=QtCore.Qt.TransformationMode


		"""
		res = super(QPixmap,self).scaledToHeight(h,mode)
		isinstance(res,QtGui.QPixmap)
		return res
	#----------------------------------------------------------------------
	def scaledToWidth(self,w,mode=None):
		"""
		scaledToWidth(w,mode=None)
			w=QtCore.int
			mode=QtCore.Qt.TransformationMode


		"""
		res = super(QPixmap,self).scaledToWidth(w,mode)
		isinstance(res,QtGui.QPixmap)
		return res
	#----------------------------------------------------------------------
	def scroll(self,*args,**kwargs):
		"""
		scroll(dx,dy,x,y,width,height,exposed=None)
			dx=QtCore.int
			dy=QtCore.int
			x=QtCore.int
			y=QtCore.int
			width=QtCore.int
			height=QtCore.int
			exposed=QtGui.QRegion

		scroll(dx,dy,rect,exposed=None)
			dx=QtCore.int
			dy=QtCore.int
			rect=QtCore.QRect
			exposed=QtGui.QRegion

		This convenience function is equivalent to calling QPixmap::scroll(dx , dy , PySide.QtCore.QRect (x , y , width , height ), exposed ).
		"""
		res = super(QPixmap,self).scroll(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setAlphaChannel(self,arg__1):
		"""
		setAlphaChannel(arg__1)
			arg__1=QtGui.QPixmap

		Sets the alpha channel of this pixmap to the given alphaChannel by converting the alphaChannel into 32 bit and using the intensity of the RGB pixel values.
		The effect of this function is undefined when the pixmap is being painted on.
		"""
		res = super(QPixmap,self).setAlphaChannel(arg__1)
		return res
	#----------------------------------------------------------------------
	def setMask(self,arg__1):
		"""
		setMask(arg__1)
			arg__1=QtGui.QBitmap

		Sets a mask bitmap.
		This function merges the mask with the pixmaps alpha channel
		A pixel value of 1 on the mask means the pixmaps pixel is unchanged; a value of 0 means the pixel is transparent
		The mask must have the same size as this pixmap.
		Setting a null mask resets the mask, leaving the previously transparent pixels black
		The effect of this function is undefined when the pixmap is being painted on.
		"""
		res = super(QPixmap,self).setMask(arg__1)
		return res
	#----------------------------------------------------------------------
	def transformed(self,*args,**kwargs):
		"""
		transformed(arg__1,mode=None)
			arg__1=QtGui.QTransform
			mode=QtCore.Qt.TransformationMode

		transformed(arg__1,mode=None)
			arg__1=QtGui.QMatrix
			mode=QtCore.Qt.TransformationMode


		"""
		res = super(QPixmap,self).transformed(*args,**kwargs)
		isinstance(res,QtGui.QPixmap)
		return res
	#----------------------------------------------------------------------
	def x11SetScreen(self,screen):
		"""
		x11SetScreen(screen)
			screen=QtCore.int


		"""
		res = super(QPixmap,self).x11SetScreen(screen)
		return res

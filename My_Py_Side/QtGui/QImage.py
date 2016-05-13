from PySide import QtGui, QtCore

class QImage(QtGui.QImage):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QImage,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def allGray(self):
		"""
		Returns true if all the colors in the image are shades of gray (i.e
		their red, green and blue components are equal); otherwise false.
		Note that this function is slow for images without color table.
		"""
		res = super(QImage,self).allGray()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def alphaChannel(self):
		"""
		Returns the alpha channel of the image as a new grayscale PySide.QtGui.QImage in which each pixels red, green, and blue values are given the alpha value of the original image
		The color depth of the returned image is 8-bit.
		You can see an example of use of this function in PySide.QtGui.QPixmap s PySide.QtGui.QPixmap.alphaChannel() , which works in the same way as this function on QPixmaps.
		Most usecases for this function can be replaced with PySide.QtGui.QPainter and using composition modes.
		"""
		res = super(QImage,self).alphaChannel()
		isinstance(res,QtGui.QImage)
		return res
	#----------------------------------------------------------------------
	def bitPlaneCount(self):
		"""
		Returns the number of bit planes in the image.
		The number of bit planes is the number of bits of color and transparency information for each pixel
		This is different from (i.e
		smaller than) the depth when the image format contains unused bits.
		"""
		res = super(QImage,self).bitPlaneCount()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def byteCount(self):
		"""
		Returns the number of bytes occupied by the image data.
		"""
		res = super(QImage,self).byteCount()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def bytesPerLine(self):
		"""
		Returns the number of bytes per image scanline.
		This is equivalent to PySide.QtGui.QImage.byteCount() / PySide.QtGui.QImage.height() .
		"""
		res = super(QImage,self).bytesPerLine()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def cacheKey(self):
		"""
		Returns a number that identifies the contents of this PySide.QtGui.QImage object
		Distinct PySide.QtGui.QImage objects can only have the same key if they refer to the same contents.
		The key will change when the image is altered.
		"""
		res = super(QImage,self).cacheKey()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def colorTable(self):
		"""
		Returns a list of the colors contained in the images color table, or an empty list if the image does not have a color table
		"""
		res = super(QImage,self).colorTable()
		return res
	#----------------------------------------------------------------------
	def constBits(self):
		"""
		Returns a pointer to the first pixel data.
		Note that PySide.QtGui.QImage uses implicit data sharing , but this function does not perform a deep copy of the shared pixel data, because the returned data is const.
		"""
		res = super(QImage,self).constBits()
		isinstance(res,QtCore.uchar)
		return res
	#----------------------------------------------------------------------
	def dotsPerMeterX(self):
		"""
		Returns the number of pixels that fit horizontally in a physical meter
		Together with PySide.QtGui.QImage.dotsPerMeterY() , this number defines the intended scale and aspect ratio of the image.
		"""
		res = super(QImage,self).dotsPerMeterX()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def dotsPerMeterY(self):
		"""
		Returns the number of pixels that fit vertically in a physical meter
		Together with PySide.QtGui.QImage.dotsPerMeterX() , this number defines the intended scale and aspect ratio of the image.
		"""
		res = super(QImage,self).dotsPerMeterY()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def format(self):
		"""
		Returns the format of the image.
		"""
		res = super(QImage,self).format()
		isinstance(res,QtGui.QImage.Format)
		return res
	#----------------------------------------------------------------------
	def hasAlphaChannel(self):
		"""
		Returns true if the image has a format that respects the alpha channel, otherwise returns false.
		"""
		res = super(QImage,self).hasAlphaChannel()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isGrayscale(self):
		"""
		For 32-bit images, this function is equivalent to PySide.QtGui.QImage.allGray() .
		For 8-bpp images, this function returns true if color(i) is QRgb (i, i, i) for all indexes of the color table; otherwise returns false.
		"""
		res = super(QImage,self).isGrayscale()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if it is a null image, otherwise returns false.
		A null image has all parameters set to zero and no allocated data.
		"""
		res = super(QImage,self).isNull()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def numBytes(self):
		"""
		Returns the number of bytes occupied by the image data.
		"""
		res = super(QImage,self).numBytes()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def offset(self):
		"""
		Returns the number of pixels by which the image is intended to be offset by when positioning relative to other images.
		"""
		res = super(QImage,self).offset()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def rect(self):
		"""
		Returns the enclosing rectangle (0, 0, PySide.QtGui.QImage.width() , PySide.QtGui.QImage.height() ) of the image.
		"""
		res = super(QImage,self).rect()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def rgbSwapped(self):
		"""
		Returns a PySide.QtGui.QImage in which the values of the red and blue components of all pixels have been swapped, effectively converting an RGB image to an BGR image.
		The original PySide.QtGui.QImage is not changed.
		"""
		res = super(QImage,self).rgbSwapped()
		isinstance(res,QtGui.QImage)
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""
		Returns the size of the image, i.e
		its PySide.QtGui.QImage.width() and PySide.QtGui.QImage.height() .
		"""
		res = super(QImage,self).size()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def textKeys(self):
		"""
		Returns the text keys for this image.
		You can use these keys with PySide.QtGui.QImage.text() to list the image text for a certain key.
		"""
		res = super(QImage,self).textKeys()
		return res
	#----------------------------------------------------------------------
	def color(self,i):
		"""
		color(i)
			i=QtCore.int

		Returns the color in the color table at index i
		The first color is at index 0.
		The colors in an images color table are specified as ARGB quadruplets ( QRgb )
		Use the qAlpha() , qRed() , qGreen() , and qBlue() functions to get the color value components.
		"""
		res = super(QImage,self).color(i)
		return res
	#----------------------------------------------------------------------
	def constScanLine(self,arg__1):
		"""
		constScanLine(arg__1)
			arg__1=QtCore.int

		Returns a pointer to the pixel data at the scanline with index i
		The first scanline is at index 0.
		The scanline data is aligned on a 32-bit boundary.
		Note that PySide.QtGui.QImage uses implicit data sharing , but this function does not perform a deep copy of the shared pixel data, because the returned data is const.
		"""
		res = super(QImage,self).constScanLine(arg__1)
		isinstance(res,QtCore.uchar)
		return res
	#----------------------------------------------------------------------
	def convertToFormat(self,*args,**kwargs):
		"""
		convertToFormat(f,colorTable,flags=None)
			f=QtGui.QImage.Format
			colorTable=unKnown
			flags=QtCore.Qt.ImageConversionFlags

		convertToFormat(f,flags=None)
			f=QtGui.QImage.Format
			flags=QtCore.Qt.ImageConversionFlags


		"""
		res = super(QImage,self).convertToFormat(*args,**kwargs)
		isinstance(res,QtGui.QImage)
		return res
	#----------------------------------------------------------------------
	def copy(self,*args,**kwargs):
		"""
		copy(rect=None)
			rect=QtCore.QRect

		copy(x,y,w,h)
			x=QtCore.int
			y=QtCore.int
			w=QtCore.int
			h=QtCore.int

		Returns a sub-area of the image as a new image.
		The returned image is copied from the position (rectangle
		x() , rectangle
		y() ) in this image, and will always have the size of the given rectangle .
		In areas beyond this image, pixels are set to 0
		For 32-bit RGB images, this means black; for 32-bit ARGB images, this means transparent black; for 8-bit images, this means the color with index 0 in the color table which can be anything; for 1-bit images, this means Qt.color0 .
		If the given rectangle is a null rectangle the entire image is copied.
		"""
		res = super(QImage,self).copy(*args,**kwargs)
		isinstance(res,QtGui.QImage)
		return res
	#----------------------------------------------------------------------
	def createAlphaMask(self,flags=None):
		"""
		createAlphaMask(flags=None)
			flags=QtCore.Qt.ImageConversionFlags


		"""
		res = super(QImage,self).createAlphaMask(flags)
		isinstance(res,QtGui.QImage)
		return res
	#----------------------------------------------------------------------
	def createHeuristicMask(self,clipTight=None):
		"""
		createHeuristicMask(clipTight=None)
			clipTight=QtCore.bool

		Creates and returns a 1-bpp heuristic mask for this image.
		The function works by selecting a color from one of the corners, then chipping away pixels of that color starting at all the edges
		The four corners vote for which color is to be masked away
		In case of a draw (this generally means that this function is not applicable to the image), the result is arbitrary.
		The returned image has little-endian bit order (i.e
		the images format is QImage.Format_MonoLSB ), which you can convert to big-endian ( QImage.Format_Mono ) using the PySide.QtGui.QImage.convertToFormat() function.
		If clipTight is true (the default) the mask is just large enough to cover the pixels; otherwise, the mask is larger than the data pixels.
		Note that this function disregards the alpha buffer.
		"""
		res = super(QImage,self).createHeuristicMask(clipTight)
		isinstance(res,QtGui.QImage)
		return res
	#----------------------------------------------------------------------
	def createMaskFromColor(self,color,mode=None):
		"""
		createMaskFromColor(color,mode=None)
			color=long
			mode=QtCore.Qt.MaskMode


		"""
		res = super(QImage,self).createMaskFromColor(color,mode)
		isinstance(res,QtGui.QImage)
		return res
	#----------------------------------------------------------------------
	def fill(self,pixel):
		"""
		fill(pixel)
			pixel=QtCore.uint

		Fills the entire image with the given pixelValue .
		If the depth of this image is 1, only the lowest bit is used
		If you say fill(0), fill(2), etc., the image is filled with 0s
		If you say fill(1), fill(3), etc., the image is filled with 1s
		If the depth is 8, the lowest 8 bits are used and if the depth is 16 the lowest 16 bits are used.
		Note: QImage.pixel() returns the color of the pixel at the given coordinates while QColor.pixel() returns the pixel value of the underlying window system (essentially an index value), so normally you will want to use QImage.pixel() to use a color from an existing image or QColor.rgb() to use a specific color.
		"""
		res = super(QImage,self).fill(pixel)
		return res
	#----------------------------------------------------------------------
	def invertPixels(self,mode=None):
		"""
		invertPixels(mode=None)
			mode=QtGui.QImage.InvertMode

		Inverts all pixel values in the image.
		The given invert mode only have a meaning when the images depth is 32
		The default mode is InvertRgb , which leaves the alpha channel unchanged
		If the mode is InvertRgba , the alpha bits are also inverted.
		Inverting an 8-bit image means to replace all pixels using color index i with a pixel using color index 255 minus i
		The same is the case for a 1-bit image
		Note that the color table is not changed.
		"""
		res = super(QImage,self).invertPixels(mode)
		return res
	#----------------------------------------------------------------------
	def load(self,*args,**kwargs):
		"""
		load(device,format)
			device=QtCore.QIODevice
			format=str

		load(fileName,format=None)
			fileName=unicode
			format=str

		This is an overloaded function.
		This function reads a PySide.QtGui.QImage from the given device
		This can, for example, be used to load an image directly into a PySide.QtCore.QByteArray .
		"""
		res = super(QImage,self).load(*args,**kwargs)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def loadFromData(self,data,aformat=None):
		"""
		loadFromData(data,aformat=None)
			data=QtCore.QByteArray
			aformat=str

		This is an overloaded function.
		Loads an image from the given PySide.QtCore.QByteArray data .
		"""
		res = super(QImage,self).loadFromData(data,aformat)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def mirrored(self,horizontally=None,vertically=None):
		"""
		mirrored(horizontally=None,vertically=None)
			horizontally=QtCore.bool
			vertically=QtCore.bool

		Returns a mirror of the image, mirrored in the horizontal and/or the vertical direction depending on whether horizontal and vertical are set to true or false.
		Note that the original image is not changed.
		"""
		res = super(QImage,self).mirrored(horizontally,vertically)
		isinstance(res,QtGui.QImage)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,arg__1):
		"""
		__ne__(arg__1)
			arg__1=QtGui.QImage

		Returns true if this image and the given image have different contents; otherwise returns false.
		The comparison can be slow, unless there is some obvious difference, such as different widths, in which case the function will return quickly.
		"""
		res = super(QImage,self).__ne__(arg__1)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,arg__1):
		"""
		__eq__(arg__1)
			arg__1=QtGui.QImage

		Returns true if this image and the given image have the same contents; otherwise returns false.
		The comparison can be slow, unless there is some obvious difference (e.g
		different size or format), in which case the function will return quickly.
		"""
		res = super(QImage,self).__eq__(arg__1)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def pixel(self,*args,**kwargs):
		"""
		pixel(x,y)
			x=QtCore.int
			y=QtCore.int

		pixel(pt)
			pt=QtCore.QPoint

		This is an overloaded function.
		Returns the color of the pixel at coordinates (x , y ).
		"""
		res = super(QImage,self).pixel(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def pixelIndex(self,*args,**kwargs):
		"""
		pixelIndex(x,y)
			x=QtCore.int
			y=QtCore.int

		pixelIndex(pt)
			pt=QtCore.QPoint

		This is an overloaded function.
		Returns the pixel index at (x , y ).
		"""
		res = super(QImage,self).pixelIndex(*args,**kwargs)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def save(self,*args,**kwargs):
		"""
		save(fileName,format=None,quality=None)
			fileName=unicode
			format=str
			quality=QtCore.int

		save(device,format=None,quality=None)
			device=QtCore.QIODevice
			format=str
			quality=QtCore.int

		Saves the image to the file with the given fileName , using the given image file format and quality factor
		If format is 0, PySide.QtGui.QImage will attempt to guess the format by looking at fileName s suffix.
		The quality factor must be in the range 0 to 100 or -1
		Specify 0 to obtain small compressed files, 100 for large uncompressed files, and -1 (the default) to use the default settings.
		Returns true if the image was successfully saved; otherwise returns false.
		"""
		res = super(QImage,self).save(*args,**kwargs)
		isinstance(res,QtCore.bool)
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
		res = super(QImage,self).scaled(*args,**kwargs)
		isinstance(res,QtGui.QImage)
		return res
	#----------------------------------------------------------------------
	def scaledToHeight(self,h,mode=None):
		"""
		scaledToHeight(h,mode=None)
			h=QtCore.int
			mode=QtCore.Qt.TransformationMode


		"""
		res = super(QImage,self).scaledToHeight(h,mode)
		isinstance(res,QtGui.QImage)
		return res
	#----------------------------------------------------------------------
	def scaledToWidth(self,w,mode=None):
		"""
		scaledToWidth(w,mode=None)
			w=QtCore.int
			mode=QtCore.Qt.TransformationMode


		"""
		res = super(QImage,self).scaledToWidth(w,mode)
		isinstance(res,QtGui.QImage)
		return res
	#----------------------------------------------------------------------
	def setAlphaChannel(self,alphaChannel):
		"""
		setAlphaChannel(alphaChannel)
			alphaChannel=QtGui.QImage

		Sets the alpha channel of this image to the given alphaChannel .
		If alphaChannel is an 8 bit grayscale image, the intensity values are written into this buffer directly
		Otherwise, alphaChannel is converted to 32 bit and the intensity of the RGB pixel values is used.
		Note that the image will be converted to the Format_ARGB32_Premultiplied format if the function succeeds.
		Use one of the composition modes in QPainter.CompositionMode instead.
		"""
		res = super(QImage,self).setAlphaChannel(alphaChannel)
		return res
	#----------------------------------------------------------------------
	def setColor(self,i,c):
		"""
		setColor(i,c)
			i=QtCore.int
			c=long


		"""
		res = super(QImage,self).setColor(i,c)
		return res
	#----------------------------------------------------------------------
	def setColorCount(self,arg__1):
		"""
		setColorCount(arg__1)
			arg__1=QtCore.int

		Resizes the color table to contain colorCount entries.
		If the color table is expanded, all the extra colors will be set to transparent (i.e qRgba(0, 0, 0, 0)).
		When the image is used, the color table must be large enough to have entries for all the pixel/index values present in the image, otherwise the results are undefined.
		"""
		res = super(QImage,self).setColorCount(arg__1)
		return res
	#----------------------------------------------------------------------
	def setColorTable(self,colors):
		"""
		setColorTable(colors)
			colors=unKnown


		"""
		res = super(QImage,self).setColorTable(colors)
		return res
	#----------------------------------------------------------------------
	def setDotsPerMeterX(self,arg__1):
		"""
		setDotsPerMeterX(arg__1)
			arg__1=QtCore.int

		Sets the number of pixels that fit horizontally in a physical meter, to x .
		Together with PySide.QtGui.QImage.dotsPerMeterY() , this number defines the intended scale and aspect ratio of the image, and determines the scale at which PySide.QtGui.QPainter will draw graphics on the image
		It does not change the scale or aspect ratio of the image when it is rendered on other paint devices.
		"""
		res = super(QImage,self).setDotsPerMeterX(arg__1)
		return res
	#----------------------------------------------------------------------
	def setDotsPerMeterY(self,arg__1):
		"""
		setDotsPerMeterY(arg__1)
			arg__1=QtCore.int

		Sets the number of pixels that fit vertically in a physical meter, to y .
		Together with PySide.QtGui.QImage.dotsPerMeterX() , this number defines the intended scale and aspect ratio of the image, and determines the scale at which PySide.QtGui.QPainter will draw graphics on the image
		It does not change the scale or aspect ratio of the image when it is rendered on other paint devices.
		"""
		res = super(QImage,self).setDotsPerMeterY(arg__1)
		return res
	#----------------------------------------------------------------------
	def setNumColors(self,arg__1):
		"""
		setNumColors(arg__1)
			arg__1=QtCore.int

		Resizes the color table to contain numColors entries.
		"""
		res = super(QImage,self).setNumColors(arg__1)
		return res
	#----------------------------------------------------------------------
	def setOffset(self,arg__1):
		"""
		setOffset(arg__1)
			arg__1=QtCore.QPoint

		Sets the number of pixels by which the image is intended to be offset by when positioning relative to other images, to offset .
		"""
		res = super(QImage,self).setOffset(arg__1)
		return res
	#----------------------------------------------------------------------
	def setPixel(self,*args,**kwargs):
		"""
		setPixel(x,y,index_or_rgb)
			x=QtCore.int
			y=QtCore.int
			index_or_rgb=QtCore.uint

		setPixel(pt,index_or_rgb)
			pt=QtCore.QPoint
			index_or_rgb=QtCore.uint

		This is an overloaded function.
		Sets the pixel index or color at (x , y ) to index_or_rgb .
		"""
		res = super(QImage,self).setPixel(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setText(self,key,value):
		"""
		setText(key,value)
			key=unicode
			value=unicode

		Sets the image text to the given text and associate it with the given key .
		If you just want to store a single text block (i.e., a comment or just a description), you can either pass an empty key, or use a generic key like Description.
		The image text is embedded into the image data when you call PySide.QtGui.QImage.save() or QImageWriter.write() .
		Not all image formats support embedded text
		You can find out if a specific image or format supports embedding text by using QImageWriter.supportsOption()
		We give an example:
		You can use QImageWriter.supportedImageFormats() to find out which image formats are available to you.
		"""
		res = super(QImage,self).setText(key,value)
		return res
	#----------------------------------------------------------------------
	def text(self,key=None):
		"""
		text(key=None)
			key=unicode

		Returns the image text associated with the given key
		If the specified key is an empty string, the whole image text is returned, with each key-text pair separated by a newline.
		"""
		res = super(QImage,self).text(key)
		return res
	#----------------------------------------------------------------------
	def transformed(self,*args,**kwargs):
		"""
		transformed(matrix,mode=None)
			matrix=QtGui.QMatrix
			mode=QtCore.Qt.TransformationMode

		transformed(matrix,mode=None)
			matrix=QtGui.QTransform
			mode=QtCore.Qt.TransformationMode


		"""
		res = super(QImage,self).transformed(*args,**kwargs)
		isinstance(res,QtGui.QImage)
		return res
	#----------------------------------------------------------------------
	def valid(self,*args,**kwargs):
		"""
		valid(pt)
			pt=QtCore.QPoint

		valid(x,y)
			x=QtCore.int
			y=QtCore.int

		Returns true if pos is a valid coordinate pair within the image; otherwise returns false.
		"""
		res = super(QImage,self).valid(*args,**kwargs)
		isinstance(res,QtCore.bool)
		return res

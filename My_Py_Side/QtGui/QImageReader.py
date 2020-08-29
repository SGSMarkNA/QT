from PySide import QtGui, QtCore

class QImageReader(QtGui.QImageReader):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QImageReader,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def autoDetectImageFormat(self):
		"""
		Returns true if image format autodetection is enabled on this image reader; otherwise returns false
		By default, autodetection is enabled.
		"""
		res = super(QImageReader,self).autoDetectImageFormat()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def backgroundColor(self):
		"""
		Returns the background color thats used when reading an image
		If the image format does not support setting the background color an invalid color is returned.
		"""
		res = super(QImageReader,self).backgroundColor()
		isinstance(res,QtGui.QColor)
		return res
	#----------------------------------------------------------------------
	def canRead(self):
		"""
		Returns true if an image can be read for the device (i.e., the image format is supported, and the device seems to contain valid data); otherwise returns false.
		PySide.QtGui.QImageReader.canRead() is a lightweight function that only does a quick test to see if the image data is valid
		PySide.QtGui.QImageReader.read() may still return false after PySide.QtGui.QImageReader.canRead() returns true, if the image data is corrupt.
		For images that support animation, PySide.QtGui.QImageReader.canRead() returns false when all frames have been read.
		"""
		res = super(QImageReader,self).canRead()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def clipRect(self):
		"""
		Returns the clip rect (also known as the ROI, or Region Of Interest) of the image
		If no clip rect has been set, an invalid PySide.QtCore.QRect is returned.
		"""
		res = super(QImageReader,self).clipRect()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def currentImageNumber(self):
		"""
		For image formats that support animation, this function returns the sequence number of the current frame
		If the image format doesnt support animation, 0 is returned.
		This function returns -1 if an error occurred.
		"""
		res = super(QImageReader,self).currentImageNumber()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def currentImageRect(self):
		"""
		For image formats that support animation, this function returns the rect for the current frame
		Otherwise, a null rect is returned.
		"""
		res = super(QImageReader,self).currentImageRect()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def decideFormatFromContent(self):
		"""
		Returns whether the image reader should decide which plugin to use only based on the contents of the datastream rather than on the file extension.
		"""
		res = super(QImageReader,self).decideFormatFromContent()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def device(self):
		"""
		Returns the device currently assigned to PySide.QtGui.QImageReader , or 0 if no device has been assigned.
		"""
		res = super(QImageReader,self).device()
		isinstance(res,QtCore.QIODevice)
		return res
	#----------------------------------------------------------------------
	def error(self):
		"""
		Returns the type of error that occurred last.
		"""
		res = super(QImageReader,self).error()
		isinstance(res,QtGui.QImageReader.ImageReaderError)
		return res
	#----------------------------------------------------------------------
	def errorString(self):
		"""
		Returns a human readable description of the last error that occurred.
		"""
		res = super(QImageReader,self).errorString()
		return res
	#----------------------------------------------------------------------
	def fileName(self):
		"""
		If the currently assigned device is a PySide.QtCore.QFile , or if PySide.QtGui.QImageReader.setFileName() has been called, this function returns the name of the file PySide.QtGui.QImageReader reads from
		Otherwise (i.e., if no device has been assigned or the device is not a PySide.QtCore.QFile ), an empty PySide.QtCore.QString is returned.
		"""
		res = super(QImageReader,self).fileName()
		return res
	#----------------------------------------------------------------------
	def format(self):
		"""
		Returns the format PySide.QtGui.QImageReader uses for reading images.
		You can call this function after assigning a device to the reader to determine the format of the device
		For example:
		If the reader cannot read any image from the device (e.g., there is no image there, or the image has already been read), or if the format is unsupported, this function returns an empty QByteArray() .
		"""
		res = super(QImageReader,self).format()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def imageCount(self):
		"""
		For image formats that support animation, this function returns the total number of images in the animation
		If the format does not support animation, 0 is returned.
		This function returns -1 if an error occurred.
		"""
		res = super(QImageReader,self).imageCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def imageFormat(self):
		"""
		Returns the format of the image, without actually reading the image contents
		The format describes the image format QImageReader.read() returns, not the format of the actual image.
		If the image format does not support this feature, this function returns an invalid format.
		"""
		res = super(QImageReader,self).imageFormat()
		isinstance(res,QtGui.QImage.Format)
		return res
	#----------------------------------------------------------------------
	def jumpToNextImage(self):
		"""
		For image formats that support animation, this function steps over the current image, returning true if successful or false if there is no following image in the animation.
		The default implementation calls PySide.QtGui.QImageReader.read() , then discards the resulting image, but the image handler may have a more efficient way of implementing this operation.
		"""
		res = super(QImageReader,self).jumpToNextImage()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def loopCount(self):
		"""
		For image formats that support animation, this function returns the number of times the animation should loop
		If this function returns -1, it can either mean the animation should loop forever, or that an error occurred
		If an error occurred, PySide.QtGui.QImageReader.canRead() will return false.
		"""
		res = super(QImageReader,self).loopCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def nextImageDelay(self):
		"""
		For image formats that support animation, this function returns the number of milliseconds to wait until displaying the next frame in the animation
		If the image format doesnt support animation, 0 is returned.
		This function returns -1 if an error occurred.
		"""
		res = super(QImageReader,self).nextImageDelay()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def quality(self):
		"""
		Returns the quality level of the image.
		"""
		res = super(QImageReader,self).quality()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def read(self):
		"""
		Reads an image from the device
		On success, the image that was read is returned; otherwise, a null PySide.QtGui.QImage is returned
		You can then call PySide.QtGui.QImageReader.error() to find the type of error that occurred, or PySide.QtGui.QImageReader.errorString() to get a human readable description of the error.
		For image formats that support animation, calling PySide.QtGui.QImageReader.read() repeatedly will return the next frame
		When all frames have been read, a null image will be returned.
		"""
		res = super(QImageReader,self).read()
		isinstance(res,QtGui.QImage)
		return res
	#----------------------------------------------------------------------
	def scaledClipRect(self):
		"""
		Returns the scaled clip rect of the image.
		"""
		res = super(QImageReader,self).scaledClipRect()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def scaledSize(self):
		"""
		Returns the scaled size of the image.
		"""
		res = super(QImageReader,self).scaledSize()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""
		Returns the size of the image, without actually reading the image contents.
		If the image format does not support this feature, this function returns an invalid size
		Qts built-in image handlers all support this feature, but custom image format plugins are not required to do so.
		"""
		res = super(QImageReader,self).size()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def supportsAnimation(self):
		"""
		Returns true if the image format supports animation; otherwise, false is returned.
		"""
		res = super(QImageReader,self).supportsAnimation()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def textKeys(self):
		"""
		Returns the text keys for this image
		You can use these keys with PySide.QtGui.QImageReader.text() to list the image text for a certain key.
		Support for this option is implemented through QImageIOHandler.Description .
		"""
		res = super(QImageReader,self).textKeys()
		return res
	#----------------------------------------------------------------------
	def jumpToImage(self,imageNumber):
		"""
		jumpToImage(imageNumber)
			imageNumber=QtCore.int

		For image formats that support animation, this function skips to the image whose sequence number is imageNumber , returning true if successful or false if the corresponding image cannot be found.
		The next call to PySide.QtGui.QImageReader.read() will attempt to read this image.
		"""
		res = super(QImageReader,self).jumpToImage(imageNumber)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setAutoDetectImageFormat(self,enabled):
		"""
		setAutoDetectImageFormat(enabled)
			enabled=QtCore.bool

		If enabled is true, image format autodetection is enabled; otherwise, it is disabled
		By default, autodetection is enabled.
		PySide.QtGui.QImageReader uses an extensive approach to detecting the image format; firstly, if you pass a file name to PySide.QtGui.QImageReader , it will attempt to detect the file extension if the given file name does not point to an existing file, by appending supported default extensions to the given file name, one at a time
		It then uses the following approach to detect the image format:
		By disabling image format autodetection, PySide.QtGui.QImageReader will only query the plugins and built-in handlers based on the format string (i.e., no file name extensions are tested).
		"""
		res = super(QImageReader,self).setAutoDetectImageFormat(enabled)
		return res
	#----------------------------------------------------------------------
	def setBackgroundColor(self,color):
		"""
		setBackgroundColor(color)
			color=QtGui.QColor

		Sets the background color to color
		Image formats that support this operation are expected to initialize the background to color before reading an image.
		"""
		res = super(QImageReader,self).setBackgroundColor(color)
		return res
	#----------------------------------------------------------------------
	def setClipRect(self,rect):
		"""
		setClipRect(rect)
			rect=QtCore.QRect

		Sets the image clip rect (also known as the ROI, or Region Of Interest) to rect
		The coordinates of rect are relative to the untransformed image size, as returned by PySide.QtGui.QImageReader.size() .
		"""
		res = super(QImageReader,self).setClipRect(rect)
		return res
	#----------------------------------------------------------------------
	def setDecideFormatFromContent(self,ignored):
		"""
		setDecideFormatFromContent(ignored)
			ignored=QtCore.bool

		If ignored is set to true, then the image reader will ignore specified formats or file extensions and decide which plugin to use only based on the contents in the datastream.
		Setting this flag means that all image plugins gets loaded
		Each plugin will read the first bytes in the image data and decide if the plugin is compatible or not.
		This also disables auto detecting the image format.
		"""
		res = super(QImageReader,self).setDecideFormatFromContent(ignored)
		return res
	#----------------------------------------------------------------------
	def setDevice(self,device):
		"""
		setDevice(device)
			device=QtCore.QIODevice

		Sets PySide.QtGui.QImageReader s device to device
		If a device has already been set, the old device is removed from PySide.QtGui.QImageReader and is otherwise left unchanged.
		If the device is not already open, PySide.QtGui.QImageReader will attempt to open the device in QIODevice.ReadOnly mode by calling open()
		Note that this does not work for certain devices, such as PySide.QtCore.QProcess , PySide.QtNetwork.QTcpSocket and PySide.QtNetwork.QUdpSocket , where more logic is required to open the device.
		"""
		res = super(QImageReader,self).setDevice(device)
		return res
	#----------------------------------------------------------------------
	def setFileName(self,fileName):
		"""
		setFileName(fileName)
			fileName=unicode

		Sets the file name of PySide.QtGui.QImageReader to fileName
		Internally, PySide.QtGui.QImageReader will create a PySide.QtCore.QFile object and open it in QIODevice.ReadOnly mode, and use this when reading images.
		If fileName does not include a file extension (e.g., .png or .bmp), PySide.QtGui.QImageReader will cycle through all supported extensions until it finds a matching file.
		"""
		res = super(QImageReader,self).setFileName(fileName)
		return res
	#----------------------------------------------------------------------
	def setFormat(self,format):
		"""
		setFormat(format)
			format=QtCore.QByteArray

		Sets the format PySide.QtGui.QImageReader will use when reading images, to format
		format is a case insensitive text string
		Example:
		You can call PySide.QtGui.QImageReader.supportedImageFormats() for the full list of formats PySide.QtGui.QImageReader supports.
		"""
		res = super(QImageReader,self).setFormat(format)
		return res
	#----------------------------------------------------------------------
	def setQuality(self,quality):
		"""
		setQuality(quality)
			quality=QtCore.int

		This is an image format specific function that sets the quality level of the image to quality
		For image formats that do not support setting the quality, this value is ignored.
		The value range of quality depends on the image format
		For example, the jpeg format supports a quality range from 0 (low quality, high compression) to 100 (high quality, low compression).
		"""
		res = super(QImageReader,self).setQuality(quality)
		return res
	#----------------------------------------------------------------------
	def setScaledClipRect(self,rect):
		"""
		setScaledClipRect(rect)
			rect=QtCore.QRect

		Sets the scaled clip rect to rect
		The scaled clip rect is the clip rect (also known as ROI, or Region Of Interest) that is applied after the image has been scaled.
		"""
		res = super(QImageReader,self).setScaledClipRect(rect)
		return res
	#----------------------------------------------------------------------
	def setScaledSize(self,size):
		"""
		setScaledSize(size)
			size=QtCore.QSize

		Sets the scaled size of the image to size
		The scaling is performed after the initial clip rect, but before the scaled clip rect is applied
		The algorithm used for scaling depends on the image format
		By default (i.e., if the image format does not support scaling), PySide.QtGui.QImageReader will use QImage::scale() with Qt::SmoothScaling.
		"""
		res = super(QImageReader,self).setScaledSize(size)
		return res
	#----------------------------------------------------------------------
	def supportsOption(self,option):
		"""
		supportsOption(option)
			option=QtGui.QImageIOHandler.ImageOption


		"""
		res = super(QImageReader,self).supportsOption(option)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def text(self,key):
		"""
		text(key)
			key=unicode

		Returns the image text associated with key .
		Support for this option is implemented through QImageIOHandler.Description .
		"""
		res = super(QImageReader,self).text(key)
		return res

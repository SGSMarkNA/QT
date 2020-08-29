from PySide import QtGui, QtCore

class QImageIOHandler(QtGui.QImageIOHandler):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QImageIOHandler,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def canRead(self):
		"""
		Returns true if an image can be read from the device (i.e., the image format is supported, the device can be read from and the initial header information suggests that the image can be read); otherwise returns false.
		When reimplementing PySide.QtGui.QImageIOHandler.canRead() , make sure that the I/O device ( PySide.QtGui.QImageIOHandler.device() ) is left in its original state (e.g., by using peek() rather than PySide.QtGui.QImageIOHandler.read() ).
		"""
		res = super(QImageIOHandler,self).canRead()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def currentImageNumber(self):
		"""
		For image formats that support animation, this function returns the sequence number of the current image in the animation
		If this function is called before any image is PySide.QtGui.QImageIOHandler.read() , -1 is returned
		The number of the first image in the sequence is 0.
		If the image format does not support animation, 0 is returned.
		"""
		res = super(QImageIOHandler,self).currentImageNumber()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def currentImageRect(self):
		"""
		Returns the rect of the current image
		If no rect is defined for the image, and empty QRect() is returned.
		This function is useful for animations, where only parts of the frame may be updated at a time.
		"""
		res = super(QImageIOHandler,self).currentImageRect()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def device(self):
		"""
		Returns the device currently assigned to the PySide.QtGui.QImageIOHandler
		If not device has been assigned, 0 is returned.
		"""
		res = super(QImageIOHandler,self).device()
		isinstance(res,QtCore.QIODevice)
		return res
	#----------------------------------------------------------------------
	def format(self):
		"""
		Returns the format that is currently assigned to PySide.QtGui.QImageIOHandler
		If no format has been assigned, an empty string is returned.
		"""
		res = super(QImageIOHandler,self).format()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def imageCount(self):
		"""
		For image formats that support animation, this function returns the number of images in the animation
		If the image format does not support animation, or if it is unable to determine the number of images, 0 is returned.
		The default implementation returns 1 if PySide.QtGui.QImageIOHandler.canRead() returns true; otherwise 0 is returned.
		"""
		res = super(QImageIOHandler,self).imageCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def jumpToNextImage(self):
		"""
		For image formats that support animation, this function jumps to the next image.
		The default implementation does nothing, and returns false.
		"""
		res = super(QImageIOHandler,self).jumpToNextImage()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def loopCount(self):
		"""
		For image formats that support animation, this function returns the number of times the animation should loop
		If the image format does not support animation, 0 is returned.
		"""
		res = super(QImageIOHandler,self).loopCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def nextImageDelay(self):
		"""
		For image formats that support animation, this function returns the number of milliseconds to wait until reading the next image
		If the image format does not support animation, 0 is returned.
		"""
		res = super(QImageIOHandler,self).nextImageDelay()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def jumpToImage(self,imageNumber):
		"""
		jumpToImage(imageNumber)
			imageNumber=QtCore.int

		For image formats that support animation, this function jumps to the image whose sequence number is imageNumber
		The next call to PySide.QtGui.QImageIOHandler.read() will attempt to read this image.
		The default implementation does nothing, and returns false.
		"""
		res = super(QImageIOHandler,self).jumpToImage(imageNumber)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def option(self,option):
		"""
		option(option)
			option=QtGui.QImageIOHandler.ImageOption

		Returns the value assigned to option as a PySide.QtCore.QVariant
		The type of the value depends on the option
		For example, option(Size) returns a PySide.QtCore.QSize variant.
		"""
		res = super(QImageIOHandler,self).option(option)
		return res
	#----------------------------------------------------------------------
	def read(self,image):
		"""
		read(image)
			image=QtGui.QImage

		Read an image from the device, and stores it in image
		Returns true if the image is successfully read; otherwise returns false.
		For image formats that support incremental loading, and for animation formats, the image handler can assume that image points to the previous frame.
		"""
		res = super(QImageIOHandler,self).read(image)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setDevice(self,device):
		"""
		setDevice(device)
			device=QtCore.QIODevice

		Sets the device of the PySide.QtGui.QImageIOHandler to device
		The image handler will use this device when reading and writing images.
		The device can only be set once and must be set before calling PySide.QtGui.QImageIOHandler.canRead() , PySide.QtGui.QImageIOHandler.read() , PySide.QtGui.QImageIOHandler.write() , etc
		If you need to read multiple files, construct multiple instances of the appropriate PySide.QtGui.QImageIOHandler subclass.
		"""
		res = super(QImageIOHandler,self).setDevice(device)
		return res
	#----------------------------------------------------------------------
	def setFormat(self,format):
		"""
		setFormat(format)
			format=QtCore.QByteArray

		Sets the format of the PySide.QtGui.QImageIOHandler to format
		The format is most useful for handlers that support multiple image formats.
		This function is declared const so that it can be called from PySide.QtGui.QImageIOHandler.canRead() .
		"""
		res = super(QImageIOHandler,self).setFormat(format)
		return res
	#----------------------------------------------------------------------
	def setOption(self,option,value):
		"""
		setOption(option,value)
			option=QtGui.QImageIOHandler.ImageOption
			value=object

		Sets the option option with the value value .
		"""
		res = super(QImageIOHandler,self).setOption(option,value)
		return res
	#----------------------------------------------------------------------
	def supportsOption(self,option):
		"""
		supportsOption(option)
			option=QtGui.QImageIOHandler.ImageOption

		Returns true if the PySide.QtGui.QImageIOHandler supports the option option ; otherwise returns false
		For example, if the PySide.QtGui.QImageIOHandler supports the Size option, supportsOption(Size) must return true.
		"""
		res = super(QImageIOHandler,self).supportsOption(option)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def write(self,image):
		"""
		write(image)
			image=QtGui.QImage

		Writes the image image to the assigned device
		Returns true on success; otherwise returns false.
		The default implementation does nothing, and simply returns false.
		"""
		res = super(QImageIOHandler,self).write(image)
		isinstance(res,bool)
		return res

from PySide import QtGui, QtCore

class QImageWriter(QtGui.QImageWriter):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QImageWriter,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def canWrite(self):
		"""
		Returns true if PySide.QtGui.QImageWriter can write the image; i.e., the image format is supported and the assigned device is open for reading.
		"""
		res = super(QImageWriter,self).canWrite()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def compression(self):
		"""
		Returns the compression of the image.
		"""
		res = super(QImageWriter,self).compression()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def device(self):
		"""
		Returns the device currently assigned to PySide.QtGui.QImageWriter , or 0 if no device has been assigned.
		"""
		res = super(QImageWriter,self).device()
		isinstance(res,QtCore.QIODevice)
		return res
	#----------------------------------------------------------------------
	def error(self):
		"""
		Returns the type of error that last occurred.
		"""
		res = super(QImageWriter,self).error()
		isinstance(res,QtGui.QImageWriter.ImageWriterError)
		return res
	#----------------------------------------------------------------------
	def errorString(self):
		"""
		Returns a human readable description of the last error that occurred.
		"""
		res = super(QImageWriter,self).errorString()
		return res
	#----------------------------------------------------------------------
	def fileName(self):
		"""
		If the currently assigned device is a PySide.QtCore.QFile , or if PySide.QtGui.QImageWriter.setFileName() has been called, this function returns the name of the file PySide.QtGui.QImageWriter writes to
		Otherwise (i.e., if no device has been assigned or the device is not a PySide.QtCore.QFile ), an empty PySide.QtCore.QString is returned.
		"""
		res = super(QImageWriter,self).fileName()
		return res
	#----------------------------------------------------------------------
	def format(self):
		"""
		Returns the format PySide.QtGui.QImageWriter uses for writing images.
		"""
		res = super(QImageWriter,self).format()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def gamma(self):
		"""
		Returns the gamma level of the image.
		"""
		res = super(QImageWriter,self).gamma()
		isinstance(res,QtCore.float)
		return res
	#----------------------------------------------------------------------
	def quality(self):
		"""
		Returns the quality level of the image.
		"""
		res = super(QImageWriter,self).quality()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def setCompression(self,compression):
		"""
		setCompression(compression)
			compression=QtCore.int

		This is an image format specific function that set the compression of an image
		For image formats that do not support setting the compression, this value is ignored.
		The value range of compression depends on the image format
		For example, the tiff format supports two values, 0(no compression) and 1(LZW-compression).
		"""
		res = super(QImageWriter,self).setCompression(compression)
		return res
	#----------------------------------------------------------------------
	def setDevice(self,device):
		"""
		setDevice(device)
			device=QtCore.QIODevice

		Sets PySide.QtGui.QImageWriter s device to device
		If a device has already been set, the old device is removed from PySide.QtGui.QImageWriter and is otherwise left unchanged.
		If the device is not already open, PySide.QtGui.QImageWriter will attempt to open the device in QIODevice.WriteOnly mode by calling open()
		Note that this does not work for certain devices, such as PySide.QtCore.QProcess , PySide.QtNetwork.QTcpSocket and PySide.QtNetwork.QUdpSocket , where more logic is required to open the device.
		"""
		res = super(QImageWriter,self).setDevice(device)
		return res
	#----------------------------------------------------------------------
	def setFileName(self,fileName):
		"""
		setFileName(fileName)
			fileName=unicode

		Sets the file name of PySide.QtGui.QImageWriter to fileName
		Internally, PySide.QtGui.QImageWriter will create a PySide.QtCore.QFile and open it in QIODevice.WriteOnly mode, and use this file when writing images.
		"""
		res = super(QImageWriter,self).setFileName(fileName)
		return res
	#----------------------------------------------------------------------
	def setFormat(self,format):
		"""
		setFormat(format)
			format=QtCore.QByteArray

		Sets the format PySide.QtGui.QImageWriter will use when writing images, to format
		format is a case insensitive text string
		Example:
		You can call PySide.QtGui.QImageWriter.supportedImageFormats() for the full list of formats PySide.QtGui.QImageWriter supports.
		"""
		res = super(QImageWriter,self).setFormat(format)
		return res
	#----------------------------------------------------------------------
	def setGamma(self,gamma):
		"""
		setGamma(gamma)
			gamma=QtCore.float

		This is an image format specific function that sets the gamma level of the image to gamma
		For image formats that do not support setting the gamma level, this value is ignored.
		The value range of gamma depends on the image format
		For example, the png format supports a gamma range from 0.0 to 1.0.
		"""
		res = super(QImageWriter,self).setGamma(gamma)
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
		res = super(QImageWriter,self).setQuality(quality)
		return res
	#----------------------------------------------------------------------
	def setText(self,key,text):
		"""
		setText(key,text)
			key=unicode
			text=unicode

		Sets the image text associated with the key key to text
		This is useful for storing copyright information or other information about the image
		Example:
		If you want to store a single block of data (e.g., a comment), you can pass an empty key, or use a generic key like Description.
		The key and text will be embedded into the image data after calling PySide.QtGui.QImageWriter.write() .
		Support for this option is implemented through QImageIOHandler.Description .
		"""
		res = super(QImageWriter,self).setText(key,text)
		return res
	#----------------------------------------------------------------------
	def supportsOption(self,option):
		"""
		supportsOption(option)
			option=QtGui.QImageIOHandler.ImageOption


		"""
		res = super(QImageWriter,self).supportsOption(option)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def write(self,image):
		"""
		write(image)
			image=QtGui.QImage

		Writes the image image to the assigned device or file name
		Returns true on success; otherwise returns false
		If the operation fails, you can call PySide.QtGui.QImageWriter.error() to find the type of error that occurred, or PySide.QtGui.QImageWriter.errorString() to get a human readable description of the error.
		"""
		res = super(QImageWriter,self).write(image)
		isinstance(res,QtCore.bool)
		return res

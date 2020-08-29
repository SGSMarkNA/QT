from PySide import QtGui, QtCore

class QPictureIO(QtGui.QPictureIO):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QPictureIO,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def description(self):
		"""
		Returns the picture description string.
		"""
		res = super(QPictureIO,self).description()
		return res
	#----------------------------------------------------------------------
	def fileName(self):
		"""
		Returns the file name currently set.
		"""
		res = super(QPictureIO,self).fileName()
		return res
	#----------------------------------------------------------------------
	def format(self):
		"""
		Returns the picture format string or 0 if no format has been explicitly set.
		"""
		res = super(QPictureIO,self).format()
		return res
	#----------------------------------------------------------------------
	def gamma(self):
		"""
		Returns the gamma value at which the picture will be viewed.
		"""
		res = super(QPictureIO,self).gamma()
		isinstance(res,QtCore.float)
		return res
	#----------------------------------------------------------------------
	def init(self):
		"""

		"""
		res = super(QPictureIO,self).init()
		return res
	#----------------------------------------------------------------------
	def ioDevice(self):
		"""
		Returns the IO device currently set.
		"""
		res = super(QPictureIO,self).ioDevice()
		isinstance(res,QtCore.QIODevice)
		return res
	#----------------------------------------------------------------------
	def parameters(self):
		"""
		Returns the pictures parameters string.
		"""
		res = super(QPictureIO,self).parameters()
		return res
	#----------------------------------------------------------------------
	def picture(self):
		"""
		Returns the picture currently set.
		"""
		res = super(QPictureIO,self).picture()
		isinstance(res,QtGui.QPicture)
		return res
	#----------------------------------------------------------------------
	def quality(self):
		"""
		Returns the quality of the written picture, related to the compression ratio.
		"""
		res = super(QPictureIO,self).quality()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def read(self):
		"""
		Reads an picture into memory and returns true if the picture was successfully read; otherwise returns false.
		Before reading an picture you must set an IO device or a file name
		If both an IO device and a file name have been set, the IO device will be used.
		Setting the picture file format string is optional.
		Note that this function does not set the PySide.QtGui.QPictureIO.format() used to read the picture
		If you need that information, use the PySide.QtGui.QPictureIO.pictureFormat() static functions.
		Example:
		"""
		res = super(QPictureIO,self).read()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def status(self):
		"""
		Returns the pictures IO status
		A non-zero value indicates an error, whereas 0 means that the IO operation was successful.
		"""
		res = super(QPictureIO,self).status()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def write(self):
		"""
		Writes an picture to an IO device and returns true if the picture was successfully written; otherwise returns false.
		Before writing an picture you must set an IO device or a file name
		If both an IO device and a file name have been set, the IO device will be used.
		The picture will be written using the specified picture format.
		Example:
		"""
		res = super(QPictureIO,self).write()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setDescription(self,arg__1):
		"""
		setDescription(arg__1)
			arg__1=unicode

		Sets the picture description string for picture handlers that support picture descriptions to description .
		Currently, no picture format supported by Qt uses the description string.
		"""
		res = super(QPictureIO,self).setDescription(arg__1)
		return res
	#----------------------------------------------------------------------
	def setFileName(self,arg__1):
		"""
		setFileName(arg__1)
			arg__1=unicode

		Sets the name of the file to read or write an picture from to fileName .
		"""
		res = super(QPictureIO,self).setFileName(arg__1)
		return res
	#----------------------------------------------------------------------
	def setFormat(self,arg__1):
		"""
		setFormat(arg__1)
			arg__1=str

		Sets the picture format to format for the picture to be read or written.
		It is necessary to specify a format before writing an picture, but it is not necessary to specify a format before reading an picture.
		If no format has been set, Qt guesses the picture format before reading it
		If a format is set the picture will only be read if it has that format.
		"""
		res = super(QPictureIO,self).setFormat(arg__1)
		return res
	#----------------------------------------------------------------------
	def setGamma(self,arg__1):
		"""
		setGamma(arg__1)
			arg__1=QtCore.float

		Sets the gamma value at which the picture will be viewed to gamma
		If the picture format stores a gamma value for which the picture is intended to be used, then this setting will be used to modify the picture
		Setting to 0.0 will disable gamma correction (i.e
		any specification in the file will be ignored).
		The default value is 0.0.
		"""
		res = super(QPictureIO,self).setGamma(arg__1)
		return res
	#----------------------------------------------------------------------
	def setIODevice(self,arg__1):
		"""
		setIODevice(arg__1)
			arg__1=QtCore.QIODevice

		Sets the IO device to be used for reading or writing an picture.
		Setting the IO device allows pictures to be read/written to any block-oriented PySide.QtCore.QIODevice .
		If ioDevice is not null, this IO device will override file name settings.
		"""
		res = super(QPictureIO,self).setIODevice(arg__1)
		return res
	#----------------------------------------------------------------------
	def setParameters(self,arg__1):
		"""
		setParameters(arg__1)
			arg__1=str

		Sets the pictures parameter string to parameters
		This is for picture handlers that require special parameters.
		Although the current picture formats supported by Qt ignore the parameters string, it may be used in future extensions or by contributions (for example, JPEG).
		"""
		res = super(QPictureIO,self).setParameters(arg__1)
		return res
	#----------------------------------------------------------------------
	def setPicture(self,arg__1):
		"""
		setPicture(arg__1)
			arg__1=QtGui.QPicture

		Sets the picture to picture .
		"""
		res = super(QPictureIO,self).setPicture(arg__1)
		return res
	#----------------------------------------------------------------------
	def setQuality(self,arg__1):
		"""
		setQuality(arg__1)
			arg__1=QtCore.int

		Sets the quality of the written picture to q , related to the compression ratio.
		q must be in the range -1..100
		Specify 0 to obtain small compressed files, 100 for large uncompressed files
		(-1 signifies the default compression.)
		"""
		res = super(QPictureIO,self).setQuality(arg__1)
		return res
	#----------------------------------------------------------------------
	def setStatus(self,arg__1):
		"""
		setStatus(arg__1)
			arg__1=QtCore.int

		Sets the picture IO status to status
		A non-zero value indicates an error, whereas 0 means that the IO operation was successful.
		"""
		res = super(QPictureIO,self).setStatus(arg__1)
		return res

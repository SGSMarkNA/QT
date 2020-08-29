from PySide import QtGui, QtCore

class QMovie(QtGui.QMovie):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QMovie,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def backgroundColor(self):
		"""
		Returns the background color of the movie
		If no background color has been assigned, an invalid PySide.QtGui.QColor is returned.
		"""
		res = super(QMovie,self).backgroundColor()
		isinstance(res,QtGui.QColor)
		return res
	#----------------------------------------------------------------------
	def cacheMode(self):
		"""
		This property holds the movies cache mode.
		Caching frames can be useful when the underlying animation format handler that PySide.QtGui.QMovie relies on to decode the animation data does not support jumping to particular frames in the animation, or even rewinding the animation to the beginning (for looping)
		Furthermore, if the image data comes from a sequential device, it is not possible for the underlying animation handler to seek back to frames whose data has already been read (making looping altogether impossible).
		To aid in such situations, a PySide.QtGui.QMovie object can be instructed to cache the frames, at the added memory cost of keeping the frames in memory for the lifetime of the object.
		By default, this property is set to CacheNone .
		"""
		res = super(QMovie,self).cacheMode()
		isinstance(res,QtGui.QMovie.CacheMode)
		return res
	#----------------------------------------------------------------------
	def currentFrameNumber(self):
		"""
		Returns the sequence number of the current frame
		The number of the first frame in the movie is 0.
		"""
		res = super(QMovie,self).currentFrameNumber()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def currentImage(self):
		"""
		Returns the current frame as a PySide.QtGui.QImage .
		"""
		res = super(QMovie,self).currentImage()
		isinstance(res,QtGui.QImage)
		return res
	#----------------------------------------------------------------------
	def currentPixmap(self):
		"""
		Returns the current frame as a PySide.QtGui.QPixmap .
		"""
		res = super(QMovie,self).currentPixmap()
		isinstance(res,QtGui.QPixmap)
		return res
	#----------------------------------------------------------------------
	def device(self):
		"""
		Returns the device PySide.QtGui.QMovie reads image data from
		If no device has currently been assigned, 0 is returned.
		"""
		res = super(QMovie,self).device()
		isinstance(res,QtCore.QIODevice)
		return res
	#----------------------------------------------------------------------
	def fileName(self):
		"""
		Returns the name of the file that PySide.QtGui.QMovie reads image data from
		If no file name has been assigned, or if the assigned device is not a file, an empty PySide.QtCore.QString is returned.
		"""
		res = super(QMovie,self).fileName()
		return res
	#----------------------------------------------------------------------
	def finished(self):
		"""

		"""
		res = super(QMovie,self).finished()
		return res
	#----------------------------------------------------------------------
	def format(self):
		"""
		Returns the format that PySide.QtGui.QMovie uses when decoding image data
		If no format has been assigned, an empty QByteArray() is returned.
		"""
		res = super(QMovie,self).format()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def frameCount(self):
		"""
		Returns the number of frames in the movie.
		Certain animation formats do not support this feature, in which case 0 is returned.
		"""
		res = super(QMovie,self).frameCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def frameRect(self):
		"""
		Returns the rect of the last frame
		If no frame has yet been updated, an invalid PySide.QtCore.QRect is returned.
		"""
		res = super(QMovie,self).frameRect()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if the movie is valid (e.g., the image data is readable and the image format is supported); otherwise returns false.
		"""
		res = super(QMovie,self).isValid()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def loopCount(self):
		"""
		Returns the number of times the movie will loop before it finishes
		If the movie will only play once (no looping), loopCount returns 0
		If the movie loops forever, loopCount returns -1.
		Note that, if the image data comes from a sequential device (e.g
		a socket), PySide.QtGui.QMovie can only loop the movie if the PySide.QtGui.QMovie.cacheMode() is set to QMovie.CacheAll .
		"""
		res = super(QMovie,self).loopCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def nextFrameDelay(self):
		"""
		Returns the number of milliseconds PySide.QtGui.QMovie will wait before updating the next frame in the animation.
		"""
		res = super(QMovie,self).nextFrameDelay()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def scaledSize(self):
		"""
		Returns the scaled size of frames.
		"""
		res = super(QMovie,self).scaledSize()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def speed(self):
		"""
		This property holds the movies speed.
		The speed is measured in percentage of the original movie speed
		The default speed is 100%
		Example:
		"""
		res = super(QMovie,self).speed()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def started(self):
		"""

		"""
		res = super(QMovie,self).started()
		return res
	#----------------------------------------------------------------------
	def state(self):
		"""
		Returns the current state of PySide.QtGui.QMovie .
		"""
		res = super(QMovie,self).state()
		isinstance(res,QtGui.QMovie.MovieState)
		return res
	#----------------------------------------------------------------------
	def jumpToFrame(self,frameNumber):
		"""
		jumpToFrame(frameNumber)
			frameNumber=QtCore.int

		Jumps to frame number frameNumber
		Returns true on success; otherwise returns false.
		"""
		res = super(QMovie,self).jumpToFrame(frameNumber)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setBackgroundColor(self,color):
		"""
		setBackgroundColor(color)
			color=QtGui.QColor

		For image formats that support it, this function sets the background color to color .
		"""
		res = super(QMovie,self).setBackgroundColor(color)
		return res
	#----------------------------------------------------------------------
	def setCacheMode(self,mode):
		"""
		setCacheMode(mode)
			mode=QtGui.QMovie.CacheMode

		This property holds the movies cache mode.
		Caching frames can be useful when the underlying animation format handler that PySide.QtGui.QMovie relies on to decode the animation data does not support jumping to particular frames in the animation, or even rewinding the animation to the beginning (for looping)
		Furthermore, if the image data comes from a sequential device, it is not possible for the underlying animation handler to seek back to frames whose data has already been read (making looping altogether impossible).
		To aid in such situations, a PySide.QtGui.QMovie object can be instructed to cache the frames, at the added memory cost of keeping the frames in memory for the lifetime of the object.
		By default, this property is set to CacheNone .
		"""
		res = super(QMovie,self).setCacheMode(mode)
		return res
	#----------------------------------------------------------------------
	def setDevice(self,device):
		"""
		setDevice(device)
			device=QtCore.QIODevice

		Sets the current device to device
		PySide.QtGui.QMovie will read image data from this device when the movie is running.
		"""
		res = super(QMovie,self).setDevice(device)
		return res
	#----------------------------------------------------------------------
	def setFileName(self,fileName):
		"""
		setFileName(fileName)
			fileName=unicode

		Sets the name of the file that PySide.QtGui.QMovie reads image data from, to fileName .
		"""
		res = super(QMovie,self).setFileName(fileName)
		return res
	#----------------------------------------------------------------------
	def setFormat(self,format):
		"""
		setFormat(format)
			format=QtCore.QByteArray

		Sets the format that PySide.QtGui.QMovie will use when decoding image data, to format
		By default, PySide.QtGui.QMovie will attempt to guess the format of the image data.
		You can call PySide.QtGui.QMovie.supportedFormats() for the full list of formats PySide.QtGui.QMovie supports.
		"""
		res = super(QMovie,self).setFormat(format)
		return res
	#----------------------------------------------------------------------
	def setScaledSize(self,size):
		"""
		setScaledSize(size)
			size=QtCore.QSize

		Sets the scaled frame size to size .
		"""
		res = super(QMovie,self).setScaledSize(size)
		return res

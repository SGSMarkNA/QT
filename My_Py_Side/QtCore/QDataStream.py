from PySide import QtGui, QtCore

class QDataStream(QtCore.QDataStream):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDataStream,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def atEnd(self):
		"""
		Returns true if the I/O device has reached the end position (end of the stream or file) or if there is no I/O device set; otherwise returns false.
		"""
		res = super(QDataStream,self).atEnd()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def byteOrder(self):
		"""
		Returns the current byte order setting  either BigEndian or LittleEndian .
		"""
		res = super(QDataStream,self).byteOrder()
		isinstance(res,QtCore.QDataStream.ByteOrder)
		return res
	#----------------------------------------------------------------------
	def device(self):
		"""
		Returns the I/O device currently set, or 0 if no device is currently set.
		"""
		res = super(QDataStream,self).device()
		isinstance(res,QtCore.QIODevice)
		return res
	#----------------------------------------------------------------------
	def floatingPointPrecision(self):
		"""
		Returns the floating point precision of the data stream.
		"""
		res = super(QDataStream,self).floatingPointPrecision()
		isinstance(res,QtCore.QDataStream.FloatingPointPrecision)
		return res
	#----------------------------------------------------------------------
	def readBool(self):
		"""

		"""
		res = super(QDataStream,self).readBool()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def readDouble(self):
		"""

		"""
		res = super(QDataStream,self).readDouble()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def readFloat(self):
		"""

		"""
		res = super(QDataStream,self).readFloat()
		isinstance(res,QtCore.float)
		return res
	#----------------------------------------------------------------------
	def readInt16(self):
		"""

		"""
		res = super(QDataStream,self).readInt16()
		isinstance(res,QtCore.qint16)
		return res
	#----------------------------------------------------------------------
	def readInt32(self):
		"""

		"""
		res = super(QDataStream,self).readInt32()
		isinstance(res,QtCore.qint32)
		return res
	#----------------------------------------------------------------------
	def readInt64(self):
		"""

		"""
		res = super(QDataStream,self).readInt64()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def readInt8(self):
		"""

		"""
		res = super(QDataStream,self).readInt8()
		isinstance(res,QtCore.qint8)
		return res
	#----------------------------------------------------------------------
	def readQChar(self):
		"""

		"""
		res = super(QDataStream,self).readQChar()
		isinstance(res,QtCore.QChar)
		return res
	#----------------------------------------------------------------------
	def readQString(self):
		"""

		"""
		res = super(QDataStream,self).readQString()
		return res
	#----------------------------------------------------------------------
	def readQStringList(self):
		"""

		"""
		res = super(QDataStream,self).readQStringList()
		return res
	#----------------------------------------------------------------------
	def readQVariant(self):
		"""

		"""
		res = super(QDataStream,self).readQVariant()
		return res
	#----------------------------------------------------------------------
	def readString(self):
		"""

		"""
		res = super(QDataStream,self).readString()
		return res
	#----------------------------------------------------------------------
	def readUInt16(self):
		"""

		"""
		res = super(QDataStream,self).readUInt16()
		isinstance(res,QtCore.quint16)
		return res
	#----------------------------------------------------------------------
	def readUInt32(self):
		"""

		"""
		res = super(QDataStream,self).readUInt32()
		isinstance(res,QtCore.quint32)
		return res
	#----------------------------------------------------------------------
	def readUInt64(self):
		"""

		"""
		res = super(QDataStream,self).readUInt64()
		isinstance(res,QtCore.quint64)
		return res
	#----------------------------------------------------------------------
	def readUInt8(self):
		"""

		"""
		res = super(QDataStream,self).readUInt8()
		isinstance(res,QtCore.quint8)
		return res
	#----------------------------------------------------------------------
	def resetStatus(self):
		"""
		Resets the status of the data stream.
		"""
		res = super(QDataStream,self).resetStatus()
		return res
	#----------------------------------------------------------------------
	def status(self):
		"""
		Returns the status of the data stream.
		"""
		res = super(QDataStream,self).status()
		isinstance(res,QtCore.QDataStream.Status)
		return res
	#----------------------------------------------------------------------
	def unsetDevice(self):
		"""
		Unsets the I/O device
		Use setDevice(0) instead.
		"""
		res = super(QDataStream,self).unsetDevice()
		return res
	#----------------------------------------------------------------------
	def version(self):
		"""
		Returns the version number of the data serialization format.
		"""
		res = super(QDataStream,self).version()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def __lshift__(self,*args,**kwargs):
		"""
		__lshift__(item)
			item=QtGui.QTableWidgetItem

		__lshift__(arg__2)
			arg__2=QtGui.QTextFormat

		__lshift__(item)
			item=QtGui.QStandardItem

		__lshift__(arg__2)
			arg__2=QtGui.QTextLength

		__lshift__(item)
			item=QtGui.QTreeWidgetItem

		__lshift__(arg__2)
			arg__2=QtCore.QUrl

		__lshift__(arg__2)
			arg__2=QtGui.QTransform

		__lshift__(arg__2)
			arg__2=QtScript.QScriptContextInfo

		__lshift__(arg__2)
			arg__2=QtCore.QRectF

		__lshift__(regExp)
			regExp=QtCore.QRegExp

		__lshift__(arg__2)
			arg__2=QtGui.QSizePolicy

		__lshift__(arg__2)
			arg__2=QtGui.QRegion

		__lshift__(arg__2)
			arg__2=QtCore.QSize

		__lshift__(arg__2)
			arg__2=QtCore.QSizeF

		__lshift__(arg__2)
			arg__2=QtCore.QUuid

		__lshift__(history)
			history=QtWebKit.QWebHistory

		__lshift__(arg__2)
			arg__2=QtGui.QVector2D

		__lshift__(arg__2)
			arg__2=QtGui.QVector3D

		__lshift__(arg__2)
			arg__2=QtGui.QVector4D

		__lshift__(arg__2)
			arg__2=QtCore.QRect

		__lshift__(arg__2)
			arg__2=QtCore.QTime

		__lshift__(arg__2)
			arg__2=QtCore.QEasingCurve

		__lshift__(arg__2)
			arg__2=QtGui.QFont

		__lshift__(arg__2)
			arg__2=QtCore.QLine

		__lshift__(arg__2)
			arg__2=QtNetwork.QHostAddress

		__lshift__(arg__2)
			arg__2=QtGui.QImage

		__lshift__(ks)
			ks=QtGui.QKeySequence

		__lshift__(arg__2)
			arg__2=QtGui.QIcon

		__lshift__(arg__2)
			arg__2=QtCore.QDateTime

		__lshift__(arg__2)
			arg__2=QtCore.QBitArray

		__lshift__(arg__2)
			arg__2=QtCore.QDate

		__lshift__(arg__2)
			arg__2=QtGui.QBrush

		__lshift__(arg__2)
			arg__2=QtGui.QColor

		__lshift__(cursor)
			cursor=QtGui.QCursor

		__lshift__(arg__2)
			arg__2=QtCore.QByteArray

		__lshift__(arg__2)
			arg__2=QtGui.QQuaternion

		__lshift__(arg__2)
			arg__2=QtGui.QPicture

		__lshift__(arg__2)
			arg__2=QtGui.QPixmap

		__lshift__(arg__2)
			arg__2=QtGui.QPen

		__lshift__(arg__2)
			arg__2=QtCore.QPoint

		__lshift__(polygon)
			polygon=QtGui.QPolygon

		__lshift__(array)
			array=QtGui.QPolygonF

		__lshift__(arg__2)
			arg__2=QtCore.QPointF

		__lshift__(arg__2)
			arg__2=QtCore.QLineF

		__lshift__(item)
			item=QtGui.QListWidgetItem

		__lshift__(arg__2)
			arg__2=QtCore.QLocale

		__lshift__(arg__2)
			arg__2=QtGui.QMatrix

		__lshift__(p)
			p=QtGui.QPalette

		__lshift__(arg__2)
			arg__2=QtGui.QMatrix4x4

		__lshift__(arg__2)
			arg__2=QtNetwork.QNetworkCacheMetaData

		__lshift__(arg__2)
			arg__2=QtGui.QPainterPath


		"""
		res = super(QDataStream,self).__lshift__(*args,**kwargs)
		isinstance(res,QtCore.QDataStream)
		return res
	#----------------------------------------------------------------------
	def __rshift__(self,*args,**kwargs):
		"""
		__rshift__(arg__2)
			arg__2=QtGui.QTextLength

		__rshift__(arg__2)
			arg__2=QtCore.QTime

		__rshift__(arg__2)
			arg__2=QtGui.QTransform

		__rshift__(arg__2)
			arg__2=QtCore.QUrl

		__rshift__(arg__2)
			arg__2=QtGui.QTextFormat

		__rshift__(arg__2)
			arg__2=QtCore.QUuid

		__rshift__(item)
			item=QtGui.QTreeWidgetItem

		__rshift__(item)
			item=QtGui.QStandardItem

		__rshift__(arg__2)
			arg__2=QtGui.QRegion

		__rshift__(arg__2)
			arg__2=QtScript.QScriptContextInfo

		__rshift__(item)
			item=QtGui.QTableWidgetItem

		__rshift__(arg__2)
			arg__2=QtCore.QSize

		__rshift__(arg__2)
			arg__2=QtGui.QSizePolicy

		__rshift__(arg__2)
			arg__2=QtGui.QVector2D

		__rshift__(arg__2)
			arg__2=QtCore.QSizeF

		__rshift__(arg__2)
			arg__2=QtGui.QVector4D

		__rshift__(arg__2)
			arg__2=QtGui.QVector3D

		__rshift__(regExp)
			regExp=QtCore.QRegExp

		__rshift__(history)
			history=QtWebKit.QWebHistory

		__rshift__(arg__2)
			arg__2=QtGui.QMatrix4x4

		__rshift__(arg__2)
			arg__2=QtGui.QFont

		__rshift__(arg__2)
			arg__2=QtNetwork.QHostAddress

		__rshift__(arg__2)
			arg__2=QtCore.QLineF

		__rshift__(arg__2)
			arg__2=QtGui.QIcon

		__rshift__(ks)
			ks=QtGui.QKeySequence

		__rshift__(arg__2)
			arg__2=QtCore.QLine

		__rshift__(arg__2)
			arg__2=QtGui.QImage

		__rshift__(arg__2)
			arg__2=QtCore.QEasingCurve

		__rshift__(arg__2)
			arg__2=QtCore.QBitArray

		__rshift__(arg__2)
			arg__2=QtGui.QBrush

		__rshift__(arg__2)
			arg__2=QtCore.QDateTime

		__rshift__(arg__2)
			arg__2=QtCore.QByteArray

		__rshift__(cursor)
			cursor=QtGui.QCursor

		__rshift__(arg__2)
			arg__2=QtCore.QDate

		__rshift__(arg__2)
			arg__2=QtGui.QColor

		__rshift__(arg__2)
			arg__2=QtCore.QRectF

		__rshift__(arg__2)
			arg__2=QtCore.QPoint

		__rshift__(arg__2)
			arg__2=QtCore.QPointF

		__rshift__(arg__2)
			arg__2=QtGui.QPixmap

		__rshift__(polygon)
			polygon=QtGui.QPolygon

		__rshift__(arg__2)
			arg__2=QtGui.QQuaternion

		__rshift__(arg__2)
			arg__2=QtCore.QRect

		__rshift__(array)
			array=QtGui.QPolygonF

		__rshift__(item)
			item=QtGui.QListWidgetItem

		__rshift__(arg__2)
			arg__2=QtCore.QLocale

		__rshift__(arg__2)
			arg__2=QtGui.QMatrix

		__rshift__(arg__2)
			arg__2=QtNetwork.QNetworkCacheMetaData

		__rshift__(arg__2)
			arg__2=QtGui.QPicture

		__rshift__(arg__2)
			arg__2=QtGui.QPainterPath

		__rshift__(p)
			p=QtGui.QPalette

		__rshift__(arg__2)
			arg__2=QtGui.QPen


		"""
		res = super(QDataStream,self).__rshift__(*args,**kwargs)
		isinstance(res,QtCore.QDataStream)
		return res
	#----------------------------------------------------------------------
	def readRawData(self,len):
		"""
		readRawData(len)
			len=QtCore.int

		Reads at most len bytes from the stream into s and returns the number of bytes read
		If an error occurs, this function returns -1.
		The buffer s must be preallocated
		The data is not encoded.
		"""
		res = super(QDataStream,self).readRawData(len)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def setByteOrder(self,arg__1):
		"""
		setByteOrder(arg__1)
			arg__1=QtCore.QDataStream.ByteOrder

		Sets the serialization byte order to bo .
		The bo parameter can be QDataStream.BigEndian or QDataStream.LittleEndian .
		The default setting is big endian
		We recommend leaving this setting unless you have special requirements.
		"""
		res = super(QDataStream,self).setByteOrder(arg__1)
		return res
	#----------------------------------------------------------------------
	def setDevice(self,arg__1):
		"""
		setDevice(arg__1)
			arg__1=QtCore.QIODevice

		void QDataStream::setDevice( PySide.QtCore.QIODevice *d)
		Sets the I/O device to d , which can be 0 to unset to current I/O device.
		"""
		res = super(QDataStream,self).setDevice(arg__1)
		return res
	#----------------------------------------------------------------------
	def setFloatingPointPrecision(self,precision):
		"""
		setFloatingPointPrecision(precision)
			precision=QtCore.QDataStream.FloatingPointPrecision

		Sets the floating point precision of the data stream to precision
		If the floating point precision is DoublePrecision and the version of the data stream is Qt_4_6 or higher, all floating point numbers will be written and read with 64-bit precision
		If the floating point precision is SinglePrecision and the version is Qt_4_6 or higher, all floating point numbers will be written and read with 32-bit precision.
		For versions prior to Qt_4_6 , the precision of floating point numbers in the data stream depends on the stream operator called.
		The default is DoublePrecision .
		"""
		res = super(QDataStream,self).setFloatingPointPrecision(precision)
		return res
	#----------------------------------------------------------------------
	def setStatus(self,status):
		"""
		setStatus(status)
			status=QtCore.QDataStream.Status

		Sets the status of the data stream to the status given.
		"""
		res = super(QDataStream,self).setStatus(status)
		return res
	#----------------------------------------------------------------------
	def setVersion(self,arg__1):
		"""
		setVersion(arg__1)
			arg__1=QtCore.int

		Sets the version number of the data serialization format to v .
		You dont have to set a version if you are using the current version of Qt, but for your own custom binary formats we recommend that you do; see Versioning in the Detailed Description.
		To accommodate new functionality, the datastream serialization format of some Qt classes has changed in some versions of Qt
		If you want to read data that was created by an earlier version of Qt, or write data that can be read by a program that was compiled with an earlier version of Qt, use this function to modify the serialization format used by PySide.QtCore.QDataStream .
		The QDataStream.Version enum provides symbolic constants for the different versions of Qt
		For example:
		"""
		res = super(QDataStream,self).setVersion(arg__1)
		return res
	#----------------------------------------------------------------------
	def skipRawData(self,len):
		"""
		skipRawData(len)
			len=QtCore.int

		Skips len bytes from the device
		Returns the number of bytes actually skipped, or -1 on error.
		This is equivalent to calling PySide.QtCore.QDataStream.readRawData() on a buffer of length len and ignoring the buffer.
		"""
		res = super(QDataStream,self).skipRawData(len)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def writeBool(self,arg__1):
		"""
		writeBool(arg__1)
			arg__1=QtCore.bool


		"""
		res = super(QDataStream,self).writeBool(arg__1)
		return res
	#----------------------------------------------------------------------
	def writeDouble(self,arg__1):
		"""
		writeDouble(arg__1)
			arg__1=QtCore.qreal


		"""
		res = super(QDataStream,self).writeDouble(arg__1)
		return res
	#----------------------------------------------------------------------
	def writeFloat(self,arg__1):
		"""
		writeFloat(arg__1)
			arg__1=QtCore.float


		"""
		res = super(QDataStream,self).writeFloat(arg__1)
		return res
	#----------------------------------------------------------------------
	def writeInt16(self,arg__1):
		"""
		writeInt16(arg__1)
			arg__1=QtCore.qint16


		"""
		res = super(QDataStream,self).writeInt16(arg__1)
		return res
	#----------------------------------------------------------------------
	def writeInt32(self,arg__1):
		"""
		writeInt32(arg__1)
			arg__1=QtCore.qint32


		"""
		res = super(QDataStream,self).writeInt32(arg__1)
		return res
	#----------------------------------------------------------------------
	def writeInt64(self,arg__1):
		"""
		writeInt64(arg__1)
			arg__1=QtCore.qint64


		"""
		res = super(QDataStream,self).writeInt64(arg__1)
		return res
	#----------------------------------------------------------------------
	def writeInt8(self,arg__1):
		"""
		writeInt8(arg__1)
			arg__1=QtCore.qint8


		"""
		res = super(QDataStream,self).writeInt8(arg__1)
		return res
	#----------------------------------------------------------------------
	def writeQChar(self,arg__1):
		"""
		writeQChar(arg__1)
			arg__1=QtCore.QChar


		"""
		res = super(QDataStream,self).writeQChar(arg__1)
		return res
	#----------------------------------------------------------------------
	def writeQString(self,arg__1):
		"""
		writeQString(arg__1)
			arg__1=unicode


		"""
		res = super(QDataStream,self).writeQString(arg__1)
		return res
	#----------------------------------------------------------------------
	def writeQStringList(self,arg__1):
		"""
		writeQStringList(arg__1)
			arg__1=list


		"""
		res = super(QDataStream,self).writeQStringList(arg__1)
		return res
	#----------------------------------------------------------------------
	def writeQVariant(self,arg__1):
		"""
		writeQVariant(arg__1)
			arg__1=object


		"""
		res = super(QDataStream,self).writeQVariant(arg__1)
		return res
	#----------------------------------------------------------------------
	def writeRawData(self,arg__1):
		"""
		writeRawData(arg__1)
			arg__1=str

		Writes len bytes from s to the stream
		Returns the number of bytes actually written, or -1 on error
		The data is not encoded.
		"""
		res = super(QDataStream,self).writeRawData(arg__1)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def writeString(self,arg__1):
		"""
		writeString(arg__1)
			arg__1=unicode


		"""
		res = super(QDataStream,self).writeString(arg__1)
		return res
	#----------------------------------------------------------------------
	def writeUInt16(self,arg__1):
		"""
		writeUInt16(arg__1)
			arg__1=QtCore.quint16


		"""
		res = super(QDataStream,self).writeUInt16(arg__1)
		return res
	#----------------------------------------------------------------------
	def writeUInt32(self,arg__1):
		"""
		writeUInt32(arg__1)
			arg__1=QtCore.quint32


		"""
		res = super(QDataStream,self).writeUInt32(arg__1)
		return res
	#----------------------------------------------------------------------
	def writeUInt64(self,arg__1):
		"""
		writeUInt64(arg__1)
			arg__1=QtCore.quint64


		"""
		res = super(QDataStream,self).writeUInt64(arg__1)
		return res
	#----------------------------------------------------------------------
	def writeUInt8(self,arg__1):
		"""
		writeUInt8(arg__1)
			arg__1=QtCore.quint8


		"""
		res = super(QDataStream,self).writeUInt8(arg__1)
		return res

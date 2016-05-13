from PySide import QtGui, QtCore

class QIODevice(QtCore.QIODevice):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QIODevice,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def aboutToClose(self):
		"""

		"""
		res = super(QIODevice,self).aboutToClose()
		return res
	#----------------------------------------------------------------------
	def atEnd(self):
		"""
		Returns true if the current read and write position is at the end of the device (i.e
		there is no more data available for reading on the device); otherwise returns false.
		For some devices, PySide.QtCore.QIODevice.atEnd() can return true even though there is more data to read
		This special case only applies to devices that generate data in direct response to you calling PySide.QtCore.QIODevice.read() (e.g., /dev or /proc files on Unix and Mac OS X, or console input / stdin on all platforms).
		"""
		res = super(QIODevice,self).atEnd()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def bytesAvailable(self):
		"""
		Returns the number of bytes that are available for reading
		This function is commonly used with sequential devices to determine the number of bytes to allocate in a buffer before reading.
		Subclasses that reimplement this function must call the base implementation in order to include the size of QIODevices buffer
		Example:
		"""
		res = super(QIODevice,self).bytesAvailable()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def bytesToWrite(self):
		"""
		For buffered devices, this function returns the number of bytes waiting to be written
		For devices with no buffer, this function returns 0.
		"""
		res = super(QIODevice,self).bytesToWrite()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def canReadLine(self):
		"""
		Returns true if a complete line of data can be read from the device; otherwise returns false.
		Note that unbuffered devices, which have no way of determining what can be read, always return false.
		This function is often called in conjunction with the PySide.QtCore.QIODevice.readyRead() signal.
		Subclasses that reimplement this function must call the base implementation in order to include the contents of the PySide.QtCore.QIODevice s buffer
		Example:
		"""
		res = super(QIODevice,self).canReadLine()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def close(self):
		"""
		First emits PySide.QtCore.QIODevice.aboutToClose() , then closes the device and sets its OpenMode to NotOpen
		The error string is also reset.
		"""
		res = super(QIODevice,self).close()
		return res
	#----------------------------------------------------------------------
	def errorString(self):
		"""
		Returns a human-readable description of the last device error that occurred.
		"""
		res = super(QIODevice,self).errorString()
		return res
	#----------------------------------------------------------------------
	def getChar(self):
		"""
		Reads one character from the device and stores it in c
		If c is 0, the character is discarded
		Returns true on success; otherwise returns false.
		"""
		res = super(QIODevice,self).getChar()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isOpen(self):
		"""
		Returns true if the device is open; otherwise returns false
		A device is open if it can be read from and/or written to
		By default, this function returns false if PySide.QtCore.QIODevice.openMode() returns NotOpen .
		"""
		res = super(QIODevice,self).isOpen()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isReadable(self):
		"""
		Returns true if data can be read from the device; otherwise returns false
		Use PySide.QtCore.QIODevice.bytesAvailable() to determine how many bytes can be read.
		This is a convenience function which checks if the OpenMode of the device contains the ReadOnly flag.
		"""
		res = super(QIODevice,self).isReadable()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isSequential(self):
		"""
		Returns true if this device is sequential; otherwise returns false.
		Sequential devices, as opposed to a random-access devices, have no concept of a start, an end, a size, or a current position, and they do not support seeking
		You can only read from the device when it reports that data is available
		The most common example of a sequential device is a network socket
		On Unix, special files such as /dev/zero and fifo pipes are sequential.
		Regular files, on the other hand, do support random access
		They have both a size and a current position, and they also support seeking backwards and forwards in the data stream
		Regular files are non-sequential.
		"""
		res = super(QIODevice,self).isSequential()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isTextModeEnabled(self):
		"""
		Returns true if the Text flag is enabled; otherwise returns false.
		"""
		res = super(QIODevice,self).isTextModeEnabled()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isWritable(self):
		"""
		Returns true if data can be written to the device; otherwise returns false.
		This is a convenience function which checks if the OpenMode of the device contains the WriteOnly flag.
		"""
		res = super(QIODevice,self).isWritable()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def openMode(self):
		"""
		Returns the mode in which the device has been opened; i.e
		ReadOnly or WriteOnly .
		"""
		res = super(QIODevice,self).openMode()
		isinstance(res,QtCore.QIODevice.OpenMode)
		return res
	#----------------------------------------------------------------------
	def pos(self):
		"""
		For random-access devices, this function returns the position that data is written to or read from
		For sequential devices or closed devices, where there is no concept of a current position, 0 is returned.
		The current read/write position of the device is maintained internally by PySide.QtCore.QIODevice , so reimplementing this function is not necessary
		When subclassing PySide.QtCore.QIODevice , use QIODevice.seek() to notify PySide.QtCore.QIODevice about changes in the device position.
		"""
		res = super(QIODevice,self).pos()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def readAll(self):
		"""
		This is an overloaded function.
		Reads all available data from the device, and returns it as a PySide.QtCore.QByteArray .
		This function has no way of reporting errors; returning an empty QByteArray() can mean either that no data was currently available for reading, or that an error occurred.
		"""
		res = super(QIODevice,self).readAll()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def readChannelFinished(self):
		"""

		"""
		res = super(QIODevice,self).readChannelFinished()
		return res
	#----------------------------------------------------------------------
	def readyRead(self):
		"""

		"""
		res = super(QIODevice,self).readyRead()
		return res
	#----------------------------------------------------------------------
	def reset(self):
		"""
		Seeks to the start of input for random-access devices
		Returns true on success; otherwise returns false (for example, if the device is not open).
		Note that when using a PySide.QtCore.QTextStream on a PySide.QtCore.QFile , calling PySide.QtCore.QIODevice.reset() on the PySide.QtCore.QFile will not have the expected result because PySide.QtCore.QTextStream buffers the file
		Use the QTextStream.seek() function instead.
		"""
		res = super(QIODevice,self).reset()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""
		For open random-access devices, this function returns the size of the device
		For open sequential devices, PySide.QtCore.QIODevice.bytesAvailable() is returned.
		If the device is closed, the size returned will not reflect the actual size of the device.
		"""
		res = super(QIODevice,self).size()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def open(self,mode):
		"""
		open(mode)
			mode=QtCore.QIODevice.OpenMode


		"""
		res = super(QIODevice,self).open(mode)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def peek(self,maxlen):
		"""
		peek(maxlen)
			maxlen=QtCore.qint64

		This is an overloaded function.
		Peeks at most maxSize bytes from the device, returning the data peeked as a PySide.QtCore.QByteArray .
		Example:
		This function has no way of reporting errors; returning an empty QByteArray() can mean either that no data was currently available for peeking, or that an error occurred.
		"""
		res = super(QIODevice,self).peek(maxlen)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def putChar(self,c):
		"""
		putChar(c)
			c=QtCore.char

		Writes the character c to the device
		Returns true on success; otherwise returns false.
		"""
		res = super(QIODevice,self).putChar(c)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def read(self,maxlen):
		"""
		read(maxlen)
			maxlen=QtCore.qint64

		This is an overloaded function.
		Reads at most maxSize bytes from the device, and returns the data read as a PySide.QtCore.QByteArray .
		This function has no way of reporting errors; returning an empty QByteArray() can mean either that no data was currently available for reading, or that an error occurred.
		"""
		res = super(QIODevice,self).read(maxlen)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def readData(self,maxlen):
		"""
		readData(maxlen)
			maxlen=QtCore.qint64

		Reads up to maxSize bytes from the device into data , and returns the number of bytes read or -1 if an error occurred
		If there are no bytes to be read, this function should return -1 if there can never be more bytes available (for example: socket closed, pipe closed, sub-process finished).
		This function is called by PySide.QtCore.QIODevice
		Reimplement this function when creating a subclass of PySide.QtCore.QIODevice .
		"""
		res = super(QIODevice,self).readData(maxlen)
		return res
	#----------------------------------------------------------------------
	def readLine(self,maxlen=None):
		"""
		readLine(maxlen=None)
			maxlen=QtCore.qint64

		This is an overloaded function.
		Reads a line from the device, but no more than maxSize characters, and returns the result as a PySide.QtCore.QByteArray .
		This function has no way of reporting errors; returning an empty QByteArray() can mean either that no data was currently available for reading, or that an error occurred.
		"""
		res = super(QIODevice,self).readLine(maxlen)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def readLineData(self,maxlen):
		"""
		readLineData(maxlen)
			maxlen=QtCore.qint64

		Reads up to maxSize characters into data and returns the number of characters read.
		This function is called by PySide.QtCore.QIODevice.readLine() , and provides its base implementation, using PySide.QtCore.QIODevice.getChar()
		Buffered devices can improve the performance of PySide.QtCore.QIODevice.readLine() by reimplementing this function.
		PySide.QtCore.QIODevice.readLine() appends a 0 byte to data ; PySide.QtCore.QIODevice.readLineData() does not need to do this.
		If you reimplement this function, be careful to return the correct value: it should return the number of bytes read in this line, including the terminating newline, or 0 if there is no line to be read at this point
		If an error occurs, it should return -1 if and only if no bytes were read
		Reading past EOF is considered an error.
		"""
		res = super(QIODevice,self).readLineData(maxlen)
		return res
	#----------------------------------------------------------------------
	def seek(self,pos):
		"""
		seek(pos)
			pos=QtCore.qint64

		For random-access devices, this function sets the current position to pos , returning true on success, or false if an error occurred
		For sequential devices, the default behavior is to do nothing and return false.
		When subclassing PySide.QtCore.QIODevice , you must call QIODevice.seek() at the start of your function to ensure integrity with PySide.QtCore.QIODevice s built-in buffer
		The base implementation always returns true.
		"""
		res = super(QIODevice,self).seek(pos)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def setErrorString(self,errorString):
		"""
		setErrorString(errorString)
			errorString=unicode

		Sets the human readable description of the last device error that occurred to str .
		"""
		res = super(QIODevice,self).setErrorString(errorString)
		return res
	#----------------------------------------------------------------------
	def setOpenMode(self,openMode):
		"""
		setOpenMode(openMode)
			openMode=QtCore.QIODevice.OpenMode


		"""
		res = super(QIODevice,self).setOpenMode(openMode)
		return res
	#----------------------------------------------------------------------
	def setTextModeEnabled(self,enabled):
		"""
		setTextModeEnabled(enabled)
			enabled=QtCore.bool

		If enabled is true, this function sets the Text flag on the device; otherwise the Text flag is removed
		This feature is useful for classes that provide custom end-of-line handling on a PySide.QtCore.QIODevice .
		"""
		res = super(QIODevice,self).setTextModeEnabled(enabled)
		return res
	#----------------------------------------------------------------------
	def ungetChar(self,c):
		"""
		ungetChar(c)
			c=QtCore.char

		Puts the character c back into the device, and decrements the current position unless the position is 0
		This function is usually called to undo a PySide.QtCore.QIODevice.getChar() operation, such as when writing a backtracking parser.
		If c was not previously read from the device, the behavior is undefined.
		"""
		res = super(QIODevice,self).ungetChar(c)
		return res
	#----------------------------------------------------------------------
	def waitForBytesWritten(self,msecs):
		"""
		waitForBytesWritten(msecs)
			msecs=QtCore.int

		For buffered devices, this function waits until a payload of buffered written data has been written to the device and the PySide.QtCore.QIODevice.bytesWritten() signal has been emitted, or until msecs milliseconds have passed
		If msecs is -1, this function will not time out
		For unbuffered devices, it returns immediately.
		Returns true if a payload of data was written to the device; otherwise returns false (i.e
		if the operation timed out, or if an error occurred).
		This function can operate without an event loop
		It is useful when writing non-GUI applications and when performing I/O operations in a non-GUI thread.
		If called from within a slot connected to the PySide.QtCore.QIODevice.bytesWritten() signal, PySide.QtCore.QIODevice.bytesWritten() will not be reemitted.
		Reimplement this function to provide a blocking API for a custom device
		The default implementation does nothing, and returns false.
		"""
		res = super(QIODevice,self).waitForBytesWritten(msecs)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def waitForReadyRead(self,msecs):
		"""
		waitForReadyRead(msecs)
			msecs=QtCore.int

		Blocks until new data is available for reading and the PySide.QtCore.QIODevice.readyRead() signal has been emitted, or until msecs milliseconds have passed
		If msecs is -1, this function will not time out.
		Returns true if new data is available for reading; otherwise returns false (if the operation timed out or if an error occurred).
		This function can operate without an event loop
		It is useful when writing non-GUI applications and when performing I/O operations in a non-GUI thread.
		If called from within a slot connected to the PySide.QtCore.QIODevice.readyRead() signal, PySide.QtCore.QIODevice.readyRead() will not be reemitted.
		Reimplement this function to provide a blocking API for a custom device
		The default implementation does nothing, and returns false.
		"""
		res = super(QIODevice,self).waitForReadyRead(msecs)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def write(self,*args,**kwargs):
		"""
		write(data)
			data=str

		write(data)
			data=QtCore.QByteArray

		This is an overloaded function.
		Writes data from a zero-terminated string of 8-bit characters to the device
		Returns the number of bytes that were actually written, or -1 if an error occurred
		This is equivalent to
		"""
		res = super(QIODevice,self).write(*args,**kwargs)
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def writeData(self,data,len):
		"""
		writeData(data,len)
			data=str
			len=QtCore.qint64

		Writes up to maxSize bytes from data to the device
		Returns the number of bytes written, or -1 if an error occurred.
		This function is called by PySide.QtCore.QIODevice
		Reimplement this function when creating a subclass of PySide.QtCore.QIODevice .
		"""
		res = super(QIODevice,self).writeData(data,len)
		isinstance(res,QtCore.qint64)
		return res

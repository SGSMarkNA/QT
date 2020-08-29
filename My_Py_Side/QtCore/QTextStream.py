from PySide import QtGui, QtCore

class QTextStream(QtCore.QTextStream):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextStream,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def atEnd(self):
		"""
		Returns true if there is no more data to be read from the PySide.QtCore.QTextStream ; otherwise returns false
		This is similar to, but not the same as calling QIODevice.atEnd() , as PySide.QtCore.QTextStream also takes into account its internal Unicode buffer.
		"""
		res = super(QTextStream,self).atEnd()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def autoDetectUnicode(self):
		"""
		Returns true if automatic Unicode detection is enabled, otherwise returns false
		Automatic Unicode detection is enabled by default.
		"""
		res = super(QTextStream,self).autoDetectUnicode()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def codec(self):
		"""
		Returns the codec that is current assigned to the stream.
		"""
		res = super(QTextStream,self).codec()
		isinstance(res,QtCore.QTextCodec)
		return res
	#----------------------------------------------------------------------
	def device(self):
		"""
		Returns the current device associated with the PySide.QtCore.QTextStream , or 0 if no device has been assigned.
		"""
		res = super(QTextStream,self).device()
		isinstance(res,QtCore.QIODevice)
		return res
	#----------------------------------------------------------------------
	def fieldAlignment(self):
		"""
		Returns the current field alignment.
		"""
		res = super(QTextStream,self).fieldAlignment()
		isinstance(res,QtCore.QTextStream.FieldAlignment)
		return res
	#----------------------------------------------------------------------
	def fieldWidth(self):
		"""
		Returns the current field width.
		"""
		res = super(QTextStream,self).fieldWidth()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def flush(self):
		"""
		Flushes any buffered data waiting to be written to the device.
		If PySide.QtCore.QTextStream operates on a string, this function does nothing.
		"""
		res = super(QTextStream,self).flush()
		return res
	#----------------------------------------------------------------------
	def generateByteOrderMark(self):
		"""
		Returns true if PySide.QtCore.QTextStream is set to generate the UTF BOM (Byte Order Mark) when using a UTF codec; otherwise returns false
		UTF BOM generation is set to false by default.
		"""
		res = super(QTextStream,self).generateByteOrderMark()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def integerBase(self):
		"""
		Returns the current base of integers
		0 means that the base is detected when reading, or 10 (decimal) when generating numbers.
		"""
		res = super(QTextStream,self).integerBase()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def locale(self):
		"""
		Returns the locale for this stream
		The default locale is C.
		"""
		res = super(QTextStream,self).locale()
		isinstance(res,QtCore.QLocale)
		return res
	#----------------------------------------------------------------------
	def numberFlags(self):
		"""
		Returns the current number flags.
		"""
		res = super(QTextStream,self).numberFlags()
		isinstance(res,QtCore.QTextStream.NumberFlags)
		return res
	#----------------------------------------------------------------------
	def padChar(self):
		"""
		Returns the current pad character.
		"""
		res = super(QTextStream,self).padChar()
		isinstance(res,QtCore.QChar)
		return res
	#----------------------------------------------------------------------
	def pos(self):
		"""
		Returns the device position corresponding to the current position of the stream, or -1 if an error occurs (e.g., if there is no device or string, or if theres a device error).
		Because PySide.QtCore.QTextStream is buffered, this function may have to seek the device to reconstruct a valid device position
		This operation can be expensive, so you may want to avoid calling this function in a tight loop.
		"""
		res = super(QTextStream,self).pos()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def readAll(self):
		"""
		Reads the entire content of the stream, and returns it as a PySide.QtCore.QString
		Avoid this function when working on large files, as it will consume a significant amount of memory.
		Calling PySide.QtCore.QTextStream.readLine() is better if you do not know how much data is available.
		"""
		res = super(QTextStream,self).readAll()
		return res
	#----------------------------------------------------------------------
	def realNumberNotation(self):
		"""
		Returns the current real number notation.
		"""
		res = super(QTextStream,self).realNumberNotation()
		isinstance(res,QtCore.QTextStream.RealNumberNotation)
		return res
	#----------------------------------------------------------------------
	def realNumberPrecision(self):
		"""
		Returns the current real number precision, or the number of fraction digits PySide.QtCore.QTextStream will write when generating real numbers.
		"""
		res = super(QTextStream,self).realNumberPrecision()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def reset(self):
		"""
		Resets PySide.QtCore.QTextStream s formatting options, bringing it back to its original constructed state
		The device, string and any buffered data is left untouched.
		"""
		res = super(QTextStream,self).reset()
		return res
	#----------------------------------------------------------------------
	def resetStatus(self):
		"""
		Resets the status of the text stream.
		"""
		res = super(QTextStream,self).resetStatus()
		return res
	#----------------------------------------------------------------------
	def skipWhiteSpace(self):
		"""
		Reads and discards whitespace from the stream until either a non-space character is detected, or until PySide.QtCore.QTextStream.atEnd() returns true
		This function is useful when reading a stream character by character.
		Whitespace characters are all characters for which QChar.isSpace() returns true.
		"""
		res = super(QTextStream,self).skipWhiteSpace()
		return res
	#----------------------------------------------------------------------
	def status(self):
		"""
		Returns the status of the text stream.
		"""
		res = super(QTextStream,self).status()
		isinstance(res,QtCore.QTextStream.Status)
		return res
	#----------------------------------------------------------------------
	def string(self):
		"""
		Returns the current string assigned to the PySide.QtCore.QTextStream , or 0 if no string has been assigned.
		"""
		res = super(QTextStream,self).string()
		return res
	#----------------------------------------------------------------------
	def __lshift__(self,*args,**kwargs):
		"""
		__lshift__(i)
			i=QtCore.signed

		__lshift__(i)
			i=long

		__lshift__(f)
			f=QtCore.double

		__lshift__(arg__2)
			arg__2=QtGui.QSplitter

		__lshift__(ch)
			ch=QtCore.char

		__lshift__(m)
			m=QtCore.QTextStreamManipulator

		__lshift__(ch)
			ch=QtCore.QChar

		__lshift__(c)
			c=str

		__lshift__(s)
			s=unicode

		__lshift__(array)
			array=QtCore.QByteArray

		__lshift__(arg__2)
			arg__2=QtXml.QDomNode

		This is an overloaded function.
		Writes the signed long i to the stream.
		"""
		res = super(QTextStream,self).__lshift__(*args,**kwargs)
		isinstance(res,QtCore.QTextStream)
		return res
	#----------------------------------------------------------------------
	def __rshift__(self,*args,**kwargs):
		"""
		__rshift__(array)
			array=QtCore.QByteArray

		__rshift__(arg__2)
			arg__2=QtGui.QSplitter

		This is an overloaded function.
		Converts the word to ISO-8859-1, then stores it in array .
		"""
		res = super(QTextStream,self).__rshift__(*args,**kwargs)
		isinstance(res,QtCore.QTextStream)
		return res
	#----------------------------------------------------------------------
	def read(self,maxlen):
		"""
		read(maxlen)
			maxlen=QtCore.qint64

		Reads at most maxlen characters from the stream, and returns the data read as a PySide.QtCore.QString .
		"""
		res = super(QTextStream,self).read(maxlen)
		return res
	#----------------------------------------------------------------------
	def readLine(self,maxlen=None):
		"""
		readLine(maxlen=None)
			maxlen=QtCore.qint64

		Reads one line of text from the stream, and returns it as a PySide.QtCore.QString
		The maximum allowed line length is set to maxlen
		If the stream contains lines longer than this, then the lines will be split after maxlen characters and returned in parts.
		If maxlen is 0, the lines can be of any length
		A common value for maxlen is 75.
		The returned line has no trailing end-of-line characters (n or rn), so calling QString.trimmed() is unnecessary.
		If the stream has read to the end of the file, PySide.QtCore.QTextStream.readLine() will return a null PySide.QtCore.QString
		For strings, or for devices that support it, you can explicitly test for the end of the stream using PySide.QtCore.QTextStream.atEnd() .
		"""
		res = super(QTextStream,self).readLine(maxlen)
		return res
	#----------------------------------------------------------------------
	def seek(self,pos):
		"""
		seek(pos)
			pos=QtCore.qint64

		Seeks to the position pos in the device
		Returns true on success; otherwise returns false.
		"""
		res = super(QTextStream,self).seek(pos)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setAutoDetectUnicode(self,enabled):
		"""
		setAutoDetectUnicode(enabled)
			enabled=QtCore.bool

		If enabled is true, PySide.QtCore.QTextStream will attempt to detect Unicode encoding by peeking into the stream data to see if it can find the UTF-16 or UTF-32 BOM (Byte Order Mark)
		If this mark is found, PySide.QtCore.QTextStream will replace the current codec with the UTF codec.
		This function can be used together with PySide.QtCore.QTextStream.setCodec()
		It is common to set the codec to UTF-8, and then enable UTF-16 detection.
		"""
		res = super(QTextStream,self).setAutoDetectUnicode(enabled)
		return res
	#----------------------------------------------------------------------
	def setCodec(self,*args,**kwargs):
		"""
		setCodec(codecName)
			codecName=str

		setCodec(codec)
			codec=QtCore.QTextCodec

		Sets the codec for this stream to the PySide.QtCore.QTextCodec for the encoding specified by codecName
		Common values for codecName include ISO 8859-1, UTF-8, and UTF-16
		If the encoding isnt recognized, nothing happens.
		Example:
		"""
		res = super(QTextStream,self).setCodec(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setDevice(self,device):
		"""
		setDevice(device)
			device=QtCore.QIODevice

		Sets the current device to device
		If a device has already been assigned, PySide.QtCore.QTextStream will call PySide.QtCore.QTextStream.flush() before the old device is replaced.
		"""
		res = super(QTextStream,self).setDevice(device)
		return res
	#----------------------------------------------------------------------
	def setFieldAlignment(self,alignment):
		"""
		setFieldAlignment(alignment)
			alignment=QtCore.QTextStream.FieldAlignment

		Sets the field alignment to mode
		When used together with PySide.QtCore.QTextStream.setFieldWidth() , this function allows you to generate formatted output with text aligned to the left, to the right or center aligned.
		"""
		res = super(QTextStream,self).setFieldAlignment(alignment)
		return res
	#----------------------------------------------------------------------
	def setFieldWidth(self,width):
		"""
		setFieldWidth(width)
			width=QtCore.int

		Sets the current field width to width
		If width is 0 (the default), the field width is equal to the length of the generated text.
		"""
		res = super(QTextStream,self).setFieldWidth(width)
		return res
	#----------------------------------------------------------------------
	def setGenerateByteOrderMark(self,generate):
		"""
		setGenerateByteOrderMark(generate)
			generate=QtCore.bool

		If generate is true and a UTF codec is used, PySide.QtCore.QTextStream will insert the BOM (Byte Order Mark) before any data has been written to the device
		If generate is false, no BOM will be inserted
		This function must be called before any data is written
		Otherwise, it does nothing.
		"""
		res = super(QTextStream,self).setGenerateByteOrderMark(generate)
		return res
	#----------------------------------------------------------------------
	def setIntegerBase(self,base):
		"""
		setIntegerBase(base)
			base=QtCore.int

		Sets the base of integers to base , both for reading and for generating numbers
		base can be either 2 (binary), 8 (octal), 10 (decimal) or 16 (hexadecimal)
		If base is 0, PySide.QtCore.QTextStream will attempt to detect the base by inspecting the data on the stream
		When generating numbers, PySide.QtCore.QTextStream assumes base is 10 unless the base has been set explicitly.
		"""
		res = super(QTextStream,self).setIntegerBase(base)
		return res
	#----------------------------------------------------------------------
	def setLocale(self,locale):
		"""
		setLocale(locale)
			locale=QtCore.QLocale

		Sets the locale for this stream to locale
		The specified locale is used for conversions between numbers and their string representations.
		The default locale is C and it is a special case - the thousands group separator is not used for backward compatibility reasons.
		"""
		res = super(QTextStream,self).setLocale(locale)
		return res
	#----------------------------------------------------------------------
	def setNumberFlags(self,flags):
		"""
		setNumberFlags(flags)
			flags=QtCore.QTextStream.NumberFlags


		"""
		res = super(QTextStream,self).setNumberFlags(flags)
		return res
	#----------------------------------------------------------------------
	def setPadChar(self,ch):
		"""
		setPadChar(ch)
			ch=QtCore.QChar

		Sets the pad character to ch
		The default value is the ASCII space character ( ), or PySide.QtCore.QChar (0x20)
		This character is used to fill in the space in fields when generating text.
		Example:
		The string s contains:
		"""
		res = super(QTextStream,self).setPadChar(ch)
		return res
	#----------------------------------------------------------------------
	def setRealNumberNotation(self,notation):
		"""
		setRealNumberNotation(notation)
			notation=QtCore.QTextStream.RealNumberNotation

		Sets the real number notation to notation ( SmartNotation , FixedNotation , ScientificNotation )
		When reading and generating numbers, PySide.QtCore.QTextStream uses this value to detect the formatting of real numbers.
		"""
		res = super(QTextStream,self).setRealNumberNotation(notation)
		return res
	#----------------------------------------------------------------------
	def setRealNumberPrecision(self,precision):
		"""
		setRealNumberPrecision(precision)
			precision=QtCore.int

		Sets the precision of real numbers to precision
		This value describes the number of fraction digits PySide.QtCore.QTextStream should write when generating real numbers.
		The precision cannot be a negative value
		The default value is 6.
		"""
		res = super(QTextStream,self).setRealNumberPrecision(precision)
		return res
	#----------------------------------------------------------------------
	def setStatus(self,status):
		"""
		setStatus(status)
			status=QtCore.QTextStream.Status

		Sets the status of the text stream to the status given.
		"""
		res = super(QTextStream,self).setStatus(status)
		return res

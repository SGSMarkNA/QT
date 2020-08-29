from PySide import QtGui, QtCore

class QTextCodec(QtCore.QTextCodec):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextCodec,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def aliases(self):
		"""
		Subclasses can return a number of aliases for the codec in question.
		Standard aliases for codecs can be found in the IANA character-sets encoding file .
		"""
		res = super(QTextCodec,self).aliases()
		return res
	#----------------------------------------------------------------------
	def makeDecoder(self):
		"""
		Creates a PySide.QtCore.QTextDecoder which stores enough state to decode chunks of char * data to create chunks of Unicode data.
		The caller is responsible for deleting the returned object.
		"""
		res = super(QTextCodec,self).makeDecoder()
		isinstance(res,QtCore.QTextDecoder)
		return res
	#----------------------------------------------------------------------
	def makeEncoder(self):
		"""
		Creates a PySide.QtCore.QTextEncoder which stores enough state to encode chunks of Unicode data as char * data.
		The caller is responsible for deleting the returned object.
		"""
		res = super(QTextCodec,self).makeEncoder()
		isinstance(res,QtCore.QTextEncoder)
		return res
	#----------------------------------------------------------------------
	def mibEnum(self):
		"""
		Subclasses of PySide.QtCore.QTextCodec must reimplement this function
		It returns the MIBenum (see IANA character-sets encoding file for more information)
		It is important that each PySide.QtCore.QTextCodec subclass returns the correct unique value for this function.
		"""
		res = super(QTextCodec,self).mibEnum()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def name(self):
		"""
		PySide.QtCore.QTextCodec subclasses must reimplement this function
		It returns the name of the encoding supported by the subclass.
		If the codec is registered as a character set in the IANA character-sets encoding file this method should return the preferred mime name for the codec if defined, otherwise its name.
		"""
		res = super(QTextCodec,self).name()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def canEncode(self,*args,**kwargs):
		"""
		canEncode(arg__1)
			arg__1=QtCore.QChar

		canEncode(arg__1)
			arg__1=unicode

		Returns true if the Unicode character ch can be fully encoded with this codec; otherwise returns false.
		"""
		res = super(QTextCodec,self).canEncode(*args,**kwargs)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def convertFromUnicode(self,in,length,state):
		"""
		convertFromUnicode(in,length,state)
			in=QtCore.QChar
			length=QtCore.int
			state=QtCore.QTextCodec::ConverterState

		PySide.QtCore.QTextCodec subclasses must reimplement this function.
		Converts the first number of characters from the input array from Unicode to the encoding of the subclass, and returns the result in a PySide.QtCore.QByteArray .
		state can be 0 in which case the conversion is stateless and default conversion rules should be used
		If state is not 0, the codec should save the state after the conversion in state , and adjust the remainingChars and invalidChars members of the struct.
		"""
		res = super(QTextCodec,self).convertFromUnicode(in,length,state)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def convertToUnicode(self,in,length,state):
		"""
		convertToUnicode(in,length,state)
			in=str
			length=QtCore.int
			state=QtCore.QTextCodec::ConverterState

		PySide.QtCore.QTextCodec subclasses must reimplement this function.
		Converts the first len characters of chars from the encoding of the subclass to Unicode, and returns the result in a PySide.QtCore.QString .
		state can be 0, in which case the conversion is stateless and default conversion rules should be used
		If state is not 0, the codec should save the state after the conversion in state , and adjust the remainingChars and invalidChars members of the struct.
		"""
		res = super(QTextCodec,self).convertToUnicode(in,length,state)
		return res
	#----------------------------------------------------------------------
	def fromUnicode(self,*args,**kwargs):
		"""
		fromUnicode(in,length,state=None)
			in=QtCore.QChar
			length=QtCore.int
			state=QtCore.QTextCodec::ConverterState

		fromUnicode(uc)
			uc=unicode

		Converts the first number of characters from the input array from Unicode to the encoding of this codec, and returns the result in a PySide.QtCore.QByteArray .
		The state of the convertor used is updated.
		"""
		res = super(QTextCodec,self).fromUnicode(*args,**kwargs)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def makeDecoder(self,flags):
		"""
		makeDecoder(flags)
			flags=QtCore.QTextCodec.ConversionFlags


		"""
		res = super(QTextCodec,self).makeDecoder(flags)
		isinstance(res,QtCore.QTextDecoder)
		return res
	#----------------------------------------------------------------------
	def makeEncoder(self,flags):
		"""
		makeEncoder(flags)
			flags=QtCore.QTextCodec.ConversionFlags


		"""
		res = super(QTextCodec,self).makeEncoder(flags)
		isinstance(res,QtCore.QTextEncoder)
		return res
	#----------------------------------------------------------------------
	def toUnicode(self,*args,**kwargs):
		"""
		toUnicode(in,length,state=None)
			in=str
			length=QtCore.int
			state=QtCore.QTextCodec::ConverterState

		toUnicode(arg__1)
			arg__1=QtCore.QByteArray

		toUnicode(chars)
			chars=str

		Converts the first size characters from the input from the encoding of this codec to Unicode, and returns the result in a PySide.QtCore.QString .
		The state of the convertor used is updated.
		"""
		res = super(QTextCodec,self).toUnicode(*args,**kwargs)
		return res

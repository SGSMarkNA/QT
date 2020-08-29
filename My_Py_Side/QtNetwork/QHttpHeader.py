from PySide import QtGui, QtCore

class QHttpHeader(QtNetwork.QHttpHeader):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QHttpHeader,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def contentLength(self):
		"""
		Returns the value of the special HTTP header field content-length .
		"""
		res = super(QHttpHeader,self).contentLength()
		isinstance(res,QtCore.uint)
		return res
	#----------------------------------------------------------------------
	def contentType(self):
		"""
		Returns the value of the special HTTP header field content-type .
		"""
		res = super(QHttpHeader,self).contentType()
		return res
	#----------------------------------------------------------------------
	def hasContentLength(self):
		"""
		Returns true if the header has an entry for the special HTTP header field content-length ; otherwise returns false.
		"""
		res = super(QHttpHeader,self).hasContentLength()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def hasContentType(self):
		"""
		Returns true if the header has an entry for the special HTTP header field content-type ; otherwise returns false.
		"""
		res = super(QHttpHeader,self).hasContentType()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if the HTTP header is valid; otherwise returns false.
		A PySide.QtNetwork.QHttpHeader is invalid if it was created by parsing a malformed string.
		"""
		res = super(QHttpHeader,self).isValid()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def keys(self):
		"""
		Returns a list of the keys in the HTTP header.
		"""
		res = super(QHttpHeader,self).keys()
		return res
	#----------------------------------------------------------------------
	def majorVersion(self):
		"""
		Returns the major protocol-version of the HTTP header.
		"""
		res = super(QHttpHeader,self).majorVersion()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def minorVersion(self):
		"""
		Returns the minor protocol-version of the HTTP header.
		"""
		res = super(QHttpHeader,self).minorVersion()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def toString(self):
		"""
		Returns a string representation of the HTTP header.
		The string is suitable for use by the constructor that takes a PySide.QtCore.QString
		It consists of lines with the format: key, colon, space, value, rn.
		"""
		res = super(QHttpHeader,self).toString()
		return res
	#----------------------------------------------------------------------
	def values(self):
		"""
		Returns all the entries in the header.
		"""
		res = super(QHttpHeader,self).values()
		return res
	#----------------------------------------------------------------------
	def addValue(self,key,value):
		"""
		addValue(key,value)
			key=unicode
			value=unicode

		Adds a new entry with the key and value .
		"""
		res = super(QHttpHeader,self).addValue(key,value)
		return res
	#----------------------------------------------------------------------
	def allValues(self,key):
		"""
		allValues(key)
			key=unicode

		Returns all the entries with the given key
		If no entry has this key , an empty string list is returned.
		"""
		res = super(QHttpHeader,self).allValues(key)
		return res
	#----------------------------------------------------------------------
	def hasKey(self,key):
		"""
		hasKey(key)
			key=unicode

		Returns true if the HTTP header has an entry with the given key ; otherwise returns false.
		"""
		res = super(QHttpHeader,self).hasKey(key)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def parse(self,str):
		"""
		parse(str)
			str=unicode

		Parses the HTTP header string str for header fields and adds the keys/values it finds
		If the string is not parsed successfully the PySide.QtNetwork.QHttpHeader becomes invalid .
		Returns true if str was successfully parsed; otherwise returns false.
		"""
		res = super(QHttpHeader,self).parse(str)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def parseLine(self,line,number):
		"""
		parseLine(line,number)
			line=unicode
			number=QtCore.int

		Parses the single HTTP header line line which has the format key, colon, space, value, and adds key/value to the headers
		The linenumber is number
		Returns true if the line was successfully parsed and the key/value added; otherwise returns false.
		"""
		res = super(QHttpHeader,self).parseLine(line,number)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def removeAllValues(self,key):
		"""
		removeAllValues(key)
			key=unicode

		Removes all the entries with the key key from the HTTP header.
		"""
		res = super(QHttpHeader,self).removeAllValues(key)
		return res
	#----------------------------------------------------------------------
	def removeValue(self,key):
		"""
		removeValue(key)
			key=unicode

		Removes the entry with the key key from the HTTP header.
		"""
		res = super(QHttpHeader,self).removeValue(key)
		return res
	#----------------------------------------------------------------------
	def setContentLength(self,len):
		"""
		setContentLength(len)
			len=QtCore.int

		Sets the value of the special HTTP header field content-length to len .
		"""
		res = super(QHttpHeader,self).setContentLength(len)
		return res
	#----------------------------------------------------------------------
	def setContentType(self,type):
		"""
		setContentType(type)
			type=unicode

		Sets the value of the special HTTP header field content-type to type .
		"""
		res = super(QHttpHeader,self).setContentType(type)
		return res
	#----------------------------------------------------------------------
	def setValid(self,arg__1):
		"""
		setValid(arg__1)
			arg__1=QtCore.bool


		"""
		res = super(QHttpHeader,self).setValid(arg__1)
		return res
	#----------------------------------------------------------------------
	def setValue(self,key,value):
		"""
		setValue(key,value)
			key=unicode
			value=unicode

		Sets the value of the entry with the key to value .
		If no entry with key exists, a new entry with the given key and value is created
		If an entry with the key already exists, the first value is discarded and replaced with the given value .
		"""
		res = super(QHttpHeader,self).setValue(key,value)
		return res
	#----------------------------------------------------------------------
	def setValues(self,values):
		"""
		setValues(values)
			values=unKnown


		"""
		res = super(QHttpHeader,self).setValues(values)
		return res
	#----------------------------------------------------------------------
	def value(self,key):
		"""
		value(key)
			key=unicode

		Returns the first value for the entry with the given key
		If no entry has this key , an empty string is returned.
		"""
		res = super(QHttpHeader,self).value(key)
		return res

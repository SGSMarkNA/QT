from PySide import QtGui, QtCore

class QXmlInputSource(QtXml.QXmlInputSource):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QXmlInputSource,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def data(self):
		"""
		Returns the data the input source contains or an empty string if the input source does not contain any data.
		"""
		res = super(QXmlInputSource,self).data()
		return res
	#----------------------------------------------------------------------
	def fetchData(self):
		"""
		This function reads more data from the device that was set during construction
		If the input source already contained data, this function deletes that data first.
		This object contains no data after a call to this function if the object was constructed without a device to read data from or if this function was not able to get more data from the device.
		There are two occasions where a fetch is done implicitly by another function call: during construction (so that the object starts out with some initial data where available), and during a call to PySide.QtXml.QXmlInputSource.next() (if the data had run out).
		You dont normally need to use this function if you use PySide.QtXml.QXmlInputSource.next() .
		"""
		res = super(QXmlInputSource,self).fetchData()
		return res
	#----------------------------------------------------------------------
	def init(self):
		"""

		"""
		res = super(QXmlInputSource,self).init()
		return res
	#----------------------------------------------------------------------
	def next(self):
		"""
		Returns the next character of the input source
		If this function reaches the end of available data, it returns QXmlInputSource.EndOfData
		If you call PySide.QtXml.QXmlInputSource.next() after that, it tries to fetch more data by calling PySide.QtXml.QXmlInputSource.fetchData()
		If the PySide.QtXml.QXmlInputSource.fetchData() call results in new data, this function returns the first character of that data; otherwise it returns QXmlInputSource.EndOfDocument .
		Readers, such as PySide.QtXml.QXmlSimpleReader , will assume that the end of the XML document has been reached if the this function returns QXmlInputSource.EndOfDocument , and will check that the supplied input is well-formed
		Therefore, when reimplementing this function, it is important to ensure that this behavior is duplicated.
		"""
		res = super(QXmlInputSource,self).next()
		isinstance(res,QtCore.QChar)
		return res
	#----------------------------------------------------------------------
	def reset(self):
		"""
		This function sets the position used by PySide.QtXml.QXmlInputSource.next() to the beginning of the data returned by PySide.QtXml.QXmlInputSource.data()
		This is useful if you want to use the input source for more than one parse.
		"""
		res = super(QXmlInputSource,self).reset()
		return res
	#----------------------------------------------------------------------
	def fromRawData(self,data,beginning=None):
		"""
		fromRawData(data,beginning=None)
			data=QtCore.QByteArray
			beginning=QtCore.bool

		This function reads the XML file from data and tries to recognize the encoding
		It converts the raw data data into a PySide.QtCore.QString and returns it
		It tries its best to get the correct encoding for the XML file.
		If beginning is true, this function assumes that the data starts at the beginning of a new XML document and looks for an encoding declaration
		If beginning is false, it converts the raw data using the encoding determined from prior calls.
		"""
		res = super(QXmlInputSource,self).fromRawData(data,beginning)
		return res
	#----------------------------------------------------------------------
	def setData(self,*args,**kwargs):
		"""
		setData(dat)
			dat=QtCore.QByteArray

		setData(dat)
			dat=unicode

		This is an overloaded function.
		The data dat is passed through the correct text-codec, before it is set.
		"""
		res = super(QXmlInputSource,self).setData(*args,**kwargs)
		return res

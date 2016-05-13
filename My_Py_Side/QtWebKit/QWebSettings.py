from PySide import QtGui, QtCore

class QWebSettings(QtWebKit.QWebSettings):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QWebSettings,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def defaultTextEncoding(self):
		"""
		Returns the default text encoding.
		"""
		res = super(QWebSettings,self).defaultTextEncoding()
		return res
	#----------------------------------------------------------------------
	def localStoragePath(self):
		"""
		Returns the path for HTML5 local storage.
		"""
		res = super(QWebSettings,self).localStoragePath()
		return res
	#----------------------------------------------------------------------
	def userStyleSheetUrl(self):
		"""
		Returns the location of the user stylesheet.
		"""
		res = super(QWebSettings,self).userStyleSheetUrl()
		isinstance(res,QtCore.QUrl)
		return res
	#----------------------------------------------------------------------
	def fontFamily(self,which):
		"""
		fontFamily(which)
			which=QtWebKit.QWebSettings.FontFamily

		Returns the actual font family for the specified generic font family, which .
		"""
		res = super(QWebSettings,self).fontFamily(which)
		return res
	#----------------------------------------------------------------------
	def fontSize(self,type):
		"""
		fontSize(type)
			type=QtWebKit.QWebSettings.FontSize

		Returns the default font size for type .
		"""
		res = super(QWebSettings,self).fontSize(type)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def resetAttribute(self,attr):
		"""
		resetAttribute(attr)
			attr=QtWebKit.QWebSettings.WebAttribute

		Resets the setting of attribute to the value specified in the global PySide.QtWebKit.QWebSettings instance.
		This function has no effect on the global PySide.QtWebKit.QWebSettings instance.
		"""
		res = super(QWebSettings,self).resetAttribute(attr)
		return res
	#----------------------------------------------------------------------
	def resetFontFamily(self,which):
		"""
		resetFontFamily(which)
			which=QtWebKit.QWebSettings.FontFamily

		Resets the actual font family specified by which to the one set in the global PySide.QtWebKit.QWebSettings instance.
		This function has no effect on the global PySide.QtWebKit.QWebSettings instance.
		"""
		res = super(QWebSettings,self).resetFontFamily(which)
		return res
	#----------------------------------------------------------------------
	def resetFontSize(self,type):
		"""
		resetFontSize(type)
			type=QtWebKit.QWebSettings.FontSize

		Resets the font size for type to the size specified in the global settings object.
		This function has no effect on the global PySide.QtWebKit.QWebSettings instance.
		"""
		res = super(QWebSettings,self).resetFontSize(type)
		return res
	#----------------------------------------------------------------------
	def setAttribute(self,attr,on):
		"""
		setAttribute(attr,on)
			attr=QtWebKit.QWebSettings.WebAttribute
			on=QtCore.bool

		Enables or disables the specified attribute feature depending on the value of on .
		"""
		res = super(QWebSettings,self).setAttribute(attr,on)
		return res
	#----------------------------------------------------------------------
	def setDefaultTextEncoding(self,encoding):
		"""
		setDefaultTextEncoding(encoding)
			encoding=unicode

		Specifies the default text encoding system.
		The encoding , must be a string describing an encoding such as utf-8, iso-8859-1, etc
		If left empty a default value will be used
		For a more extensive list of encoding names see PySide.QtCore.QTextCodec
		"""
		res = super(QWebSettings,self).setDefaultTextEncoding(encoding)
		return res
	#----------------------------------------------------------------------
	def setFontFamily(self,which,family):
		"""
		setFontFamily(which,family)
			which=QtWebKit.QWebSettings.FontFamily
			family=unicode

		Sets the actual font family to family for the specified generic family, which .
		"""
		res = super(QWebSettings,self).setFontFamily(which,family)
		return res
	#----------------------------------------------------------------------
	def setFontSize(self,type,size):
		"""
		setFontSize(type,size)
			type=QtWebKit.QWebSettings.FontSize
			size=QtCore.int

		Sets the font size for type to size .
		"""
		res = super(QWebSettings,self).setFontSize(type,size)
		return res
	#----------------------------------------------------------------------
	def setLocalStoragePath(self,path):
		"""
		setLocalStoragePath(path)
			path=unicode

		Sets the path for HTML5 local storage to path .
		For more information on HTML5 local storage see the Web Storage standard.
		Support for local storage can enabled by setting the LocalStorageEnabled attribute.
		"""
		res = super(QWebSettings,self).setLocalStoragePath(path)
		return res
	#----------------------------------------------------------------------
	def setUserStyleSheetUrl(self,location):
		"""
		setUserStyleSheetUrl(location)
			location=QtCore.QUrl

		Specifies the location of a user stylesheet to load with every web page.
		The location must be either a path on the local filesystem, or a data URL with UTF-8 and Base64 encoded data, such as:
		data:text/css;charset=utf-8;base64,cCB7IGJhY2tncm91bmQtY29sb3I6IHJlZCB9Ow==
		"""
		res = super(QWebSettings,self).setUserStyleSheetUrl(location)
		return res
	#----------------------------------------------------------------------
	def testAttribute(self,attr):
		"""
		testAttribute(attr)
			attr=QtWebKit.QWebSettings.WebAttribute

		Returns true if attribute is enabled; otherwise returns false.
		"""
		res = super(QWebSettings,self).testAttribute(attr)
		isinstance(res,QtCore.bool)
		return res

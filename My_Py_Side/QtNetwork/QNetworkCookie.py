from PySide import QtGui, QtCore

class QNetworkCookie(QtNetwork.QNetworkCookie):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QNetworkCookie,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def domain(self):
		"""
		Returns the domain this cookie is associated with
		This corresponds to the domain field of the cookie string.
		Note that the domain here may start with a dot, which is not a valid hostname
		However, it means this cookie matches all hostnames ending with that domain name.
		"""
		res = super(QNetworkCookie,self).domain()
		return res
	#----------------------------------------------------------------------
	def expirationDate(self):
		"""
		Returns the expiration date for this cookie
		If this cookie is a session cookie, the PySide.QtCore.QDateTime returned will not be valid
		If the date is in the past, this cookie has already expired and should not be sent again back to a remote server.
		The expiration date corresponds to the parameters of the expires entry in the cookie string.
		"""
		res = super(QNetworkCookie,self).expirationDate()
		isinstance(res,QtCore.QDateTime)
		return res
	#----------------------------------------------------------------------
	def isHttpOnly(self):
		"""
		Returns true if the HttpOnly flag is enabled for this cookie.
		A cookie that is HttpOnly is only set and retrieved by the network requests and replies; i.e., the HTTP protocol
		It is not accessible from scripts running on browsers.
		"""
		res = super(QNetworkCookie,self).isHttpOnly()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isSecure(self):
		"""
		Returns true if the secure option was specified in the cookie string, false otherwise.
		Secure cookies may contain private information and should not be resent over unencrypted connections.
		"""
		res = super(QNetworkCookie,self).isSecure()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isSessionCookie(self):
		"""
		Returns true if this cookie is a session cookie
		A session cookie is a cookie which has no expiration date, which means it should be discarded when the applications concept of session is over (usually, when the application exits).
		"""
		res = super(QNetworkCookie,self).isSessionCookie()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def name(self):
		"""
		Returns the name of this cookie
		The only mandatory field of a cookie is its name, without which it is not considered valid.
		"""
		res = super(QNetworkCookie,self).name()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def path(self):
		"""
		Returns the path associated with this cookie
		This corresponds to the path field of the cookie string.
		"""
		res = super(QNetworkCookie,self).path()
		return res
	#----------------------------------------------------------------------
	def value(self):
		"""
		Returns this cookies value, as specified in the cookie string
		Note that a cookie is still valid if its value is empty.
		Cookie name-value pairs are considered opaque to the application: that is, their values dont mean anything.
		"""
		res = super(QNetworkCookie,self).value()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtNetwork.QNetworkCookie

		Returns true if this cookie is not equal to other .
		"""
		res = super(QNetworkCookie,self).__ne__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtNetwork.QNetworkCookie

		Returns true if this cookie is equal to other
		This function only returns true if all fields of the cookie are the same.
		However, in some contexts, two cookies of the same name could be considered equal.
		"""
		res = super(QNetworkCookie,self).__eq__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def setDomain(self,domain):
		"""
		setDomain(domain)
			domain=unicode

		Sets the domain associated with this cookie to be domain .
		"""
		res = super(QNetworkCookie,self).setDomain(domain)
		return res
	#----------------------------------------------------------------------
	def setExpirationDate(self,date):
		"""
		setExpirationDate(date)
			date=QtCore.QDateTime

		Sets the expiration date of this cookie to date
		Setting an invalid expiration date to this cookie will mean its a session cookie.
		"""
		res = super(QNetworkCookie,self).setExpirationDate(date)
		return res
	#----------------------------------------------------------------------
	def setHttpOnly(self,enable):
		"""
		setHttpOnly(enable)
			enable=QtCore.bool

		Sets this cookies HttpOnly flag to enable .
		"""
		res = super(QNetworkCookie,self).setHttpOnly(enable)
		return res
	#----------------------------------------------------------------------
	def setName(self,cookieName):
		"""
		setName(cookieName)
			cookieName=QtCore.QByteArray

		Sets the name of this cookie to be cookieName
		Note that setting a cookie name to an empty PySide.QtCore.QByteArray will make this cookie invalid.
		"""
		res = super(QNetworkCookie,self).setName(cookieName)
		return res
	#----------------------------------------------------------------------
	def setPath(self,path):
		"""
		setPath(path)
			path=unicode

		Sets the path associated with this cookie to be path .
		"""
		res = super(QNetworkCookie,self).setPath(path)
		return res
	#----------------------------------------------------------------------
	def setSecure(self,enable):
		"""
		setSecure(enable)
			enable=QtCore.bool

		Sets the secure flag of this cookie to enable .
		Secure cookies may contain private information and should not be resent over unencrypted connections.
		"""
		res = super(QNetworkCookie,self).setSecure(enable)
		return res
	#----------------------------------------------------------------------
	def setValue(self,value):
		"""
		setValue(value)
			value=QtCore.QByteArray

		Sets the value of this cookie to be value .
		"""
		res = super(QNetworkCookie,self).setValue(value)
		return res
	#----------------------------------------------------------------------
	def toRawForm(self,form=None):
		"""
		toRawForm(form=None)
			form=QtNetwork.QNetworkCookie.RawForm

		Returns the raw form of this PySide.QtNetwork.QNetworkCookie
		The PySide.QtCore.QByteArray returned by this function is suitable for an HTTP header, either in a server response (the Set-Cookie header) or the client request (the Cookie header)
		You can choose from one of two formats, using form .
		"""
		res = super(QNetworkCookie,self).toRawForm(form)
		isinstance(res,QtCore.QByteArray)
		return res

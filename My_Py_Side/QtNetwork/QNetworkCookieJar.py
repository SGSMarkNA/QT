from PySide import QtGui, QtCore

class QNetworkCookieJar(QtNetwork.QNetworkCookieJar):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QNetworkCookieJar,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def allCookies(self):
		"""
		Returns all cookies stored in this cookie jar
		This function is suitable for derived classes to save cookies to disk, as well as to implement cookie expiration and other policies.
		"""
		res = super(QNetworkCookieJar,self).allCookies()
		return res
	#----------------------------------------------------------------------
	def cookiesForUrl(self,url):
		"""
		cookiesForUrl(url)
			url=QtCore.QUrl

		Returns the cookies to be added to when a request is sent to url
		This function is called by the default QNetworkAccessManager.createRequest() , which adds the cookies returned by this function to the request being sent.
		If more than one cookie with the same name is found, but with differing paths, the one with longer path is returned before the one with shorter path
		In other words, this function returns cookies sorted decreasingly by path length.
		The default PySide.QtNetwork.QNetworkCookieJar class implements only a very basic security policy (it makes sure that the cookies domain and path match the replys)
		To enhance the security policy with your own algorithms, override PySide.QtNetwork.QNetworkCookieJar.cookiesForUrl() .
		"""
		res = super(QNetworkCookieJar,self).cookiesForUrl(url)
		return res
	#----------------------------------------------------------------------
	def setAllCookies(self,cookieList):
		"""
		setAllCookies(cookieList)
			cookieList=unKnown


		"""
		res = super(QNetworkCookieJar,self).setAllCookies(cookieList)
		return res
	#----------------------------------------------------------------------
	def setCookiesFromUrl(self,cookieList,url):
		"""
		setCookiesFromUrl(cookieList,url)
			cookieList=unKnown
			url=QtCore.QUrl


		"""
		res = super(QNetworkCookieJar,self).setCookiesFromUrl(cookieList,url)
		isinstance(res,QtCore.bool)
		return res

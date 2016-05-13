from PySide import QtGui, QtCore

class QWebView(QtWebKit.QWebView):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QWebView,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def history(self):
		"""
		Returns a pointer to the views history of navigated web pages.
		It is equivalent to
		"""
		res = super(QWebView,self).history()
		isinstance(res,QtWebKit.QWebHistory)
		return res
	#----------------------------------------------------------------------
	def icon(self):
		"""
		This property holds the icon associated with the web page currently viewed.
		By default, this property contains a null icon.
		"""
		res = super(QWebView,self).icon()
		isinstance(res,QtGui.QIcon)
		return res
	#----------------------------------------------------------------------
	def iconChanged(self):
		"""

		"""
		res = super(QWebView,self).iconChanged()
		return res
	#----------------------------------------------------------------------
	def isModified(self):
		"""
		This property holds whether the document was modified by the user.
		Parts of HTML documents can be editable for example through the contenteditable attribute on HTML elements.
		By default, this property is false.
		"""
		res = super(QWebView,self).isModified()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def loadStarted(self):
		"""

		"""
		res = super(QWebView,self).loadStarted()
		return res
	#----------------------------------------------------------------------
	def page(self):
		"""
		Returns a pointer to the underlying web page.
		"""
		res = super(QWebView,self).page()
		isinstance(res,QtWebKit.QWebPage)
		return res
	#----------------------------------------------------------------------
	def renderHints(self):
		"""
		This property holds the default render hints for the view.
		These hints are used to initialize PySide.QtGui.QPainter before painting the Web page.
		QPainter.TextAntialiasing is enabled by default.
		"""
		res = super(QWebView,self).renderHints()
		isinstance(res,QtGui.QPainter.RenderHints)
		return res
	#----------------------------------------------------------------------
	def selectedText(self):
		"""
		This property holds the text currently selected.
		By default, this property contains an empty string.
		"""
		res = super(QWebView,self).selectedText()
		return res
	#----------------------------------------------------------------------
	def selectionChanged(self):
		"""

		"""
		res = super(QWebView,self).selectionChanged()
		return res
	#----------------------------------------------------------------------
	def settings(self):
		"""
		Returns a pointer to the view/page specific settings object.
		It is equivalent to
		"""
		res = super(QWebView,self).settings()
		isinstance(res,QtWebKit.QWebSettings)
		return res
	#----------------------------------------------------------------------
	def textSizeMultiplier(self):
		"""
		This property holds the scaling factor for all text in the frame.
		Use setZoomFactor instead, in combination with the ZoomTextOnly attribute in PySide.QtWebKit.QWebSettings .
		By default, this property contains a value of 1.0.
		"""
		res = super(QWebView,self).textSizeMultiplier()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def title(self):
		"""
		This property holds the title of the web page currently viewed.
		By default, this property contains an empty string.
		"""
		res = super(QWebView,self).title()
		return res
	#----------------------------------------------------------------------
	def url(self):
		"""
		This property holds the url of the web page currently viewed.
		Setting this property clears the view and loads the URL.
		By default, this property contains an empty, invalid URL.
		"""
		res = super(QWebView,self).url()
		isinstance(res,QtCore.QUrl)
		return res
	#----------------------------------------------------------------------
	def zoomFactor(self):
		"""
		This property holds the zoom factor for the view.
		"""
		res = super(QWebView,self).zoomFactor()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def createWindow(self,type):
		"""
		createWindow(type)
			type=QtWebKit.QWebPage.WebWindowType


		"""
		res = super(QWebView,self).createWindow(type)
		isinstance(res,QtWebKit.QWebView)
		return res
	#----------------------------------------------------------------------
	def findText(self,subString,options=None):
		"""
		findText(subString,options=None)
			subString=unicode
			options=QtWebKit.QWebPage.FindFlags


		"""
		res = super(QWebView,self).findText(subString,options)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def load(self,*args,**kwargs):
		"""
		load(url)
			url=QtCore.QUrl

		load(request,operation=None,body=None)
			request=QtNetwork.QNetworkRequest
			operation=QtNetwork.QNetworkAccessManager.Operation
			body=QtCore.QByteArray

		Loads the specified url and displays it.
		"""
		res = super(QWebView,self).load(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def pageAction(self,action):
		"""
		pageAction(action)
			action=QtWebKit.QWebPage.WebAction


		"""
		res = super(QWebView,self).pageAction(action)
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def setContent(self,data,mimeType=None,baseUrl=None):
		"""
		setContent(data,mimeType=None,baseUrl=None)
			data=QtCore.QByteArray
			mimeType=unicode
			baseUrl=QtCore.QUrl

		Sets the content of the web view to the specified content data
		If the mimeType argument is empty it is currently assumed that the content is HTML but in future versions we may introduce auto-detection.
		External objects referenced in the content are located relative to baseUrl .
		The data is loaded immediately; external objects are loaded asynchronously.
		"""
		res = super(QWebView,self).setContent(data,mimeType,baseUrl)
		return res
	#----------------------------------------------------------------------
	def setHtml(self,html,baseUrl=None):
		"""
		setHtml(html,baseUrl=None)
			html=unicode
			baseUrl=QtCore.QUrl

		Sets the content of the web view to the specified html .
		External objects such as stylesheets or images referenced in the HTML document are located relative to baseUrl .
		The html is loaded immediately; external objects are loaded asynchronously.
		When using this method, WebKit assumes that external resources such as JavaScript programs or style sheets are encoded in UTF-8 unless otherwise specified
		For example, the encoding of an external script can be specified through the charset attribute of the HTML script tag
		Alternatively, the encoding can also be specified by the web server.
		"""
		res = super(QWebView,self).setHtml(html,baseUrl)
		return res
	#----------------------------------------------------------------------
	def setPage(self,page):
		"""
		setPage(page)
			page=QtWebKit.QWebPage

		Makes page the new web page of the web view.
		The parent PySide.QtCore.QObject of the provided page remains the owner of the object
		If the current document is a child of the web view, it will be deleted.
		"""
		res = super(QWebView,self).setPage(page)
		return res
	#----------------------------------------------------------------------
	def setRenderHint(self,hint,enabled=None):
		"""
		setRenderHint(hint,enabled=None)
			hint=QtGui.QPainter.RenderHint
			enabled=QtCore.bool


		"""
		res = super(QWebView,self).setRenderHint(hint,enabled)
		return res
	#----------------------------------------------------------------------
	def setRenderHints(self,hints):
		"""
		setRenderHints(hints)
			hints=QtGui.QPainter.RenderHints

		This property holds the default render hints for the view.
		These hints are used to initialize PySide.QtGui.QPainter before painting the Web page.
		QPainter.TextAntialiasing is enabled by default.
		"""
		res = super(QWebView,self).setRenderHints(hints)
		return res
	#----------------------------------------------------------------------
	def setTextSizeMultiplier(self,factor):
		"""
		setTextSizeMultiplier(factor)
			factor=QtCore.qreal

		This property holds the scaling factor for all text in the frame.
		Use setZoomFactor instead, in combination with the ZoomTextOnly attribute in PySide.QtWebKit.QWebSettings .
		By default, this property contains a value of 1.0.
		"""
		res = super(QWebView,self).setTextSizeMultiplier(factor)
		return res
	#----------------------------------------------------------------------
	def setUrl(self,url):
		"""
		setUrl(url)
			url=QtCore.QUrl

		This property holds the url of the web page currently viewed.
		Setting this property clears the view and loads the URL.
		By default, this property contains an empty, invalid URL.
		"""
		res = super(QWebView,self).setUrl(url)
		return res
	#----------------------------------------------------------------------
	def setZoomFactor(self,factor):
		"""
		setZoomFactor(factor)
			factor=QtCore.qreal

		This property holds the zoom factor for the view.
		"""
		res = super(QWebView,self).setZoomFactor(factor)
		return res
	#----------------------------------------------------------------------
	def triggerPageAction(self,action,checked=None):
		"""
		triggerPageAction(action,checked=None)
			action=QtWebKit.QWebPage.WebAction
			checked=QtCore.bool


		"""
		res = super(QWebView,self).triggerPageAction(action,checked)
		return res

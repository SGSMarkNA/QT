from PySide import QtGui, QtCore

class QGraphicsWebView(QtWebKit.QGraphicsWebView):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsWebView,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def history(self):
		"""
		Returns a pointer to the views history of navigated web pages.
		It is equivalent to
		"""
		res = super(QGraphicsWebView,self).history()
		isinstance(res,QtWebKit.QWebHistory)
		return res
	#----------------------------------------------------------------------
	def icon(self):
		"""
		This property holds the icon associated with the web page currently viewed.
		By default, this property contains a null icon.
		"""
		res = super(QGraphicsWebView,self).icon()
		isinstance(res,QtGui.QIcon)
		return res
	#----------------------------------------------------------------------
	def iconChanged(self):
		"""

		"""
		res = super(QGraphicsWebView,self).iconChanged()
		return res
	#----------------------------------------------------------------------
	def isModified(self):
		"""
		This property holds whether the document was modified by the user.
		Parts of HTML documents can be editable for example through the contenteditable attribute on HTML elements.
		By default, this property is false.
		"""
		res = super(QGraphicsWebView,self).isModified()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isTiledBackingStoreFrozen(self):
		"""
		This property holds whether the tiled backing store updates its contents.
		If the tiled backing store is enabled using QWebSettings.TiledBackingStoreEnabled attribute, this property can be used to disable backing store updates temporarily
		This can be useful for example for running a smooth animation that changes the scale of the PySide.QtWebKit.QGraphicsWebView .
		When the backing store is unfrozen, its contents will be automatically updated to match the current state of the document
		If the PySide.QtWebKit.QGraphicsWebView scale was changed, the backing store is also re-rendered using the new scale.
		If the tiled backing store is not enabled, this property does nothing.
		"""
		res = super(QGraphicsWebView,self).isTiledBackingStoreFrozen()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def loadStarted(self):
		"""

		"""
		res = super(QGraphicsWebView,self).loadStarted()
		return res
	#----------------------------------------------------------------------
	def page(self):
		"""
		Returns a pointer to the underlying web page.
		"""
		res = super(QGraphicsWebView,self).page()
		isinstance(res,QtWebKit.QWebPage)
		return res
	#----------------------------------------------------------------------
	def resizesToContents(self):
		"""
		This property holds whether the size of the PySide.QtWebKit.QGraphicsWebView and its viewport changes to match the contents size.
		If this property is set, the PySide.QtWebKit.QGraphicsWebView will automatically change its size to match the size of the main frame contents
		As a result the top level frame will never have scrollbars
		It will also make CSS fixed positioning to behave like absolute positioning with elements positioned relative to the document instead of the viewport.
		This property should be used in conjunction with the QWebPage.preferredContentsSize property
		If not explicitly set, the preferredContentsSize is automatically set to a reasonable value.
		"""
		res = super(QGraphicsWebView,self).resizesToContents()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def settings(self):
		"""
		Returns a pointer to the view/page specific settings object.
		It is equivalent to
		"""
		res = super(QGraphicsWebView,self).settings()
		isinstance(res,QtWebKit.QWebSettings)
		return res
	#----------------------------------------------------------------------
	def title(self):
		"""
		This property holds the title of the web page currently viewed.
		By default, this property contains an empty string.
		"""
		res = super(QGraphicsWebView,self).title()
		return res
	#----------------------------------------------------------------------
	def url(self):
		"""
		This property holds the url of the web page currently viewed.
		Setting this property clears the view and loads the URL.
		By default, this property contains an empty, invalid URL.
		"""
		res = super(QGraphicsWebView,self).url()
		isinstance(res,QtCore.QUrl)
		return res
	#----------------------------------------------------------------------
	def zoomFactor(self):
		"""
		This property holds the zoom factor for the view.
		"""
		res = super(QGraphicsWebView,self).zoomFactor()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def findText(self,subString,options=None):
		"""
		findText(subString,options=None)
			subString=unicode
			options=QtWebKit.QWebPage.FindFlags


		"""
		res = super(QGraphicsWebView,self).findText(subString,options)
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
		res = super(QGraphicsWebView,self).load(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def pageAction(self,action):
		"""
		pageAction(action)
			action=QtWebKit.QWebPage.WebAction


		"""
		res = super(QGraphicsWebView,self).pageAction(action)
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def setContent(self,data,mimeType=None,baseUrl=None):
		"""
		setContent(data,mimeType=None,baseUrl=None)
			data=QtCore.QByteArray
			mimeType=unicode
			baseUrl=QtCore.QUrl

		Sets the content of the web graphicsitem to the specified content data
		If the mimeType argument is empty it is currently assumed that the content is HTML but in future versions we may introduce auto-detection.
		External objects referenced in the content are located relative to baseUrl .
		The data is loaded immediately; external objects are loaded asynchronously.
		"""
		res = super(QGraphicsWebView,self).setContent(data,mimeType,baseUrl)
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
		res = super(QGraphicsWebView,self).setHtml(html,baseUrl)
		return res
	#----------------------------------------------------------------------
	def setPage(self,arg__1):
		"""
		setPage(arg__1)
			arg__1=QtWebKit.QWebPage

		Makes page the new web page of the web graphicsitem.
		The parent PySide.QtCore.QObject of the provided page remains the owner of the object
		If the current document is a child of the web view, it will be deleted.
		"""
		res = super(QGraphicsWebView,self).setPage(arg__1)
		return res
	#----------------------------------------------------------------------
	def setResizesToContents(self,enabled):
		"""
		setResizesToContents(enabled)
			enabled=QtCore.bool

		This property holds whether the size of the PySide.QtWebKit.QGraphicsWebView and its viewport changes to match the contents size.
		If this property is set, the PySide.QtWebKit.QGraphicsWebView will automatically change its size to match the size of the main frame contents
		As a result the top level frame will never have scrollbars
		It will also make CSS fixed positioning to behave like absolute positioning with elements positioned relative to the document instead of the viewport.
		This property should be used in conjunction with the QWebPage.preferredContentsSize property
		If not explicitly set, the preferredContentsSize is automatically set to a reasonable value.
		"""
		res = super(QGraphicsWebView,self).setResizesToContents(enabled)
		return res
	#----------------------------------------------------------------------
	def setTiledBackingStoreFrozen(self,frozen):
		"""
		setTiledBackingStoreFrozen(frozen)
			frozen=QtCore.bool

		This property holds whether the tiled backing store updates its contents.
		If the tiled backing store is enabled using QWebSettings.TiledBackingStoreEnabled attribute, this property can be used to disable backing store updates temporarily
		This can be useful for example for running a smooth animation that changes the scale of the PySide.QtWebKit.QGraphicsWebView .
		When the backing store is unfrozen, its contents will be automatically updated to match the current state of the document
		If the PySide.QtWebKit.QGraphicsWebView scale was changed, the backing store is also re-rendered using the new scale.
		If the tiled backing store is not enabled, this property does nothing.
		"""
		res = super(QGraphicsWebView,self).setTiledBackingStoreFrozen(frozen)
		return res
	#----------------------------------------------------------------------
	def setUrl(self,arg__1):
		"""
		setUrl(arg__1)
			arg__1=QtCore.QUrl

		This property holds the url of the web page currently viewed.
		Setting this property clears the view and loads the URL.
		By default, this property contains an empty, invalid URL.
		"""
		res = super(QGraphicsWebView,self).setUrl(arg__1)
		return res
	#----------------------------------------------------------------------
	def setZoomFactor(self,arg__1):
		"""
		setZoomFactor(arg__1)
			arg__1=QtCore.qreal

		This property holds the zoom factor for the view.
		"""
		res = super(QGraphicsWebView,self).setZoomFactor(arg__1)
		return res
	#----------------------------------------------------------------------
	def triggerPageAction(self,action,checked=None):
		"""
		triggerPageAction(action,checked=None)
			action=QtWebKit.QWebPage.WebAction
			checked=QtCore.bool


		"""
		res = super(QGraphicsWebView,self).triggerPageAction(action,checked)
		return res

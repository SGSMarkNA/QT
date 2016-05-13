from PySide import QtGui, QtCore

class QWebFrame(QtWebKit.QWebFrame):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QWebFrame,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def baseUrl(self):
		"""
		This property holds the base URL of the frame, can be used to resolve relative URLs.
		"""
		res = super(QWebFrame,self).baseUrl()
		isinstance(res,QtCore.QUrl)
		return res
	#----------------------------------------------------------------------
	def childFrames(self):
		"""
		Returns a list of all frames that are direct children of this frame.
		"""
		res = super(QWebFrame,self).childFrames()
		return res
	#----------------------------------------------------------------------
	def contentsSize(self):
		"""
		This property holds the size of the contents in this frame.
		"""
		res = super(QWebFrame,self).contentsSize()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def documentElement(self):
		"""
		Returns the document element of this frame.
		The document element provides access to the entire structured content of the frame.
		"""
		res = super(QWebFrame,self).documentElement()
		isinstance(res,QtWebKit.QWebElement)
		return res
	#----------------------------------------------------------------------
	def frameName(self):
		"""
		The name of this frame as defined by the parent frame.
		"""
		res = super(QWebFrame,self).frameName()
		return res
	#----------------------------------------------------------------------
	def geometry(self):
		"""
		Return the geometry of the frame relative to its parent frame.
		"""
		res = super(QWebFrame,self).geometry()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def hasFocus(self):
		"""
		Returns true if this frame has keyboard input focus; otherwise, returns false.
		"""
		res = super(QWebFrame,self).hasFocus()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def icon(self):
		"""
		This property holds the icon associated with this frame.
		"""
		res = super(QWebFrame,self).icon()
		isinstance(res,QtGui.QIcon)
		return res
	#----------------------------------------------------------------------
	def iconChanged(self):
		"""

		"""
		res = super(QWebFrame,self).iconChanged()
		return res
	#----------------------------------------------------------------------
	def initialLayoutCompleted(self):
		"""

		"""
		res = super(QWebFrame,self).initialLayoutCompleted()
		return res
	#----------------------------------------------------------------------
	def javaScriptWindowObjectCleared(self):
		"""

		"""
		res = super(QWebFrame,self).javaScriptWindowObjectCleared()
		return res
	#----------------------------------------------------------------------
	def loadStarted(self):
		"""

		"""
		res = super(QWebFrame,self).loadStarted()
		return res
	#----------------------------------------------------------------------
	def metaData(self):
		"""
		Returns the meta data in this frame as a QMultiMap
		The meta data consists of the name and content attributes of the of the <meta> tags in the HTML document.
		For example:
		Given the above HTML code the PySide.QtWebKit.QWebFrame.metaData() function will return a map with two entries:
		This function returns a multi map to support multiple meta tags with the same attribute name.
		"""
		res = super(QWebFrame,self).metaData()
		return res
	#----------------------------------------------------------------------
	def page(self):
		"""
		The web page that contains this frame.
		"""
		res = super(QWebFrame,self).page()
		isinstance(res,QtWebKit.QWebPage)
		return res
	#----------------------------------------------------------------------
	def pageChanged(self):
		"""

		"""
		res = super(QWebFrame,self).pageChanged()
		return res
	#----------------------------------------------------------------------
	def parentFrame(self):
		"""
		Returns the parent frame of this frame, or 0 if the frame is the web pages main frame.
		This is equivalent to qobject_cast< PySide.QtWebKit.QWebFrame *>(frame-> PySide.QtCore.QObject.parent() ).
		"""
		res = super(QWebFrame,self).parentFrame()
		isinstance(res,QtWebKit.QWebFrame)
		return res
	#----------------------------------------------------------------------
	def pos(self):
		"""
		Returns the position of the frame relative to its parent frame.
		"""
		res = super(QWebFrame,self).pos()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def provisionalLoad(self):
		"""

		"""
		res = super(QWebFrame,self).provisionalLoad()
		return res
	#----------------------------------------------------------------------
	def renderTreeDump(self):
		"""
		Returns a dump of the rendering tree
		This is mainly useful for debugging html.
		"""
		res = super(QWebFrame,self).renderTreeDump()
		return res
	#----------------------------------------------------------------------
	def requestedUrl(self):
		"""
		The URL requested to loaded by the frame currently viewed
		The URL may differ from the one returned by PySide.QtWebKit.QWebFrame.url() if a DNS resolution or a redirection occurs.
		"""
		res = super(QWebFrame,self).requestedUrl()
		isinstance(res,QtCore.QUrl)
		return res
	#----------------------------------------------------------------------
	def scrollPosition(self):
		"""
		This property holds the position the frame is currently scrolled to..
		"""
		res = super(QWebFrame,self).scrollPosition()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def securityOrigin(self):
		"""
		Returns the frames security origin.
		"""
		res = super(QWebFrame,self).securityOrigin()
		isinstance(res,QtWebKit.QWebSecurityOrigin)
		return res
	#----------------------------------------------------------------------
	def setFocus(self):
		"""
		Gives keyboard input focus to this frame.
		"""
		res = super(QWebFrame,self).setFocus()
		return res
	#----------------------------------------------------------------------
	def textSizeMultiplier(self):
		"""
		This property holds the scaling factor for all text in the frame.
		Use setZoomFactor instead, in combination with the ZoomTextOnly attribute in PySide.QtWebKit.QWebSettings .
		"""
		res = super(QWebFrame,self).textSizeMultiplier()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def title(self):
		"""
		This property holds the title of the frame as defined by the HTML &lt;title&gt; element.
		"""
		res = super(QWebFrame,self).title()
		return res
	#----------------------------------------------------------------------
	def toHtml(self):
		"""
		Returns the frames content as HTML, enclosed in HTML and BODY tags.
		"""
		res = super(QWebFrame,self).toHtml()
		return res
	#----------------------------------------------------------------------
	def toPlainText(self):
		"""
		Returns the content of this frame converted to plain text, completely stripped of all HTML formatting.
		"""
		res = super(QWebFrame,self).toPlainText()
		return res
	#----------------------------------------------------------------------
	def url(self):
		"""
		This property holds the url of the frame currently viewed.
		Setting this property clears the view and loads the URL.
		By default, this property contains an empty, invalid URL.
		"""
		res = super(QWebFrame,self).url()
		isinstance(res,QtCore.QUrl)
		return res
	#----------------------------------------------------------------------
	def zoomFactor(self):
		"""
		This property holds the zoom factor for the frame.
		"""
		res = super(QWebFrame,self).zoomFactor()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def addToJavaScriptWindowObject(self,*args,**kwargs):
		"""
		addToJavaScriptWindowObject(name,object)
			name=unicode
			object=QtCore.QObject

		addToJavaScriptWindowObject(name,object,ownership)
			name=unicode
			object=QtCore.QObject
			ownership=QtScript.QScriptEngine.ValueOwnership

		Make object available under name from within the frames JavaScript context
		The object will be inserted as a child of the frames window object.
		Qt properties will be exposed as JavaScript properties and slots as JavaScript methods.
		If you want to ensure that your QObjects remain accessible after loading a new URL, you should add them in a slot connected to the PySide.QtWebKit.QWebFrame.javaScriptWindowObjectCleared() signal.
		If Javascript is not enabled for this page, then this method does nothing.
		The object will never be explicitly deleted by QtWebKit .
		"""
		res = super(QWebFrame,self).addToJavaScriptWindowObject(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def findAllElements(self,selectorQuery):
		"""
		findAllElements(selectorQuery)
			selectorQuery=unicode

		Returns a new list of elements matching the given CSS selector selectorQuery
		If there are no matching elements, an empty list is returned.
		Standard CSS2 selector syntax is used for the query.
		"""
		res = super(QWebFrame,self).findAllElements(selectorQuery)
		isinstance(res,QtWebKit.QWebElementCollection)
		return res
	#----------------------------------------------------------------------
	def findFirstElement(self,selectorQuery):
		"""
		findFirstElement(selectorQuery)
			selectorQuery=unicode

		Returns the first element in the frames document that matches the given CSS selector selectorQuery
		If there is no matching element, a null element is returned.
		Standard CSS2 selector syntax is used for the query.
		"""
		res = super(QWebFrame,self).findFirstElement(selectorQuery)
		isinstance(res,QtWebKit.QWebElement)
		return res
	#----------------------------------------------------------------------
	def hitTestContent(self,pos):
		"""
		hitTestContent(pos)
			pos=QtCore.QPoint

		Performs a hit test on the frame contents at the given position pos and returns the hit test result.
		"""
		res = super(QWebFrame,self).hitTestContent(pos)
		isinstance(res,QtWebKit.QWebHitTestResult)
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

		Loads url into this frame.
		"""
		res = super(QWebFrame,self).load(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def render(self,*args,**kwargs):
		"""
		render(arg__1,layer,clip=None)
			arg__1=QtGui.QPainter
			layer=QtWebKit.QWebFrame.RenderLayer
			clip=QtGui.QRegion

		render(arg__1,clip)
			arg__1=QtGui.QPainter
			clip=QtGui.QRegion

		render(arg__1)
			arg__1=QtGui.QPainter

		Render the layer of the frame using painter clipping to clip .
		"""
		res = super(QWebFrame,self).render(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def scroll(self,arg__1,arg__2):
		"""
		scroll(arg__1,arg__2)
			arg__1=QtCore.int
			arg__2=QtCore.int

		Scrolls the frame dx pixels to the right and dy pixels downward
		Both dx and dy may be negative.
		"""
		res = super(QWebFrame,self).scroll(arg__1,arg__2)
		return res
	#----------------------------------------------------------------------
	def scrollBarGeometry(self,orientation):
		"""
		scrollBarGeometry(orientation)
			orientation=QtCore.Qt.Orientation


		"""
		res = super(QWebFrame,self).scrollBarGeometry(orientation)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def scrollBarMaximum(self,orientation):
		"""
		scrollBarMaximum(orientation)
			orientation=QtCore.Qt.Orientation


		"""
		res = super(QWebFrame,self).scrollBarMaximum(orientation)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def scrollBarMinimum(self,orientation):
		"""
		scrollBarMinimum(orientation)
			orientation=QtCore.Qt.Orientation


		"""
		res = super(QWebFrame,self).scrollBarMinimum(orientation)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def scrollBarPolicy(self,orientation):
		"""
		scrollBarPolicy(orientation)
			orientation=QtCore.Qt.Orientation


		"""
		res = super(QWebFrame,self).scrollBarPolicy(orientation)
		isinstance(res,QtCore.Qt.ScrollBarPolicy)
		return res
	#----------------------------------------------------------------------
	def scrollBarValue(self,orientation):
		"""
		scrollBarValue(orientation)
			orientation=QtCore.Qt.Orientation


		"""
		res = super(QWebFrame,self).scrollBarValue(orientation)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def scrollToAnchor(self,anchor):
		"""
		scrollToAnchor(anchor)
			anchor=unicode

		Scrolls the frame to the given anchor name.
		"""
		res = super(QWebFrame,self).scrollToAnchor(anchor)
		return res
	#----------------------------------------------------------------------
	def setContent(self,data,mimeType=None,baseUrl=None):
		"""
		setContent(data,mimeType=None,baseUrl=None)
			data=QtCore.QByteArray
			mimeType=unicode
			baseUrl=QtCore.QUrl

		Sets the content of this frame to the specified content data
		If the mimeType argument is empty it is currently assumed that the content is HTML but in future versions we may introduce auto-detection.
		External objects referenced in the content are located relative to baseUrl .
		The data is loaded immediately; external objects are loaded asynchronously.
		"""
		res = super(QWebFrame,self).setContent(data,mimeType,baseUrl)
		return res
	#----------------------------------------------------------------------
	def setHtml(self,html,baseUrl=None):
		"""
		setHtml(html,baseUrl=None)
			html=unicode
			baseUrl=QtCore.QUrl

		Sets the content of this frame to html
		baseUrl is optional and used to resolve relative URLs in the document, such as referenced images or stylesheets.
		The html is loaded immediately; external objects are loaded asynchronously.
		If a script in the html runs longer than the default script timeout (currently 10 seconds), for example due to being blocked by a modal JavaScript alert dialog, this method will return as soon as possible after the timeout and any subsequent html will be loaded asynchronously.
		When using this method WebKit assumes that external resources such as JavaScript programs or style sheets are encoded in UTF-8 unless otherwise specified
		For example, the encoding of an external script can be specified through the charset attribute of the HTML script tag
		It is also possible for the encoding to be specified by web server.
		"""
		res = super(QWebFrame,self).setHtml(html,baseUrl)
		return res
	#----------------------------------------------------------------------
	def setScrollBarPolicy(self,orientation,policy):
		"""
		setScrollBarPolicy(orientation,policy)
			orientation=QtCore.Qt.Orientation
			policy=QtCore.Qt.ScrollBarPolicy


		"""
		res = super(QWebFrame,self).setScrollBarPolicy(orientation,policy)
		return res
	#----------------------------------------------------------------------
	def setScrollBarValue(self,orientation,value):
		"""
		setScrollBarValue(orientation,value)
			orientation=QtCore.Qt.Orientation
			value=QtCore.int


		"""
		res = super(QWebFrame,self).setScrollBarValue(orientation,value)
		return res
	#----------------------------------------------------------------------
	def setScrollPosition(self,pos):
		"""
		setScrollPosition(pos)
			pos=QtCore.QPoint

		This property holds the position the frame is currently scrolled to..
		"""
		res = super(QWebFrame,self).setScrollPosition(pos)
		return res
	#----------------------------------------------------------------------
	def setTextSizeMultiplier(self,factor):
		"""
		setTextSizeMultiplier(factor)
			factor=QtCore.qreal

		This property holds the scaling factor for all text in the frame.
		Use setZoomFactor instead, in combination with the ZoomTextOnly attribute in PySide.QtWebKit.QWebSettings .
		"""
		res = super(QWebFrame,self).setTextSizeMultiplier(factor)
		return res
	#----------------------------------------------------------------------
	def setUrl(self,url):
		"""
		setUrl(url)
			url=QtCore.QUrl

		This property holds the url of the frame currently viewed.
		Setting this property clears the view and loads the URL.
		By default, this property contains an empty, invalid URL.
		"""
		res = super(QWebFrame,self).setUrl(url)
		return res
	#----------------------------------------------------------------------
	def setZoomFactor(self,factor):
		"""
		setZoomFactor(factor)
			factor=QtCore.qreal

		This property holds the zoom factor for the frame.
		"""
		res = super(QWebFrame,self).setZoomFactor(factor)
		return res

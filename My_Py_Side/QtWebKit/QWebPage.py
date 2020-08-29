from PySide import QtGui, QtCore

class QWebPage(QtWebKit.QWebPage):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QWebPage,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def bytesReceived(self):
		"""
		Returns the number of bytes that were received from the network to render the current page.
		"""
		res = super(QWebPage,self).bytesReceived()
		isinstance(res,QtCore.quint64)
		return res
	#----------------------------------------------------------------------
	def contentsChanged(self):
		"""

		"""
		res = super(QWebPage,self).contentsChanged()
		return res
	#----------------------------------------------------------------------
	def createStandardContextMenu(self):
		"""
		This function creates the standard context menu which is shown when the user clicks on the web page with the right mouse button
		It is called from the default contextMenuEvent() handler
		The popup menus ownership is transferred to the caller.
		"""
		res = super(QWebPage,self).createStandardContextMenu()
		isinstance(res,QtGui.QMenu)
		return res
	#----------------------------------------------------------------------
	def currentFrame(self):
		"""
		Returns the frame currently active.
		"""
		res = super(QWebPage,self).currentFrame()
		isinstance(res,QtWebKit.QWebFrame)
		return res
	#----------------------------------------------------------------------
	def forwardUnsupportedContent(self):
		"""
		This property holds whether PySide.QtWebKit.QWebPage should forward unsupported content.
		If enabled, the PySide.QtWebKit.QWebPage.unsupportedContent() signal is emitted with a network reply that can be used to read the content.
		If disabled, the download of such content is aborted immediately.
		By default unsupported content is not forwarded.
		"""
		res = super(QWebPage,self).forwardUnsupportedContent()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def history(self):
		"""
		Returns a pointer to the views history of navigated web pages.
		"""
		res = super(QWebPage,self).history()
		isinstance(res,QtWebKit.QWebHistory)
		return res
	#----------------------------------------------------------------------
	def isContentEditable(self):
		"""
		This property holds whether the content in this PySide.QtWebKit.QWebPage is editable or not.
		If this property is enabled the contents of the page can be edited by the user through a visible cursor
		If disabled (the default) only HTML elements in the web page with their contenteditable attribute set are editable.
		"""
		res = super(QWebPage,self).isContentEditable()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isModified(self):
		"""
		This property holds whether the page contains unsubmitted form data, or the contents have been changed..
		By default, this property is false.
		"""
		res = super(QWebPage,self).isModified()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def linkDelegationPolicy(self):
		"""
		This property holds how PySide.QtWebKit.QWebPage should delegate the handling of links through the PySide.QtWebKit.QWebPage.linkClicked() signal.
		The default is to delegate no links.
		"""
		res = super(QWebPage,self).linkDelegationPolicy()
		isinstance(res,QtWebKit.QWebPage.LinkDelegationPolicy)
		return res
	#----------------------------------------------------------------------
	def loadStarted(self):
		"""

		"""
		res = super(QWebPage,self).loadStarted()
		return res
	#----------------------------------------------------------------------
	def mainFrame(self):
		"""
		Returns the main frame of the page.
		The main frame provides access to the hierarchy of sub-frames and is also needed if you want to explicitly render a web page into a given painter.
		"""
		res = super(QWebPage,self).mainFrame()
		isinstance(res,QtWebKit.QWebFrame)
		return res
	#----------------------------------------------------------------------
	def microFocusChanged(self):
		"""

		"""
		res = super(QWebPage,self).microFocusChanged()
		return res
	#----------------------------------------------------------------------
	def networkAccessManager(self):
		"""
		Returns the PySide.QtNetwork.QNetworkAccessManager that is responsible for serving network requests for this PySide.QtWebKit.QWebPage .
		"""
		res = super(QWebPage,self).networkAccessManager()
		isinstance(res,QtNetwork.QNetworkAccessManager)
		return res
	#----------------------------------------------------------------------
	def palette(self):
		"""
		This property holds the pages palette.
		The base brush of the palette is used to draw the background of the main frame.
		By default, this property contains the applications default palette.
		"""
		res = super(QWebPage,self).palette()
		isinstance(res,QtGui.QPalette)
		return res
	#----------------------------------------------------------------------
	def pluginFactory(self):
		"""
		Returns the PySide.QtWebKit.QWebPluginFactory that is responsible for creating plugins embedded into this PySide.QtWebKit.QWebPage
		If no plugin factory is installed a null pointer is returned.
		"""
		res = super(QWebPage,self).pluginFactory()
		isinstance(res,QtWebKit.QWebPluginFactory)
		return res
	#----------------------------------------------------------------------
	def preferredContentsSize(self):
		"""
		This property holds the preferred size of the contents.
		If this property is set to a valid size, it is used to lay out the page
		If it is not set (the default), the viewport size is used instead.
		"""
		res = super(QWebPage,self).preferredContentsSize()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def qt_metacall(self):
		"""

		"""
		res = super(QWebPage,self).qt_metacall()
		return res
	#----------------------------------------------------------------------
	def selectedText(self):
		"""
		This property holds the text currently selected.
		By default, this property contains an empty string.
		"""
		res = super(QWebPage,self).selectedText()
		return res
	#----------------------------------------------------------------------
	def selectionChanged(self):
		"""

		"""
		res = super(QWebPage,self).selectionChanged()
		return res
	#----------------------------------------------------------------------
	def settings(self):
		"""
		Returns a pointer to the pages settings object.
		"""
		res = super(QWebPage,self).settings()
		isinstance(res,QtWebKit.QWebSettings)
		return res
	#----------------------------------------------------------------------
	def totalBytes(self):
		"""
		Returns the total number of bytes that were received from the network to render the current page, including extra content such as embedded images.
		"""
		res = super(QWebPage,self).totalBytes()
		isinstance(res,QtCore.quint64)
		return res
	#----------------------------------------------------------------------
	def undoStack(self):
		"""
		Returns a pointer to the undo stack used for editable content.
		"""
		res = super(QWebPage,self).undoStack()
		isinstance(res,QtGui.QUndoStack)
		return res
	#----------------------------------------------------------------------
	def view(self):
		"""
		Returns the view widget that is associated with the web page.
		"""
		res = super(QWebPage,self).view()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def viewportSize(self):
		"""
		This property holds the size of the viewport.
		The size affects for example the visibility of scrollbars if the document is larger than the viewport.
		By default, for a newly-created Web page, this property contains a size with zero width and height.
		"""
		res = super(QWebPage,self).viewportSize()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def windowCloseRequested(self):
		"""

		"""
		res = super(QWebPage,self).windowCloseRequested()
		return res
	#----------------------------------------------------------------------
	def acceptNavigationRequest(self,frame,request,type):
		"""
		acceptNavigationRequest(frame,request,type)
			frame=QtWebKit.QWebFrame
			request=QtNetwork.QNetworkRequest
			type=QtWebKit.QWebPage.NavigationType

		This function is called whenever WebKit requests to navigate frame to the resource specified by request by means of the specified navigation type type .
		If frame is a null pointer then navigation to a new window is requested
		If the request is accepted PySide.QtWebKit.QWebPage.createWindow() will be called.
		The default implementation interprets the pages PySide.QtWebKit.QWebPage.linkDelegationPolicy() and emits linkClicked accordingly or returns true to let PySide.QtWebKit.QWebPage handle the navigation itself.
		"""
		res = super(QWebPage,self).acceptNavigationRequest(frame,request,type)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def action(self,action):
		"""
		action(action)
			action=QtWebKit.QWebPage.WebAction

		Returns a PySide.QtGui.QAction for the specified QWebPage.WebAction action .
		The action is owned by the PySide.QtWebKit.QWebPage but you can customize the look by changing its properties.
		PySide.QtWebKit.QWebPage also takes care of implementing the action, so that upon triggering the corresponding action is performed on the page.
		"""
		res = super(QWebPage,self).action(action)
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def chooseFile(self,originatingFrame,oldFile):
		"""
		chooseFile(originatingFrame,oldFile)
			originatingFrame=QtWebKit.QWebFrame
			oldFile=unicode

		This function is called when the web content requests a file name, for example as a result of the user clicking on a file upload button in a HTML form.
		A suggested filename may be provided in suggestedFile
		The frame originating the request is provided as parentFrame .
		"""
		res = super(QWebPage,self).chooseFile(originatingFrame,oldFile)
		return res
	#----------------------------------------------------------------------
	def createPlugin(self,classid,url,paramNames,paramValues):
		"""
		createPlugin(classid,url,paramNames,paramValues)
			classid=unicode
			url=QtCore.QUrl
			paramNames=list
			paramValues=list

		This function is called whenever WebKit encounters a HTML object element with type application/x-qt-plugin
		It is called regardless of the value of QWebSettings.PluginsEnabled
		The classid , url , paramNames and paramValues correspond to the HTML object element attributes and child elements to configure the embeddable object.
		"""
		res = super(QWebPage,self).createPlugin(classid,url,paramNames,paramValues)
		isinstance(res,QtCore.QObject)
		return res
	#----------------------------------------------------------------------
	def createWindow(self,type):
		"""
		createWindow(type)
			type=QtWebKit.QWebPage.WebWindowType

		This function is called whenever WebKit wants to create a new window of the given type , for example when a JavaScript program requests to open a document in a new window.
		If the new window can be created, the new windows PySide.QtWebKit.QWebPage is returned; otherwise a null pointer is returned.
		If the view associated with the web page is a PySide.QtWebKit.QWebView object, then the default implementation forwards the request to PySide.QtWebKit.QWebView s PySide.QtWebKit.QWebPage.createWindow() function; otherwise it returns a null pointer.
		If type is WebModalDialog , the application must call setWindowModality( Qt.ApplicationModal ) on the new window.
		"""
		res = super(QWebPage,self).createWindow(type)
		isinstance(res,QtWebKit.QWebPage)
		return res
	#----------------------------------------------------------------------
	def extension(self,extension,option=None,output=None):
		"""
		extension(extension,option=None,output=None)
			extension=QtWebKit.QWebPage.Extension
			option=QtWebKit.QWebPage::ExtensionOption
			output=QtWebKit.QWebPage::ExtensionReturn

		This virtual function can be reimplemented in a PySide.QtWebKit.QWebPage subclass to provide support for extensions
		The option argument is provided as input to the extension; the output results can be stored in output .
		The behavior of this function is determined by extension
		The option and output values are typically casted to the corresponding types (for example, ChooseMultipleFilesExtensionOption and ChooseMultipleFilesExtensionReturn for ChooseMultipleFilesExtension ).
		You can call PySide.QtWebKit.QWebPage.supportsExtension() to check if an extension is supported by the page.
		Returns true if the extension was called successfully; otherwise returns false.
		"""
		res = super(QWebPage,self).extension(extension,option,output)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def findText(self,subString,options=None):
		"""
		findText(subString,options=None)
			subString=unicode
			options=QtWebKit.QWebPage.FindFlags


		"""
		res = super(QWebPage,self).findText(subString,options)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def focusNextPrevChild(self,next):
		"""
		focusNextPrevChild(next)
			next=QtCore.bool

		Similar to QWidget.focusNextPrevChild() it focuses the next focusable web element if next is true; otherwise the previous element is focused.
		Returns true if it can find a new focusable element, or false if it cant.
		"""
		res = super(QWebPage,self).focusNextPrevChild(next)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def frameAt(self,pos):
		"""
		frameAt(pos)
			pos=QtCore.QPoint

		Returns the frame at the given point pos , or 0 if there is no frame at that position.
		"""
		res = super(QWebPage,self).frameAt(pos)
		isinstance(res,QtWebKit.QWebFrame)
		return res
	#----------------------------------------------------------------------
	def inputMethodQuery(self,property):
		"""
		inputMethodQuery(property)
			property=QtCore.Qt.InputMethodQuery


		"""
		res = super(QWebPage,self).inputMethodQuery(property)
		return res
	#----------------------------------------------------------------------
	def javaScriptAlert(self,originatingFrame,msg):
		"""
		javaScriptAlert(originatingFrame,msg)
			originatingFrame=QtWebKit.QWebFrame
			msg=unicode

		This function is called whenever a JavaScript program running inside frame calls the alert() function with the message msg .
		The default implementation shows the message, msg , with QMessageBox::information.
		"""
		res = super(QWebPage,self).javaScriptAlert(originatingFrame,msg)
		return res
	#----------------------------------------------------------------------
	def javaScriptConfirm(self,originatingFrame,msg):
		"""
		javaScriptConfirm(originatingFrame,msg)
			originatingFrame=QtWebKit.QWebFrame
			msg=unicode

		This function is called whenever a JavaScript program running inside frame calls the confirm() function with the message, msg
		Returns true if the user confirms the message; otherwise returns false.
		The default implementation executes the query using QMessageBox::information with QMessageBox.Yes and QMessageBox.No buttons.
		"""
		res = super(QWebPage,self).javaScriptConfirm(originatingFrame,msg)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def javaScriptConsoleMessage(self,message,lineNumber,sourceID):
		"""
		javaScriptConsoleMessage(message,lineNumber,sourceID)
			message=unicode
			lineNumber=QtCore.int
			sourceID=unicode

		This function is called whenever a JavaScript program tries to print a message to the web browsers console.
		For example in case of evaluation errors the source URL may be provided in sourceID as well as the lineNumber .
		The default implementation prints nothing.
		"""
		res = super(QWebPage,self).javaScriptConsoleMessage(message,lineNumber,sourceID)
		return res
	#----------------------------------------------------------------------
	def javaScriptPrompt(self,originatingFrame,msg,defaultValue):
		"""
		javaScriptPrompt(originatingFrame,msg,defaultValue)
			originatingFrame=QtWebKit.QWebFrame
			msg=unicode
			defaultValue=unicode

		This function is called whenever a JavaScript program running inside frame tries to prompt the user for input
		The program may provide an optional message, msg , as well as a default value for the input in defaultValue .
		If the prompt was cancelled by the user the implementation should return false; otherwise the result should be written to result and true should be returned
		If the prompt was not cancelled by the user, the implementation should return true and the result string must not be null.
		The default implementation uses QInputDialog.getText() .
		"""
		res = super(QWebPage,self).javaScriptPrompt(originatingFrame,msg,defaultValue)
		return res
	#----------------------------------------------------------------------
	def setContentEditable(self,editable):
		"""
		setContentEditable(editable)
			editable=QtCore.bool

		This property holds whether the content in this PySide.QtWebKit.QWebPage is editable or not.
		If this property is enabled the contents of the page can be edited by the user through a visible cursor
		If disabled (the default) only HTML elements in the web page with their contenteditable attribute set are editable.
		"""
		res = super(QWebPage,self).setContentEditable(editable)
		return res
	#----------------------------------------------------------------------
	def setForwardUnsupportedContent(self,forward):
		"""
		setForwardUnsupportedContent(forward)
			forward=QtCore.bool

		This property holds whether PySide.QtWebKit.QWebPage should forward unsupported content.
		If enabled, the PySide.QtWebKit.QWebPage.unsupportedContent() signal is emitted with a network reply that can be used to read the content.
		If disabled, the download of such content is aborted immediately.
		By default unsupported content is not forwarded.
		"""
		res = super(QWebPage,self).setForwardUnsupportedContent(forward)
		return res
	#----------------------------------------------------------------------
	def setLinkDelegationPolicy(self,policy):
		"""
		setLinkDelegationPolicy(policy)
			policy=QtWebKit.QWebPage.LinkDelegationPolicy

		This property holds how PySide.QtWebKit.QWebPage should delegate the handling of links through the PySide.QtWebKit.QWebPage.linkClicked() signal.
		The default is to delegate no links.
		"""
		res = super(QWebPage,self).setLinkDelegationPolicy(policy)
		return res
	#----------------------------------------------------------------------
	def setNetworkAccessManager(self,manager):
		"""
		setNetworkAccessManager(manager)
			manager=QtNetwork.QNetworkAccessManager

		Sets the PySide.QtNetwork.QNetworkAccessManager manager responsible for serving network requests for this PySide.QtWebKit.QWebPage .
		"""
		res = super(QWebPage,self).setNetworkAccessManager(manager)
		return res
	#----------------------------------------------------------------------
	def setPalette(self,palette):
		"""
		setPalette(palette)
			palette=QtGui.QPalette

		This property holds the pages palette.
		The base brush of the palette is used to draw the background of the main frame.
		By default, this property contains the applications default palette.
		"""
		res = super(QWebPage,self).setPalette(palette)
		return res
	#----------------------------------------------------------------------
	def setPluginFactory(self,factory):
		"""
		setPluginFactory(factory)
			factory=QtWebKit.QWebPluginFactory

		Sets the PySide.QtWebKit.QWebPluginFactory factory responsible for creating plugins embedded into this PySide.QtWebKit.QWebPage .
		Note: The plugin factory is only used if the QWebSettings.PluginsEnabled attribute is enabled.
		"""
		res = super(QWebPage,self).setPluginFactory(factory)
		return res
	#----------------------------------------------------------------------
	def setPreferredContentsSize(self,size):
		"""
		setPreferredContentsSize(size)
			size=QtCore.QSize

		This property holds the preferred size of the contents.
		If this property is set to a valid size, it is used to lay out the page
		If it is not set (the default), the viewport size is used instead.
		"""
		res = super(QWebPage,self).setPreferredContentsSize(size)
		return res
	#----------------------------------------------------------------------
	def setView(self,view):
		"""
		setView(view)
			view=QtGui.QWidget

		Sets the view that is associated with the web page.
		"""
		res = super(QWebPage,self).setView(view)
		return res
	#----------------------------------------------------------------------
	def setViewportSize(self,size):
		"""
		setViewportSize(size)
			size=QtCore.QSize

		This property holds the size of the viewport.
		The size affects for example the visibility of scrollbars if the document is larger than the viewport.
		By default, for a newly-created Web page, this property contains a size with zero width and height.
		"""
		res = super(QWebPage,self).setViewportSize(size)
		return res
	#----------------------------------------------------------------------
	def supportsExtension(self,extension):
		"""
		supportsExtension(extension)
			extension=QtWebKit.QWebPage.Extension

		This virtual function returns true if the web page supports extension ; otherwise false is returned.
		"""
		res = super(QWebPage,self).supportsExtension(extension)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def swallowContextMenuEvent(self,event):
		"""
		swallowContextMenuEvent(event)
			event=QtGui.QContextMenuEvent

		Filters the context menu event, event , through handlers for scrollbars and custom event handlers in the web page
		Returns true if the event was handled; otherwise false.
		A web page may swallow a context menu event through a custom event handler, allowing for context menus to be implemented in HTML/JavaScript
		This is used by Google Maps, for example.
		"""
		res = super(QWebPage,self).swallowContextMenuEvent(event)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def triggerAction(self,action,checked=None):
		"""
		triggerAction(action,checked=None)
			action=QtWebKit.QWebPage.WebAction
			checked=QtCore.bool

		This function can be called to trigger the specified action
		It is also called by QtWebKit if the user triggers the action, for example through a context menu item.
		If action is a checkable action then checked specified whether the action is toggled or not.
		"""
		res = super(QWebPage,self).triggerAction(action,checked)
		return res
	#----------------------------------------------------------------------
	def updatePositionDependentActions(self,pos):
		"""
		updatePositionDependentActions(pos)
			pos=QtCore.QPoint

		Updates the pages actions depending on the position pos
		For example if pos is over an image element the CopyImageToClipboard action is enabled.
		"""
		res = super(QWebPage,self).updatePositionDependentActions(pos)
		return res
	#----------------------------------------------------------------------
	def userAgentForUrl(self,url):
		"""
		userAgentForUrl(url)
			url=QtCore.QUrl

		This function is called when a user agent for HTTP requests is needed
		You can reimplement this function to dynamically return different user agents for different URLs, based on the url parameter.
		The default implementation returns the following value:
		Mozilla/5.0 (%Platform%; %Security%; %Subplatform%; %Locale%) AppleWebKit/%WebKitVersion% (KHTML, like Gecko) %AppVersion Safari/%WebKitVersion%
		On mobile platforms such as Symbian S60 and Maemo, Mobile Safari is used instead of Safari.
		In this string the following values are replaced at run-time:
		"""
		res = super(QWebPage,self).userAgentForUrl(url)
		return res

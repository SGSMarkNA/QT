from PySide import QtGui, QtCore

class QTextBrowser(QtGui.QTextBrowser):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextBrowser,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def backward(self):
		"""
		Changes the document displayed to the previous document in the list of documents built by navigating links
		Does nothing if there is no previous document.
		"""
		res = super(QTextBrowser,self).backward()
		return res
	#----------------------------------------------------------------------
	def backwardHistoryCount(self):
		"""
		Returns the number of locations backward in the history.
		"""
		res = super(QTextBrowser,self).backwardHistoryCount()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def clearHistory(self):
		"""
		Clears the history of visited documents and disables the forward and backward navigation.
		"""
		res = super(QTextBrowser,self).clearHistory()
		return res
	#----------------------------------------------------------------------
	def forward(self):
		"""
		Changes the document displayed to the next document in the list of documents built by navigating links
		Does nothing if there is no next document.
		"""
		res = super(QTextBrowser,self).forward()
		return res
	#----------------------------------------------------------------------
	def forwardHistoryCount(self):
		"""
		Returns the number of locations forward in the history.
		"""
		res = super(QTextBrowser,self).forwardHistoryCount()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def historyChanged(self):
		"""

		"""
		res = super(QTextBrowser,self).historyChanged()
		return res
	#----------------------------------------------------------------------
	def home(self):
		"""
		Changes the document displayed to be the first document from the history.
		"""
		res = super(QTextBrowser,self).home()
		return res
	#----------------------------------------------------------------------
	def isBackwardAvailable(self):
		"""
		Returns true if the text browser can go backward in the document history using PySide.QtGui.QTextBrowser.backward() .
		"""
		res = super(QTextBrowser,self).isBackwardAvailable()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isForwardAvailable(self):
		"""
		Returns true if the text browser can go forward in the document history using PySide.QtGui.QTextBrowser.forward() .
		"""
		res = super(QTextBrowser,self).isForwardAvailable()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def openExternalLinks(self):
		"""
		Specifies whether PySide.QtGui.QTextBrowser should automatically open links to external sources using QDesktopServices.openUrl() instead of emitting the anchorClicked signal
		Links are considered external if their scheme is neither file or qrc.
		The default value is false.
		"""
		res = super(QTextBrowser,self).openExternalLinks()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def openLinks(self):
		"""
		This property specifies whether PySide.QtGui.QTextBrowser should automatically open links the user tries to activate by mouse or keyboard.
		Regardless of the value of this property the anchorClicked signal is always emitted.
		The default value is true.
		"""
		res = super(QTextBrowser,self).openLinks()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def reload(self):
		"""
		Reloads the current set source.
		"""
		res = super(QTextBrowser,self).reload()
		return res
	#----------------------------------------------------------------------
	def searchPaths(self):
		"""
		This property holds the search paths used by the text browser to find supporting content.
		PySide.QtGui.QTextBrowser uses this list to locate images and documents.
		By default, this property contains an empty string list.
		"""
		res = super(QTextBrowser,self).searchPaths()
		return res
	#----------------------------------------------------------------------
	def source(self):
		"""
		This property holds the name of the displayed document..
		This is a an invalid url if no document is displayed or if the source is unknown.
		When setting this property PySide.QtGui.QTextBrowser tries to find a document with the specified name in the paths of the PySide.QtGui.QTextBrowser.searchPaths() property and directory of the current source, unless the value is an absolute file path
		It also checks for optional anchors and scrolls the document accordingly
		If the first tag in the document is <qt type=detail> , the document is displayed as a popup rather than as new document in the browser window itself
		Otherwise, the document is displayed normally in the text browser with the text set to the contents of the named document with PySide.QtGui.QTextEdit.setHtml() .
		By default, this property contains an empty URL.
		"""
		res = super(QTextBrowser,self).source()
		isinstance(res,QtCore.QUrl)
		return res
	#----------------------------------------------------------------------
	def historyTitle(self,arg__1):
		"""
		historyTitle(arg__1)
			arg__1=QtCore.int

		Returns the PySide.QtGui.QTextEdit.documentTitle() of the HistoryItem.
		"""
		res = super(QTextBrowser,self).historyTitle(arg__1)
		return res
	#----------------------------------------------------------------------
	def historyUrl(self,arg__1):
		"""
		historyUrl(arg__1)
			arg__1=QtCore.int

		Returns the url of the HistoryItem.
		"""
		res = super(QTextBrowser,self).historyUrl(arg__1)
		isinstance(res,QtCore.QUrl)
		return res
	#----------------------------------------------------------------------
	def setOpenExternalLinks(self,open):
		"""
		setOpenExternalLinks(open)
			open=QtCore.bool

		Specifies whether PySide.QtGui.QTextBrowser should automatically open links to external sources using QDesktopServices.openUrl() instead of emitting the anchorClicked signal
		Links are considered external if their scheme is neither file or qrc.
		The default value is false.
		"""
		res = super(QTextBrowser,self).setOpenExternalLinks(open)
		return res
	#----------------------------------------------------------------------
	def setOpenLinks(self,open):
		"""
		setOpenLinks(open)
			open=QtCore.bool

		This property specifies whether PySide.QtGui.QTextBrowser should automatically open links the user tries to activate by mouse or keyboard.
		Regardless of the value of this property the anchorClicked signal is always emitted.
		The default value is true.
		"""
		res = super(QTextBrowser,self).setOpenLinks(open)
		return res
	#----------------------------------------------------------------------
	def setSearchPaths(self,paths):
		"""
		setSearchPaths(paths)
			paths=list

		This property holds the search paths used by the text browser to find supporting content.
		PySide.QtGui.QTextBrowser uses this list to locate images and documents.
		By default, this property contains an empty string list.
		"""
		res = super(QTextBrowser,self).setSearchPaths(paths)
		return res
	#----------------------------------------------------------------------
	def setSource(self,name):
		"""
		setSource(name)
			name=QtCore.QUrl

		This property holds the name of the displayed document..
		This is a an invalid url if no document is displayed or if the source is unknown.
		When setting this property PySide.QtGui.QTextBrowser tries to find a document with the specified name in the paths of the PySide.QtGui.QTextBrowser.searchPaths() property and directory of the current source, unless the value is an absolute file path
		It also checks for optional anchors and scrolls the document accordingly
		If the first tag in the document is <qt type=detail> , the document is displayed as a popup rather than as new document in the browser window itself
		Otherwise, the document is displayed normally in the text browser with the text set to the contents of the named document with PySide.QtGui.QTextEdit.setHtml() .
		By default, this property contains an empty URL.
		"""
		res = super(QTextBrowser,self).setSource(name)
		return res

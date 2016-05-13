from PySide import QtGui, QtCore

class QWebHitTestResult(QtWebKit.QWebHitTestResult):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QWebHitTestResult,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def alternateText(self):
		"""
		Returns the alternate text of the element
		This corresponds to the HTML alt attribute.
		"""
		res = super(QWebHitTestResult,self).alternateText()
		return res
	#----------------------------------------------------------------------
	def boundingRect(self):
		"""
		Returns the bounding rect of the element.
		"""
		res = super(QWebHitTestResult,self).boundingRect()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def element(self):
		"""
		Returns the underlying DOM element as PySide.QtWebKit.QWebElement .
		"""
		res = super(QWebHitTestResult,self).element()
		isinstance(res,QtWebKit.QWebElement)
		return res
	#----------------------------------------------------------------------
	def enclosingBlockElement(self):
		"""
		Returns the block element that encloses the element hit.
		A block element is an element that is rendered using the CSS block style
		This includes for example text paragraphs.
		"""
		res = super(QWebHitTestResult,self).enclosingBlockElement()
		isinstance(res,QtWebKit.QWebElement)
		return res
	#----------------------------------------------------------------------
	def frame(self):
		"""
		Returns the frame the hit test was executed in.
		"""
		res = super(QWebHitTestResult,self).frame()
		isinstance(res,QtWebKit.QWebFrame)
		return res
	#----------------------------------------------------------------------
	def imageUrl(self):
		"""
		Returns the url of the image.
		"""
		res = super(QWebHitTestResult,self).imageUrl()
		isinstance(res,QtCore.QUrl)
		return res
	#----------------------------------------------------------------------
	def isContentEditable(self):
		"""
		Returns true if the content is editable by the user; otherwise returns false.
		"""
		res = super(QWebHitTestResult,self).isContentEditable()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isContentSelected(self):
		"""
		Returns true if the content tested is part of the selection; otherwise returns false.
		"""
		res = super(QWebHitTestResult,self).isContentSelected()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if the hit test result is null; otherwise returns false.
		"""
		res = super(QWebHitTestResult,self).isNull()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def linkElement(self):
		"""
		Returns the element that represents the link.
		"""
		res = super(QWebHitTestResult,self).linkElement()
		isinstance(res,QtWebKit.QWebElement)
		return res
	#----------------------------------------------------------------------
	def linkTargetFrame(self):
		"""
		Returns the frame that will load the link if it is activated.
		"""
		res = super(QWebHitTestResult,self).linkTargetFrame()
		isinstance(res,QtWebKit.QWebFrame)
		return res
	#----------------------------------------------------------------------
	def linkText(self):
		"""
		Returns the text of the link.
		"""
		res = super(QWebHitTestResult,self).linkText()
		return res
	#----------------------------------------------------------------------
	def linkTitle(self):
		"""
		Returns the title of the link.
		"""
		res = super(QWebHitTestResult,self).linkTitle()
		isinstance(res,QtCore.QUrl)
		return res
	#----------------------------------------------------------------------
	def linkUrl(self):
		"""
		Returns the url to which the link points to.
		"""
		res = super(QWebHitTestResult,self).linkUrl()
		isinstance(res,QtCore.QUrl)
		return res
	#----------------------------------------------------------------------
	def pixmap(self):
		"""
		Returns a PySide.QtGui.QPixmap containing the image
		A null pixmap is returned if the element being tested is not an image.
		"""
		res = super(QWebHitTestResult,self).pixmap()
		isinstance(res,QtGui.QPixmap)
		return res
	#----------------------------------------------------------------------
	def pos(self):
		"""
		Returns the position where the hit test occured.
		"""
		res = super(QWebHitTestResult,self).pos()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def title(self):
		"""
		Returns the title of the nearest enclosing HTML element.
		"""
		res = super(QWebHitTestResult,self).title()
		return res

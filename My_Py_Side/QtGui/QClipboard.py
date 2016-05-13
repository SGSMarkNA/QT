from PySide import QtGui, QtCore

class QClipboard(QtGui.QClipboard):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QClipboard,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def dataChanged(self):
		"""

		"""
		res = super(QClipboard,self).dataChanged()
		return res
	#----------------------------------------------------------------------
	def findBufferChanged(self):
		"""

		"""
		res = super(QClipboard,self).findBufferChanged()
		return res
	#----------------------------------------------------------------------
	def ownsClipboard(self):
		"""
		Returns true if this clipboard object owns the clipboard data; otherwise returns false.
		"""
		res = super(QClipboard,self).ownsClipboard()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def ownsFindBuffer(self):
		"""
		Returns true if this clipboard object owns the find buffer data; otherwise returns false.
		"""
		res = super(QClipboard,self).ownsFindBuffer()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def ownsSelection(self):
		"""
		Returns true if this clipboard object owns the mouse selection data; otherwise returns false.
		"""
		res = super(QClipboard,self).ownsSelection()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def selectionChanged(self):
		"""

		"""
		res = super(QClipboard,self).selectionChanged()
		return res
	#----------------------------------------------------------------------
	def supportsFindBuffer(self):
		"""
		Returns true if the clipboard supports a separate search buffer; otherwise returns false.
		"""
		res = super(QClipboard,self).supportsFindBuffer()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def supportsSelection(self):
		"""
		Returns true if the clipboard supports mouse selection; otherwise returns false.
		"""
		res = super(QClipboard,self).supportsSelection()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def clear(self,mode=None):
		"""
		clear(mode=None)
			mode=QtGui.QClipboard.Mode

		Clear the clipboard contents.
		The mode argument is used to control which part of the system clipboard is used
		If mode is QClipboard.Clipboard , this function clears the global clipboard contents
		If mode is QClipboard.Selection , this function clears the global mouse selection contents
		If mode is QClipboard.FindBuffer , this function clears the search string buffer.
		"""
		res = super(QClipboard,self).clear(mode)
		return res
	#----------------------------------------------------------------------
	def emitChanged(self,mode):
		"""
		emitChanged(mode)
			mode=QtGui.QClipboard.Mode


		"""
		res = super(QClipboard,self).emitChanged(mode)
		return res
	#----------------------------------------------------------------------
	def image(self,mode=None):
		"""
		image(mode=None)
			mode=QtGui.QClipboard.Mode

		Returns the clipboard image, or returns a null image if the clipboard does not contain an image or if it contains an image in an unsupported image format.
		The mode argument is used to control which part of the system clipboard is used
		If mode is QClipboard.Clipboard , the image is retrieved from the global clipboard
		If mode is QClipboard.Selection , the image is retrieved from the global mouse selection.
		"""
		res = super(QClipboard,self).image(mode)
		isinstance(res,QtGui.QImage)
		return res
	#----------------------------------------------------------------------
	def mimeData(self,mode=None):
		"""
		mimeData(mode=None)
			mode=QtGui.QClipboard.Mode

		Returns a reference to a PySide.QtCore.QMimeData representation of the current clipboard data.
		The mode argument is used to control which part of the system clipboard is used
		If mode is QClipboard.Clipboard , the data is retrieved from the global clipboard
		If mode is QClipboard.Selection , the data is retrieved from the global mouse selection
		If mode is QClipboard.FindBuffer , the data is retrieved from the search string buffer.
		The PySide.QtGui.QClipboard.text() , PySide.QtGui.QClipboard.image() , and PySide.QtGui.QClipboard.pixmap() functions are simpler wrappers for retrieving text, image, and pixmap data.
		"""
		res = super(QClipboard,self).mimeData(mode)
		isinstance(res,QtCore.QMimeData)
		return res
	#----------------------------------------------------------------------
	def ownsMode(self,mode):
		"""
		ownsMode(mode)
			mode=QtGui.QClipboard.Mode


		"""
		res = super(QClipboard,self).ownsMode(mode)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def pixmap(self,mode=None):
		"""
		pixmap(mode=None)
			mode=QtGui.QClipboard.Mode

		Returns the clipboard pixmap, or null if the clipboard does not contain a pixmap
		Note that this can lose information
		For example, if the image is 24-bit and the display is 8-bit, the result is converted to 8 bits, and if the image has an alpha channel, the result just has a mask.
		The mode argument is used to control which part of the system clipboard is used
		If mode is QClipboard.Clipboard , the pixmap is retrieved from the global clipboard
		If mode is QClipboard.Selection , the pixmap is retrieved from the global mouse selection.
		"""
		res = super(QClipboard,self).pixmap(mode)
		isinstance(res,QtGui.QPixmap)
		return res
	#----------------------------------------------------------------------
	def setImage(self,arg__1,mode=None):
		"""
		setImage(arg__1,mode=None)
			arg__1=QtGui.QImage
			mode=QtGui.QClipboard.Mode

		Copies the image into the clipboard.
		The mode argument is used to control which part of the system clipboard is used
		If mode is QClipboard.Clipboard , the image is stored in the global clipboard
		If mode is QClipboard.Selection , the data is stored in the global mouse selection.
		This is shorthand for:
		"""
		res = super(QClipboard,self).setImage(arg__1,mode)
		return res
	#----------------------------------------------------------------------
	def setMimeData(self,data,mode=None):
		"""
		setMimeData(data,mode=None)
			data=QtCore.QMimeData
			mode=QtGui.QClipboard.Mode

		Sets the clipboard data to src
		Ownership of the data is transferred to the clipboard
		If you want to remove the data either call PySide.QtGui.QClipboard.clear() or call PySide.QtGui.QClipboard.setMimeData() again with new data.
		The mode argument is used to control which part of the system clipboard is used
		If mode is QClipboard.Clipboard , the data is stored in the global clipboard
		If mode is QClipboard.Selection , the data is stored in the global mouse selection
		If mode is QClipboard.FindBuffer , the data is stored in the search string buffer.
		The PySide.QtGui.QClipboard.setText() , PySide.QtGui.QClipboard.setImage() and PySide.QtGui.QClipboard.setPixmap() functions are simpler wrappers for setting text, image and pixmap data respectively.
		"""
		res = super(QClipboard,self).setMimeData(data,mode)
		return res
	#----------------------------------------------------------------------
	def setPixmap(self,arg__1,mode=None):
		"""
		setPixmap(arg__1,mode=None)
			arg__1=QtGui.QPixmap
			mode=QtGui.QClipboard.Mode

		Copies pixmap into the clipboard
		Note that this is slower than PySide.QtGui.QClipboard.setImage() because it needs to convert the PySide.QtGui.QPixmap to a PySide.QtGui.QImage first.
		The mode argument is used to control which part of the system clipboard is used
		If mode is QClipboard.Clipboard , the pixmap is stored in the global clipboard
		If mode is QClipboard.Selection , the pixmap is stored in the global mouse selection.
		"""
		res = super(QClipboard,self).setPixmap(arg__1,mode)
		return res
	#----------------------------------------------------------------------
	def setText(self,arg__1,mode=None):
		"""
		setText(arg__1,mode=None)
			arg__1=unicode
			mode=QtGui.QClipboard.Mode

		Copies text into the clipboard as plain text.
		The mode argument is used to control which part of the system clipboard is used
		If mode is QClipboard.Clipboard , the text is stored in the global clipboard
		If mode is QClipboard.Selection , the text is stored in the global mouse selection
		If mode is QClipboard.FindBuffer , the text is stored in the search string buffer.
		"""
		res = super(QClipboard,self).setText(arg__1,mode)
		return res
	#----------------------------------------------------------------------
	def supportsMode(self,mode):
		"""
		supportsMode(mode)
			mode=QtGui.QClipboard.Mode


		"""
		res = super(QClipboard,self).supportsMode(mode)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def text(self,*args,**kwargs):
		"""
		text(subtype,mode=None)
			subtype=unicode
			mode=QtGui.QClipboard.Mode

		text(mode=None)
			mode=QtGui.QClipboard.Mode

		This is an overloaded function.
		Returns the clipboard text in subtype subtype , or an empty string if the clipboard does not contain any text
		If subtype is null, any subtype is acceptable, and subtype is set to the chosen subtype.
		The mode argument is used to control which part of the system clipboard is used
		If mode is QClipboard.Clipboard , the text is retrieved from the global clipboard
		If mode is QClipboard.Selection , the text is retrieved from the global mouse selection.
		Common values for subtype are plain and html.
		Note that calling this function repeatedly, for instance from a key event handler, may be slow
		In such cases, you should use the dataChanged() signal instead.
		"""
		res = super(QClipboard,self).text(*args,**kwargs)
		return res

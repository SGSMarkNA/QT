from PySide import QtGui, QtCore

class QPrintPreviewWidget(QtGui.QPrintPreviewWidget):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QPrintPreviewWidget,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def currentPage(self):
		"""
		Returns the currently viewed page in the preview.
		"""
		res = super(QPrintPreviewWidget,self).currentPage()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def numPages(self):
		"""
		Returns the number of pages in the preview.
		"""
		res = super(QPrintPreviewWidget,self).numPages()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def orientation(self):
		"""
		Returns the current orientation of the preview
		This value is obtained from the PySide.QtGui.QPrinter object associated with the preview.
		"""
		res = super(QPrintPreviewWidget,self).orientation()
		isinstance(res,QtGui.QPrinter.Orientation)
		return res
	#----------------------------------------------------------------------
	def pageCount(self):
		"""
		Returns the number of pages in the preview.
		"""
		res = super(QPrintPreviewWidget,self).pageCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def previewChanged(self):
		"""

		"""
		res = super(QPrintPreviewWidget,self).previewChanged()
		return res
	#----------------------------------------------------------------------
	def viewMode(self):
		"""
		Returns the current view mode
		The default view mode is SinglePageView .
		"""
		res = super(QPrintPreviewWidget,self).viewMode()
		isinstance(res,QtGui.QPrintPreviewWidget.ViewMode)
		return res
	#----------------------------------------------------------------------
	def zoomFactor(self):
		"""
		Returns the zoom factor of the view.
		"""
		res = super(QPrintPreviewWidget,self).zoomFactor()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def zoomMode(self):
		"""
		Returns the current zoom mode.
		"""
		res = super(QPrintPreviewWidget,self).zoomMode()
		isinstance(res,QtGui.QPrintPreviewWidget.ZoomMode)
		return res

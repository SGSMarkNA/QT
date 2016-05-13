from PySide import QtGui, QtCore

class QSplitterHandle(QtGui.QSplitterHandle):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSplitterHandle,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def opaqueResize(self):
		"""
		Returns true if widgets are resized dynamically (opaquely), otherwise returns false
		This value is controlled by the PySide.QtGui.QSplitter .
		"""
		res = super(QSplitterHandle,self).opaqueResize()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def orientation(self):
		"""
		Returns the handles orientation
		This is usually propagated from the PySide.QtGui.QSplitter .
		"""
		res = super(QSplitterHandle,self).orientation()
		isinstance(res,QtCore.Qt.Orientation)
		return res
	#----------------------------------------------------------------------
	def splitter(self):
		"""
		Returns the splitter associated with this splitter handle.
		"""
		res = super(QSplitterHandle,self).splitter()
		isinstance(res,QtGui.QSplitter)
		return res
	#----------------------------------------------------------------------
	def closestLegalPosition(self,p):
		"""
		closestLegalPosition(p)
			p=QtCore.int

		Returns the closest legal position to pos of the splitter handle
		The positions are measured from the left or top edge of the splitter, even for right-to-left languages.
		"""
		res = super(QSplitterHandle,self).closestLegalPosition(p)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def moveSplitter(self,p):
		"""
		moveSplitter(p)
			p=QtCore.int

		Tells the splitter to move this handle to position pos , which is the distance from the left or top edge of the widget.
		Note that pos is also measured from the left (or top) for right-to-left languages
		This function will map pos to the appropriate position before calling QSplitter.moveSplitter() .
		"""
		res = super(QSplitterHandle,self).moveSplitter(p)
		return res
	#----------------------------------------------------------------------
	def setOrientation(self,o):
		"""
		setOrientation(o)
			o=QtCore.Qt.Orientation


		"""
		res = super(QSplitterHandle,self).setOrientation(o)
		return res

from PySide import QtGui, QtCore

class QGLColormap(QtOpenGL.QGLColormap):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGLColormap,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def detach_helper(self):
		"""

		"""
		res = super(QGLColormap,self).detach_helper()
		return res
	#----------------------------------------------------------------------
	def handle(self):
		"""
		Returns the handle for this color map.
		"""
		res = super(QGLColormap,self).handle()
		isinstance(res,QtCore.Qt::HANDLE)
		return res
	#----------------------------------------------------------------------
	def isEmpty(self):
		"""
		Returns true if the colormap is empty or it is not in use by a PySide.QtOpenGL.QGLWidget ; otherwise returns false.
		A colormap with no color values set is considered to be empty
		For historical reasons, a colormap that has color values set but which is not in use by a PySide.QtOpenGL.QGLWidget is also considered empty.
		Compare PySide.QtOpenGL.QGLColormap.size() with zero to determine if the colormap is empty regardless of whether it is in use by a PySide.QtOpenGL.QGLWidget or not.
		"""
		res = super(QGLColormap,self).isEmpty()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""
		Returns the number of colorcells in the colormap.
		"""
		res = super(QGLColormap,self).size()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def entryColor(self,idx):
		"""
		entryColor(idx)
			idx=QtCore.int

		Returns the QRgb value in the colorcell with index idx .
		"""
		res = super(QGLColormap,self).entryColor(idx)
		isinstance(res,QtGui.QColor)
		return res
	#----------------------------------------------------------------------
	def entryRgb(self,idx):
		"""
		entryRgb(idx)
			idx=QtCore.int

		Returns the QRgb value in the colorcell with index idx .
		"""
		res = super(QGLColormap,self).entryRgb(idx)
		return res
	#----------------------------------------------------------------------
	def find(self,color):
		"""
		find(color)
			color=long


		"""
		res = super(QGLColormap,self).find(color)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def findNearest(self,color):
		"""
		findNearest(color)
			color=long


		"""
		res = super(QGLColormap,self).findNearest(color)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def setEntries(self,count,colors,base=None):
		"""
		setEntries(count,colors,base=None)
			count=QtCore.int
			colors=long
			base=QtCore.int


		"""
		res = super(QGLColormap,self).setEntries(count,colors,base)
		return res
	#----------------------------------------------------------------------
	def setEntry(self,*args,**kwargs):
		"""
		setEntry(idx,color)
			idx=QtCore.int
			color=long

		setEntry(idx,color)
			idx=QtCore.int
			color=QtGui.QColor


		"""
		res = super(QGLColormap,self).setEntry(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setHandle(self,ahandle):
		"""
		setHandle(ahandle)
			ahandle=QtCore.Qt::HANDLE


		"""
		res = super(QGLColormap,self).setHandle(ahandle)
		return res

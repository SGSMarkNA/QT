from PySide import QtGui, QtCore

class QX11Info(QtGui.QX11Info):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QX11Info,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def cells(self):
		"""
		Returns the number of cells.
		"""
		res = super(QX11Info,self).cells()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def colormap(self):
		"""
		Returns a handle for the color map.
		"""
		res = super(QX11Info,self).colormap()
		isinstance(res,QtCore.Qt::HANDLE)
		return res
	#----------------------------------------------------------------------
	def defaultColormap(self):
		"""
		Returns true if there is a default color map; otherwise returns false.
		"""
		res = super(QX11Info,self).defaultColormap()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def defaultVisual(self):
		"""
		Returns true if there is a default visual; otherwise returns false.
		"""
		res = super(QX11Info,self).defaultVisual()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def depth(self):
		"""
		Returns the color depth (bits per pixel) of the X display.
		"""
		res = super(QX11Info,self).depth()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def screen(self):
		"""
		Returns the number of the screen currently in use.
		The return value is an X screen number
		Be aware that if the users system uses Xinerama (as opposed to traditional X11 multiscreen), there is only one X screen
		Use PySide.QtGui.QDesktopWidget to query for information about Xinerama screens.
		"""
		res = super(QX11Info,self).screen()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def visual(self):
		"""
		Returns the current visual.
		"""
		res = super(QX11Info,self).visual()
		isinstance(res,void)
		return res
	#----------------------------------------------------------------------
	def cloneX11Data(self,arg__1):
		"""
		cloneX11Data(arg__1)
			arg__1=QtGui.QPaintDevice

		Makes a deep copy of the X11-specific data of fromDevice , if it is not null
		Otherwise this function sets it to null.
		"""
		res = super(QX11Info,self).cloneX11Data(arg__1)
		return res
	#----------------------------------------------------------------------
	def copyX11Data(self,arg__1):
		"""
		copyX11Data(arg__1)
			arg__1=QtGui.QPaintDevice

		Makes a shallow copy of the X11-specific data of fromDevice , if it is not null
		Otherwise this function sets it to null.
		"""
		res = super(QX11Info,self).copyX11Data(arg__1)
		return res

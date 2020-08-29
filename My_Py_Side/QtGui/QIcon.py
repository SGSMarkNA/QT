from PySide import QtGui, QtCore

class QIcon(QtGui.QIcon):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QIcon,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def cacheKey(self):
		"""
		Returns a number that identifies the contents of this PySide.QtGui.QIcon object
		Distinct PySide.QtGui.QIcon objects can have the same key if they refer to the same contents.
		The PySide.QtGui.QIcon.cacheKey() will change when the icon is altered via PySide.QtGui.QIcon.addPixmap() or PySide.QtGui.QIcon.addFile() .
		Cache keys are mostly useful in conjunction with caching.
		"""
		res = super(QIcon,self).cacheKey()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if the icon is empty; otherwise returns false.
		An icon is empty if it has neither a pixmap nor a filename.
		Note: Even a non-null icon might not be able to create valid pixmaps, eg
		if the file does not exist or cannot be read.
		"""
		res = super(QIcon,self).isNull()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def name(self):
		"""
		Returns the name used to create the icon, if available.
		Depending on the way the icon was created, it may have an associated name
		This is the case for icons created with PySide.QtGui.QIcon.fromTheme() or icons using a PySide.QtGui.QIconEngine which supports the QIconEngineV2.IconNameHook .
		"""
		res = super(QIcon,self).name()
		return res
	#----------------------------------------------------------------------
	def actualSize(self,size,mode=None,state=None):
		"""
		actualSize(size,mode=None,state=None)
			size=QtCore.QSize
			mode=QtGui.QIcon.Mode
			state=QtGui.QIcon.State

		Returns the actual size of the icon for the requested size , mode , and state
		The result might be smaller than requested, but never larger.
		"""
		res = super(QIcon,self).actualSize(size,mode,state)
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def addFile(self,fileName,size=None,mode=None,state=None):
		"""
		addFile(fileName,size=None,mode=None,state=None)
			fileName=unicode
			size=QtCore.QSize
			mode=QtGui.QIcon.Mode
			state=QtGui.QIcon.State

		Adds an image from the file with the given fileName to the icon, as a specialization for size , mode and state
		The file will be loaded on demand
		Note: custom icon engines are free to ignore additionally added pixmaps.
		If fileName contains a relative path (e.g
		the filename only) the relevant file must be found relative to the runtime working directory.
		The file name can be either refer to an actual file on disk or to one of the applications embedded resources
		See the Resource System overview for details on how to embed images and other resource files in the applications executable.
		Use the QImageReader.supportedImageFormats() and QImageWriter.supportedImageFormats() functions to retrieve a complete list of the supported file formats.
		Note: When you add a non-empty filename to a PySide.QtGui.QIcon , the icon becomes non-null, even if the file doesnt exist or points to a corrupt file.
		"""
		res = super(QIcon,self).addFile(fileName,size,mode,state)
		return res
	#----------------------------------------------------------------------
	def addPixmap(self,pixmap,mode=None,state=None):
		"""
		addPixmap(pixmap,mode=None,state=None)
			pixmap=QtGui.QPixmap
			mode=QtGui.QIcon.Mode
			state=QtGui.QIcon.State

		Adds pixmap to the icon, as a specialization for mode and state .
		Custom icon engines are free to ignore additionally added pixmaps.
		"""
		res = super(QIcon,self).addPixmap(pixmap,mode,state)
		return res
	#----------------------------------------------------------------------
	def availableSizes(self,mode=None,state=None):
		"""
		availableSizes(mode=None,state=None)
			mode=QtGui.QIcon.Mode
			state=QtGui.QIcon.State

		Returns a list of available icon sizes for the specified mode and state .
		"""
		res = super(QIcon,self).availableSizes(mode,state)
		return res
	#----------------------------------------------------------------------
	def paint(self,*args,**kwargs):
		"""
		paint(painter,x,y,w,h,alignment=None,mode=None,state=None)
			painter=QtGui.QPainter
			x=QtCore.int
			y=QtCore.int
			w=QtCore.int
			h=QtCore.int
			alignment=QtCore.Qt.Alignment
			mode=QtGui.QIcon.Mode
			state=QtGui.QIcon.State

		paint(painter,rect,alignment=None,mode=None,state=None)
			painter=QtGui.QPainter
			rect=QtCore.QRect
			alignment=QtCore.Qt.Alignment
			mode=QtGui.QIcon.Mode
			state=QtGui.QIcon.State


		"""
		res = super(QIcon,self).paint(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def pixmap(self,*args,**kwargs):
		"""
		pixmap(w,h,mode=None,state=None)
			w=QtCore.int
			h=QtCore.int
			mode=QtGui.QIcon.Mode
			state=QtGui.QIcon.State

		pixmap(extent,mode=None,state=None)
			extent=QtCore.int
			mode=QtGui.QIcon.Mode
			state=QtGui.QIcon.State

		pixmap(size,mode=None,state=None)
			size=QtCore.QSize
			mode=QtGui.QIcon.Mode
			state=QtGui.QIcon.State

		This is an overloaded function.
		Returns a pixmap of size PySide.QtCore.QSize (w , h )
		The pixmap might be smaller than requested, but never larger.
		"""
		res = super(QIcon,self).pixmap(*args,**kwargs)
		isinstance(res,QtGui.QPixmap)
		return res

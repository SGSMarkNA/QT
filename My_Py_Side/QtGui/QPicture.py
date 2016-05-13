from PySide import QtGui, QtCore

class QPicture(QtGui.QPicture):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QPicture,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def boundingRect(self):
		"""
		Returns the pictures bounding rectangle or an invalid rectangle if the picture contains no data.
		"""
		res = super(QPicture,self).boundingRect()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def data(self):
		"""
		Returns a pointer to the picture data
		The pointer is only valid until the next non-const function is called on this picture
		The returned pointer is 0 if the picture contains no data.
		"""
		res = super(QPicture,self).data()
		return res
	#----------------------------------------------------------------------
	def detach_helper(self):
		"""

		"""
		res = super(QPicture,self).detach_helper()
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if the picture contains no data; otherwise returns false.
		"""
		res = super(QPicture,self).isNull()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""
		Returns the size of the picture data.
		"""
		res = super(QPicture,self).size()
		isinstance(res,QtCore.uint)
		return res
	#----------------------------------------------------------------------
	def exec(self,p,ds,i):
		"""
		exec(p,ds,i)
			p=QtGui.QPainter
			ds=QtCore.QDataStream
			i=QtCore.int


		"""
		res = super(QPicture,self).exec(p,ds,i)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def load(self,*args,**kwargs):
		"""
		load(fileName,format=None)
			fileName=unicode
			format=str

		load(dev,format=None)
			dev=QtCore.QIODevice
			format=str

		Loads a picture from the file specified by fileName and returns true if successful; otherwise returns false.
		Please note that the format parameter has been deprecated and will have no effect.
		"""
		res = super(QPicture,self).load(*args,**kwargs)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def play(self,p):
		"""
		play(p)
			p=QtGui.QPainter

		Replays the picture using painter , and returns true if successful; otherwise returns false.
		This function does exactly the same as QPainter.drawPicture() with (x, y) = (0, 0).
		"""
		res = super(QPicture,self).play(p)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def save(self,*args,**kwargs):
		"""
		save(fileName,format=None)
			fileName=unicode
			format=str

		save(dev,format=None)
			dev=QtCore.QIODevice
			format=str

		Saves a picture to the file specified by fileName and returns true if successful; otherwise returns false.
		Please note that the format parameter has been deprecated and will have no effect.
		"""
		res = super(QPicture,self).save(*args,**kwargs)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def setBoundingRect(self,r):
		"""
		setBoundingRect(r)
			r=QtCore.QRect

		Sets the pictures bounding rectangle to r
		The automatically calculated value is overridden.
		"""
		res = super(QPicture,self).setBoundingRect(r)
		return res
	#----------------------------------------------------------------------
	def setData(self,data):
		"""
		setData(data)
			data=str

		Sets the picture data directly from data and size
		This function copies the input data.
		"""
		res = super(QPicture,self).setData(data)
		return res

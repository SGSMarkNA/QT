from PySide import QtGui, QtCore

class QBuffer(QtCore.QBuffer):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QBuffer,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def buffer(self):
		"""
		This is an overloaded function.
		This is the same as PySide.QtCore.QBuffer.data() .
		"""
		res = super(QBuffer,self).buffer()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def data(self):
		"""
		Returns the data contained in the buffer.
		This is the same as PySide.QtCore.QBuffer.buffer() .
		"""
		res = super(QBuffer,self).data()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def setBuffer(self,a):
		"""
		setBuffer(a)
			a=QtCore.QByteArray

		Makes PySide.QtCore.QBuffer uses the PySide.QtCore.QByteArray pointed to by byteArray as its internal buffer
		The caller is responsible for ensuring that byteArray remains valid until the PySide.QtCore.QBuffer is destroyed, or until PySide.QtCore.QBuffer.setBuffer() is called to change the buffer
		PySide.QtCore.QBuffer doesnt take ownership of the PySide.QtCore.QByteArray .
		Does nothing if PySide.QtCore.QIODevice.isOpen() is true.
		If you open the buffer in write-only mode or read-write mode and write something into the PySide.QtCore.QBuffer , byteArray will be modified.
		Example:
		If byteArray is 0, the buffer creates its own internal PySide.QtCore.QByteArray to work on
		This byte array is initially empty.
		"""
		res = super(QBuffer,self).setBuffer(a)
		return res
	#----------------------------------------------------------------------
	def setData(self,data):
		"""
		setData(data)
			data=QtCore.QByteArray

		Sets the contents of the internal buffer to be data
		This is the same as assigning data to PySide.QtCore.QBuffer.buffer() .
		Does nothing if PySide.QtCore.QIODevice.isOpen() is true.
		"""
		res = super(QBuffer,self).setData(data)
		return res

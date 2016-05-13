from PySide import QtGui, QtCore

class QBitmap(QtGui.QBitmap):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QBitmap,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Clears the bitmap, setting all its bits to Qt.color0 .
		"""
		res = super(QBitmap,self).clear()
		return res
	#----------------------------------------------------------------------
	def transformed(self,*args,**kwargs):
		"""
		transformed(matrix)
			matrix=QtGui.QTransform

		transformed(arg__1)
			arg__1=QtGui.QMatrix

		Returns a copy of this bitmap, transformed according to the given matrix .
		"""
		res = super(QBitmap,self).transformed(*args,**kwargs)
		isinstance(res,QtGui.QBitmap)
		return res

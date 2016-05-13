from PySide import QtGui, QtCore

class QCursor(QtGui.QCursor):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QCursor,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def bitmap(self):
		"""
		Returns the cursor bitmap, or 0 if it is one of the standard cursors.
		"""
		res = super(QCursor,self).bitmap()
		isinstance(res,QtGui.QBitmap)
		return res
	#----------------------------------------------------------------------
	def hotSpot(self):
		"""
		Returns the cursor hot spot, or (0, 0) if it is one of the standard cursors.
		"""
		res = super(QCursor,self).hotSpot()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def mask(self):
		"""
		Returns the cursor bitmap mask, or 0 if it is one of the standard cursors.
		"""
		res = super(QCursor,self).mask()
		isinstance(res,QtGui.QBitmap)
		return res
	#----------------------------------------------------------------------
	def pixmap(self):
		"""
		Returns the cursor pixmap
		This is only valid if the cursor is a pixmap cursor.
		"""
		res = super(QCursor,self).pixmap()
		isinstance(res,QtGui.QPixmap)
		return res
	#----------------------------------------------------------------------
	def shape(self):
		"""
		Returns the cursor shape identifier
		The return value is one of the Qt.CursorShape enum values (cast to an int).
		"""
		res = super(QCursor,self).shape()
		isinstance(res,QtCore.Qt.CursorShape)
		return res
	#----------------------------------------------------------------------
	def setShape(self,newShape):
		"""
		setShape(newShape)
			newShape=QtCore.Qt.CursorShape


		"""
		res = super(QCursor,self).setShape(newShape)
		return res

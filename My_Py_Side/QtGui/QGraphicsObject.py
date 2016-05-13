from PySide import QtGui, QtCore

class QGraphicsObject(QtGui.QGraphicsObject):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsObject,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def childrenChanged(self):
		"""

		"""
		res = super(QGraphicsObject,self).childrenChanged()
		return res
	#----------------------------------------------------------------------
	def enabledChanged(self):
		"""

		"""
		res = super(QGraphicsObject,self).enabledChanged()
		return res
	#----------------------------------------------------------------------
	def heightChanged(self):
		"""

		"""
		res = super(QGraphicsObject,self).heightChanged()
		return res
	#----------------------------------------------------------------------
	def opacityChanged(self):
		"""

		"""
		res = super(QGraphicsObject,self).opacityChanged()
		return res
	#----------------------------------------------------------------------
	def parentChanged(self):
		"""

		"""
		res = super(QGraphicsObject,self).parentChanged()
		return res
	#----------------------------------------------------------------------
	def rotationChanged(self):
		"""

		"""
		res = super(QGraphicsObject,self).rotationChanged()
		return res
	#----------------------------------------------------------------------
	def scaleChanged(self):
		"""

		"""
		res = super(QGraphicsObject,self).scaleChanged()
		return res
	#----------------------------------------------------------------------
	def visibleChanged(self):
		"""

		"""
		res = super(QGraphicsObject,self).visibleChanged()
		return res
	#----------------------------------------------------------------------
	def widthChanged(self):
		"""

		"""
		res = super(QGraphicsObject,self).widthChanged()
		return res
	#----------------------------------------------------------------------
	def xChanged(self):
		"""

		"""
		res = super(QGraphicsObject,self).xChanged()
		return res
	#----------------------------------------------------------------------
	def yChanged(self):
		"""

		"""
		res = super(QGraphicsObject,self).yChanged()
		return res
	#----------------------------------------------------------------------
	def zChanged(self):
		"""

		"""
		res = super(QGraphicsObject,self).zChanged()
		return res
	#----------------------------------------------------------------------
	def grabGesture(self,type,flags=None):
		"""
		grabGesture(type,flags=None)
			type=QtCore.Qt.GestureType
			flags=QtCore.Qt.GestureFlags


		"""
		res = super(QGraphicsObject,self).grabGesture(type,flags)
		return res
	#----------------------------------------------------------------------
	def ungrabGesture(self,type):
		"""
		ungrabGesture(type)
			type=QtCore.Qt.GestureType


		"""
		res = super(QGraphicsObject,self).ungrabGesture(type)
		return res

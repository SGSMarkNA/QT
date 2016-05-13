from PySide import QtGui, QtCore

class QPropertyAnimation(QtCore.QPropertyAnimation):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QPropertyAnimation,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def propertyName(self):
		"""
		This property holds the target property name for this animation.
		This property defines the target property name for this animation
		The property name is required for the animation to operate.
		"""
		res = super(QPropertyAnimation,self).propertyName()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def targetObject(self):
		"""
		This property holds the target PySide.QtCore.QObject for this animation..
		This property defines the target PySide.QtCore.QObject for this animation.
		"""
		res = super(QPropertyAnimation,self).targetObject()
		isinstance(res,QtCore.QObject)
		return res
	#----------------------------------------------------------------------
	def setPropertyName(self,propertyName):
		"""
		setPropertyName(propertyName)
			propertyName=QtCore.QByteArray

		This property holds the target property name for this animation.
		This property defines the target property name for this animation
		The property name is required for the animation to operate.
		"""
		res = super(QPropertyAnimation,self).setPropertyName(propertyName)
		return res
	#----------------------------------------------------------------------
	def setTargetObject(self,target):
		"""
		setTargetObject(target)
			target=QtCore.QObject

		This property holds the target PySide.QtCore.QObject for this animation..
		This property defines the target PySide.QtCore.QObject for this animation.
		"""
		res = super(QPropertyAnimation,self).setTargetObject(target)
		return res

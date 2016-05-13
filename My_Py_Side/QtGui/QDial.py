from PySide import QtGui, QtCore

class QDial(QtGui.QDial):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDial,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def notchSize(self):
		"""
		This property holds the current notch size.
		The notch size is in range control units, not pixels, and if possible it is a multiple of PySide.QtGui.QAbstractSlider.singleStep() that results in an on-screen notch size near PySide.QtGui.QDial.notchTarget() .
		By default, this property has a value of 1.
		"""
		res = super(QDial,self).notchSize()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def notchTarget(self):
		"""
		This property holds the target number of pixels between notches.
		The notch target is the number of pixels PySide.QtGui.QDial attempts to put between each notch.
		The actual size may differ from the target size.
		The default notch target is 3.7 pixels.
		"""
		res = super(QDial,self).notchTarget()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def notchesVisible(self):
		"""
		This property holds whether the notches are shown.
		If the property is true, a series of notches are drawn around the dial to indicate the range of values available; otherwise no notches are shown.
		By default, this property is disabled.
		"""
		res = super(QDial,self).notchesVisible()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def wrapping(self):
		"""
		This property holds whether wrapping is enabled.
		If true, wrapping is enabled; otherwise some space is inserted at the bottom of the dial to separate the ends of the range of valid values.
		If enabled, the arrow can be oriented at any angle on the dial
		If disabled, the arrow will be restricted to the upper part of the dial; if it is rotated into the space at the bottom of the dial, it will be clamped to the closest end of the valid range of values.
		By default this property is false.
		"""
		res = super(QDial,self).wrapping()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def initStyleOption(self,option):
		"""
		initStyleOption(option)
			option=QtGui.QStyleOptionSlider

		Initialize option with the values from this PySide.QtGui.QDial
		This method is useful for subclasses when they need a PySide.QtGui.QStyleOptionSlider , but dont want to fill in all the information themselves.
		"""
		res = super(QDial,self).initStyleOption(option)
		return res
	#----------------------------------------------------------------------
	def setNotchTarget(self,target):
		"""
		setNotchTarget(target)
			target=QtCore.double


		"""
		res = super(QDial,self).setNotchTarget(target)
		return res

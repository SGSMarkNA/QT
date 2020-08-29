from PySide import QtGui, QtCore

class Phonon(phonon.Phonon):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(Phonon,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def audioOutput(self):
		"""

		"""
		res = super(Phonon,self).audioOutput()
		isinstance(res,phonon.Phonon::AudioOutput)
		return res
	#----------------------------------------------------------------------
	def hasTracking(self):
		"""
		This property holds whether slider tracking is enabled.
		If tracking is enabled (the default), the volume changes while the slider is being dragged
		If tracking is disabled, the volume changes only when the user releases the slider.
		"""
		res = super(Phonon,self).hasTracking()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def iconSize(self):
		"""
		This property holds the icon size used for the mute button/icon..
		The default size is defined by the GUI style.
		"""
		res = super(Phonon,self).iconSize()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def isMuteVisible(self):
		"""
		This property holds whether the mute button/icon next to the slider is visible.
		By default the mute button/icon is visible.
		"""
		res = super(Phonon,self).isMuteVisible()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def maximumVolume(self):
		"""
		This property holds the maximum volume that can be set with this slider.
		By default the maximum value is 1.0 (100%).
		"""
		res = super(Phonon,self).maximumVolume()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def orientation(self):
		"""
		This property holds the orientation of the slider.
		The orientation must be Qt.Vertical (the default) or Qt.Horizontal .
		"""
		res = super(Phonon,self).orientation()
		isinstance(res,QtCore.Qt.Orientation)
		return res
	#----------------------------------------------------------------------
	def pageStep(self):
		"""
		This property holds the page step.
		The larger of two natural steps that a slider provides and typically corresponds to the user pressing PageUp or PageDown.
		Defaults to 5 (5% of the voltage).
		"""
		res = super(Phonon,self).pageStep()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def singleStep(self):
		"""
		This property holds the single step.
		The smaller of two natural steps that a slider provides and typically corresponds to the user pressing an arrow key.
		Defaults to 1 (1% of the voltage).
		"""
		res = super(Phonon,self).singleStep()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def setPageStep(self,milliseconds):
		"""
		setPageStep(milliseconds)
			milliseconds=QtCore.int

		This property holds the page step.
		The larger of two natural steps that a slider provides and typically corresponds to the user pressing PageUp or PageDown.
		Defaults to 5 (5% of the voltage).
		"""
		res = super(Phonon,self).setPageStep(milliseconds)
		return res
	#----------------------------------------------------------------------
	def setSingleStep(self,milliseconds):
		"""
		setSingleStep(milliseconds)
			milliseconds=QtCore.int

		This property holds the single step.
		The smaller of two natural steps that a slider provides and typically corresponds to the user pressing an arrow key.
		Defaults to 1 (1% of the voltage).
		"""
		res = super(Phonon,self).setSingleStep(milliseconds)
		return res
	#----------------------------------------------------------------------
	def setTracking(self,tracking):
		"""
		setTracking(tracking)
			tracking=QtCore.bool

		This property holds whether slider tracking is enabled.
		If tracking is enabled (the default), the volume changes while the slider is being dragged
		If tracking is disabled, the volume changes only when the user releases the slider.
		"""
		res = super(Phonon,self).setTracking(tracking)
		return res

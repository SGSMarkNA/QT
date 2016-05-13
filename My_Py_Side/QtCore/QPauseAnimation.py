from PySide import QtGui, QtCore

class QPauseAnimation(QtCore.QPauseAnimation):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QPauseAnimation,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def setDuration(self,msecs):
		"""
		setDuration(msecs)
			msecs=QtCore.int

		This property holds the duration of the pause..
		The duration of the pause
		The duration should not be negative
		The default duration is 250 milliseconds.
		"""
		res = super(QPauseAnimation,self).setDuration(msecs)
		return res

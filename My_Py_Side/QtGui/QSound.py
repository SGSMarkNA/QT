from PySide import QtGui, QtCore

class QSound(QtGui.QSound):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSound,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def fileName(self):
		"""
		Returns the filename associated with this PySide.QtGui.QSound object.
		"""
		res = super(QSound,self).fileName()
		return res
	#----------------------------------------------------------------------
	def isFinished(self):
		"""
		Returns true if the sound has finished playing; otherwise returns false.
		"""
		res = super(QSound,self).isFinished()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def loops(self):
		"""
		Returns the number of times the sound will play.
		"""
		res = super(QSound,self).loops()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def loopsRemaining(self):
		"""
		Returns the remaining number of times the sound will loop (this value decreases each time the sound is played).
		"""
		res = super(QSound,self).loopsRemaining()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def setLoops(self,arg__1):
		"""
		setLoops(arg__1)
			arg__1=QtCore.int

		Sets the sound to repeat the given number of times when it is played.
		Note that passing the value -1 will cause the sound to loop indefinitely.
		"""
		res = super(QSound,self).setLoops(arg__1)
		return res

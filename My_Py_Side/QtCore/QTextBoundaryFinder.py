from PySide import QtGui, QtCore

class QTextBoundaryFinder(QtCore.QTextBoundaryFinder):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextBoundaryFinder,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def boundaryReasons(self):
		"""
		Returns the reasons for the boundary finder to have chosen the current position as a boundary.
		"""
		res = super(QTextBoundaryFinder,self).boundaryReasons()
		isinstance(res,QtCore.QTextBoundaryFinder.BoundaryReasons)
		return res
	#----------------------------------------------------------------------
	def isAtBoundary(self):
		"""
		Returns true if the objects PySide.QtCore.QTextBoundaryFinder.position() is currently at a valid text boundary.
		"""
		res = super(QTextBoundaryFinder,self).isAtBoundary()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if the text boundary finder is valid; otherwise returns false
		A default PySide.QtCore.QTextBoundaryFinder is invalid.
		"""
		res = super(QTextBoundaryFinder,self).isValid()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def position(self):
		"""
		Returns the current position of the PySide.QtCore.QTextBoundaryFinder .
		The range is from 0 (the beginning of the string) to the length of the string inclusive.
		"""
		res = super(QTextBoundaryFinder,self).position()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def string(self):
		"""
		Returns the string the PySide.QtCore.QTextBoundaryFinder object operates on.
		"""
		res = super(QTextBoundaryFinder,self).string()
		return res
	#----------------------------------------------------------------------
	def toEnd(self):
		"""
		Moves the finder to the end of the string
		This is equivalent to setPosition(string
		length() ).
		"""
		res = super(QTextBoundaryFinder,self).toEnd()
		return res
	#----------------------------------------------------------------------
	def toNextBoundary(self):
		"""
		Moves the PySide.QtCore.QTextBoundaryFinder to the next boundary position and returns that position.
		Returns -1 if there is no next boundary.
		"""
		res = super(QTextBoundaryFinder,self).toNextBoundary()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def toPreviousBoundary(self):
		"""
		Moves the PySide.QtCore.QTextBoundaryFinder to the previous boundary position and returns that position.
		Returns -1 if there is no previous boundary.
		"""
		res = super(QTextBoundaryFinder,self).toPreviousBoundary()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def toStart(self):
		"""
		Moves the finder to the start of the string
		This is equivalent to setPosition(0).
		"""
		res = super(QTextBoundaryFinder,self).toStart()
		return res
	#----------------------------------------------------------------------
	def type(self):
		"""
		Returns the type of the PySide.QtCore.QTextBoundaryFinder .
		"""
		res = super(QTextBoundaryFinder,self).type()
		isinstance(res,QtCore.QTextBoundaryFinder.BoundaryType)
		return res
	#----------------------------------------------------------------------
	def setPosition(self,position):
		"""
		setPosition(position)
			position=QtCore.int

		Sets the current position of the PySide.QtCore.QTextBoundaryFinder to position .
		If position is out of bounds, it will be bound to only valid positions
		In this case, valid positions are from 0 to the length of the string inclusive.
		"""
		res = super(QTextBoundaryFinder,self).setPosition(position)
		return res

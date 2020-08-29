from PySide import QtGui, QtCore

class QTableWidgetSelectionRange(QtGui.QTableWidgetSelectionRange):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTableWidgetSelectionRange,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def bottomRow(self):
		"""
		Returns the bottom row of the range.
		"""
		res = super(QTableWidgetSelectionRange,self).bottomRow()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def columnCount(self):
		"""
		Returns the number of columns in the range.
		This is equivalent to PySide.QtGui.QTableWidgetSelectionRange.rightColumn() - PySide.QtGui.QTableWidgetSelectionRange.leftColumn() + 1.
		"""
		res = super(QTableWidgetSelectionRange,self).columnCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def leftColumn(self):
		"""
		Returns the left column of the range.
		"""
		res = super(QTableWidgetSelectionRange,self).leftColumn()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def rightColumn(self):
		"""
		Returns the right column of the range.
		"""
		res = super(QTableWidgetSelectionRange,self).rightColumn()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def rowCount(self):
		"""
		Returns the number of rows in the range.
		This is equivalent to PySide.QtGui.QTableWidgetSelectionRange.bottomRow() - PySide.QtGui.QTableWidgetSelectionRange.topRow() + 1.
		"""
		res = super(QTableWidgetSelectionRange,self).rowCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def topRow(self):
		"""
		Returns the top row of the range.
		"""
		res = super(QTableWidgetSelectionRange,self).topRow()
		isinstance(res,int)
		return res

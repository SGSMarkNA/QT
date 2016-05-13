from PySide import QtGui, QtCore

class QTextTableCellFormat(QtGui.QTextTableCellFormat):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextTableCellFormat,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def bottomPadding(self):
		"""
		Gets the bottom padding of the table cell.
		"""
		res = super(QTextTableCellFormat,self).bottomPadding()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def leftPadding(self):
		"""
		Gets the left padding of the table cell.
		"""
		res = super(QTextTableCellFormat,self).leftPadding()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def rightPadding(self):
		"""
		Gets the right padding of the table cell.
		"""
		res = super(QTextTableCellFormat,self).rightPadding()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def topPadding(self):
		"""
		Gets the top padding of the table cell.
		"""
		res = super(QTextTableCellFormat,self).topPadding()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def setBottomPadding(self,padding):
		"""
		setBottomPadding(padding)
			padding=QtCore.qreal

		Sets the bottom padding of the table cell.
		"""
		res = super(QTextTableCellFormat,self).setBottomPadding(padding)
		return res
	#----------------------------------------------------------------------
	def setLeftPadding(self,padding):
		"""
		setLeftPadding(padding)
			padding=QtCore.qreal

		Sets the left padding of the table cell.
		"""
		res = super(QTextTableCellFormat,self).setLeftPadding(padding)
		return res
	#----------------------------------------------------------------------
	def setPadding(self,padding):
		"""
		setPadding(padding)
			padding=QtCore.qreal

		Sets the left, right, top, and bottom padding of the table cell.
		"""
		res = super(QTextTableCellFormat,self).setPadding(padding)
		return res
	#----------------------------------------------------------------------
	def setRightPadding(self,padding):
		"""
		setRightPadding(padding)
			padding=QtCore.qreal

		Sets the right padding of the table cell.
		"""
		res = super(QTextTableCellFormat,self).setRightPadding(padding)
		return res
	#----------------------------------------------------------------------
	def setTopPadding(self,padding):
		"""
		setTopPadding(padding)
			padding=QtCore.qreal

		Sets the top padding of the table cell.
		"""
		res = super(QTextTableCellFormat,self).setTopPadding(padding)
		return res

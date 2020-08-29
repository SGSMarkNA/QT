from PySide import QtGui, QtCore

class QTextTableCell(QtGui.QTextTableCell):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextTableCell,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def begin(self):
		"""
		Returns a frame iterator pointing to the beginning of the tables cell.
		"""
		res = super(QTextTableCell,self).begin()
		isinstance(res,QtGui.QTextFrame::iterator)
		return res
	#----------------------------------------------------------------------
	def column(self):
		"""
		Returns the number of the column in the table that contains this cell.
		"""
		res = super(QTextTableCell,self).column()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def columnSpan(self):
		"""
		Returns the number of columns this cell spans
		The default is 1.
		"""
		res = super(QTextTableCell,self).columnSpan()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def end(self):
		"""
		Returns a frame iterator pointing to the end of the tables cell.
		"""
		res = super(QTextTableCell,self).end()
		isinstance(res,QtGui.QTextFrame::iterator)
		return res
	#----------------------------------------------------------------------
	def firstCursorPosition(self):
		"""
		Returns the first valid cursor position in this cell.
		"""
		res = super(QTextTableCell,self).firstCursorPosition()
		isinstance(res,QtGui.QTextCursor)
		return res
	#----------------------------------------------------------------------
	def firstPosition(self):
		"""
		Returns the first valid position in the document occupied by this cell.
		"""
		res = super(QTextTableCell,self).firstPosition()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def format(self):
		"""
		Returns the cells character format.
		"""
		res = super(QTextTableCell,self).format()
		isinstance(res,QtGui.QTextCharFormat)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if this is a valid table cell; otherwise returns false.
		"""
		res = super(QTextTableCell,self).isValid()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def lastCursorPosition(self):
		"""
		Returns the last valid cursor position in this cell.
		"""
		res = super(QTextTableCell,self).lastCursorPosition()
		isinstance(res,QtGui.QTextCursor)
		return res
	#----------------------------------------------------------------------
	def lastPosition(self):
		"""
		Returns the last valid position in the document occupied by this cell.
		"""
		res = super(QTextTableCell,self).lastPosition()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def row(self):
		"""
		Returns the number of the row in the table that contains this cell.
		"""
		res = super(QTextTableCell,self).row()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def rowSpan(self):
		"""
		Returns the number of rows this cell spans
		The default is 1.
		"""
		res = super(QTextTableCell,self).rowSpan()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def tableCellFormatIndex(self):
		"""
		Returns the index of the tableCells format in the documents internal list of formats.
		"""
		res = super(QTextTableCell,self).tableCellFormatIndex()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtGui.QTextTableCell

		Returns true if this cell object and the other cell object describe different cells; otherwise returns false.
		"""
		res = super(QTextTableCell,self).__ne__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtGui.QTextTableCell

		Returns true if this cell object and the other cell object describe the same cell; otherwise returns false.
		"""
		res = super(QTextTableCell,self).__eq__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setFormat(self,format):
		"""
		setFormat(format)
			format=QtGui.QTextCharFormat

		Sets the cells character format to format
		This can for example be used to change the background color of the entire cell:
		PySide.QtGui.QTextTableCell cell = table->cellAt(2, 3); PySide.QtGui.QTextCharFormat format = cell
		PySide.QtGui.QTextTableCell.format() ; format.setBackground( Qt.blue ); cell.setFormat(format);
		Note that the cells row or column span cannot be changed through this function
		You have to use QTextTable::mergeCells and QTextTable::splitCell instead.
		"""
		res = super(QTextTableCell,self).setFormat(format)
		return res

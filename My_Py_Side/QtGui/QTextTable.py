from PySide import QtGui, QtCore

class QTextTable(QtGui.QTextTable):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextTable,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def columns(self):
		"""
		Returns the number of columns in the table.
		"""
		res = super(QTextTable,self).columns()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def rows(self):
		"""
		Returns the number of rows in the table.
		"""
		res = super(QTextTable,self).rows()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def appendColumns(self,count):
		"""
		appendColumns(count)
			count=QtCore.int

		Appends count columns at the right side of the table.
		"""
		res = super(QTextTable,self).appendColumns(count)
		return res
	#----------------------------------------------------------------------
	def appendRows(self,count):
		"""
		appendRows(count)
			count=QtCore.int

		Appends count rows at the bottom of the table.
		"""
		res = super(QTextTable,self).appendRows(count)
		return res
	#----------------------------------------------------------------------
	def cellAt(self,*args,**kwargs):
		"""
		cellAt(row,col)
			row=QtCore.int
			col=QtCore.int

		cellAt(position)
			position=QtCore.int

		cellAt(c)
			c=QtGui.QTextCursor

		Returns the table cell at the given row and column in the table.
		"""
		res = super(QTextTable,self).cellAt(*args,**kwargs)
		isinstance(res,QtGui.QTextTableCell)
		return res
	#----------------------------------------------------------------------
	def insertColumns(self,pos,num):
		"""
		insertColumns(pos,num)
			pos=QtCore.int
			num=QtCore.int

		Inserts a number of columns before the column with the specified index .
		"""
		res = super(QTextTable,self).insertColumns(pos,num)
		return res
	#----------------------------------------------------------------------
	def insertRows(self,pos,num):
		"""
		insertRows(pos,num)
			pos=QtCore.int
			num=QtCore.int

		Inserts a number of rows before the row with the specified index .
		"""
		res = super(QTextTable,self).insertRows(pos,num)
		return res
	#----------------------------------------------------------------------
	def mergeCells(self,*args,**kwargs):
		"""
		mergeCells(row,col,numRows,numCols)
			row=QtCore.int
			col=QtCore.int
			numRows=QtCore.int
			numCols=QtCore.int

		mergeCells(cursor)
			cursor=QtGui.QTextCursor

		Merges the cell at the specified row and column with the adjacent cells into one cell
		The new cell will span numRows rows and numCols columns
		If numRows or numCols is less than the current number of rows or columns the cell spans then this method does nothing.
		"""
		res = super(QTextTable,self).mergeCells(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def removeColumns(self,pos,num):
		"""
		removeColumns(pos,num)
			pos=QtCore.int
			num=QtCore.int

		Removes a number of columns starting with the column at the specified index .
		"""
		res = super(QTextTable,self).removeColumns(pos,num)
		return res
	#----------------------------------------------------------------------
	def removeRows(self,pos,num):
		"""
		removeRows(pos,num)
			pos=QtCore.int
			num=QtCore.int

		Removes a number of rows starting with the row at the specified index .
		"""
		res = super(QTextTable,self).removeRows(pos,num)
		return res
	#----------------------------------------------------------------------
	def resize(self,rows,cols):
		"""
		resize(rows,cols)
			rows=QtCore.int
			cols=QtCore.int

		Resizes the table to contain the required number of rows and columns .
		"""
		res = super(QTextTable,self).resize(rows,cols)
		return res
	#----------------------------------------------------------------------
	def rowEnd(self,c):
		"""
		rowEnd(c)
			c=QtGui.QTextCursor

		Returns a cursor pointing to the end of the row that contains the given cursor .
		"""
		res = super(QTextTable,self).rowEnd(c)
		isinstance(res,QtGui.QTextCursor)
		return res
	#----------------------------------------------------------------------
	def rowStart(self,c):
		"""
		rowStart(c)
			c=QtGui.QTextCursor

		Returns a cursor pointing to the start of the row that contains the given cursor .
		"""
		res = super(QTextTable,self).rowStart(c)
		isinstance(res,QtGui.QTextCursor)
		return res
	#----------------------------------------------------------------------
	def setFormat(self,format):
		"""
		setFormat(format)
			format=QtGui.QTextTableFormat

		Sets the tables format .
		"""
		res = super(QTextTable,self).setFormat(format)
		return res
	#----------------------------------------------------------------------
	def splitCell(self,row,col,numRows,numCols):
		"""
		splitCell(row,col,numRows,numCols)
			row=QtCore.int
			col=QtCore.int
			numRows=QtCore.int
			numCols=QtCore.int

		Splits the specified cell at row and column into an array of multiple cells with dimensions specified by numRows and numCols .
		"""
		res = super(QTextTable,self).splitCell(row,col,numRows,numCols)
		return res

from PySide import QtGui, QtCore

class QTextTableFormat(QtGui.QTextTableFormat):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextTableFormat,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def alignment(self):
		"""
		Returns the tables alignment.
		"""
		res = super(QTextTableFormat,self).alignment()
		isinstance(res,QtCore.Qt.Alignment)
		return res
	#----------------------------------------------------------------------
	def cellPadding(self):
		"""
		Returns the tables cell padding
		This describes the distance between the border of a cell and its contents.
		"""
		res = super(QTextTableFormat,self).cellPadding()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def cellSpacing(self):
		"""
		Returns the tables cell spacing
		This describes the distance between adjacent cells.
		"""
		res = super(QTextTableFormat,self).cellSpacing()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def clearColumnWidthConstraints(self):
		"""
		Clears the column width constraints for the table.
		"""
		res = super(QTextTableFormat,self).clearColumnWidthConstraints()
		return res
	#----------------------------------------------------------------------
	def columnWidthConstraints(self):
		"""
		Returns a list of constraints used by this table format to control the appearance of columns in a table.
		"""
		res = super(QTextTableFormat,self).columnWidthConstraints()
		return res
	#----------------------------------------------------------------------
	def columns(self):
		"""
		Returns the number of columns specified by the table format.
		"""
		res = super(QTextTableFormat,self).columns()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def headerRowCount(self):
		"""
		Returns the number of rows in the table that define the header.
		"""
		res = super(QTextTableFormat,self).headerRowCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def setAlignment(self,alignment):
		"""
		setAlignment(alignment)
			alignment=QtCore.Qt.Alignment


		"""
		res = super(QTextTableFormat,self).setAlignment(alignment)
		return res
	#----------------------------------------------------------------------
	def setCellPadding(self,padding):
		"""
		setCellPadding(padding)
			padding=QtCore.qreal

		Sets the cell padding for the table
		This determines the distance between the border of a cell and its contents.
		"""
		res = super(QTextTableFormat,self).setCellPadding(padding)
		return res
	#----------------------------------------------------------------------
	def setCellSpacing(self,spacing):
		"""
		setCellSpacing(spacing)
			spacing=QtCore.qreal

		Sets the cell spacing for the table
		This determines the distance between adjacent cells.
		"""
		res = super(QTextTableFormat,self).setCellSpacing(spacing)
		return res
	#----------------------------------------------------------------------
	def setColumnWidthConstraints(self,constraints):
		"""
		setColumnWidthConstraints(constraints)
			constraints=unKnown


		"""
		res = super(QTextTableFormat,self).setColumnWidthConstraints(constraints)
		return res
	#----------------------------------------------------------------------
	def setColumns(self,columns):
		"""
		setColumns(columns)
			columns=QtCore.int

		Sets the number of columns required by the table format.
		"""
		res = super(QTextTableFormat,self).setColumns(columns)
		return res
	#----------------------------------------------------------------------
	def setHeaderRowCount(self,count):
		"""
		setHeaderRowCount(count)
			count=QtCore.int

		Declares the first count rows of the table as table header
		The table header rows get repeated when a table is broken across a page boundary.
		"""
		res = super(QTextTableFormat,self).setHeaderRowCount(count)
		return res

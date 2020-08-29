from PySide import QtGui, QtCore

class QGridLayout(QtGui.QGridLayout):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGridLayout,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def columnCount(self):
		"""
		Returns the number of columns in this grid.
		"""
		res = super(QGridLayout,self).columnCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def horizontalSpacing(self):
		"""

		"""
		res = super(QGridLayout,self).horizontalSpacing()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def originCorner(self):
		"""
		Returns the corner thats used for the grids origin, i.e
		for position (0, 0).
		"""
		res = super(QGridLayout,self).originCorner()
		isinstance(res,QtCore.Qt.Corner)
		return res
	#----------------------------------------------------------------------
	def rowCount(self):
		"""
		Returns the number of rows in this grid.
		"""
		res = super(QGridLayout,self).rowCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def verticalSpacing(self):
		"""

		"""
		res = super(QGridLayout,self).verticalSpacing()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def addItem(self,item,row,column,rowSpan=None,columnSpan=None,alignment=None):
		"""
		addItem(item,row,column,rowSpan=None,columnSpan=None,alignment=None)
			item=QtGui.QLayoutItem
			row=QtCore.int
			column=QtCore.int
			rowSpan=QtCore.int
			columnSpan=QtCore.int
			alignment=QtCore.Qt.Alignment


		"""
		res = super(QGridLayout,self).addItem(item,row,column,rowSpan,columnSpan,alignment)
		return res
	#----------------------------------------------------------------------
	def addLayout(self,*args,**kwargs):
		"""
		addLayout(arg__1,row,column,rowSpan,columnSpan,alignment=None)
			arg__1=QtGui.QLayout
			row=QtCore.int
			column=QtCore.int
			rowSpan=QtCore.int
			columnSpan=QtCore.int
			alignment=QtCore.Qt.Alignment

		addLayout(arg__1,row,column,alignment=None)
			arg__1=QtGui.QLayout
			row=QtCore.int
			column=QtCore.int
			alignment=QtCore.Qt.Alignment


		"""
		res = super(QGridLayout,self).addLayout(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def addWidget(self,*args,**kwargs):
		"""
		addWidget(arg__1,row,column,alignment=None)
			arg__1=QtGui.QWidget
			row=QtCore.int
			column=QtCore.int
			alignment=QtCore.Qt.Alignment

		addWidget(arg__1,row,column,rowSpan,columnSpan,alignment=None)
			arg__1=QtGui.QWidget
			row=QtCore.int
			column=QtCore.int
			rowSpan=QtCore.int
			columnSpan=QtCore.int
			alignment=QtCore.Qt.Alignment


		"""
		res = super(QGridLayout,self).addWidget(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def cellRect(self,row,column):
		"""
		cellRect(row,column)
			row=QtCore.int
			column=QtCore.int

		Returns the geometry of the cell with row row and column column in the grid
		Returns an invalid rectangle if row or column is outside the grid.
		"""
		res = super(QGridLayout,self).cellRect(row,column)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def columnMinimumWidth(self,column):
		"""
		columnMinimumWidth(column)
			column=QtCore.int

		Returns the column spacing for column column .
		"""
		res = super(QGridLayout,self).columnMinimumWidth(column)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def columnStretch(self,column):
		"""
		columnStretch(column)
			column=QtCore.int

		Returns the stretch factor for column column .
		"""
		res = super(QGridLayout,self).columnStretch(column)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def getItemPosition(self,idx):
		"""
		getItemPosition(idx)
			idx=QtCore.int

		Returns the position information of the item with the given index .
		The variables passed as row and column are updated with the position of the item in the layout, and the rowSpan and columnSpan variables are updated with the vertical and horizontal spans of the item.
		"""
		res = super(QGridLayout,self).getItemPosition(idx)
		return res
	#----------------------------------------------------------------------
	def itemAtPosition(self,row,column):
		"""
		itemAtPosition(row,column)
			row=QtCore.int
			column=QtCore.int

		Returns the layout item that occupies cell (row , column ), or 0 if the cell is empty.
		"""
		res = super(QGridLayout,self).itemAtPosition(row,column)
		isinstance(res,QtGui.QLayoutItem)
		return res
	#----------------------------------------------------------------------
	def rowMinimumHeight(self,row):
		"""
		rowMinimumHeight(row)
			row=QtCore.int

		Returns the minimum width set for row row .
		"""
		res = super(QGridLayout,self).rowMinimumHeight(row)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def rowStretch(self,row):
		"""
		rowStretch(row)
			row=QtCore.int

		Returns the stretch factor for row row .
		"""
		res = super(QGridLayout,self).rowStretch(row)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def setColumnMinimumWidth(self,column,minSize):
		"""
		setColumnMinimumWidth(column,minSize)
			column=QtCore.int
			minSize=QtCore.int

		Sets the minimum width of column column to minSize pixels.
		"""
		res = super(QGridLayout,self).setColumnMinimumWidth(column,minSize)
		return res
	#----------------------------------------------------------------------
	def setColumnStretch(self,column,stretch):
		"""
		setColumnStretch(column,stretch)
			column=QtCore.int
			stretch=QtCore.int

		Sets the stretch factor of column column to stretch
		The first column is number 0.
		The stretch factor is relative to the other columns in this grid
		Columns with a higher stretch factor take more of the available space.
		The default stretch factor is 0
		If the stretch factor is 0 and no other column in this table can grow at all, the column may still grow.
		An alternative approach is to add spacing using PySide.QtGui.QGridLayout.addItem() with a PySide.QtGui.QSpacerItem .
		"""
		res = super(QGridLayout,self).setColumnStretch(column,stretch)
		return res
	#----------------------------------------------------------------------
	def setDefaultPositioning(self,n,orient):
		"""
		setDefaultPositioning(n,orient)
			n=QtCore.int
			orient=QtCore.Qt.Orientation


		"""
		res = super(QGridLayout,self).setDefaultPositioning(n,orient)
		return res
	#----------------------------------------------------------------------
	def setHorizontalSpacing(self,spacing):
		"""
		setHorizontalSpacing(spacing)
			spacing=QtCore.int


		"""
		res = super(QGridLayout,self).setHorizontalSpacing(spacing)
		return res
	#----------------------------------------------------------------------
	def setOriginCorner(self,arg__1):
		"""
		setOriginCorner(arg__1)
			arg__1=QtCore.Qt.Corner


		"""
		res = super(QGridLayout,self).setOriginCorner(arg__1)
		return res
	#----------------------------------------------------------------------
	def setRowMinimumHeight(self,row,minSize):
		"""
		setRowMinimumHeight(row,minSize)
			row=QtCore.int
			minSize=QtCore.int

		Sets the minimum height of row row to minSize pixels.
		"""
		res = super(QGridLayout,self).setRowMinimumHeight(row,minSize)
		return res
	#----------------------------------------------------------------------
	def setRowStretch(self,row,stretch):
		"""
		setRowStretch(row,stretch)
			row=QtCore.int
			stretch=QtCore.int

		Sets the stretch factor of row row to stretch
		The first row is number 0.
		The stretch factor is relative to the other rows in this grid
		Rows with a higher stretch factor take more of the available space.
		The default stretch factor is 0
		If the stretch factor is 0 and no other row in this table can grow at all, the row may still grow.
		"""
		res = super(QGridLayout,self).setRowStretch(row,stretch)
		return res
	#----------------------------------------------------------------------
	def setVerticalSpacing(self,spacing):
		"""
		setVerticalSpacing(spacing)
			spacing=QtCore.int


		"""
		res = super(QGridLayout,self).setVerticalSpacing(spacing)
		return res

from PySide import QtGui, QtCore

class QGraphicsGridLayout(QtGui.QGraphicsGridLayout):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsGridLayout,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def columnCount(self):
		"""
		Returns the number of columns in the grid layout
		This is always one more than the index of the last column that is occupied by a layout item (empty columns are counted except for those at the end).
		"""
		res = super(QGraphicsGridLayout,self).columnCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def horizontalSpacing(self):
		"""
		Returns the default horizontal spacing for the grid layout.
		"""
		res = super(QGraphicsGridLayout,self).horizontalSpacing()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def rowCount(self):
		"""
		Returns the number of rows in the grid layout
		This is always one more than the index of the last row that is occupied by a layout item (empty rows are counted except for those at the end).
		"""
		res = super(QGraphicsGridLayout,self).rowCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def verticalSpacing(self):
		"""
		Returns the default vertical spacing for the grid layout.
		"""
		res = super(QGraphicsGridLayout,self).verticalSpacing()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def addItem(self,*args,**kwargs):
		"""
		addItem(item,row,column,rowSpan,columnSpan,alignment=None)
			item=QtGui.QGraphicsLayoutItem
			row=QtCore.int
			column=QtCore.int
			rowSpan=QtCore.int
			columnSpan=QtCore.int
			alignment=QtCore.Qt.Alignment

		addItem(item,row,column,alignment=None)
			item=QtGui.QGraphicsLayoutItem
			row=QtCore.int
			column=QtCore.int
			alignment=QtCore.Qt.Alignment


		"""
		res = super(QGraphicsGridLayout,self).addItem(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def alignment(self,item):
		"""
		alignment(item)
			item=QtGui.QGraphicsLayoutItem

		Returns the alignment for item .
		"""
		res = super(QGraphicsGridLayout,self).alignment(item)
		isinstance(res,QtCore.Qt.Alignment)
		return res
	#----------------------------------------------------------------------
	def columnAlignment(self,column):
		"""
		columnAlignment(column)
			column=QtCore.int

		Returns the alignment for column .
		"""
		res = super(QGraphicsGridLayout,self).columnAlignment(column)
		isinstance(res,QtCore.Qt.Alignment)
		return res
	#----------------------------------------------------------------------
	def columnMaximumWidth(self,column):
		"""
		columnMaximumWidth(column)
			column=QtCore.int

		Returns the maximum width for column .
		"""
		res = super(QGraphicsGridLayout,self).columnMaximumWidth(column)
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def columnMinimumWidth(self,column):
		"""
		columnMinimumWidth(column)
			column=QtCore.int

		Returns the minimum width for column .
		"""
		res = super(QGraphicsGridLayout,self).columnMinimumWidth(column)
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def columnPreferredWidth(self,column):
		"""
		columnPreferredWidth(column)
			column=QtCore.int

		Returns the preferred width for column .
		"""
		res = super(QGraphicsGridLayout,self).columnPreferredWidth(column)
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def columnSpacing(self,column):
		"""
		columnSpacing(column)
			column=QtCore.int

		Returns the column spacing for column .
		"""
		res = super(QGraphicsGridLayout,self).columnSpacing(column)
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def columnStretchFactor(self,column):
		"""
		columnStretchFactor(column)
			column=QtCore.int

		Returns the stretch factor for column .
		"""
		res = super(QGraphicsGridLayout,self).columnStretchFactor(column)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def itemAt(self,row,column):
		"""
		itemAt(row,column)
			row=QtCore.int
			column=QtCore.int

		Returns a pointer to the layout item at (row , column ).
		"""
		res = super(QGraphicsGridLayout,self).itemAt(row,column)
		isinstance(res,QtGui.QGraphicsLayoutItem)
		return res
	#----------------------------------------------------------------------
	def rowAlignment(self,row):
		"""
		rowAlignment(row)
			row=QtCore.int

		Returns the alignment of row .
		"""
		res = super(QGraphicsGridLayout,self).rowAlignment(row)
		isinstance(res,QtCore.Qt.Alignment)
		return res
	#----------------------------------------------------------------------
	def rowMaximumHeight(self,row):
		"""
		rowMaximumHeight(row)
			row=QtCore.int

		Returns the maximum height for row, row .
		"""
		res = super(QGraphicsGridLayout,self).rowMaximumHeight(row)
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def rowMinimumHeight(self,row):
		"""
		rowMinimumHeight(row)
			row=QtCore.int

		Returns the minimum height for row, row .
		"""
		res = super(QGraphicsGridLayout,self).rowMinimumHeight(row)
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def rowPreferredHeight(self,row):
		"""
		rowPreferredHeight(row)
			row=QtCore.int

		Returns the preferred height for row, row .
		"""
		res = super(QGraphicsGridLayout,self).rowPreferredHeight(row)
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def rowSpacing(self,row):
		"""
		rowSpacing(row)
			row=QtCore.int

		Returns the row spacing for row .
		"""
		res = super(QGraphicsGridLayout,self).rowSpacing(row)
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def rowStretchFactor(self,row):
		"""
		rowStretchFactor(row)
			row=QtCore.int

		Returns the stretch factor for row .
		"""
		res = super(QGraphicsGridLayout,self).rowStretchFactor(row)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def setAlignment(self,item,alignment):
		"""
		setAlignment(item,alignment)
			item=QtGui.QGraphicsLayoutItem
			alignment=QtCore.Qt.Alignment


		"""
		res = super(QGraphicsGridLayout,self).setAlignment(item,alignment)
		return res
	#----------------------------------------------------------------------
	def setColumnAlignment(self,column,alignment):
		"""
		setColumnAlignment(column,alignment)
			column=QtCore.int
			alignment=QtCore.Qt.Alignment


		"""
		res = super(QGraphicsGridLayout,self).setColumnAlignment(column,alignment)
		return res
	#----------------------------------------------------------------------
	def setColumnFixedWidth(self,column,width):
		"""
		setColumnFixedWidth(column,width)
			column=QtCore.int
			width=QtCore.qreal

		Sets the fixed width of column to width .
		"""
		res = super(QGraphicsGridLayout,self).setColumnFixedWidth(column,width)
		return res
	#----------------------------------------------------------------------
	def setColumnMaximumWidth(self,column,width):
		"""
		setColumnMaximumWidth(column,width)
			column=QtCore.int
			width=QtCore.qreal

		Sets the maximum width of column to width .
		"""
		res = super(QGraphicsGridLayout,self).setColumnMaximumWidth(column,width)
		return res
	#----------------------------------------------------------------------
	def setColumnMinimumWidth(self,column,width):
		"""
		setColumnMinimumWidth(column,width)
			column=QtCore.int
			width=QtCore.qreal

		Sets the minimum width for column to width .
		"""
		res = super(QGraphicsGridLayout,self).setColumnMinimumWidth(column,width)
		return res
	#----------------------------------------------------------------------
	def setColumnPreferredWidth(self,column,width):
		"""
		setColumnPreferredWidth(column,width)
			column=QtCore.int
			width=QtCore.qreal

		Sets the preferred width for column to width .
		"""
		res = super(QGraphicsGridLayout,self).setColumnPreferredWidth(column,width)
		return res
	#----------------------------------------------------------------------
	def setColumnSpacing(self,column,spacing):
		"""
		setColumnSpacing(column,spacing)
			column=QtCore.int
			spacing=QtCore.qreal

		Sets the spacing for column to spacing .
		"""
		res = super(QGraphicsGridLayout,self).setColumnSpacing(column,spacing)
		return res
	#----------------------------------------------------------------------
	def setColumnStretchFactor(self,column,stretch):
		"""
		setColumnStretchFactor(column,stretch)
			column=QtCore.int
			stretch=QtCore.int

		Sets the stretch factor for column to stretch .
		"""
		res = super(QGraphicsGridLayout,self).setColumnStretchFactor(column,stretch)
		return res
	#----------------------------------------------------------------------
	def setHorizontalSpacing(self,spacing):
		"""
		setHorizontalSpacing(spacing)
			spacing=QtCore.qreal

		Sets the default horizontal spacing for the grid layout to spacing .
		"""
		res = super(QGraphicsGridLayout,self).setHorizontalSpacing(spacing)
		return res
	#----------------------------------------------------------------------
	def setRowAlignment(self,row,alignment):
		"""
		setRowAlignment(row,alignment)
			row=QtCore.int
			alignment=QtCore.Qt.Alignment


		"""
		res = super(QGraphicsGridLayout,self).setRowAlignment(row,alignment)
		return res
	#----------------------------------------------------------------------
	def setRowFixedHeight(self,row,height):
		"""
		setRowFixedHeight(row,height)
			row=QtCore.int
			height=QtCore.qreal

		Sets the fixed height for row, row , to height .
		"""
		res = super(QGraphicsGridLayout,self).setRowFixedHeight(row,height)
		return res
	#----------------------------------------------------------------------
	def setRowMaximumHeight(self,row,height):
		"""
		setRowMaximumHeight(row,height)
			row=QtCore.int
			height=QtCore.qreal

		Sets the maximum height for row, row , to height .
		"""
		res = super(QGraphicsGridLayout,self).setRowMaximumHeight(row,height)
		return res
	#----------------------------------------------------------------------
	def setRowMinimumHeight(self,row,height):
		"""
		setRowMinimumHeight(row,height)
			row=QtCore.int
			height=QtCore.qreal

		Sets the minimum height for row, row , to height .
		"""
		res = super(QGraphicsGridLayout,self).setRowMinimumHeight(row,height)
		return res
	#----------------------------------------------------------------------
	def setRowPreferredHeight(self,row,height):
		"""
		setRowPreferredHeight(row,height)
			row=QtCore.int
			height=QtCore.qreal

		Sets the preferred height for row, row , to height .
		"""
		res = super(QGraphicsGridLayout,self).setRowPreferredHeight(row,height)
		return res
	#----------------------------------------------------------------------
	def setRowSpacing(self,row,spacing):
		"""
		setRowSpacing(row,spacing)
			row=QtCore.int
			spacing=QtCore.qreal

		Sets the spacing for row to spacing .
		"""
		res = super(QGraphicsGridLayout,self).setRowSpacing(row,spacing)
		return res
	#----------------------------------------------------------------------
	def setRowStretchFactor(self,row,stretch):
		"""
		setRowStretchFactor(row,stretch)
			row=QtCore.int
			stretch=QtCore.int

		Sets the stretch factor for row to stretch .
		"""
		res = super(QGraphicsGridLayout,self).setRowStretchFactor(row,stretch)
		return res
	#----------------------------------------------------------------------
	def setSpacing(self,spacing):
		"""
		setSpacing(spacing)
			spacing=QtCore.qreal

		Sets the grid layouts default spacing, both vertical and horizontal, to spacing .
		"""
		res = super(QGraphicsGridLayout,self).setSpacing(spacing)
		return res
	#----------------------------------------------------------------------
	def setVerticalSpacing(self,spacing):
		"""
		setVerticalSpacing(spacing)
			spacing=QtCore.qreal

		Sets the default vertical spacing for the grid layout to spacing .
		"""
		res = super(QGraphicsGridLayout,self).setVerticalSpacing(spacing)
		return res

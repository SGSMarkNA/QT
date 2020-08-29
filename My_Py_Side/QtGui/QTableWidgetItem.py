from PySide import QtGui, QtCore

class QTableWidgetItem(QtGui.QTableWidgetItem):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTableWidgetItem,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def background(self):
		"""
		Returns the brush used to render the items background.
		"""
		res = super(QTableWidgetItem,self).background()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def checkState(self):
		"""
		Returns the checked state of the table item.
		"""
		res = super(QTableWidgetItem,self).checkState()
		isinstance(res,QtCore.Qt.CheckState)
		return res
	#----------------------------------------------------------------------
	def clone(self):
		"""
		Creates a copy of the item.
		"""
		res = super(QTableWidgetItem,self).clone()
		isinstance(res,QtGui.QTableWidgetItem)
		return res
	#----------------------------------------------------------------------
	def column(self):
		"""
		Returns the column of the item in the table
		If the item is not in a table, this function will return -1.
		"""
		res = super(QTableWidgetItem,self).column()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def flags(self):
		"""
		Returns the flags used to describe the item
		These determine whether the item can be checked, edited, and selected.
		"""
		res = super(QTableWidgetItem,self).flags()
		isinstance(res,QtCore.Qt.ItemFlags)
		return res
	#----------------------------------------------------------------------
	def font(self):
		"""
		Returns the font used to render the items text.
		"""
		res = super(QTableWidgetItem,self).font()
		isinstance(res,QtGui.QFont)
		return res
	#----------------------------------------------------------------------
	def foreground(self):
		"""
		Returns the brush used to render the items foreground (e.g
		text).
		"""
		res = super(QTableWidgetItem,self).foreground()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def icon(self):
		"""
		Returns the items icon.
		"""
		res = super(QTableWidgetItem,self).icon()
		isinstance(res,QtGui.QIcon)
		return res
	#----------------------------------------------------------------------
	def isSelected(self):
		"""
		Returns true if the item is selected, otherwise returns false.
		"""
		res = super(QTableWidgetItem,self).isSelected()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def row(self):
		"""
		Returns the row of the item in the table
		If the item is not in a table, this function will return -1.
		"""
		res = super(QTableWidgetItem,self).row()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def sizeHint(self):
		"""
		Returns the size hint set for the table item.
		"""
		res = super(QTableWidgetItem,self).sizeHint()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def statusTip(self):
		"""
		Returns the items status tip.
		"""
		res = super(QTableWidgetItem,self).statusTip()
		return res
	#----------------------------------------------------------------------
	def tableWidget(self):
		"""
		Returns the table widget that contains the item.
		"""
		res = super(QTableWidgetItem,self).tableWidget()
		isinstance(res,QtGui.QTableWidget)
		return res
	#----------------------------------------------------------------------
	def text(self):
		"""
		Returns the items text.
		"""
		res = super(QTableWidgetItem,self).text()
		return res
	#----------------------------------------------------------------------
	def textAlignment(self):
		"""
		Returns the text alignment for the items text.
		"""
		res = super(QTableWidgetItem,self).textAlignment()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def toolTip(self):
		"""
		Returns the items tooltip.
		"""
		res = super(QTableWidgetItem,self).toolTip()
		return res
	#----------------------------------------------------------------------
	def type(self):
		"""
		Returns the type passed to the PySide.QtGui.QTableWidgetItem constructor.
		"""
		res = super(QTableWidgetItem,self).type()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def whatsThis(self):
		"""
		Returns the items Whats This? help.
		"""
		res = super(QTableWidgetItem,self).whatsThis()
		return res
	#----------------------------------------------------------------------
	def data(self,role):
		"""
		data(role)
			role=QtCore.int

		Returns the items data for the given role .
		"""
		res = super(QTableWidgetItem,self).data(role)
		return res
	#----------------------------------------------------------------------
	def __lt__(self,other):
		"""
		__lt__(other)
			other=QtGui.QTableWidgetItem

		Returns true if the item is less than the other item; otherwise returns false.
		"""
		res = super(QTableWidgetItem,self).__lt__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def read(self,in):
		"""
		read(in)
			in=QtCore.QDataStream

		Reads the item from stream in .
		"""
		res = super(QTableWidgetItem,self).read(in)
		return res
	#----------------------------------------------------------------------
	def setBackground(self,brush):
		"""
		setBackground(brush)
			brush=QtGui.QBrush

		Sets the items background brush to the specified brush .
		"""
		res = super(QTableWidgetItem,self).setBackground(brush)
		return res
	#----------------------------------------------------------------------
	def setCheckState(self,state):
		"""
		setCheckState(state)
			state=QtCore.Qt.CheckState


		"""
		res = super(QTableWidgetItem,self).setCheckState(state)
		return res
	#----------------------------------------------------------------------
	def setData(self,role,value):
		"""
		setData(role,value)
			role=QtCore.int
			value=object

		Sets the items data for the given role to the specified value .
		"""
		res = super(QTableWidgetItem,self).setData(role,value)
		return res
	#----------------------------------------------------------------------
	def setFlags(self,flags):
		"""
		setFlags(flags)
			flags=QtCore.Qt.ItemFlags


		"""
		res = super(QTableWidgetItem,self).setFlags(flags)
		return res
	#----------------------------------------------------------------------
	def setFont(self,font):
		"""
		setFont(font)
			font=QtGui.QFont

		Sets the font used to display the items text to the given font .
		"""
		res = super(QTableWidgetItem,self).setFont(font)
		return res
	#----------------------------------------------------------------------
	def setForeground(self,brush):
		"""
		setForeground(brush)
			brush=QtGui.QBrush

		Sets the items foreground brush to the specified brush .
		"""
		res = super(QTableWidgetItem,self).setForeground(brush)
		return res
	#----------------------------------------------------------------------
	def setIcon(self,icon):
		"""
		setIcon(icon)
			icon=QtGui.QIcon

		Sets the items icon to the icon specified.
		"""
		res = super(QTableWidgetItem,self).setIcon(icon)
		return res
	#----------------------------------------------------------------------
	def setSelected(self,select):
		"""
		setSelected(select)
			select=QtCore.bool

		Sets the selected state of the item to select .
		"""
		res = super(QTableWidgetItem,self).setSelected(select)
		return res
	#----------------------------------------------------------------------
	def setSizeHint(self,size):
		"""
		setSizeHint(size)
			size=QtCore.QSize

		Sets the size hint for the table item to be size
		If no size hint is set, the item delegate will compute the size hint based on the item data.
		"""
		res = super(QTableWidgetItem,self).setSizeHint(size)
		return res
	#----------------------------------------------------------------------
	def setStatusTip(self,statusTip):
		"""
		setStatusTip(statusTip)
			statusTip=unicode

		Sets the status tip for the table item to the text specified by statusTip
		PySide.QtGui.QTableWidget mouse tracking needs to be enabled for this feature to work.
		"""
		res = super(QTableWidgetItem,self).setStatusTip(statusTip)
		return res
	#----------------------------------------------------------------------
	def setText(self,text):
		"""
		setText(text)
			text=unicode

		Sets the items text to the text specified.
		"""
		res = super(QTableWidgetItem,self).setText(text)
		return res
	#----------------------------------------------------------------------
	def setTextAlignment(self,alignment):
		"""
		setTextAlignment(alignment)
			alignment=QtCore.int

		Sets the text alignment for the items text to the alignment specified.
		"""
		res = super(QTableWidgetItem,self).setTextAlignment(alignment)
		return res
	#----------------------------------------------------------------------
	def setToolTip(self,toolTip):
		"""
		setToolTip(toolTip)
			toolTip=unicode

		Sets the items tooltip to the string specified by toolTip .
		"""
		res = super(QTableWidgetItem,self).setToolTip(toolTip)
		return res
	#----------------------------------------------------------------------
	def setWhatsThis(self,whatsThis):
		"""
		setWhatsThis(whatsThis)
			whatsThis=unicode

		Sets the items Whats This? help to the string specified by whatsThis .
		"""
		res = super(QTableWidgetItem,self).setWhatsThis(whatsThis)
		return res
	#----------------------------------------------------------------------
	def write(self,out):
		"""
		write(out)
			out=QtCore.QDataStream

		Writes the item to stream out .
		"""
		res = super(QTableWidgetItem,self).write(out)
		return res

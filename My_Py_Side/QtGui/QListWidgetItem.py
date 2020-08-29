from PySide import QtGui, QtCore

class QListWidgetItem(QtGui.QListWidgetItem):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QListWidgetItem,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def background(self):
		"""
		Returns the brush used to display the list items background.
		"""
		res = super(QListWidgetItem,self).background()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def checkState(self):
		"""
		Returns the checked state of the list item (see Qt.CheckState ).
		"""
		res = super(QListWidgetItem,self).checkState()
		isinstance(res,QtCore.Qt.CheckState)
		return res
	#----------------------------------------------------------------------
	def clone(self):
		"""
		Creates an exact copy of the item.
		"""
		res = super(QListWidgetItem,self).clone()
		isinstance(res,QtGui.QListWidgetItem)
		return res
	#----------------------------------------------------------------------
	def flags(self):
		"""
		Returns the item flags for this item (see Qt.ItemFlags ).
		"""
		res = super(QListWidgetItem,self).flags()
		isinstance(res,QtCore.Qt.ItemFlags)
		return res
	#----------------------------------------------------------------------
	def font(self):
		"""
		Returns the font used to display this list items text.
		"""
		res = super(QListWidgetItem,self).font()
		isinstance(res,QtGui.QFont)
		return res
	#----------------------------------------------------------------------
	def foreground(self):
		"""
		Returns the brush used to display the list items foreground (e.g
		text).
		"""
		res = super(QListWidgetItem,self).foreground()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def icon(self):
		"""
		Returns the list items icon.
		"""
		res = super(QListWidgetItem,self).icon()
		isinstance(res,QtGui.QIcon)
		return res
	#----------------------------------------------------------------------
	def isHidden(self):
		"""
		Returns true if the item is hidden; otherwise returns false.
		"""
		res = super(QListWidgetItem,self).isHidden()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isSelected(self):
		"""
		Returns true if the item is selected; otherwise returns false.
		"""
		res = super(QListWidgetItem,self).isSelected()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def listWidget(self):
		"""
		Returns the list widget containing the item.
		"""
		res = super(QListWidgetItem,self).listWidget()
		isinstance(res,QtGui.QListWidget)
		return res
	#----------------------------------------------------------------------
	def sizeHint(self):
		"""
		Returns the size hint set for the list item.
		"""
		res = super(QListWidgetItem,self).sizeHint()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def statusTip(self):
		"""
		Returns the list items status tip.
		"""
		res = super(QListWidgetItem,self).statusTip()
		return res
	#----------------------------------------------------------------------
	def text(self):
		"""
		Returns the list items text.
		"""
		res = super(QListWidgetItem,self).text()
		return res
	#----------------------------------------------------------------------
	def textAlignment(self):
		"""
		Returns the text alignment for the list item.
		"""
		res = super(QListWidgetItem,self).textAlignment()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def toolTip(self):
		"""
		Returns the list items tooltip.
		"""
		res = super(QListWidgetItem,self).toolTip()
		return res
	#----------------------------------------------------------------------
	def type(self):
		"""
		Returns the type passed to the PySide.QtGui.QListWidgetItem constructor.
		"""
		res = super(QListWidgetItem,self).type()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def whatsThis(self):
		"""
		Returns the list items Whats This? help text.
		"""
		res = super(QListWidgetItem,self).whatsThis()
		return res
	#----------------------------------------------------------------------
	def data(self,role):
		"""
		data(role)
			role=QtCore.int

		Returns the items data for a given role
		Reimplement this function if you need extra roles or special behavior for certain roles.
		"""
		res = super(QListWidgetItem,self).data(role)
		return res
	#----------------------------------------------------------------------
	def __lt__(self,other):
		"""
		__lt__(other)
			other=QtGui.QListWidgetItem

		Returns true if this items text is less then other items text; otherwise returns false.
		"""
		res = super(QListWidgetItem,self).__lt__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def read(self,in):
		"""
		read(in)
			in=QtCore.QDataStream

		Reads the item from stream in .
		"""
		res = super(QListWidgetItem,self).read(in)
		return res
	#----------------------------------------------------------------------
	def setBackground(self,brush):
		"""
		setBackground(brush)
			brush=QtGui.QBrush

		Sets the background brush of the list item to the given brush .
		"""
		res = super(QListWidgetItem,self).setBackground(brush)
		return res
	#----------------------------------------------------------------------
	def setCheckState(self,state):
		"""
		setCheckState(state)
			state=QtCore.Qt.CheckState


		"""
		res = super(QListWidgetItem,self).setCheckState(state)
		return res
	#----------------------------------------------------------------------
	def setData(self,role,value):
		"""
		setData(role,value)
			role=QtCore.int
			value=object

		Sets the data for a given role to the given value
		Reimplement this function if you need extra roles or special behavior for certain roles.
		"""
		res = super(QListWidgetItem,self).setData(role,value)
		return res
	#----------------------------------------------------------------------
	def setFlags(self,flags):
		"""
		setFlags(flags)
			flags=QtCore.Qt.ItemFlags


		"""
		res = super(QListWidgetItem,self).setFlags(flags)
		return res
	#----------------------------------------------------------------------
	def setFont(self,font):
		"""
		setFont(font)
			font=QtGui.QFont

		Sets the font used when painting the item to the given font .
		"""
		res = super(QListWidgetItem,self).setFont(font)
		return res
	#----------------------------------------------------------------------
	def setForeground(self,brush):
		"""
		setForeground(brush)
			brush=QtGui.QBrush

		Sets the foreground brush of the list item to the given brush .
		"""
		res = super(QListWidgetItem,self).setForeground(brush)
		return res
	#----------------------------------------------------------------------
	def setHidden(self,hide):
		"""
		setHidden(hide)
			hide=QtCore.bool

		Hides the item if hide is true; otherwise shows the item.
		"""
		res = super(QListWidgetItem,self).setHidden(hide)
		return res
	#----------------------------------------------------------------------
	def setIcon(self,icon):
		"""
		setIcon(icon)
			icon=QtGui.QIcon

		Sets the icon for the list item to the given icon .
		"""
		res = super(QListWidgetItem,self).setIcon(icon)
		return res
	#----------------------------------------------------------------------
	def setSelected(self,select):
		"""
		setSelected(select)
			select=QtCore.bool

		Sets the selected state of the item to select .
		"""
		res = super(QListWidgetItem,self).setSelected(select)
		return res
	#----------------------------------------------------------------------
	def setSizeHint(self,size):
		"""
		setSizeHint(size)
			size=QtCore.QSize

		Sets the size hint for the list item to be size
		If no size hint is set, the item delegate will compute the size hint based on the item data.
		"""
		res = super(QListWidgetItem,self).setSizeHint(size)
		return res
	#----------------------------------------------------------------------
	def setStatusTip(self,statusTip):
		"""
		setStatusTip(statusTip)
			statusTip=unicode

		Sets the status tip for the list item to the text specified by statusTip
		PySide.QtGui.QListWidget mouseTracking needs to be enabled for this feature to work.
		"""
		res = super(QListWidgetItem,self).setStatusTip(statusTip)
		return res
	#----------------------------------------------------------------------
	def setText(self,text):
		"""
		setText(text)
			text=unicode

		Sets the text for the list widget items to the given text .
		"""
		res = super(QListWidgetItem,self).setText(text)
		return res
	#----------------------------------------------------------------------
	def setTextAlignment(self,alignment):
		"""
		setTextAlignment(alignment)
			alignment=QtCore.int

		Sets the list items text alignment to alignment .
		"""
		res = super(QListWidgetItem,self).setTextAlignment(alignment)
		return res
	#----------------------------------------------------------------------
	def setToolTip(self,toolTip):
		"""
		setToolTip(toolTip)
			toolTip=unicode

		Sets the tooltip for the list item to the text specified by toolTip .
		"""
		res = super(QListWidgetItem,self).setToolTip(toolTip)
		return res
	#----------------------------------------------------------------------
	def setWhatsThis(self,whatsThis):
		"""
		setWhatsThis(whatsThis)
			whatsThis=unicode

		Sets the Whats This? help for the list item to the text specified by whatsThis .
		"""
		res = super(QListWidgetItem,self).setWhatsThis(whatsThis)
		return res
	#----------------------------------------------------------------------
	def write(self,out):
		"""
		write(out)
			out=QtCore.QDataStream

		Writes the item to stream out .
		"""
		res = super(QListWidgetItem,self).write(out)
		return res

from PySide import QtGui, QtCore

class QTreeWidgetItem(QtGui.QTreeWidgetItem):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTreeWidgetItem,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def childCount(self):
		"""
		Returns the number of child items.
		"""
		res = super(QTreeWidgetItem,self).childCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def childIndicatorPolicy(self):
		"""
		Returns the item indicator policy
		This policy decides when the tree branch expand/collapse indicator is shown.
		"""
		res = super(QTreeWidgetItem,self).childIndicatorPolicy()
		isinstance(res,QtGui.QTreeWidgetItem.ChildIndicatorPolicy)
		return res
	#----------------------------------------------------------------------
	def clone(self):
		"""
		Creates a deep copy of the item and of its children.
		"""
		res = super(QTreeWidgetItem,self).clone()
		isinstance(res,QtGui.QTreeWidgetItem)
		return res
	#----------------------------------------------------------------------
	def columnCount(self):
		"""
		Returns the number of columns in the item.
		"""
		res = super(QTreeWidgetItem,self).columnCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def emitDataChanged(self):
		"""
		Causes the model associated with this item to emit a PySide.QtCore.QAbstractItemModel.dataChanged() () signal for this item.
		You normally only need to call this function if you have subclassed PySide.QtGui.QTreeWidgetItem and reimplemented PySide.QtGui.QTreeWidgetItem.data() and/or PySide.QtGui.QTreeWidgetItem.setData() .
		"""
		res = super(QTreeWidgetItem,self).emitDataChanged()
		return res
	#----------------------------------------------------------------------
	def executePendingSort(self):
		"""

		"""
		res = super(QTreeWidgetItem,self).executePendingSort()
		return res
	#----------------------------------------------------------------------
	def flags(self):
		"""
		Returns the flags used to describe the item
		These determine whether the item can be checked, edited, and selected.
		The default value for flags is Qt.ItemIsSelectable | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsDragEnabled
		If the item was constructed with a parent, flags will in addition contain Qt.ItemIsDropEnabled .
		"""
		res = super(QTreeWidgetItem,self).flags()
		isinstance(res,QtCore.Qt.ItemFlags)
		return res
	#----------------------------------------------------------------------
	def isDisabled(self):
		"""
		Returns true if the item is disabled; otherwise returns false.
		"""
		res = super(QTreeWidgetItem,self).isDisabled()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isExpanded(self):
		"""
		Returns true if the item is expanded, otherwise returns false.
		"""
		res = super(QTreeWidgetItem,self).isExpanded()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isFirstColumnSpanned(self):
		"""
		Returns true if the item is spanning all the columns in a row; otherwise returns false.
		"""
		res = super(QTreeWidgetItem,self).isFirstColumnSpanned()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isHidden(self):
		"""
		Returns true if the item is hidden, otherwise returns false.
		"""
		res = super(QTreeWidgetItem,self).isHidden()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isSelected(self):
		"""
		Returns true if the item is selected, otherwise returns false.
		"""
		res = super(QTreeWidgetItem,self).isSelected()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def itemChanged(self):
		"""

		"""
		res = super(QTreeWidgetItem,self).itemChanged()
		return res
	#----------------------------------------------------------------------
	def parent(self):
		"""
		Returns the items parent.
		"""
		res = super(QTreeWidgetItem,self).parent()
		isinstance(res,QtGui.QTreeWidgetItem)
		return res
	#----------------------------------------------------------------------
	def takeChildren(self):
		"""
		Removes the list of children and returns it, otherwise returns an empty list.
		"""
		res = super(QTreeWidgetItem,self).takeChildren()
		return res
	#----------------------------------------------------------------------
	def treeWidget(self):
		"""
		Returns the tree widget that contains the item.
		"""
		res = super(QTreeWidgetItem,self).treeWidget()
		isinstance(res,QtGui.QTreeWidget)
		return res
	#----------------------------------------------------------------------
	def type(self):
		"""
		Returns the type passed to the PySide.QtGui.QTreeWidgetItem constructor.
		"""
		res = super(QTreeWidgetItem,self).type()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def addChild(self,child):
		"""
		addChild(child)
			child=QtGui.QTreeWidgetItem

		Appends the child item to the list of children.
		"""
		res = super(QTreeWidgetItem,self).addChild(child)
		return res
	#----------------------------------------------------------------------
	def addChildren(self,children):
		"""
		addChildren(children)
			children=unKnown


		"""
		res = super(QTreeWidgetItem,self).addChildren(children)
		return res
	#----------------------------------------------------------------------
	def background(self,column):
		"""
		background(column)
			column=QtCore.int

		Returns the brush used to render the background of the specified column .
		"""
		res = super(QTreeWidgetItem,self).background(column)
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def checkState(self,column):
		"""
		checkState(column)
			column=QtCore.int

		Returns the check state of the label in the given column .
		"""
		res = super(QTreeWidgetItem,self).checkState(column)
		isinstance(res,QtCore.Qt.CheckState)
		return res
	#----------------------------------------------------------------------
	def child(self,index):
		"""
		child(index)
			index=QtCore.int

		Returns the item at the given index in the list of the items children.
		"""
		res = super(QTreeWidgetItem,self).child(index)
		isinstance(res,QtGui.QTreeWidgetItem)
		return res
	#----------------------------------------------------------------------
	def childrenCheckState(self,column):
		"""
		childrenCheckState(column)
			column=QtCore.int


		"""
		res = super(QTreeWidgetItem,self).childrenCheckState(column)
		return res
	#----------------------------------------------------------------------
	def data(self,column,role):
		"""
		data(column,role)
			column=QtCore.int
			role=QtCore.int

		Returns the value for the items column and role .
		"""
		res = super(QTreeWidgetItem,self).data(column,role)
		return res
	#----------------------------------------------------------------------
	def font(self,column):
		"""
		font(column)
			column=QtCore.int

		Returns the font used to render the text in the specified column .
		"""
		res = super(QTreeWidgetItem,self).font(column)
		isinstance(res,QtGui.QFont)
		return res
	#----------------------------------------------------------------------
	def foreground(self,column):
		"""
		foreground(column)
			column=QtCore.int

		Returns the brush used to render the foreground (e.g
		text) of the specified column .
		"""
		res = super(QTreeWidgetItem,self).foreground(column)
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def icon(self,column):
		"""
		icon(column)
			column=QtCore.int

		Returns the icon that is displayed in the specified column .
		"""
		res = super(QTreeWidgetItem,self).icon(column)
		isinstance(res,QtGui.QIcon)
		return res
	#----------------------------------------------------------------------
	def indexOfChild(self,child):
		"""
		indexOfChild(child)
			child=QtGui.QTreeWidgetItem

		Returns the index of the given child in the items list of children.
		"""
		res = super(QTreeWidgetItem,self).indexOfChild(child)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def insertChild(self,index,child):
		"""
		insertChild(index,child)
			index=QtCore.int
			child=QtGui.QTreeWidgetItem

		Inserts the child item at index in the list of children.
		If the child has already been inserted somewhere else it wont be inserted again.
		"""
		res = super(QTreeWidgetItem,self).insertChild(index,child)
		return res
	#----------------------------------------------------------------------
	def insertChildren(self,index,children):
		"""
		insertChildren(index,children)
			index=QtCore.int
			children=unKnown


		"""
		res = super(QTreeWidgetItem,self).insertChildren(index,children)
		return res
	#----------------------------------------------------------------------
	def __lt__(self,other):
		"""
		__lt__(other)
			other=QtGui.QTreeWidgetItem

		Returns true if the text in the item is less than the text in the other item, otherwise returns false.
		"""
		res = super(QTreeWidgetItem,self).__lt__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def read(self,in):
		"""
		read(in)
			in=QtCore.QDataStream

		Reads the item from stream in
		This only reads data into a single item.
		"""
		res = super(QTreeWidgetItem,self).read(in)
		return res
	#----------------------------------------------------------------------
	def removeChild(self,child):
		"""
		removeChild(child)
			child=QtGui.QTreeWidgetItem

		Removes the given item indicated by child
		The removed item will not be deleted.
		"""
		res = super(QTreeWidgetItem,self).removeChild(child)
		return res
	#----------------------------------------------------------------------
	def setBackground(self,column,brush):
		"""
		setBackground(column,brush)
			column=QtCore.int
			brush=QtGui.QBrush

		Sets the background brush of the label in the given column to the specified brush .
		"""
		res = super(QTreeWidgetItem,self).setBackground(column,brush)
		return res
	#----------------------------------------------------------------------
	def setCheckState(self,column,state):
		"""
		setCheckState(column,state)
			column=QtCore.int
			state=QtCore.Qt.CheckState


		"""
		res = super(QTreeWidgetItem,self).setCheckState(column,state)
		return res
	#----------------------------------------------------------------------
	def setChildIndicatorPolicy(self,policy):
		"""
		setChildIndicatorPolicy(policy)
			policy=QtGui.QTreeWidgetItem.ChildIndicatorPolicy


		"""
		res = super(QTreeWidgetItem,self).setChildIndicatorPolicy(policy)
		return res
	#----------------------------------------------------------------------
	def setData(self,column,role,value):
		"""
		setData(column,role,value)
			column=QtCore.int
			role=QtCore.int
			value=object

		Sets the value for the items column and role to the given value .
		The role describes the type of data specified by value , and is defined by the Qt.ItemDataRole enum.
		"""
		res = super(QTreeWidgetItem,self).setData(column,role,value)
		return res
	#----------------------------------------------------------------------
	def setDisabled(self,disabled):
		"""
		setDisabled(disabled)
			disabled=QtCore.bool

		Disables the item if disabled is true; otherwise enables the item.
		"""
		res = super(QTreeWidgetItem,self).setDisabled(disabled)
		return res
	#----------------------------------------------------------------------
	def setExpanded(self,expand):
		"""
		setExpanded(expand)
			expand=QtCore.bool

		Expands the item if expand is true, otherwise collapses the item.
		"""
		res = super(QTreeWidgetItem,self).setExpanded(expand)
		return res
	#----------------------------------------------------------------------
	def setFirstColumnSpanned(self,span):
		"""
		setFirstColumnSpanned(span)
			span=QtCore.bool

		Sets the first section to span all columns if span is true; otherwise all item sections are shown.
		"""
		res = super(QTreeWidgetItem,self).setFirstColumnSpanned(span)
		return res
	#----------------------------------------------------------------------
	def setFlags(self,flags):
		"""
		setFlags(flags)
			flags=QtCore.Qt.ItemFlags


		"""
		res = super(QTreeWidgetItem,self).setFlags(flags)
		return res
	#----------------------------------------------------------------------
	def setFont(self,column,font):
		"""
		setFont(column,font)
			column=QtCore.int
			font=QtGui.QFont

		Sets the font used to display the text in the given column to the given font .
		"""
		res = super(QTreeWidgetItem,self).setFont(column,font)
		return res
	#----------------------------------------------------------------------
	def setForeground(self,column,brush):
		"""
		setForeground(column,brush)
			column=QtCore.int
			brush=QtGui.QBrush

		Sets the foreground brush of the label in the given column to the specified brush .
		"""
		res = super(QTreeWidgetItem,self).setForeground(column,brush)
		return res
	#----------------------------------------------------------------------
	def setHidden(self,hide):
		"""
		setHidden(hide)
			hide=QtCore.bool

		Hides the item if hide is true, otherwise shows the item.
		"""
		res = super(QTreeWidgetItem,self).setHidden(hide)
		return res
	#----------------------------------------------------------------------
	def setIcon(self,column,icon):
		"""
		setIcon(column,icon)
			column=QtCore.int
			icon=QtGui.QIcon

		Sets the icon to be displayed in the given column to icon .
		"""
		res = super(QTreeWidgetItem,self).setIcon(column,icon)
		return res
	#----------------------------------------------------------------------
	def setSelected(self,select):
		"""
		setSelected(select)
			select=QtCore.bool

		Sets the selected state of the item to select .
		"""
		res = super(QTreeWidgetItem,self).setSelected(select)
		return res
	#----------------------------------------------------------------------
	def setSizeHint(self,column,size):
		"""
		setSizeHint(column,size)
			column=QtCore.int
			size=QtCore.QSize

		Sets the size hint for the tree item in the given column to be size
		If no size hint is set, the item delegate will compute the size hint based on the item data.
		"""
		res = super(QTreeWidgetItem,self).setSizeHint(column,size)
		return res
	#----------------------------------------------------------------------
	def setStatusTip(self,column,statusTip):
		"""
		setStatusTip(column,statusTip)
			column=QtCore.int
			statusTip=unicode

		Sets the status tip for the given column to the given statusTip
		PySide.QtGui.QTreeWidget mouse tracking needs to be enabled for this feature to work.
		"""
		res = super(QTreeWidgetItem,self).setStatusTip(column,statusTip)
		return res
	#----------------------------------------------------------------------
	def setText(self,column,text):
		"""
		setText(column,text)
			column=QtCore.int
			text=unicode

		Sets the text to be displayed in the given column to the given text .
		"""
		res = super(QTreeWidgetItem,self).setText(column,text)
		return res
	#----------------------------------------------------------------------
	def setTextAlignment(self,column,alignment):
		"""
		setTextAlignment(column,alignment)
			column=QtCore.int
			alignment=QtCore.int

		Sets the text alignment for the label in the given column to the alignment specified (see Qt.AlignmentFlag ).
		"""
		res = super(QTreeWidgetItem,self).setTextAlignment(column,alignment)
		return res
	#----------------------------------------------------------------------
	def setToolTip(self,column,toolTip):
		"""
		setToolTip(column,toolTip)
			column=QtCore.int
			toolTip=unicode

		Sets the tooltip for the given column to toolTip .
		"""
		res = super(QTreeWidgetItem,self).setToolTip(column,toolTip)
		return res
	#----------------------------------------------------------------------
	def setWhatsThis(self,column,whatsThis):
		"""
		setWhatsThis(column,whatsThis)
			column=QtCore.int
			whatsThis=unicode

		Sets the Whats This? help for the given column to whatsThis .
		"""
		res = super(QTreeWidgetItem,self).setWhatsThis(column,whatsThis)
		return res
	#----------------------------------------------------------------------
	def sizeHint(self,column):
		"""
		sizeHint(column)
			column=QtCore.int

		Returns the size hint set for the tree item in the given column (see PySide.QtCore.QSize ).
		"""
		res = super(QTreeWidgetItem,self).sizeHint(column)
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def sortChildren(self,*args,**kwargs):
		"""
		sortChildren(column,order)
			column=QtCore.int
			order=QtCore.Qt.SortOrder

		sortChildren(column,order,climb)
			column=QtCore.int
			order=QtCore.Qt.SortOrder
			climb=QtCore.bool


		"""
		res = super(QTreeWidgetItem,self).sortChildren(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def statusTip(self,column):
		"""
		statusTip(column)
			column=QtCore.int

		Returns the status tip for the contents of the given column .
		"""
		res = super(QTreeWidgetItem,self).statusTip(column)
		return res
	#----------------------------------------------------------------------
	def takeChild(self,index):
		"""
		takeChild(index)
			index=QtCore.int

		Removes the item at index and returns it, otherwise return 0.
		"""
		res = super(QTreeWidgetItem,self).takeChild(index)
		isinstance(res,QtGui.QTreeWidgetItem)
		return res
	#----------------------------------------------------------------------
	def text(self,column):
		"""
		text(column)
			column=QtCore.int

		Returns the text in the specified column .
		"""
		res = super(QTreeWidgetItem,self).text(column)
		return res
	#----------------------------------------------------------------------
	def textAlignment(self,column):
		"""
		textAlignment(column)
			column=QtCore.int

		Returns the text alignment for the label in the given column (see Qt.AlignmentFlag ).
		"""
		res = super(QTreeWidgetItem,self).textAlignment(column)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def toolTip(self,column):
		"""
		toolTip(column)
			column=QtCore.int

		Returns the tool tip for the given column .
		"""
		res = super(QTreeWidgetItem,self).toolTip(column)
		return res
	#----------------------------------------------------------------------
	def whatsThis(self,column):
		"""
		whatsThis(column)
			column=QtCore.int

		Returns the Whats This? help for the contents of the given column .
		"""
		res = super(QTreeWidgetItem,self).whatsThis(column)
		return res
	#----------------------------------------------------------------------
	def write(self,out):
		"""
		write(out)
			out=QtCore.QDataStream

		Writes the item to stream out
		This only writes data from one single item.
		"""
		res = super(QTreeWidgetItem,self).write(out)
		return res

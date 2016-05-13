import QT
import Qt_Roles_And_Enums
QtCore            = QT.QtCore
QtGui             = QT.QtGui
Qt                = QT.Qt
Item_Data_Roles   = Qt_Roles_And_Enums.Standered_Item_Data_Roles

class Tree_Widget_Item(QtGui.QTreeWidgetItem):
	''''''
	Data_Roles = Item_Data_Roles
	USER_TYPE  = QT.user_type_counter()
	def __init__(self,*args,**kwargs):
		''''''
		super(Tree_Widget_Item,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def childCount(self):
		"""
		Returns the number of child items.
		"""
		res = super(Tree_Widget_Item,self).childCount()
		
		return res
	#----------------------------------------------------------------------
	def iter_children(self):
		"""
		iterate child items.
		"""
		for index in range(self.ChildCount):
			yield self.child(index)
	#----------------------------------------------------------------------
	def childIndicatorPolicy(self):
		"""
		Returns the item indicator policy
		This policy decides when the tree branch expand/collapse indicator is shown.
		"""
		res = super(Tree_Widget_Item,self).childIndicatorPolicy()
		isinstance(res,QtGui.QTreeWidgetItem.ChildIndicatorPolicy)
		return res
	#----------------------------------------------------------------------
	def columnCount(self):
		"""
		Returns the number of columns in the item.
		"""
		res = super(Tree_Widget_Item,self).columnCount()
		
		return res
	#----------------------------------------------------------------------
	def emitDataChanged(self):
		"""
		Causes the model associated with this item to emit a PySide.QtCore.QAbstractItemModel.dataChanged() () signal for this item.
		You normally only need to call this function if you have subclassed PySide.QtGui.QTreeWidgetItem and reimplemented PySide.QtGui.QTreeWidgetItem.data() and/or PySide.QtGui.QTreeWidgetItem.setData() .
		"""
		res = super(Tree_Widget_Item,self).emitDataChanged()
		return res
	#----------------------------------------------------------------------
	def executePendingSort(self):
		"""

		"""
		res = super(Tree_Widget_Item,self).executePendingSort()
		return res
	#----------------------------------------------------------------------
	def flags(self):
		"""
		Returns the flags used to describe the item
		These determine whether the item can be checked, edited, and selected.
		The default value for flags is Qt.ItemIsSelectable | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsDragEnabled
		If the item was constructed with a parent, flags will in addition contain Qt.ItemIsDropEnabled .
		"""
		res = super(Tree_Widget_Item,self).flags()
		isinstance(res,QtCore.Qt.ItemFlags)
		return res
	#----------------------------------------------------------------------
	def isDisabled(self):
		"""
		Returns true if the item is disabled; otherwise returns false.
		"""
		res = super(Tree_Widget_Item,self).isDisabled()
		
		return res
	#----------------------------------------------------------------------
	def isExpanded(self):
		"""
		Returns true if the item is expanded, otherwise returns false.
		"""
		res = super(Tree_Widget_Item,self).isExpanded()
		
		return res
	#----------------------------------------------------------------------
	def isFirstColumnSpanned(self):
		"""
		Returns true if the item is spanning all the columns in a row; otherwise returns false.
		"""
		res = super(Tree_Widget_Item,self).isFirstColumnSpanned()
		
		return res
	#----------------------------------------------------------------------
	def isHidden(self):
		"""
		Returns true if the item is hidden, otherwise returns false.
		"""
		res = super(Tree_Widget_Item,self).isHidden()
		
		return res
	#----------------------------------------------------------------------
	def isSelected(self):
		"""
		Returns true if the item is selected, otherwise returns false.
		"""
		res = super(Tree_Widget_Item,self).isSelected()
		
		return res
	#----------------------------------------------------------------------
	def parent(self):
		"""
		Returns the items parent.
		"""
		res = super(Tree_Widget_Item,self).parent()
		isinstance(res,QtGui.QTreeWidgetItem)
		return res
	#----------------------------------------------------------------------
	def takeChildren(self):
		"""
		Removes the list of children and returns it, otherwise returns an empty list.
		"""
		res = super(Tree_Widget_Item,self).takeChildren()
		return res
	#----------------------------------------------------------------------
	def treeWidget(self):
		"""
		Returns the tree widget that contains the item.
		"""
		res = super(Tree_Widget_Item,self).treeWidget()
		isinstance(res,QtGui.QTreeWidget)
		return res
	#----------------------------------------------------------------------
	def type(self):
		"""
		Returns the type passed to the PySide.QtGui.QTreeWidgetItem constructor.
		"""
		return self.USER_TYPE
	#----------------------------------------------------------------------
	def addChild(self,child):
		"""
		addChild(child)
			child=QtGui.QTreeWidgetItem

		Appends the child item to the list of children.
		"""
		res = super(Tree_Widget_Item,self).addChild(child)
		return res
	#----------------------------------------------------------------------
	def addChildren(self,children):
		"""
		addChildren(children)
			children=unKnown


		"""
		res = super(Tree_Widget_Item,self).addChildren(children)
		return res
	#----------------------------------------------------------------------
	def background(self,column=0):
		"""
		background(column)
			column=QtCore.int

		Returns the brush used to render the background of the specified column .
		"""
		res = super(Tree_Widget_Item,self).background(column)
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def checkState(self,column=0):
		"""
		checkState(column)
			column=QtCore.int

		Returns the check state of the label in the given column .
		"""
		res = super(Tree_Widget_Item,self).checkState(column)
		isinstance(res,QtCore.Qt.CheckState)
		return res
	#----------------------------------------------------------------------
	def child(self,index):
		"""
		child(index)
			index=QtCore.int

		Returns the item at the given index in the list of the items children.
		"""
		res = super(Tree_Widget_Item,self).child(index)
		isinstance(res,QtGui.QTreeWidgetItem)
		return res
	#----------------------------------------------------------------------
	def children(self):
		res = []
		for row in  range(self.ChildCount):
			res.append(self.child(row))
		return res
	#----------------------------------------------------------------------
	def childrenCheckState(self,column=0):
		"""
		childrenCheckState(column)
			column=QtCore.int


		"""
		res = super(Tree_Widget_Item,self).childrenCheckState(column)
		return res
	#----------------------------------------------------------------------
	def data(self,column=0,role=Item_Data_Roles.DISPLAY):
		"""
		data(column,role)
			column=QtCore.int
			role=QtCore.int

		Returns the value for the items column and role .
		"""
		res = super(Tree_Widget_Item,self).data(column,role)
		return res
	#----------------------------------------------------------------------
	def font(self,column=0):
		"""
		font(column)
			column=QtCore.int

		Returns the font used to render the text in the specified column .
		"""
		res = super(Tree_Widget_Item,self).font(column)
		isinstance(res,QtGui.QFont)
		return res
	#----------------------------------------------------------------------
	def foreground(self,column=0):
		"""
		foreground(column)
			column=QtCore.int

		Returns the brush used to render the foreground (e.g
		text) of the specified column .
		"""
		res = super(Tree_Widget_Item,self).foreground(column)
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def icon(self,column=0):
		"""
		icon(column)
			column=QtCore.int

		Returns the icon that is displayed in the specified column .
		"""
		res = super(Tree_Widget_Item,self).icon(column)
		isinstance(res,QtGui.QIcon)
		return res
	#----------------------------------------------------------------------
	def indexOfChild(self,child):
		"""
		indexOfChild(child)
			child=QtGui.QTreeWidgetItem

		Returns the index of the given child in the items list of children.
		"""
		res = super(Tree_Widget_Item,self).indexOfChild(child)
		
		return res
	#----------------------------------------------------------------------
	def row(self):
		""""""
		parent = self.parent()
		if parent == None:
			parent = self.treeWidget()
			return parent.indexOfTopLevelItem(self)
		else:
			return parent.indexOfChild(self)
	#----------------------------------------------------------------------
	def insertChild(self,index,child):
		"""
		insertChild(index,child)
			index=QtCore.int
			child=QtGui.QTreeWidgetItem

		Inserts the child item at index in the list of children.
		If the child has already been inserted somewhere else it wont be inserted again.
		"""
		res = super(Tree_Widget_Item,self).insertChild(index,child)
		return res
	#----------------------------------------------------------------------
	def insertChildren(self,index,children):
		"""
		insertChildren(index,children)
			index=QtCore.int
			children=unKnown


		"""
		res = super(Tree_Widget_Item,self).insertChildren(index,children)
		return res
	#----------------------------------------------------------------------
	def read(self,stream):
		"""
		read(in)
			in=QtCore.QDataStream

		Reads the item from stream in
		This only reads data into a single item.
		"""
		res = super(Tree_Widget_Item,self).read(stream)
		return res
	#----------------------------------------------------------------------
	def removeChild(self,child):
		"""
		removeChild(child)
			child=QtGui.QTreeWidgetItem

		Removes the given item indicated by child
		The removed item will not be deleted.
		"""
		res = super(Tree_Widget_Item,self).removeChild(child)
		return res
	#----------------------------------------------------------------------
	def remove_Child_By_value(self, value, column=0, role=Item_Data_Roles.DISPLAY, max=1):
		count = 0
		for child in self.iter_children():
			if child.data(column=column, role=role) == value:
				self.removeChild(child)
				count += 1
				if count == max:
					break
	#----------------------------------------------------------------------
	def setBackground(self,column=0,brush=None):
		"""
		setBackground(column,brush)
			column=QtCore.int
			brush=QtGui.QBrush

		Sets the background brush of the label in the given column to the specified brush .
		"""
		res = super(Tree_Widget_Item,self).setBackground(column,brush)
		return res
	#----------------------------------------------------------------------
	def setCheckState(self,column=0,state=None):
		"""
		setCheckState(column,state)
			column=QtCore.int
			state=QtCore.Qt.CheckState


		"""
		res = super(Tree_Widget_Item,self).setCheckState(column,state)
		return res
	#----------------------------------------------------------------------
	def setChildIndicatorPolicy(self,policy):
		"""
		setChildIndicatorPolicy(policy)
			policy=QtGui.QTreeWidgetItem.ChildIndicatorPolicy


		"""
		res = super(Tree_Widget_Item,self).setChildIndicatorPolicy(policy)
		return res
	#----------------------------------------------------------------------
	def setData(self,column=0,role=Item_Data_Roles.DISPLAY,value=""):
		"""
		setData(column,role,value)
			column=QtCore.int
			role=QtCore.int
			value=object

		Sets the value for the items column and role to the given value .
		The role describes the type of data specified by value , and is defined by the Qt.ItemDataRole enum.
		"""
		res = super(Tree_Widget_Item,self).setData(column,role,value)
		return res
	#----------------------------------------------------------------------
	def setDisabled(self,disabled=True):
		"""
		setDisabled(disabled)
			disabled=QtCore.bool

		Disables the item if disabled is true; otherwise enables the item.
		"""
		res = super(Tree_Widget_Item,self).setDisabled(disabled)
		return res
	#----------------------------------------------------------------------
	def setExpanded(self,expand=True):
		"""
		setExpanded(expand)
			expand=QtCore.bool

		Expands the item if expand is true, otherwise collapses the item.
		"""
		res = super(Tree_Widget_Item,self).setExpanded(expand)
		return res
	#----------------------------------------------------------------------
	def setFirstColumnSpanned(self,span):
		"""
		setFirstColumnSpanned(span)
			span=QtCore.bool

		Sets the first section to span all columns if span is true; otherwise all item sections are shown.
		"""
		res = super(Tree_Widget_Item,self).setFirstColumnSpanned(span)
		return res
	#----------------------------------------------------------------------
	def setFlags(self,flags):
		"""
		setFlags(flags)
			flags=QtCore.Qt.ItemFlags


		"""
		res = super(Tree_Widget_Item,self).setFlags(flags)
		return res
	#----------------------------------------------------------------------
	def setFont(self,column,font):
		"""
		setFont(column,font)
			column=QtCore.int
			font=QtGui.QFont

		Sets the font used to display the text in the given column to the given font .
		"""
		res = super(Tree_Widget_Item,self).setFont(column,font)
		return res
	#----------------------------------------------------------------------
	def setForeground(self,column,brush):
		"""
		setForeground(column,brush)
			column=QtCore.int
			brush=QtGui.QBrush

		Sets the foreground brush of the label in the given column to the specified brush .
		"""
		res = super(Tree_Widget_Item,self).setForeground(column,brush)
		return res
	#----------------------------------------------------------------------
	def setHidden(self,hide):
		"""
		setHidden(hide)
			hide=QtCore.bool

		Hides the item if hide is true, otherwise shows the item.
		"""
		res = super(Tree_Widget_Item,self).setHidden(hide)
		return res
	#----------------------------------------------------------------------
	def setIcon(self,column,icon):
		"""
		setIcon(column,icon)
			column=QtCore.int
			icon=QtGui.QIcon

		Sets the icon to be displayed in the given column to icon .
		"""
		res = super(Tree_Widget_Item,self).setIcon(column,icon)
		return res
	#----------------------------------------------------------------------
	def setSelected(self,select):
		"""
		setSelected(select)
			select=QtCore.bool

		Sets the selected state of the item to select .
		"""
		res = super(Tree_Widget_Item,self).setSelected(select)
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
		res = super(Tree_Widget_Item,self).setSizeHint(column,size)
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
		res = super(Tree_Widget_Item,self).setStatusTip(column,statusTip)
		return res
	#----------------------------------------------------------------------
	def setText(self,column,text):
		"""
		setText(column,text)
			column=QtCore.int
			text=unicode

		Sets the text to be displayed in the given column to the given text .
		"""
		res = super(Tree_Widget_Item,self).setText(column,text)
		return res
	#----------------------------------------------------------------------
	def setTextAlignment(self,column,alignment):
		"""
		setTextAlignment(column,alignment)
			column=QtCore.int
			alignment=QtCore.int

		Sets the text alignment for the label in the given column to the alignment specified (see Qt.AlignmentFlag ).
		"""
		res = super(Tree_Widget_Item,self).setTextAlignment(column,alignment)
		return res
	#----------------------------------------------------------------------
	def setToolTip(self,column,toolTip):
		"""
		setToolTip(column,toolTip)
			column=QtCore.int
			toolTip=unicode

		Sets the tooltip for the given column to toolTip .
		"""
		res = super(Tree_Widget_Item,self).setToolTip(column,toolTip)
		return res
	#----------------------------------------------------------------------
	def setWhatsThis(self,column,whatsThis):
		"""
		setWhatsThis(column,whatsThis)
			column=QtCore.int
			whatsThis=unicode

		Sets the Whats This? help for the given column to whatsThis .
		"""
		res = super(Tree_Widget_Item,self).setWhatsThis(column,whatsThis)
		return res
	#----------------------------------------------------------------------
	def sizeHint(self,column=0):
		"""
		sizeHint(column)
			column=QtCore.int

		Returns the size hint set for the tree item in the given column (see PySide.QtCore.QSize ).
		"""
		res = super(Tree_Widget_Item,self).sizeHint(column)
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
		res = super(Tree_Widget_Item,self).sortChildren(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def statusTip(self,column=0):
		"""
		statusTip(column)
			column=QtCore.int

		Returns the status tip for the contents of the given column .
		"""
		res = super(Tree_Widget_Item,self).statusTip(column)
		return res
	#----------------------------------------------------------------------
	def takeChild(self,index):
		"""
		takeChild(index)
			index=QtCore.int

		Removes the item at index and returns it, otherwise return 0.
		"""
		res = super(Tree_Widget_Item,self).takeChild(index)
		isinstance(res,QtGui.QTreeWidgetItem)
		return res
	#----------------------------------------------------------------------
	def text(self,column=0):
		"""
		text(column)
			column=QtCore.int

		Returns the text in the specified column .
		"""
		res = super(Tree_Widget_Item,self).text(column)
		return res
	#----------------------------------------------------------------------
	def textAlignment(self,column=0):
		"""
		textAlignment(column)
			column=QtCore.int

		Returns the text alignment for the label in the given column (see Qt.AlignmentFlag ).
		"""
		res = super(Tree_Widget_Item,self).textAlignment(column)
		
		return res
	#----------------------------------------------------------------------
	def toolTip(self,column=0):
		"""
		toolTip(column)
			column=QtCore.int

		Returns the tool tip for the given column .
		"""
		res = super(Tree_Widget_Item,self).toolTip(column)
		return res
	#----------------------------------------------------------------------
	def whatsThis(self,column=0):
		"""
		whatsThis(column)
			column=QtCore.int

		Returns the Whats This? help for the contents of the given column .
		"""
		res = super(Tree_Widget_Item,self).whatsThis(column)
		return res
	#----------------------------------------------------------------------
	def write(self,out):
		"""
		write(out)
			out=QtCore.QDataStream

		Writes the item to stream out
		This only writes data from one single item.
		"""
		res = super(Tree_Widget_Item,self).write(out)
		return res
	
	ChildCount  = property(childCount)
	Disabled    = property(isDisabled,setDisabled)
	Expanded    = property(isExpanded,setExpanded)
	Hidden      = property(isHidden,setHidden)
	Selected    = property(isSelected,setSelected)
	Flags       = property(flags,setFlags)
	ColumnCount = property(columnCount)
	IsDisabled  = property(isDisabled, setDisabled)
	Foreground  = property(foreground, setForeground)
	Icon        = property(icon, setIcon)
	Font        = property(font, setFont)
	CheckState  = property(checkState, setCheckState)
	Background  = property(background, setBackground)
	Parent      = property(parent)
	IsExpanded  = property(isExpanded, setExpanded)
	IsHidden    = property(isHidden, setHidden)


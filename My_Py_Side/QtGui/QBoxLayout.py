from PySide import QtGui, QtCore

class QBoxLayout(QtGui.QBoxLayout):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QBoxLayout,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def direction(self):
		"""
		Returns the direction of the box
		PySide.QtGui.QBoxLayout.addWidget() and PySide.QtGui.QBoxLayout.addSpacing() work in this direction; the stretch stretches in this direction.
		"""
		res = super(QBoxLayout,self).direction()
		isinstance(res,QtGui.QBoxLayout.Direction)
		return res
	#----------------------------------------------------------------------
	def addLayout(self,layout,stretch=None):
		"""
		addLayout(layout,stretch=None)
			layout=QtGui.QLayout
			stretch=QtCore.int

		Adds layout to the end of the box, with serial stretch factor stretch .
		"""
		res = super(QBoxLayout,self).addLayout(layout,stretch)
		return res
	#----------------------------------------------------------------------
	def addSpacerItem(self,spacerItem):
		"""
		addSpacerItem(spacerItem)
			spacerItem=QtGui.QSpacerItem

		Adds spacerItem to the end of this box layout.
		"""
		res = super(QBoxLayout,self).addSpacerItem(spacerItem)
		return res
	#----------------------------------------------------------------------
	def addSpacing(self,size):
		"""
		addSpacing(size)
			size=QtCore.int

		Adds a non-stretchable space (a PySide.QtGui.QSpacerItem ) with size size to the end of this box layout
		PySide.QtGui.QBoxLayout provides default margin and spacing
		This function adds additional space.
		"""
		res = super(QBoxLayout,self).addSpacing(size)
		return res
	#----------------------------------------------------------------------
	def addStretch(self,stretch=None):
		"""
		addStretch(stretch=None)
			stretch=QtCore.int

		Adds a stretchable space (a PySide.QtGui.QSpacerItem ) with zero minimum size and stretch factor stretch to the end of this box layout.
		"""
		res = super(QBoxLayout,self).addStretch(stretch)
		return res
	#----------------------------------------------------------------------
	def addStrut(self,arg__1):
		"""
		addStrut(arg__1)
			arg__1=QtCore.int

		Limits the perpendicular dimension of the box (e.g
		height if the box is LeftToRight ) to a minimum of size
		Other constraints may increase the limit.
		"""
		res = super(QBoxLayout,self).addStrut(arg__1)
		return res
	#----------------------------------------------------------------------
	def addWidget(self,arg__1,stretch=None,alignment=None):
		"""
		addWidget(arg__1,stretch=None,alignment=None)
			arg__1=QtGui.QWidget
			stretch=QtCore.int
			alignment=QtCore.Qt.Alignment


		"""
		res = super(QBoxLayout,self).addWidget(arg__1,stretch,alignment)
		return res
	#----------------------------------------------------------------------
	def insertItem(self,index,arg__2):
		"""
		insertItem(index,arg__2)
			index=QtCore.int
			arg__2=QtGui.QLayoutItem

		Inserts item into this box layout at position index
		If index is negative, the item is added at the end.
		"""
		res = super(QBoxLayout,self).insertItem(index,arg__2)
		return res
	#----------------------------------------------------------------------
	def insertLayout(self,index,layout,stretch=None):
		"""
		insertLayout(index,layout,stretch=None)
			index=QtCore.int
			layout=QtGui.QLayout
			stretch=QtCore.int

		Inserts layout at position index , with stretch factor stretch
		If index is negative, the layout is added at the end.
		layout becomes a child of the box layout.
		"""
		res = super(QBoxLayout,self).insertLayout(index,layout,stretch)
		return res
	#----------------------------------------------------------------------
	def insertSpacerItem(self,index,spacerItem):
		"""
		insertSpacerItem(index,spacerItem)
			index=QtCore.int
			spacerItem=QtGui.QSpacerItem

		Inserts spacerItem at position index , with zero minimum size and stretch factor
		If index is negative the space is added at the end.
		"""
		res = super(QBoxLayout,self).insertSpacerItem(index,spacerItem)
		return res
	#----------------------------------------------------------------------
	def insertSpacing(self,index,size):
		"""
		insertSpacing(index,size)
			index=QtCore.int
			size=QtCore.int

		Inserts a non-stretchable space (a PySide.QtGui.QSpacerItem ) at position index , with size size
		If index is negative the space is added at the end.
		The box layout has default margin and spacing
		This function adds additional space.
		"""
		res = super(QBoxLayout,self).insertSpacing(index,size)
		return res
	#----------------------------------------------------------------------
	def insertStretch(self,index,stretch=None):
		"""
		insertStretch(index,stretch=None)
			index=QtCore.int
			stretch=QtCore.int

		Inserts a stretchable space (a PySide.QtGui.QSpacerItem ) at position index , with zero minimum size and stretch factor stretch
		If index is negative the space is added at the end.
		"""
		res = super(QBoxLayout,self).insertStretch(index,stretch)
		return res
	#----------------------------------------------------------------------
	def insertWidget(self,index,widget,stretch=None,alignment=None):
		"""
		insertWidget(index,widget,stretch=None,alignment=None)
			index=QtCore.int
			widget=QtGui.QWidget
			stretch=QtCore.int
			alignment=QtCore.Qt.Alignment


		"""
		res = super(QBoxLayout,self).insertWidget(index,widget,stretch,alignment)
		return res
	#----------------------------------------------------------------------
	def setDirection(self,arg__1):
		"""
		setDirection(arg__1)
			arg__1=QtGui.QBoxLayout.Direction

		Sets the direction of this layout to direction .
		"""
		res = super(QBoxLayout,self).setDirection(arg__1)
		return res
	#----------------------------------------------------------------------
	def setStretch(self,index,stretch):
		"""
		setStretch(index,stretch)
			index=QtCore.int
			stretch=QtCore.int

		Sets the stretch factor at position index
		to stretch .
		"""
		res = super(QBoxLayout,self).setStretch(index,stretch)
		return res
	#----------------------------------------------------------------------
	def setStretchFactor(self,*args,**kwargs):
		"""
		setStretchFactor(w,stretch)
			w=QtGui.QWidget
			stretch=QtCore.int

		setStretchFactor(l,stretch)
			l=QtGui.QLayout
			stretch=QtCore.int

		Sets the stretch factor for widget to stretch and returns true if widget is found in this layout (not including child layouts); otherwise returns false.
		"""
		res = super(QBoxLayout,self).setStretchFactor(*args,**kwargs)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def stretch(self,index):
		"""
		stretch(index)
			index=QtCore.int

		Returns the stretch factor at position index .
		"""
		res = super(QBoxLayout,self).stretch(index)
		isinstance(res,int)
		return res

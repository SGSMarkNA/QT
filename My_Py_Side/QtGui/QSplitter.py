from PySide import QtGui, QtCore

class QSplitter(QtGui.QSplitter):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSplitter,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def childrenCollapsible(self):
		"""
		This property holds whether child widgets can be resized down to size 0 by the user.
		By default, children are collapsible
		It is possible to enable and disable the collapsing of individual children using PySide.QtGui.QSplitter.setCollapsible() .
		"""
		res = super(QSplitter,self).childrenCollapsible()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def count(self):
		"""
		Returns the number of widgets contained in the splitters layout.
		"""
		res = super(QSplitter,self).count()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def createHandle(self):
		"""
		Returns a new splitter handle as a child widget of this splitter
		This function can be reimplemented in subclasses to provide support for custom handles.
		"""
		res = super(QSplitter,self).createHandle()
		isinstance(res,QtGui.QSplitterHandle)
		return res
	#----------------------------------------------------------------------
	def handleWidth(self):
		"""
		This property holds the width of the splitter handles.
		By default, this property contains a value that depends on the users platform and style preferences.
		If you set PySide.QtGui.QSplitter.handleWidth() to 1, the actual grab area will grow to overlap a few pixels of its respective widgets.
		"""
		res = super(QSplitter,self).handleWidth()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def opaqueResize(self):
		"""
		This property holds whether resizing is opaque.
		Opaque resizing is on by default.
		"""
		res = super(QSplitter,self).opaqueResize()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def orientation(self):
		"""
		This property holds the orientation of the splitter.
		By default the orientation is horizontal (i.e., the widgets are laid out side by side)
		The possible orientations are Qt.Horizontal and Qt.Vertical .
		"""
		res = super(QSplitter,self).orientation()
		isinstance(res,QtCore.Qt.Orientation)
		return res
	#----------------------------------------------------------------------
	def refresh(self):
		"""
		Updates the splitters state
		You should not need to call this function.
		"""
		res = super(QSplitter,self).refresh()
		return res
	#----------------------------------------------------------------------
	def saveState(self):
		"""
		Saves the state of the splitters layout.
		Typically this is used in conjunction with PySide.QtCore.QSettings to remember the size for a future session
		A version number is stored as part of the data
		Here is an example:
		"""
		res = super(QSplitter,self).saveState()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def sizes(self):
		"""
		Returns a list of the size parameters of all the widgets in this splitter.
		If the splitters orientation is horizontal, the list contains the widgets width in pixels, from left to right; if the orientation is vertical, the list contains the widgets height in pixels, from top to bottom.
		Giving the values to another splitters PySide.QtGui.QSplitter.setSizes() function will produce a splitter with the same layout as this one.
		Note that invisible widgets have a size of 0.
		"""
		res = super(QSplitter,self).sizes()
		return res
	#----------------------------------------------------------------------
	def addWidget(self,widget):
		"""
		addWidget(widget)
			widget=QtGui.QWidget

		Adds the given widget to the splitters layout after all the other items.
		If widget is already in the splitter, it will be moved to the new position.
		"""
		res = super(QSplitter,self).addWidget(widget)
		return res
	#----------------------------------------------------------------------
	def closestLegalPosition(self,arg__1,arg__2):
		"""
		closestLegalPosition(arg__1,arg__2)
			arg__1=QtCore.int
			arg__2=QtCore.int

		Returns the closest legal position to pos of the widget with index index .
		For right-to-left languages such as Arabic and Hebrew, the layout of horizontal splitters is reversed
		Positions are then measured from the right edge of the widget.
		"""
		res = super(QSplitter,self).closestLegalPosition(arg__1,arg__2)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def getRange(self,index):
		"""
		getRange(index)
			index=QtCore.int

		Returns the valid range of the splitter with index index in *``min`` and *``max`` if min and max are not 0.
		"""
		res = super(QSplitter,self).getRange(index)
		return res
	#----------------------------------------------------------------------
	def handle(self,index):
		"""
		handle(index)
			index=QtCore.int

		Returns the handle to the left (or above) for the item in the splitters layout at the given index
		The handle at index 0 is always hidden.
		For right-to-left languages such as Arabic and Hebrew, the layout of horizontal splitters is reversed
		The handle will be to the right of the widget at index .
		"""
		res = super(QSplitter,self).handle(index)
		isinstance(res,QtGui.QSplitterHandle)
		return res
	#----------------------------------------------------------------------
	def indexOf(self,w):
		"""
		indexOf(w)
			w=QtGui.QWidget

		Returns the index in the splitters layout of the specified widget
		This also works for handles.
		Handles are numbered from 0
		There are as many handles as there are child widgets, but the handle at position 0 is always hidden.
		"""
		res = super(QSplitter,self).indexOf(w)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def insertWidget(self,index,widget):
		"""
		insertWidget(index,widget)
			index=QtCore.int
			widget=QtGui.QWidget

		Inserts the widget specified into the splitters layout at the given index .
		If widget is already in the splitter, it will be moved to the new position.
		if index is an invalid index, then the widget will be inserted at the end.
		"""
		res = super(QSplitter,self).insertWidget(index,widget)
		return res
	#----------------------------------------------------------------------
	def isCollapsible(self,index):
		"""
		isCollapsible(index)
			index=QtCore.int

		Returns true if the widget at index is collapsible, otherwise returns false
		"""
		res = super(QSplitter,self).isCollapsible(index)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def moveSplitter(self,pos,index):
		"""
		moveSplitter(pos,index)
			pos=QtCore.int
			index=QtCore.int

		Moves the left or top edge of the splitter handle at index as close as possible to position pos , which is the distance from the left or top edge of the widget.
		For right-to-left languages such as Arabic and Hebrew, the layout of horizontal splitters is reversed
		pos is then the distance from the right edge of the widget.
		"""
		res = super(QSplitter,self).moveSplitter(pos,index)
		return res
	#----------------------------------------------------------------------
	def restoreState(self,state):
		"""
		restoreState(state)
			state=QtCore.QByteArray

		Restores the splitters layout to the state specified
		Returns true if the state is restored; otherwise returns false.
		Typically this is used in conjunction with PySide.QtCore.QSettings to restore the size from a past session
		Here is an example:
		Restore the splitterss state:
		A failure to restore the splitters layout may result from either invalid or out-of-date data in the supplied byte array.
		"""
		res = super(QSplitter,self).restoreState(state)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setChildrenCollapsible(self,arg__1):
		"""
		setChildrenCollapsible(arg__1)
			arg__1=QtCore.bool

		This property holds whether child widgets can be resized down to size 0 by the user.
		By default, children are collapsible
		It is possible to enable and disable the collapsing of individual children using PySide.QtGui.QSplitter.setCollapsible() .
		"""
		res = super(QSplitter,self).setChildrenCollapsible(arg__1)
		return res
	#----------------------------------------------------------------------
	def setCollapsible(self,index,arg__2):
		"""
		setCollapsible(index,arg__2)
			index=QtCore.int
			arg__2=QtCore.bool

		Sets whether the child widget at index index is collapsible to collapse .
		By default, children are collapsible, meaning that the user can resize them down to size 0, even if they have a non-zero PySide.QtGui.QWidget.minimumSize() or PySide.QtGui.QSplitter.minimumSizeHint()
		This behavior can be changed on a per-widget basis by calling this function, or globally for all the widgets in the splitter by setting the PySide.QtGui.QSplitter.childrenCollapsible() property.
		"""
		res = super(QSplitter,self).setCollapsible(index,arg__2)
		return res
	#----------------------------------------------------------------------
	def setHandleWidth(self,arg__1):
		"""
		setHandleWidth(arg__1)
			arg__1=QtCore.int

		This property holds the width of the splitter handles.
		By default, this property contains a value that depends on the users platform and style preferences.
		If you set PySide.QtGui.QSplitter.handleWidth() to 1, the actual grab area will grow to overlap a few pixels of its respective widgets.
		"""
		res = super(QSplitter,self).setHandleWidth(arg__1)
		return res
	#----------------------------------------------------------------------
	def setOpaqueResize(self,opaque=None):
		"""
		setOpaqueResize(opaque=None)
			opaque=QtCore.bool

		This property holds whether resizing is opaque.
		Opaque resizing is on by default.
		"""
		res = super(QSplitter,self).setOpaqueResize(opaque)
		return res
	#----------------------------------------------------------------------
	def setOrientation(self,arg__1):
		"""
		setOrientation(arg__1)
			arg__1=QtCore.Qt.Orientation

		This property holds the orientation of the splitter.
		By default the orientation is horizontal (i.e., the widgets are laid out side by side)
		The possible orientations are Qt.Horizontal and Qt.Vertical .
		"""
		res = super(QSplitter,self).setOrientation(arg__1)
		return res
	#----------------------------------------------------------------------
	def setRubberBand(self,position):
		"""
		setRubberBand(position)
			position=QtCore.int

		Displays a rubber band at position pos
		If pos is negative, the rubber band is removed.
		"""
		res = super(QSplitter,self).setRubberBand(position)
		return res
	#----------------------------------------------------------------------
	def setSizes(self,list):
		"""
		setSizes(list)
			list=unKnown


		"""
		res = super(QSplitter,self).setSizes(list)
		return res
	#----------------------------------------------------------------------
	def setStretchFactor(self,index,stretch):
		"""
		setStretchFactor(index,stretch)
			index=QtCore.int
			stretch=QtCore.int

		Updates the size policy of the widget at position index to have a stretch factor of stretch .
		stretch is not the effective stretch factor; the effective stretch factor is calculated by taking the initial size of the widget and multiplying it with stretch .
		This function is provided for convenience
		It is equivalent to
		"""
		res = super(QSplitter,self).setStretchFactor(index,stretch)
		return res
	#----------------------------------------------------------------------
	def widget(self,index):
		"""
		widget(index)
			index=QtCore.int

		Returns the widget at the given index in the splitters layout.
		"""
		res = super(QSplitter,self).widget(index)
		isinstance(res,QtGui.QWidget)
		return res

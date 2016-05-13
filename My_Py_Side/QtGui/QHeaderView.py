from PySide import QtGui, QtCore

class QHeaderView(QtGui.QHeaderView):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QHeaderView,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def cascadingSectionResizes(self):
		"""
		This property holds whether interactive resizing will be cascaded to the following sections once the section being resized by the user has reached its minimum size.
		This property only affects sections that have Interactive as their resize mode.
		The default value is false.
		"""
		res = super(QHeaderView,self).cascadingSectionResizes()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def count(self):
		"""
		Returns the number of sections in the header.
		"""
		res = super(QHeaderView,self).count()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def defaultAlignment(self):
		"""
		This property holds the default alignment of the text in each header section.
		"""
		res = super(QHeaderView,self).defaultAlignment()
		isinstance(res,QtCore.Qt.Alignment)
		return res
	#----------------------------------------------------------------------
	def defaultSectionSize(self):
		"""
		This property holds the default size of the header sections before resizing..
		This property only affects sections that have Interactive or Fixed as their resize mode.
		"""
		res = super(QHeaderView,self).defaultSectionSize()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def geometriesChanged(self):
		"""

		"""
		res = super(QHeaderView,self).geometriesChanged()
		return res
	#----------------------------------------------------------------------
	def hiddenSectionCount(self):
		"""
		Returns the number of sections in the header that has been hidden.
		"""
		res = super(QHeaderView,self).hiddenSectionCount()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def highlightSections(self):
		"""
		This property holds whether the sections containing selected items are highlighted.
		By default, this property is false.
		"""
		res = super(QHeaderView,self).highlightSections()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def initialize(self):
		"""

		"""
		res = super(QHeaderView,self).initialize()
		return res
	#----------------------------------------------------------------------
	def initializeSections(self):
		"""

		"""
		res = super(QHeaderView,self).initializeSections()
		return res
	#----------------------------------------------------------------------
	def isClickable(self):
		"""
		Returns true if the header is clickable; otherwise returns false
		A clickable header could be set up to allow the user to change the representation of the data in the view related to the header.
		"""
		res = super(QHeaderView,self).isClickable()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isMovable(self):
		"""
		Returns true if the header can be moved by the user; otherwise returns false.
		"""
		res = super(QHeaderView,self).isMovable()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isSortIndicatorShown(self):
		"""
		This property holds whether the sort indicator is shown.
		By default, this property is false.
		"""
		res = super(QHeaderView,self).isSortIndicatorShown()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def length(self):
		"""
		Returns the length along the orientation of the header.
		"""
		res = super(QHeaderView,self).length()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def minimumSectionSize(self):
		"""
		This property holds the minimum size of the header sections..
		The minimum section size is the smallest section size allowed
		If the minimum section size is set to -1, PySide.QtGui.QHeaderView will use the maximum of the global strut or the font metrics size.
		This property is honored by all resize modes .
		"""
		res = super(QHeaderView,self).minimumSectionSize()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def offset(self):
		"""
		Returns the offset of the header: this is the headers left-most (or top-most for vertical headers) visible pixel.
		"""
		res = super(QHeaderView,self).offset()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def orientation(self):
		"""
		Returns the orientation of the header.
		"""
		res = super(QHeaderView,self).orientation()
		isinstance(res,QtCore.Qt.Orientation)
		return res
	#----------------------------------------------------------------------
	def saveState(self):
		"""
		Saves the current state of this header view.
		To restore the saved state, pass the return value to PySide.QtGui.QHeaderView.restoreState() .
		"""
		res = super(QHeaderView,self).saveState()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def sectionsHidden(self):
		"""
		Returns true if sections in the header has been hidden; otherwise returns false;
		"""
		res = super(QHeaderView,self).sectionsHidden()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def sectionsMoved(self):
		"""
		Returns true if sections in the header has been moved; otherwise returns false;
		"""
		res = super(QHeaderView,self).sectionsMoved()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def sortIndicatorOrder(self):
		"""
		Returns the order for the sort indicator
		If no section has a sort indicator the return value of this function is undefined.
		"""
		res = super(QHeaderView,self).sortIndicatorOrder()
		isinstance(res,QtCore.Qt.SortOrder)
		return res
	#----------------------------------------------------------------------
	def sortIndicatorSection(self):
		"""
		Returns the logical index of the section that has a sort indicator
		By default this is section 0.
		"""
		res = super(QHeaderView,self).sortIndicatorSection()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def stretchLastSection(self):
		"""
		This property holds whether the last visible section in the header takes up all the available space.
		The default value is false.
		"""
		res = super(QHeaderView,self).stretchLastSection()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def stretchSectionCount(self):
		"""
		Returns the number of sections that are set to resize mode stretch
		In views, this can be used to see if the headerview needs to resize the sections when the views geometry changes.
		"""
		res = super(QHeaderView,self).stretchSectionCount()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def hideSection(self,logicalIndex):
		"""
		hideSection(logicalIndex)
			logicalIndex=QtCore.int

		Hides the section specified by logicalIndex .
		"""
		res = super(QHeaderView,self).hideSection(logicalIndex)
		return res
	#----------------------------------------------------------------------
	def initStyleOption(self,option):
		"""
		initStyleOption(option)
			option=QtGui.QStyleOptionHeader

		Initialize option with the values from this PySide.QtGui.QHeaderView
		This method is useful for subclasses when they need a PySide.QtGui.QStyleOptionHeader , but do not want to fill in all the information themselves.
		"""
		res = super(QHeaderView,self).initStyleOption(option)
		return res
	#----------------------------------------------------------------------
	def initializeSections(self,start,end):
		"""
		initializeSections(start,end)
			start=QtCore.int
			end=QtCore.int


		"""
		res = super(QHeaderView,self).initializeSections(start,end)
		return res
	#----------------------------------------------------------------------
	def isSectionHidden(self,logicalIndex):
		"""
		isSectionHidden(logicalIndex)
			logicalIndex=QtCore.int

		Returns true if the section specified by logicalIndex is explicitly hidden from the user; otherwise returns false.
		"""
		res = super(QHeaderView,self).isSectionHidden(logicalIndex)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def logicalIndex(self,visualIndex):
		"""
		logicalIndex(visualIndex)
			visualIndex=QtCore.int

		Returns the logicalIndex for the section at the given visualIndex position, or -1 if visualIndex < 0 or visualIndex >= QHeaderView.count() .
		Note that the visualIndex is not affected by hidden sections.
		"""
		res = super(QHeaderView,self).logicalIndex(visualIndex)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def logicalIndexAt(self,*args,**kwargs):
		"""
		logicalIndexAt(x,y)
			x=QtCore.int
			y=QtCore.int

		logicalIndexAt(position)
			position=QtCore.int

		logicalIndexAt(pos)
			pos=QtCore.QPoint

		Returns the logical index of the section at the given coordinate
		If the header is horizontal x will be used, otherwise y will be used to find the logical index.
		"""
		res = super(QHeaderView,self).logicalIndexAt(*args,**kwargs)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def moveSection(self,from,to):
		"""
		moveSection(from,to)
			from=QtCore.int
			to=QtCore.int

		Moves the section at visual index from to occupy visual index to .
		"""
		res = super(QHeaderView,self).moveSection(from,to)
		return res
	#----------------------------------------------------------------------
	def paintSection(self,painter,rect,logicalIndex):
		"""
		paintSection(painter,rect,logicalIndex)
			painter=QtGui.QPainter
			rect=QtCore.QRect
			logicalIndex=QtCore.int

		Paints the section specified by the given logicalIndex , using the given painter and rect .
		Normally, you do not have to call this function.
		"""
		res = super(QHeaderView,self).paintSection(painter,rect,logicalIndex)
		return res
	#----------------------------------------------------------------------
	def resizeMode(self,logicalIndex):
		"""
		resizeMode(logicalIndex)
			logicalIndex=QtCore.int

		Returns the resize mode that applies to the section specified by the given logicalIndex .
		"""
		res = super(QHeaderView,self).resizeMode(logicalIndex)
		isinstance(res,QtGui.QHeaderView.ResizeMode)
		return res
	#----------------------------------------------------------------------
	def resizeSection(self,logicalIndex,size):
		"""
		resizeSection(logicalIndex,size)
			logicalIndex=QtCore.int
			size=QtCore.int

		Resizes the section specified by logicalIndex to size measured in pixels.
		"""
		res = super(QHeaderView,self).resizeSection(logicalIndex,size)
		return res
	#----------------------------------------------------------------------
	def resizeSections(self,mode):
		"""
		resizeSections(mode)
			mode=QtGui.QHeaderView.ResizeMode


		"""
		res = super(QHeaderView,self).resizeSections(mode)
		return res
	#----------------------------------------------------------------------
	def restoreState(self,state):
		"""
		restoreState(state)
			state=QtCore.QByteArray

		Restores the state of this header view
		This function returns true if the state was restored; otherwise returns false.
		"""
		res = super(QHeaderView,self).restoreState(state)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def sectionPosition(self,logicalIndex):
		"""
		sectionPosition(logicalIndex)
			logicalIndex=QtCore.int

		Returns the section position of the given logicalIndex , or -1 if the section is hidden.
		"""
		res = super(QHeaderView,self).sectionPosition(logicalIndex)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def sectionSize(self,logicalIndex):
		"""
		sectionSize(logicalIndex)
			logicalIndex=QtCore.int

		Returns the width (or height for vertical headers) of the given logicalIndex .
		"""
		res = super(QHeaderView,self).sectionSize(logicalIndex)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def sectionSizeFromContents(self,logicalIndex):
		"""
		sectionSizeFromContents(logicalIndex)
			logicalIndex=QtCore.int

		Returns the size of the contents of the section specified by the given logicalIndex .
		"""
		res = super(QHeaderView,self).sectionSizeFromContents(logicalIndex)
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def sectionSizeHint(self,logicalIndex):
		"""
		sectionSizeHint(logicalIndex)
			logicalIndex=QtCore.int

		Returns a suitable size hint for the section specified by logicalIndex .
		"""
		res = super(QHeaderView,self).sectionSizeHint(logicalIndex)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def sectionViewportPosition(self,logicalIndex):
		"""
		sectionViewportPosition(logicalIndex)
			logicalIndex=QtCore.int

		Returns the section viewport position of the given logicalIndex .
		If the section is hidden, the return value is undefined.
		"""
		res = super(QHeaderView,self).sectionViewportPosition(logicalIndex)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def setCascadingSectionResizes(self,enable):
		"""
		setCascadingSectionResizes(enable)
			enable=QtCore.bool

		This property holds whether interactive resizing will be cascaded to the following sections once the section being resized by the user has reached its minimum size.
		This property only affects sections that have Interactive as their resize mode.
		The default value is false.
		"""
		res = super(QHeaderView,self).setCascadingSectionResizes(enable)
		return res
	#----------------------------------------------------------------------
	def setClickable(self,clickable):
		"""
		setClickable(clickable)
			clickable=QtCore.bool

		If clickable is true, the header will respond to single clicks.
		"""
		res = super(QHeaderView,self).setClickable(clickable)
		return res
	#----------------------------------------------------------------------
	def setDefaultAlignment(self,alignment):
		"""
		setDefaultAlignment(alignment)
			alignment=QtCore.Qt.Alignment

		This property holds the default alignment of the text in each header section.
		"""
		res = super(QHeaderView,self).setDefaultAlignment(alignment)
		return res
	#----------------------------------------------------------------------
	def setDefaultSectionSize(self,size):
		"""
		setDefaultSectionSize(size)
			size=QtCore.int

		This property holds the default size of the header sections before resizing..
		This property only affects sections that have Interactive or Fixed as their resize mode.
		"""
		res = super(QHeaderView,self).setDefaultSectionSize(size)
		return res
	#----------------------------------------------------------------------
	def setHighlightSections(self,highlight):
		"""
		setHighlightSections(highlight)
			highlight=QtCore.bool

		This property holds whether the sections containing selected items are highlighted.
		By default, this property is false.
		"""
		res = super(QHeaderView,self).setHighlightSections(highlight)
		return res
	#----------------------------------------------------------------------
	def setMinimumSectionSize(self,size):
		"""
		setMinimumSectionSize(size)
			size=QtCore.int

		This property holds the minimum size of the header sections..
		The minimum section size is the smallest section size allowed
		If the minimum section size is set to -1, PySide.QtGui.QHeaderView will use the maximum of the global strut or the font metrics size.
		This property is honored by all resize modes .
		"""
		res = super(QHeaderView,self).setMinimumSectionSize(size)
		return res
	#----------------------------------------------------------------------
	def setMovable(self,movable):
		"""
		setMovable(movable)
			movable=QtCore.bool

		If movable is true, the header may be moved by the user; otherwise it is fixed in place.
		"""
		res = super(QHeaderView,self).setMovable(movable)
		return res
	#----------------------------------------------------------------------
	def setResizeMode(self,*args,**kwargs):
		"""
		setResizeMode(logicalIndex,mode)
			logicalIndex=QtCore.int
			mode=QtGui.QHeaderView.ResizeMode

		setResizeMode(mode)
			mode=QtGui.QHeaderView.ResizeMode

		This is an overloaded function.
		Sets the constraints on how the section specified by logicalIndex in the header can be resized to those described by the given mode
		The logical index should exist at the time this function is called.
		"""
		res = super(QHeaderView,self).setResizeMode(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setSectionHidden(self,logicalIndex,hide):
		"""
		setSectionHidden(logicalIndex,hide)
			logicalIndex=QtCore.int
			hide=QtCore.bool

		If hide is true the section specified by logicalIndex is hidden; otherwise the section is shown.
		"""
		res = super(QHeaderView,self).setSectionHidden(logicalIndex,hide)
		return res
	#----------------------------------------------------------------------
	def setSortIndicator(self,logicalIndex,order):
		"""
		setSortIndicator(logicalIndex,order)
			logicalIndex=QtCore.int
			order=QtCore.Qt.SortOrder


		"""
		res = super(QHeaderView,self).setSortIndicator(logicalIndex,order)
		return res
	#----------------------------------------------------------------------
	def setSortIndicatorShown(self,show):
		"""
		setSortIndicatorShown(show)
			show=QtCore.bool

		This property holds whether the sort indicator is shown.
		By default, this property is false.
		"""
		res = super(QHeaderView,self).setSortIndicatorShown(show)
		return res
	#----------------------------------------------------------------------
	def setStretchLastSection(self,stretch):
		"""
		setStretchLastSection(stretch)
			stretch=QtCore.bool

		This property holds whether the last visible section in the header takes up all the available space.
		The default value is false.
		"""
		res = super(QHeaderView,self).setStretchLastSection(stretch)
		return res
	#----------------------------------------------------------------------
	def showSection(self,logicalIndex):
		"""
		showSection(logicalIndex)
			logicalIndex=QtCore.int

		Shows the section specified by logicalIndex .
		"""
		res = super(QHeaderView,self).showSection(logicalIndex)
		return res
	#----------------------------------------------------------------------
	def swapSections(self,first,second):
		"""
		swapSections(first,second)
			first=QtCore.int
			second=QtCore.int

		Swaps the section at visual index first with the section at visual index second .
		"""
		res = super(QHeaderView,self).swapSections(first,second)
		return res
	#----------------------------------------------------------------------
	def visualIndex(self,logicalIndex):
		"""
		visualIndex(logicalIndex)
			logicalIndex=QtCore.int

		Returns the visual index position of the section specified by the given logicalIndex , or -1 otherwise.
		Hidden sections still have valid visual indexes.
		"""
		res = super(QHeaderView,self).visualIndex(logicalIndex)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def visualIndexAt(self,position):
		"""
		visualIndexAt(position)
			position=QtCore.int

		Returns the visual index of the section that covers the given position in the viewport.
		"""
		res = super(QHeaderView,self).visualIndexAt(position)
		isinstance(res,QtCore.int)
		return res

from PySide import QtGui, QtCore

class QStatusBar(QtGui.QStatusBar):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QStatusBar,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def currentMessage(self):
		"""
		Returns the temporary message currently shown, or an empty string if there is no such message.
		"""
		res = super(QStatusBar,self).currentMessage()
		return res
	#----------------------------------------------------------------------
	def hideOrShow(self):
		"""
		Ensures that the right widgets are visible.
		Used by the PySide.QtGui.QStatusBar.showMessage() and PySide.QtGui.QStatusBar.clearMessage() functions.
		"""
		res = super(QStatusBar,self).hideOrShow()
		return res
	#----------------------------------------------------------------------
	def isSizeGripEnabled(self):
		"""
		This property holds whether the PySide.QtGui.QSizeGrip in the bottom-right corner of the status bar is enabled.
		The size grip is enabled by default.
		"""
		res = super(QStatusBar,self).isSizeGripEnabled()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def reformat(self):
		"""
		Changes the status bars appearance to account for item changes.
		Special subclasses may need this function, but geometry management will usually take care of any necessary rearrangements.
		"""
		res = super(QStatusBar,self).reformat()
		return res
	#----------------------------------------------------------------------
	def addPermanentWidget(self,widget,stretch=None):
		"""
		addPermanentWidget(widget,stretch=None)
			widget=QtGui.QWidget
			stretch=QtCore.int

		Adds the given widget permanently to this status bar, reparenting the widget if it isnt already a child of this PySide.QtGui.QStatusBar object
		The stretch parameter is used to compute a suitable size for the given widget as the status bar grows and shrinks
		The default stretch factor is 0, i.e giving the widget a minimum of space.
		Permanently means that the widget may not be obscured by temporary messages
		It is is located at the far right of the status bar.
		"""
		res = super(QStatusBar,self).addPermanentWidget(widget,stretch)
		return res
	#----------------------------------------------------------------------
	def addWidget(self,widget,stretch=None):
		"""
		addWidget(widget,stretch=None)
			widget=QtGui.QWidget
			stretch=QtCore.int

		Adds the given widget to this status bar, reparenting the widget if it isnt already a child of this PySide.QtGui.QStatusBar object
		The stretch parameter is used to compute a suitable size for the given widget as the status bar grows and shrinks
		The default stretch factor is 0, i.e giving the widget a minimum of space.
		The widget is located to the far left of the first permanent widget (see PySide.QtGui.QStatusBar.addPermanentWidget() ) and may be obscured by temporary messages.
		"""
		res = super(QStatusBar,self).addWidget(widget,stretch)
		return res
	#----------------------------------------------------------------------
	def insertPermanentWidget(self,index,widget,stretch=None):
		"""
		insertPermanentWidget(index,widget,stretch=None)
			index=QtCore.int
			widget=QtGui.QWidget
			stretch=QtCore.int

		Inserts the given widget at the given index permanently to this status bar, reparenting the widget if it isnt already a child of this PySide.QtGui.QStatusBar object
		If index is out of range, the widget is appended (in which case it is the actual index of the widget that is returned).
		The stretch parameter is used to compute a suitable size for the given widget as the status bar grows and shrinks
		The default stretch factor is 0, i.e giving the widget a minimum of space.
		Permanently means that the widget may not be obscured by temporary messages
		It is is located at the far right of the status bar.
		"""
		res = super(QStatusBar,self).insertPermanentWidget(index,widget,stretch)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def insertWidget(self,index,widget,stretch=None):
		"""
		insertWidget(index,widget,stretch=None)
			index=QtCore.int
			widget=QtGui.QWidget
			stretch=QtCore.int

		Inserts the given widget at the given index to this status bar, reparenting the widget if it isnt already a child of this PySide.QtGui.QStatusBar object
		If index is out of range, the widget is appended (in which case it is the actual index of the widget that is returned).
		The stretch parameter is used to compute a suitable size for the given widget as the status bar grows and shrinks
		The default stretch factor is 0, i.e giving the widget a minimum of space.
		The widget is located to the far left of the first permanent widget (see PySide.QtGui.QStatusBar.addPermanentWidget() ) and may be obscured by temporary messages.
		"""
		res = super(QStatusBar,self).insertWidget(index,widget,stretch)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def removeWidget(self,widget):
		"""
		removeWidget(widget)
			widget=QtGui.QWidget

		Removes the specified widget from the status bar.
		"""
		res = super(QStatusBar,self).removeWidget(widget)
		return res
	#----------------------------------------------------------------------
	def setSizeGripEnabled(self,arg__1):
		"""
		setSizeGripEnabled(arg__1)
			arg__1=QtCore.bool

		This property holds whether the PySide.QtGui.QSizeGrip in the bottom-right corner of the status bar is enabled.
		The size grip is enabled by default.
		"""
		res = super(QStatusBar,self).setSizeGripEnabled(arg__1)
		return res

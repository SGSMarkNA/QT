from PySide import QtGui, QtCore

class QWorkspace(QtGui.QWorkspace):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QWorkspace,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def activeWindow(self):
		"""
		Returns a pointer to the widget corresponding to the active child window, or 0 if no window is active.
		"""
		res = super(QWorkspace,self).activeWindow()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def background(self):
		"""
		This property holds the workspaces background.
		"""
		res = super(QWorkspace,self).background()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def scrollBarsEnabled(self):
		"""
		This property holds whether the workspace provides scroll bars.
		If this property is true, the workspace will provide scroll bars if any of the child windows extend beyond the edges of the visible workspace
		The workspace area will automatically increase to contain child windows if they are resized beyond the right or bottom edges of the visible area.
		If this property is false (the default), resizing child windows out of the visible area of the workspace is not permitted, although it is still possible to position them partially outside the visible area.
		"""
		res = super(QWorkspace,self).scrollBarsEnabled()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def addWindow(self,w,flags=None):
		"""
		addWindow(w,flags=None)
			w=QtGui.QWidget
			flags=QtCore.Qt.WindowFlags


		"""
		res = super(QWorkspace,self).addWindow(w,flags)
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def setBackground(self,background):
		"""
		setBackground(background)
			background=QtGui.QBrush

		This property holds the workspaces background.
		"""
		res = super(QWorkspace,self).setBackground(background)
		return res
	#----------------------------------------------------------------------
	def setScrollBarsEnabled(self,enable):
		"""
		setScrollBarsEnabled(enable)
			enable=QtCore.bool

		This property holds whether the workspace provides scroll bars.
		If this property is true, the workspace will provide scroll bars if any of the child windows extend beyond the edges of the visible workspace
		The workspace area will automatically increase to contain child windows if they are resized beyond the right or bottom edges of the visible area.
		If this property is false (the default), resizing child windows out of the visible area of the workspace is not permitted, although it is still possible to position them partially outside the visible area.
		"""
		res = super(QWorkspace,self).setScrollBarsEnabled(enable)
		return res
	#----------------------------------------------------------------------
	def windowList(self,order=None):
		"""
		windowList(order=None)
			order=QtGui.QWorkspace.WindowOrder

		Returns a list of all visible or minimized child windows
		If order is CreationOrder (the default), the windows are listed in the order in which they were inserted into the workspace
		If order is StackingOrder , the windows are listed in their stacking order, with the topmost window as the last item in the list.
		"""
		res = super(QWorkspace,self).windowList(order)
		return res

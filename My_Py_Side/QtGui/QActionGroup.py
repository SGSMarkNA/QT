from PySide import QtGui, QtCore

class QActionGroup(QtGui.QActionGroup):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QActionGroup,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def actions(self):
		"""
		Returns the list of this groupss actions
		This may be empty.
		"""
		res = super(QActionGroup,self).actions()
		return res
	#----------------------------------------------------------------------
	def checkedAction(self):
		"""
		Returns the currently checked action in the group, or 0 if none are checked.
		"""
		res = super(QActionGroup,self).checkedAction()
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def isEnabled(self):
		"""
		This property holds whether the action group is enabled.
		Each action in the group will be enabled or disabled unless it has been explicitly disabled.
		"""
		res = super(QActionGroup,self).isEnabled()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isExclusive(self):
		"""
		This property holds whether the action group does exclusive checking.
		If exclusive is true, only one checkable action in the action group can ever be active at any time
		If the user chooses another checkable action in the group, the one they chose becomes active and the one that was active becomes inactive.
		"""
		res = super(QActionGroup,self).isExclusive()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isVisible(self):
		"""
		This property holds whether the action group is visible.
		Each action in the action group will match the visible state of this group unless it has been explicitly hidden.
		"""
		res = super(QActionGroup,self).isVisible()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def addAction(self,*args,**kwargs):
		"""
		addAction(text)
			text=unicode

		addAction(a)
			a=QtGui.QAction

		addAction(icon,text)
			icon=QtGui.QIcon
			text=unicode

		Creates and returns an action with text
		The newly created action is a child of this action group.
		Normally an action is added to a group by creating it with the group as parent, so this function is not usually used.
		"""
		res = super(QActionGroup,self).addAction(*args,**kwargs)
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def removeAction(self,a):
		"""
		removeAction(a)
			a=QtGui.QAction

		Removes the action from this group
		The action will have no parent as a result.
		"""
		res = super(QActionGroup,self).removeAction(a)
		return res

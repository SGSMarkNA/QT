from PySide import QtGui, QtCore

class QButtonGroup(QtGui.QButtonGroup):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QButtonGroup,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def buttons(self):
		"""
		Returns the list of this groupss buttons
		This may be empty.
		"""
		res = super(QButtonGroup,self).buttons()
		return res
	#----------------------------------------------------------------------
	def checkedButton(self):
		"""
		Returns the button groups checked button, or 0 if no buttons are checked.
		"""
		res = super(QButtonGroup,self).checkedButton()
		isinstance(res,QtGui.QAbstractButton)
		return res
	#----------------------------------------------------------------------
	def checkedId(self):
		"""
		Returns the id of the PySide.QtGui.QButtonGroup.checkedButton() , or -1 if no button is checked.
		"""
		res = super(QButtonGroup,self).checkedId()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def exclusive(self):
		"""
		This property holds whether the button group is exclusive.
		If this property is true then only one button in the group can be checked at any given time
		The user can click on any button to check it, and that button will replace the existing one as the checked button in the group.
		In an exclusive group, the user cannot uncheck the currently checked button by clicking on it; instead, another button in the group must be clicked to set the new checked button for that group.
		By default, this property is true.
		"""
		res = super(QButtonGroup,self).exclusive()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def addButton(self,*args,**kwargs):
		"""
		addButton(arg__1,id)
			arg__1=QtGui.QAbstractButton
			id=QtCore.int

		addButton(arg__1)
			arg__1=QtGui.QAbstractButton

		Adds the given button to the button group, with the given id
		It is recommended to assign only positive ids.
		"""
		res = super(QButtonGroup,self).addButton(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def button(self,id):
		"""
		button(id)
			id=QtCore.int

		Returns the button with the specified id , or 0 if no such button exists.
		"""
		res = super(QButtonGroup,self).button(id)
		isinstance(res,QtGui.QAbstractButton)
		return res
	#----------------------------------------------------------------------
	def id(self,button):
		"""
		id(button)
			button=QtGui.QAbstractButton

		Returns the id for the specified button , or -1 if no such button exists.
		"""
		res = super(QButtonGroup,self).id(button)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def removeButton(self,arg__1):
		"""
		removeButton(arg__1)
			arg__1=QtGui.QAbstractButton

		Removes the given button from the button group.
		"""
		res = super(QButtonGroup,self).removeButton(arg__1)
		return res
	#----------------------------------------------------------------------
	def setExclusive(self,arg__1):
		"""
		setExclusive(arg__1)
			arg__1=QtCore.bool

		This property holds whether the button group is exclusive.
		If this property is true then only one button in the group can be checked at any given time
		The user can click on any button to check it, and that button will replace the existing one as the checked button in the group.
		In an exclusive group, the user cannot uncheck the currently checked button by clicking on it; instead, another button in the group must be clicked to set the new checked button for that group.
		By default, this property is true.
		"""
		res = super(QButtonGroup,self).setExclusive(arg__1)
		return res
	#----------------------------------------------------------------------
	def setId(self,button,id):
		"""
		setId(button,id)
			button=QtGui.QAbstractButton
			id=QtCore.int

		Sets the id for the specified button
		Note that id can not be -1.
		"""
		res = super(QButtonGroup,self).setId(button,id)
		return res

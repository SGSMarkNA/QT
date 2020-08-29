from PySide import QtGui, QtCore

class QGroupBox(QtGui.QGroupBox):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGroupBox,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def alignment(self):
		"""
		This property holds the alignment of the group box title..
		Most styles place the title at the top of the frame
		The horizontal alignment of the title can be specified using single values from the following list:
		The default alignment is Qt.AlignLeft .
		"""
		res = super(QGroupBox,self).alignment()
		isinstance(res,QtCore.Qt.Alignment)
		return res
	#----------------------------------------------------------------------
	def isCheckable(self):
		"""
		This property holds whether the group box has a checkbox in its title.
		If this property is true, the group box displays its title using a checkbox in place of an ordinary label
		If the checkbox is checked, the group boxs children are enabled; otherwise they are disabled and inaccessible.
		By default, group boxes are not checkable.
		If this property is enabled for a group box, it will also be initially checked to ensure that its contents are enabled.
		"""
		res = super(QGroupBox,self).isCheckable()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isChecked(self):
		"""
		This property holds whether the group box is checked.
		If the group box is checkable, it is displayed with a check box
		If the check box is checked, the group boxs children are enabled; otherwise the children are disabled and are inaccessible to the user.
		By default, checkable group boxes are also checked.
		"""
		res = super(QGroupBox,self).isChecked()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isFlat(self):
		"""
		This property holds whether the group box is painted flat or has a frame.
		A group box usually consists of a surrounding frame with a title at the top
		If this property is enabled, only the top part of the frame is drawn in most styles; otherwise the whole frame is drawn.
		By default, this property is disabled; i.e
		group boxes are not flat unless explicitly specified.
		"""
		res = super(QGroupBox,self).isFlat()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def title(self):
		"""
		This property holds the group box title text.
		The group box title text will have a keyboard shortcut if the title contains an ampersand (&) followed by a letter.
		In the example above, Alt+U moves the keyboard focus to the group box
		See the QShortcut documentation for details (to display an actual ampersand, use &&).
		There is no default title text.
		"""
		res = super(QGroupBox,self).title()
		return res
	#----------------------------------------------------------------------
	def initStyleOption(self,option):
		"""
		initStyleOption(option)
			option=QtGui.QStyleOptionGroupBox

		Initialize option with the values from this PySide.QtGui.QGroupBox
		This method is useful for subclasses when they need a PySide.QtGui.QStyleOptionGroupBox , but dont want to fill in all the information themselves.
		"""
		res = super(QGroupBox,self).initStyleOption(option)
		return res
	#----------------------------------------------------------------------
	def setAlignment(self,alignment):
		"""
		setAlignment(alignment)
			alignment=QtCore.int


		"""
		res = super(QGroupBox,self).setAlignment(alignment)
		return res
	#----------------------------------------------------------------------
	def setCheckable(self,checkable):
		"""
		setCheckable(checkable)
			checkable=QtCore.bool

		This property holds whether the group box has a checkbox in its title.
		If this property is true, the group box displays its title using a checkbox in place of an ordinary label
		If the checkbox is checked, the group boxs children are enabled; otherwise they are disabled and inaccessible.
		By default, group boxes are not checkable.
		If this property is enabled for a group box, it will also be initially checked to ensure that its contents are enabled.
		"""
		res = super(QGroupBox,self).setCheckable(checkable)
		return res
	#----------------------------------------------------------------------
	def setFlat(self,flat):
		"""
		setFlat(flat)
			flat=QtCore.bool

		This property holds whether the group box is painted flat or has a frame.
		A group box usually consists of a surrounding frame with a title at the top
		If this property is enabled, only the top part of the frame is drawn in most styles; otherwise the whole frame is drawn.
		By default, this property is disabled; i.e
		group boxes are not flat unless explicitly specified.
		"""
		res = super(QGroupBox,self).setFlat(flat)
		return res
	#----------------------------------------------------------------------
	def setTitle(self,title):
		"""
		setTitle(title)
			title=unicode

		This property holds the group box title text.
		The group box title text will have a keyboard shortcut if the title contains an ampersand (&) followed by a letter.
		In the example above, Alt+U moves the keyboard focus to the group box
		See the QShortcut documentation for details (to display an actual ampersand, use &&).
		There is no default title text.
		"""
		res = super(QGroupBox,self).setTitle(title)
		return res

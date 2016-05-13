from PySide import QtGui, QtCore

class QToolBox(QtGui.QToolBox):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QToolBox,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def count(self):
		"""
		This property holds The number of items contained in the toolbox..
		By default, this property has a value of 0.
		"""
		res = super(QToolBox,self).count()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def currentIndex(self):
		"""
		This property holds the index of the current item.
		By default, for an empty toolbox, this property has a value of -1.
		"""
		res = super(QToolBox,self).currentIndex()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def currentWidget(self):
		"""
		Returns a pointer to the current widget, or 0 if there is no such item.
		"""
		res = super(QToolBox,self).currentWidget()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def addItem(self,*args,**kwargs):
		"""
		addItem(widget,text)
			widget=QtGui.QWidget
			text=unicode

		addItem(widget,icon,text)
			widget=QtGui.QWidget
			icon=QtGui.QIcon
			text=unicode

		This is an overloaded function.
		Adds the widget w in a new tab at bottom of the toolbox
		The new tabs text is set to text
		Returns the new tabs index.
		"""
		res = super(QToolBox,self).addItem(*args,**kwargs)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def indexOf(self,widget):
		"""
		indexOf(widget)
			widget=QtGui.QWidget

		Returns the index of widget , or -1 if the item does not exist.
		"""
		res = super(QToolBox,self).indexOf(widget)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def insertItem(self,*args,**kwargs):
		"""
		insertItem(index,widget,icon,text)
			index=QtCore.int
			widget=QtGui.QWidget
			icon=QtGui.QIcon
			text=unicode

		insertItem(index,widget,text)
			index=QtCore.int
			widget=QtGui.QWidget
			text=unicode

		Inserts the widget at position index , or at the bottom of the toolbox if index is out of range
		The new items text is set to text , and the icon is displayed to the left of the text
		Returns the new items index.
		"""
		res = super(QToolBox,self).insertItem(*args,**kwargs)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def isItemEnabled(self,index):
		"""
		isItemEnabled(index)
			index=QtCore.int

		Returns true if the item at position index is enabled; otherwise returns false.
		"""
		res = super(QToolBox,self).isItemEnabled(index)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def itemIcon(self,index):
		"""
		itemIcon(index)
			index=QtCore.int

		Returns the icon of the item at position index , or a null icon if index is out of range.
		"""
		res = super(QToolBox,self).itemIcon(index)
		isinstance(res,QtGui.QIcon)
		return res
	#----------------------------------------------------------------------
	def itemInserted(self,index):
		"""
		itemInserted(index)
			index=QtCore.int

		This virtual handler is called after a new item was added or inserted at position index .
		"""
		res = super(QToolBox,self).itemInserted(index)
		return res
	#----------------------------------------------------------------------
	def itemRemoved(self,index):
		"""
		itemRemoved(index)
			index=QtCore.int

		This virtual handler is called after an item was removed from position index .
		"""
		res = super(QToolBox,self).itemRemoved(index)
		return res
	#----------------------------------------------------------------------
	def itemText(self,index):
		"""
		itemText(index)
			index=QtCore.int

		Returns the text of the item at position index , or an empty string if index is out of range.
		"""
		res = super(QToolBox,self).itemText(index)
		return res
	#----------------------------------------------------------------------
	def itemToolTip(self,index):
		"""
		itemToolTip(index)
			index=QtCore.int

		Returns the tooltip of the item at position index , or an empty string if index is out of range.
		"""
		res = super(QToolBox,self).itemToolTip(index)
		return res
	#----------------------------------------------------------------------
	def removeItem(self,index):
		"""
		removeItem(index)
			index=QtCore.int

		Removes the item at position index from the toolbox
		Note that the widget is not deleted.
		"""
		res = super(QToolBox,self).removeItem(index)
		return res
	#----------------------------------------------------------------------
	def setItemEnabled(self,index,enabled):
		"""
		setItemEnabled(index,enabled)
			index=QtCore.int
			enabled=QtCore.bool

		If enabled is true then the item at position index is enabled; otherwise the item at position index is disabled.
		"""
		res = super(QToolBox,self).setItemEnabled(index,enabled)
		return res
	#----------------------------------------------------------------------
	def setItemIcon(self,index,icon):
		"""
		setItemIcon(index,icon)
			index=QtCore.int
			icon=QtGui.QIcon

		Sets the icon of the item at position index to icon .
		"""
		res = super(QToolBox,self).setItemIcon(index,icon)
		return res
	#----------------------------------------------------------------------
	def setItemText(self,index,text):
		"""
		setItemText(index,text)
			index=QtCore.int
			text=unicode

		Sets the text of the item at position index to text .
		If the provided text contains an ampersand character (&), a mnemonic is automatically created for it
		The character that follows the & will be used as the shortcut key
		Any previous mnemonic will be overwritten, or cleared if no mnemonic is defined by the text
		See the QShortcut documentation for details (to display an actual ampersand, use &&).
		"""
		res = super(QToolBox,self).setItemText(index,text)
		return res
	#----------------------------------------------------------------------
	def setItemToolTip(self,index,toolTip):
		"""
		setItemToolTip(index,toolTip)
			index=QtCore.int
			toolTip=unicode

		Sets the tooltip of the item at position index to toolTip .
		"""
		res = super(QToolBox,self).setItemToolTip(index,toolTip)
		return res
	#----------------------------------------------------------------------
	def widget(self,index):
		"""
		widget(index)
			index=QtCore.int

		Returns the widget at position index , or 0 if there is no such item.
		"""
		res = super(QToolBox,self).widget(index)
		isinstance(res,QtGui.QWidget)
		return res

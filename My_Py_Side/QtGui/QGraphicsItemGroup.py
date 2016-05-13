from PySide import QtGui, QtCore

class QGraphicsItemGroup(QtGui.QGraphicsItemGroup):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsItemGroup,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def addToGroup(self,item):
		"""
		addToGroup(item)
			item=QtGui.QGraphicsItem

		Adds the given item to this item group
		The item will be reparented to this group, but its position and transformation relative to the scene will stay intact.
		"""
		res = super(QGraphicsItemGroup,self).addToGroup(item)
		return res
	#----------------------------------------------------------------------
	def removeFromGroup(self,item):
		"""
		removeFromGroup(item)
			item=QtGui.QGraphicsItem

		Removes the specified item from this group
		The item will be reparented to this groups parent item, or to 0 if this group has no parent
		Its position and transformation relative to the scene will stay intact.
		"""
		res = super(QGraphicsItemGroup,self).removeFromGroup(item)
		return res

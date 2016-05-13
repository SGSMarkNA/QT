from PySide import QtGui, QtCore

class QTextBlockGroup(QtGui.QTextBlockGroup):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextBlockGroup,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def blockList(self):
		"""
		Returns a (possibly empty) list of all the blocks that are part of the block group.
		"""
		res = super(QTextBlockGroup,self).blockList()
		return res
	#----------------------------------------------------------------------
	def blockFormatChanged(self,block):
		"""
		blockFormatChanged(block)
			block=QtGui.QTextBlock

		This function is called whenever the specified block of text is changed
		The text block is a member of this group.
		The base class implementation does nothing.
		"""
		res = super(QTextBlockGroup,self).blockFormatChanged(block)
		return res
	#----------------------------------------------------------------------
	def blockInserted(self,block):
		"""
		blockInserted(block)
			block=QtGui.QTextBlock

		Appends the given block to the end of the group.
		"""
		res = super(QTextBlockGroup,self).blockInserted(block)
		return res
	#----------------------------------------------------------------------
	def blockRemoved(self,block):
		"""
		blockRemoved(block)
			block=QtGui.QTextBlock

		Removes the given block from the group; the block itself is not deleted, it simply isnt a member of this group anymore.
		"""
		res = super(QTextBlockGroup,self).blockRemoved(block)
		return res

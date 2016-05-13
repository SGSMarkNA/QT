from PySide import QtGui, QtCore

class QDomNodeList(QtXml.QDomNodeList):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDomNodeList,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def count(self):
		"""
		This function is provided for Qt API consistency
		It is equivalent to PySide.QtXml.QDomNodeList.length() .
		"""
		res = super(QDomNodeList,self).count()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def isEmpty(self):
		"""
		Returns true if the list contains no items; otherwise returns false
		This function is provided for Qt API consistency.
		"""
		res = super(QDomNodeList,self).isEmpty()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def length(self):
		"""
		Returns the number of nodes in the list.
		"""
		res = super(QDomNodeList,self).length()
		isinstance(res,QtCore.uint)
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""
		This function is provided for Qt API consistency
		It is equivalent to PySide.QtXml.QDomNodeList.length() .
		"""
		res = super(QDomNodeList,self).size()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def at(self,index):
		"""
		at(index)
			index=QtCore.int

		This function is provided for Qt API consistency
		It is equivalent to PySide.QtXml.QDomNodeList.item() .
		If index is negative or if index >= PySide.QtXml.QDomNodeList.length() then a null node is returned (i.e
		a node for which QDomNode.isNull() returns true).
		"""
		res = super(QDomNodeList,self).at(index)
		isinstance(res,QtXml.QDomNode)
		return res
	#----------------------------------------------------------------------
	def item(self,index):
		"""
		item(index)
			index=QtCore.int

		Returns the node at position index .
		If index is negative or if index >= PySide.QtXml.QDomNodeList.length() then a null node is returned (i.e
		a node for which QDomNode.isNull() returns true).
		"""
		res = super(QDomNodeList,self).item(index)
		isinstance(res,QtXml.QDomNode)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,arg__1):
		"""
		__ne__(arg__1)
			arg__1=QtXml.QDomNodeList

		Returns true the node list n and this node list are not equal; otherwise returns false.
		"""
		res = super(QDomNodeList,self).__ne__(arg__1)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,arg__1):
		"""
		__eq__(arg__1)
			arg__1=QtXml.QDomNodeList

		Returns true if the node list n and this node list are equal; otherwise returns false.
		"""
		res = super(QDomNodeList,self).__eq__(arg__1)
		isinstance(res,QtCore.bool)
		return res

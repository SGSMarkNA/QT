from PySide import QtGui, QtCore

class QDomNamedNodeMap(QtXml.QDomNamedNodeMap):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDomNamedNodeMap,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def count(self):
		"""
		This function is provided for Qt API consistency
		It is equivalent to PySide.QtXml.QDomNamedNodeMap.length() .
		"""
		res = super(QDomNamedNodeMap,self).count()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def isEmpty(self):
		"""
		Returns true if the map is empty; otherwise returns false
		This function is provided for Qt API consistency.
		"""
		res = super(QDomNamedNodeMap,self).isEmpty()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def length(self):
		"""
		Returns the number of nodes in the map.
		"""
		res = super(QDomNamedNodeMap,self).length()
		isinstance(res,QtCore.uint)
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""
		This function is provided for Qt API consistency
		It is equivalent to PySide.QtXml.QDomNamedNodeMap.length() .
		"""
		res = super(QDomNamedNodeMap,self).size()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def contains(self,name):
		"""
		contains(name)
			name=unicode

		Returns true if the map contains a node called name ; otherwise returns false.
		"""
		res = super(QDomNamedNodeMap,self).contains(name)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def item(self,index):
		"""
		item(index)
			index=QtCore.int

		Retrieves the node at position index .
		This can be used to iterate over the map
		Note that the nodes in the map are ordered arbitrarily.
		"""
		res = super(QDomNamedNodeMap,self).item(index)
		isinstance(res,QtXml.QDomNode)
		return res
	#----------------------------------------------------------------------
	def namedItem(self,name):
		"""
		namedItem(name)
			name=unicode

		Returns the node called name .
		If the named node map does not contain such a node, a null node is returned
		A nodes name is the name returned by QDomNode.nodeName() .
		"""
		res = super(QDomNamedNodeMap,self).namedItem(name)
		isinstance(res,QtXml.QDomNode)
		return res
	#----------------------------------------------------------------------
	def namedItemNS(self,nsURI,localName):
		"""
		namedItemNS(nsURI,localName)
			nsURI=unicode
			localName=unicode

		Returns the node associated with the local name localName and the namespace URI nsURI .
		If the map does not contain such a node, a null node is returned.
		"""
		res = super(QDomNamedNodeMap,self).namedItemNS(nsURI,localName)
		isinstance(res,QtXml.QDomNode)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,arg__1):
		"""
		__ne__(arg__1)
			arg__1=QtXml.QDomNamedNodeMap

		Returns true if n and this named node map are not equal; otherwise returns false.
		"""
		res = super(QDomNamedNodeMap,self).__ne__(arg__1)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,arg__1):
		"""
		__eq__(arg__1)
			arg__1=QtXml.QDomNamedNodeMap

		Returns true if n and this named node map are equal; otherwise returns false.
		"""
		res = super(QDomNamedNodeMap,self).__eq__(arg__1)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def removeNamedItem(self,name):
		"""
		removeNamedItem(name)
			name=unicode

		Removes the node called name from the map.
		The function returns the removed node or a null node if the map did not contain a node called name .
		"""
		res = super(QDomNamedNodeMap,self).removeNamedItem(name)
		isinstance(res,QtXml.QDomNode)
		return res
	#----------------------------------------------------------------------
	def removeNamedItemNS(self,nsURI,localName):
		"""
		removeNamedItemNS(nsURI,localName)
			nsURI=unicode
			localName=unicode

		Removes the node with the local name localName and the namespace URI nsURI from the map.
		The function returns the removed node or a null node if the map did not contain a node with the local name localName and the namespace URI nsURI .
		"""
		res = super(QDomNamedNodeMap,self).removeNamedItemNS(nsURI,localName)
		isinstance(res,QtXml.QDomNode)
		return res
	#----------------------------------------------------------------------
	def setNamedItem(self,newNode):
		"""
		setNamedItem(newNode)
			newNode=QtXml.QDomNode

		Inserts the node newNode into the named node map
		The name used by the map is the node name of newNode as returned by QDomNode.nodeName() .
		If the new node replaces an existing node, i.e
		the map contains a node with the same name, the replaced node is returned.
		"""
		res = super(QDomNamedNodeMap,self).setNamedItem(newNode)
		isinstance(res,QtXml.QDomNode)
		return res
	#----------------------------------------------------------------------
	def setNamedItemNS(self,newNode):
		"""
		setNamedItemNS(newNode)
			newNode=QtXml.QDomNode

		Inserts the node newNode in the map
		If a node with the same namespace URI and the same local name already exists in the map, it is replaced by newNode
		If the new node replaces an existing node, the replaced node is returned.
		"""
		res = super(QDomNamedNodeMap,self).setNamedItemNS(newNode)
		isinstance(res,QtXml.QDomNode)
		return res

from PySide import QtGui, QtCore

class QXmlNamespaceSupport(QtXml.QXmlNamespaceSupport):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QXmlNamespaceSupport,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def popContext(self):
		"""
		Reverts to the previous namespace context.
		Normally, you should pop the context at the end of each XML element
		After popping the context, all namespace prefix mappings that were previously in force are restored.
		"""
		res = super(QXmlNamespaceSupport,self).popContext()
		return res
	#----------------------------------------------------------------------
	def prefixes(self):
		"""
		Returns a list of all the prefixes currently declared.
		If there is a default prefix, this function does not return it in the list; check for the default prefix using PySide.QtXml.QXmlNamespaceSupport.uri() with an argument of .
		"""
		res = super(QXmlNamespaceSupport,self).prefixes()
		return res
	#----------------------------------------------------------------------
	def pushContext(self):
		"""
		Starts a new namespace context.
		Normally, you should push a new context at the beginning of each XML element: the new context automatically inherits the declarations of its parent context, and it also keeps track of which declarations were made within this context.
		"""
		res = super(QXmlNamespaceSupport,self).pushContext()
		return res
	#----------------------------------------------------------------------
	def reset(self):
		"""
		Resets this namespace support object ready for reuse.
		"""
		res = super(QXmlNamespaceSupport,self).reset()
		return res
	#----------------------------------------------------------------------
	def prefix(self,arg__1):
		"""
		prefix(arg__1)
			arg__1=unicode

		Returns one of the prefixes mapped to the namespace URI uri .
		If more than one prefix is currently mapped to the same URI, this function makes an arbitrary selection; if you want all of the prefixes, use PySide.QtXml.QXmlNamespaceSupport.prefixes() instead.
		Note: to check for a default prefix, use the PySide.QtXml.QXmlNamespaceSupport.uri() function with an argument of .
		"""
		res = super(QXmlNamespaceSupport,self).prefix(arg__1)
		return res
	#----------------------------------------------------------------------
	def prefixes(self,arg__1):
		"""
		prefixes(arg__1)
			arg__1=unicode

		This is an overloaded function.
		Returns a list of all prefixes currently declared for the namespace URI uri .
		The xml: prefix is included
		If you only want one prefix that is mapped to the namespace URI, and you dont care which one you get, use the PySide.QtXml.QXmlNamespaceSupport.prefix() function instead.
		Note: The empty (default) prefix is never included in this list; to check for the presence of a default namespace, call PySide.QtXml.QXmlNamespaceSupport.uri() with  as the argument.
		"""
		res = super(QXmlNamespaceSupport,self).prefixes(arg__1)
		return res
	#----------------------------------------------------------------------
	def processName(self,arg__1,arg__2,arg__3,arg__4):
		"""
		processName(arg__1,arg__2,arg__3,arg__4)
			arg__1=unicode
			arg__2=QtCore.bool
			arg__3=unicode
			arg__4=unicode

		Processes a raw XML 1.0 name in the current context by removing the prefix and looking it up among the prefixes currently declared.
		qname is the raw XML 1.0 name to be processed
		isAttribute is true if the name is an attribute name.
		This function stores the namespace URI in nsuri (which will be set to an empty string if the raw name has an undeclared prefix), and stores the local name (without prefix) in localname (which will be set to an empty string if no namespace is in use).
		Note that attribute names are processed differently than element names: an unprefixed element name gets the default namespace (if any), while an unprefixed attribute name does not.
		"""
		res = super(QXmlNamespaceSupport,self).processName(arg__1,arg__2,arg__3,arg__4)
		return res
	#----------------------------------------------------------------------
	def setPrefix(self,arg__1,arg__2):
		"""
		setPrefix(arg__1,arg__2)
			arg__1=unicode
			arg__2=unicode

		This function declares a prefix pre in the current namespace context to be the namespace URI uri
		The prefix remains in force until this context is popped, unless it is shadowed in a descendant context.
		Note that there is an asymmetry in this library
		PySide.QtXml.QXmlNamespaceSupport.prefix() does not return the default  prefix, even if you have declared one; to check for a default prefix, you must look it up explicitly using PySide.QtXml.QXmlNamespaceSupport.uri()
		This asymmetry exists to make it easier to look up prefixes for attribute names, where the default prefix is not allowed.
		"""
		res = super(QXmlNamespaceSupport,self).setPrefix(arg__1,arg__2)
		return res
	#----------------------------------------------------------------------
	def splitName(self,arg__1,arg__2,arg__3):
		"""
		splitName(arg__1,arg__2,arg__3)
			arg__1=unicode
			arg__2=unicode
			arg__3=unicode

		Splits the name qname at the : and returns the prefix in prefix and the local name in localname .
		"""
		res = super(QXmlNamespaceSupport,self).splitName(arg__1,arg__2,arg__3)
		return res
	#----------------------------------------------------------------------
	def uri(self,arg__1):
		"""
		uri(arg__1)
			arg__1=unicode

		Looks up the prefix prefix in the current context and returns the currently-mapped namespace URI
		Use the empty string () for the default namespace.
		"""
		res = super(QXmlNamespaceSupport,self).uri(arg__1)
		return res

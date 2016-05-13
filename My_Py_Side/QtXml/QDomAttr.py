from PySide import QtGui, QtCore

class QDomAttr(QtXml.QDomAttr):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDomAttr,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def name(self):
		"""
		Returns the attributes name.
		"""
		res = super(QDomAttr,self).name()
		return res
	#----------------------------------------------------------------------
	def ownerElement(self):
		"""
		Returns the element node this attribute is attached to or a null node if this attribute is not attached to any element.
		"""
		res = super(QDomAttr,self).ownerElement()
		isinstance(res,QtXml.QDomElement)
		return res
	#----------------------------------------------------------------------
	def specified(self):
		"""
		Returns true if the attribute has been set by the user with PySide.QtXml.QDomAttr.setValue()
		Returns false if the value hasnt been specified or set.
		"""
		res = super(QDomAttr,self).specified()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def value(self):
		"""
		Returns the value of the attribute or an empty string if the attribute has not been specified.
		"""
		res = super(QDomAttr,self).value()
		return res
	#----------------------------------------------------------------------
	def setValue(self,arg__1):
		"""
		setValue(arg__1)
			arg__1=unicode

		Sets the attributes value to v .
		"""
		res = super(QDomAttr,self).setValue(arg__1)
		return res

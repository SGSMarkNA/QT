from PySide import QtGui, QtCore

class QDomCharacterData(QtXml.QDomCharacterData):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDomCharacterData,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def data(self):
		"""
		Returns the string stored in this object.
		If the node is a null node , it will return an empty string.
		"""
		res = super(QDomCharacterData,self).data()
		return res
	#----------------------------------------------------------------------
	def length(self):
		"""
		Returns the length of the stored string.
		"""
		res = super(QDomCharacterData,self).length()
		isinstance(res,QtCore.uint)
		return res
	#----------------------------------------------------------------------
	def appendData(self,arg):
		"""
		appendData(arg)
			arg=unicode

		Appends the string arg to the stored string.
		"""
		res = super(QDomCharacterData,self).appendData(arg)
		return res
	#----------------------------------------------------------------------
	def deleteData(self,offset,count):
		"""
		deleteData(offset,count)
			offset=long
			count=long

		Deletes a substring of length count from position offset .
		"""
		res = super(QDomCharacterData,self).deleteData(offset,count)
		return res
	#----------------------------------------------------------------------
	def insertData(self,offset,arg):
		"""
		insertData(offset,arg)
			offset=long
			arg=unicode

		Inserts the string arg into the stored string at position offset .
		"""
		res = super(QDomCharacterData,self).insertData(offset,arg)
		return res
	#----------------------------------------------------------------------
	def replaceData(self,offset,count,arg):
		"""
		replaceData(offset,count,arg)
			offset=long
			count=long
			arg=unicode

		Replaces the substring of length count starting at position offset with the string arg .
		"""
		res = super(QDomCharacterData,self).replaceData(offset,count,arg)
		return res
	#----------------------------------------------------------------------
	def setData(self,arg__1):
		"""
		setData(arg__1)
			arg__1=unicode

		Sets this objects string to v .
		"""
		res = super(QDomCharacterData,self).setData(arg__1)
		return res
	#----------------------------------------------------------------------
	def substringData(self,offset,count):
		"""
		substringData(offset,count)
			offset=long
			count=long

		Returns the substring of length count from position offset .
		"""
		res = super(QDomCharacterData,self).substringData(offset,count)
		return res

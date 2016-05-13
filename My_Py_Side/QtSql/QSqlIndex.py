from PySide import QtGui, QtCore

class QSqlIndex(QtSql.QSqlIndex):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSqlIndex,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def cursorName(self):
		"""
		Returns the name of the cursor which the index is associated with.
		"""
		res = super(QSqlIndex,self).cursorName()
		return res
	#----------------------------------------------------------------------
	def name(self):
		"""
		Returns the name of the index.
		"""
		res = super(QSqlIndex,self).name()
		return res
	#----------------------------------------------------------------------
	def append(self,field,desc):
		"""
		append(field,desc)
			field=QtSql.QSqlField
			desc=QtCore.bool

		This is an overloaded function.
		Appends the field field to the list of indexed fields
		The field is appended with an ascending sort order, unless desc is true.
		"""
		res = super(QSqlIndex,self).append(field,desc)
		return res
	#----------------------------------------------------------------------
	def createField(self,i,prefix,verbose):
		"""
		createField(i,prefix,verbose)
			i=QtCore.int
			prefix=unicode
			verbose=QtCore.bool


		"""
		res = super(QSqlIndex,self).createField(i,prefix,verbose)
		return res
	#----------------------------------------------------------------------
	def isDescending(self,i):
		"""
		isDescending(i)
			i=QtCore.int

		Returns true if field i in the index is sorted in descending order; otherwise returns false.
		"""
		res = super(QSqlIndex,self).isDescending(i)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def setCursorName(self,cursorName):
		"""
		setCursorName(cursorName)
			cursorName=unicode

		Sets the name of the cursor that the index is associated with to cursorName .
		"""
		res = super(QSqlIndex,self).setCursorName(cursorName)
		return res
	#----------------------------------------------------------------------
	def setDescending(self,i,desc):
		"""
		setDescending(i,desc)
			i=QtCore.int
			desc=QtCore.bool

		If desc is true, field i is sorted in descending order
		Otherwise, field i is sorted in ascending order (the default)
		If the field does not exist, nothing happens.
		"""
		res = super(QSqlIndex,self).setDescending(i,desc)
		return res
	#----------------------------------------------------------------------
	def setName(self,name):
		"""
		setName(name)
			name=unicode

		Sets the name of the index to name .
		"""
		res = super(QSqlIndex,self).setName(name)
		return res

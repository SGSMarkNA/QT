from PySide import QtGui, QtCore

class QSqlRecord(QtSql.QSqlRecord):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSqlRecord,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Removes all the records fields.
		"""
		res = super(QSqlRecord,self).clear()
		return res
	#----------------------------------------------------------------------
	def clearValues(self):
		"""
		Clears the value of all fields in the record and sets each field to null.
		"""
		res = super(QSqlRecord,self).clearValues()
		return res
	#----------------------------------------------------------------------
	def count(self):
		"""
		Returns the number of fields in the record.
		"""
		res = super(QSqlRecord,self).count()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def isEmpty(self):
		"""
		Returns true if there are no fields in the record; otherwise returns false.
		"""
		res = super(QSqlRecord,self).isEmpty()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def append(self,field):
		"""
		append(field)
			field=QtSql.QSqlField

		Append a copy of field field to the end of the record.
		"""
		res = super(QSqlRecord,self).append(field)
		return res
	#----------------------------------------------------------------------
	def contains(self,name):
		"""
		contains(name)
			name=unicode

		Returns true if there is a field in the record called name ; otherwise returns false.
		"""
		res = super(QSqlRecord,self).contains(name)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def field(self,*args,**kwargs):
		"""
		field(i)
			i=QtCore.int

		field(name)
			name=unicode

		Returns the field at position index
		If the position is out of range, an empty field is returned.
		"""
		res = super(QSqlRecord,self).field(*args,**kwargs)
		isinstance(res,QtSql.QSqlField)
		return res
	#----------------------------------------------------------------------
	def fieldName(self,i):
		"""
		fieldName(i)
			i=QtCore.int

		Returns the name of the field at position index
		If the field does not exist, an empty string is returned.
		"""
		res = super(QSqlRecord,self).fieldName(i)
		return res
	#----------------------------------------------------------------------
	def indexOf(self,name):
		"""
		indexOf(name)
			name=unicode

		Returns the position of the field called name within the record, or -1 if it cannot be found
		Field names are not case-sensitive
		If more than one field matches, the first one is returned.
		"""
		res = super(QSqlRecord,self).indexOf(name)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def insert(self,pos,field):
		"""
		insert(pos,field)
			pos=QtCore.int
			field=QtSql.QSqlField

		Inserts the field field at position pos in the record.
		"""
		res = super(QSqlRecord,self).insert(pos,field)
		return res
	#----------------------------------------------------------------------
	def isGenerated(self,*args,**kwargs):
		"""
		isGenerated(name)
			name=unicode

		isGenerated(i)
			i=QtCore.int

		Returns true if the record has a field called name and this field is to be generated (the default); otherwise returns false.
		"""
		res = super(QSqlRecord,self).isGenerated(*args,**kwargs)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isNull(self,*args,**kwargs):
		"""
		isNull(i)
			i=QtCore.int

		isNull(name)
			name=unicode

		This is an overloaded function.
		Returns true if the field index is null or if there is no field at position index ; otherwise returns false.
		"""
		res = super(QSqlRecord,self).isNull(*args,**kwargs)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtSql.QSqlRecord

		Returns true if this object is not identical to other ; otherwise returns false.
		"""
		res = super(QSqlRecord,self).__ne__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtSql.QSqlRecord

		Returns true if this object is identical to other (i.e., has the same fields in the same order); otherwise returns false.
		"""
		res = super(QSqlRecord,self).__eq__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def remove(self,pos):
		"""
		remove(pos)
			pos=QtCore.int

		Removes the field at position pos
		If pos is out of range, nothing happens.
		"""
		res = super(QSqlRecord,self).remove(pos)
		return res
	#----------------------------------------------------------------------
	def replace(self,pos,field):
		"""
		replace(pos,field)
			pos=QtCore.int
			field=QtSql.QSqlField

		Replaces the field at position pos with the given field
		If pos is out of range, nothing happens.
		"""
		res = super(QSqlRecord,self).replace(pos,field)
		return res
	#----------------------------------------------------------------------
	def setGenerated(self,*args,**kwargs):
		"""
		setGenerated(i,generated)
			i=QtCore.int
			generated=QtCore.bool

		setGenerated(name,generated)
			name=unicode
			generated=QtCore.bool

		This is an overloaded function.
		Sets the generated flag for the field index to generated .
		"""
		res = super(QSqlRecord,self).setGenerated(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setNull(self,*args,**kwargs):
		"""
		setNull(i)
			i=QtCore.int

		setNull(name)
			name=unicode

		Sets the value of field index to null
		If the field does not exist, nothing happens.
		"""
		res = super(QSqlRecord,self).setNull(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setValue(self,*args,**kwargs):
		"""
		setValue(i,val)
			i=QtCore.int
			val=object

		setValue(name,val)
			name=unicode
			val=object

		Sets the value of the field at position index to val
		If the field does not exist, nothing happens.
		"""
		res = super(QSqlRecord,self).setValue(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def value(self,*args,**kwargs):
		"""
		value(name)
			name=unicode

		value(i)
			i=QtCore.int

		This is an overloaded function.
		Returns the value of the field called name in the record
		If field name does not exist an invalid variant is returned.
		"""
		res = super(QSqlRecord,self).value(*args,**kwargs)
		return res

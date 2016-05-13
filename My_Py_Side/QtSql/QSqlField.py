from PySide import QtGui, QtCore

class QSqlField(QtSql.QSqlField):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSqlField,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Clears the value of the field and sets it to NULL
		If the field is read-only, nothing happens.
		"""
		res = super(QSqlField,self).clear()
		return res
	#----------------------------------------------------------------------
	def defaultValue(self):
		"""
		Returns the fields default value (which may be NULL).
		"""
		res = super(QSqlField,self).defaultValue()
		return res
	#----------------------------------------------------------------------
	def isAutoValue(self):
		"""
		Returns true if the value is auto-generated by the database, for example auto-increment primary key values.
		"""
		res = super(QSqlField,self).isAutoValue()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isGenerated(self):
		"""
		Returns true if the field is generated; otherwise returns false.
		"""
		res = super(QSqlField,self).isGenerated()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if the fields value is NULL; otherwise returns false.
		"""
		res = super(QSqlField,self).isNull()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isReadOnly(self):
		"""
		Returns true if the fields value is read-only; otherwise returns false.
		"""
		res = super(QSqlField,self).isReadOnly()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if the fields variant type is valid; otherwise returns false.
		"""
		res = super(QSqlField,self).isValid()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def length(self):
		"""
		Returns the fields length.
		If the returned value is negative, it means that the information is not available from the database.
		"""
		res = super(QSqlField,self).length()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def name(self):
		"""
		Returns the name of the field.
		"""
		res = super(QSqlField,self).name()
		return res
	#----------------------------------------------------------------------
	def precision(self):
		"""
		Returns the fields precision; this is only meaningful for numeric types.
		If the returned value is negative, it means that the information is not available from the database.
		"""
		res = super(QSqlField,self).precision()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def requiredStatus(self):
		"""
		Returns true if this is a required field; otherwise returns false
		An INSERT will fail if a required field does not have a value.
		"""
		res = super(QSqlField,self).requiredStatus()
		isinstance(res,QtSql.QSqlField.RequiredStatus)
		return res
	#----------------------------------------------------------------------
	def type(self):
		"""
		Returns the fields type as stored in the database
		Note that the actual value might have a different type, Numerical values that are too large to store in a long int or double are usually stored as strings to prevent precision loss.
		"""
		res = super(QSqlField,self).type()
		isinstance(res,QtCore.QVariant::Type)
		return res
	#----------------------------------------------------------------------
	def typeID(self):
		"""
		Returns the type ID for the field.
		If the returned value is negative, it means that the information is not available from the database.
		"""
		res = super(QSqlField,self).typeID()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def value(self):
		"""
		Returns the value of the field as a PySide.QtCore.QVariant .
		Use PySide.QtSql.QSqlField.isNull() to check if the fields value is NULL.
		"""
		res = super(QSqlField,self).value()
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtSql.QSqlField

		Returns true if the field is unequal to other ; otherwise returns false.
		"""
		res = super(QSqlField,self).__ne__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtSql.QSqlField

		Returns true if the field is equal to other ; otherwise returns false.
		"""
		res = super(QSqlField,self).__eq__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def setAutoValue(self,autoVal):
		"""
		setAutoValue(autoVal)
			autoVal=QtCore.bool

		Marks the field as an auto-generated value if autoVal is true.
		"""
		res = super(QSqlField,self).setAutoValue(autoVal)
		return res
	#----------------------------------------------------------------------
	def setDefaultValue(self,value):
		"""
		setDefaultValue(value)
			value=object

		Sets the default value used for this field to value .
		"""
		res = super(QSqlField,self).setDefaultValue(value)
		return res
	#----------------------------------------------------------------------
	def setGenerated(self,gen):
		"""
		setGenerated(gen)
			gen=QtCore.bool

		Sets the generated state
		If gen is false, no SQL will be generated for this field; otherwise, Qt classes such as PySide.QtSql.QSqlQueryModel and PySide.QtSql.QSqlTableModel will generate SQL for this field.
		"""
		res = super(QSqlField,self).setGenerated(gen)
		return res
	#----------------------------------------------------------------------
	def setLength(self,fieldLength):
		"""
		setLength(fieldLength)
			fieldLength=QtCore.int

		Sets the fields length to fieldLength
		For strings this is the maximum number of characters the string can hold; the meaning varies for other types.
		"""
		res = super(QSqlField,self).setLength(fieldLength)
		return res
	#----------------------------------------------------------------------
	def setName(self,name):
		"""
		setName(name)
			name=unicode

		Sets the name of the field to name .
		"""
		res = super(QSqlField,self).setName(name)
		return res
	#----------------------------------------------------------------------
	def setPrecision(self,precision):
		"""
		setPrecision(precision)
			precision=QtCore.int

		Sets the fields precision
		This only affects numeric fields.
		"""
		res = super(QSqlField,self).setPrecision(precision)
		return res
	#----------------------------------------------------------------------
	def setReadOnly(self,readOnly):
		"""
		setReadOnly(readOnly)
			readOnly=QtCore.bool

		Sets the read only flag of the fields value to readOnly
		A read-only field cannot have its value set with PySide.QtSql.QSqlField.setValue() and cannot be cleared to NULL with PySide.QtSql.QSqlField.clear() .
		"""
		res = super(QSqlField,self).setReadOnly(readOnly)
		return res
	#----------------------------------------------------------------------
	def setRequired(self,required):
		"""
		setRequired(required)
			required=QtCore.bool

		Sets the required status of this field to Required if required is true; otherwise sets it to Optional .
		"""
		res = super(QSqlField,self).setRequired(required)
		return res
	#----------------------------------------------------------------------
	def setRequiredStatus(self,status):
		"""
		setRequiredStatus(status)
			status=QtSql.QSqlField.RequiredStatus

		Sets the required status of this field to required .
		"""
		res = super(QSqlField,self).setRequiredStatus(status)
		return res
	#----------------------------------------------------------------------
	def setSqlType(self,type):
		"""
		setSqlType(type)
			type=QtCore.int


		"""
		res = super(QSqlField,self).setSqlType(type)
		return res
	#----------------------------------------------------------------------
	def setType(self,type):
		"""
		setType(type)
			type=QtCore.QVariant::Type


		"""
		res = super(QSqlField,self).setType(type)
		return res
	#----------------------------------------------------------------------
	def setValue(self,value):
		"""
		setValue(value)
			value=object

		Sets the value of the field to value
		If the field is read-only ( PySide.QtSql.QSqlField.isReadOnly() returns true), nothing happens.
		If the data type of value differs from the fields current data type, an attempt is made to cast it to the proper type
		This preserves the data type of the field in the case of assignment, e.g
		a PySide.QtCore.QString to an integer data type.
		To set the value to NULL, use PySide.QtSql.QSqlField.clear() .
		"""
		res = super(QSqlField,self).setValue(value)
		return res

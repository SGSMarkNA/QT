from PySide import QtGui, QtCore

class QSqlError(QtSql.QSqlError):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSqlError,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def databaseText(self):
		"""
		Returns the text of the error as reported by the database
		This may contain database-specific descriptions; it may be empty.
		"""
		res = super(QSqlError,self).databaseText()
		return res
	#----------------------------------------------------------------------
	def driverText(self):
		"""
		Returns the text of the error as reported by the driver
		This may contain database-specific descriptions
		It may also be empty.
		"""
		res = super(QSqlError,self).driverText()
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if an error is set, otherwise false.
		Example:
		"""
		res = super(QSqlError,self).isValid()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def number(self):
		"""
		Returns the database-specific error number, or -1 if it cannot be determined.
		"""
		res = super(QSqlError,self).number()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def text(self):
		"""
		This is a convenience function that returns PySide.QtSql.QSqlError.databaseText() and PySide.QtSql.QSqlError.driverText() concatenated into a single string.
		"""
		res = super(QSqlError,self).text()
		return res
	#----------------------------------------------------------------------
	def type(self):
		"""
		Returns the error type, or -1 if the type cannot be determined.
		"""
		res = super(QSqlError,self).type()
		isinstance(res,QtSql.QSqlError.ErrorType)
		return res
	#----------------------------------------------------------------------
	def setDatabaseText(self,databaseText):
		"""
		setDatabaseText(databaseText)
			databaseText=unicode

		Sets the database error text to the value of databaseText .
		"""
		res = super(QSqlError,self).setDatabaseText(databaseText)
		return res
	#----------------------------------------------------------------------
	def setDriverText(self,driverText):
		"""
		setDriverText(driverText)
			driverText=unicode

		Sets the driver error text to the value of driverText .
		"""
		res = super(QSqlError,self).setDriverText(driverText)
		return res
	#----------------------------------------------------------------------
	def setNumber(self,number):
		"""
		setNumber(number)
			number=QtCore.int

		Sets the database-specific error number to number .
		"""
		res = super(QSqlError,self).setNumber(number)
		return res
	#----------------------------------------------------------------------
	def setType(self,type):
		"""
		setType(type)
			type=QtSql.QSqlError.ErrorType

		Sets the error type to the value of type .
		"""
		res = super(QSqlError,self).setType(type)
		return res

from PySide import QtGui, QtCore

class QSqlDriver(QtSql.QSqlDriver):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSqlDriver,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def beginTransaction(self):
		"""
		This function is called to begin a transaction
		If successful, return true, otherwise return false
		The default implementation does nothing and returns false.
		"""
		res = super(QSqlDriver,self).beginTransaction()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def close(self):
		"""
		Derived classes must reimplement this pure virtual function in order to close the database connection
		Return true on success, false on failure.
		"""
		res = super(QSqlDriver,self).close()
		return res
	#----------------------------------------------------------------------
	def commitTransaction(self):
		"""
		This function is called to commit a transaction
		If successful, return true, otherwise return false
		The default implementation does nothing and returns false.
		"""
		res = super(QSqlDriver,self).commitTransaction()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def createResult(self):
		"""
		Creates an empty SQL result on the database
		Derived classes must reimplement this function and return a PySide.QtSql.QSqlResult object appropriate for their database to the caller.
		"""
		res = super(QSqlDriver,self).createResult()
		isinstance(res,QtSql.QSqlResult)
		return res
	#----------------------------------------------------------------------
	def isOpen(self):
		"""
		Returns true if the database connection is open; otherwise returns false.
		"""
		res = super(QSqlDriver,self).isOpen()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isOpenError(self):
		"""
		Returns true if the there was an error opening the database connection; otherwise returns false.
		"""
		res = super(QSqlDriver,self).isOpenError()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def lastError(self):
		"""
		Returns a PySide.QtSql.QSqlError object which contains information about the last error that occurred on the database.
		"""
		res = super(QSqlDriver,self).lastError()
		isinstance(res,QtSql.QSqlError)
		return res
	#----------------------------------------------------------------------
	def numericalPrecisionPolicy(self):
		"""
		Returns the current default precision policy for the database connection.
		"""
		res = super(QSqlDriver,self).numericalPrecisionPolicy()
		isinstance(res,QtSql.QSql.NumericalPrecisionPolicy)
		return res
	#----------------------------------------------------------------------
	def rollbackTransaction(self):
		"""
		This function is called to rollback a transaction
		If successful, return true, otherwise return false
		The default implementation does nothing and returns false.
		"""
		res = super(QSqlDriver,self).rollbackTransaction()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def subscribedToNotifications(self):
		"""
		Returns a list of the names of the event notifications that are currently subscribed to.
		"""
		res = super(QSqlDriver,self).subscribedToNotifications()
		return res
	#----------------------------------------------------------------------
	def escapeIdentifier(self,identifier,type):
		"""
		escapeIdentifier(identifier,type)
			identifier=unicode
			type=QtSql.QSqlDriver.IdentifierType

		Returns the identifier escaped according to the database rules
		identifier can either be a table name or field name, dependent on type .
		The default implementation does nothing.
		"""
		res = super(QSqlDriver,self).escapeIdentifier(identifier,type)
		return res
	#----------------------------------------------------------------------
	def formatValue(self,field,trimStrings=None):
		"""
		formatValue(field,trimStrings=None)
			field=QtSql.QSqlField
			trimStrings=QtCore.bool

		Returns a string representation of the field value for the database
		This is used, for example, when constructing INSERT and UPDATE statements.
		The default implementation returns the value formatted as a string according to the following rules:
		"""
		res = super(QSqlDriver,self).formatValue(field,trimStrings)
		return res
	#----------------------------------------------------------------------
	def hasFeature(self,f):
		"""
		hasFeature(f)
			f=QtSql.QSqlDriver.DriverFeature

		Returns true if the driver supports feature feature ; otherwise returns false.
		Note that some databases need to be PySide.QtSql.QSqlDriver.open() before this can be determined.
		"""
		res = super(QSqlDriver,self).hasFeature(f)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isIdentifierEscaped(self,identifier,type):
		"""
		isIdentifierEscaped(identifier,type)
			identifier=unicode
			type=QtSql.QSqlDriver.IdentifierType

		Returns whether identifier is escaped according to the database rules
		identifier can either be a table name or field name, dependent on type .
		"""
		res = super(QSqlDriver,self).isIdentifierEscaped(identifier,type)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def open(self,db,user=None,password=None,host=None,port=None,connOpts=None):
		"""
		open(db,user=None,password=None,host=None,port=None,connOpts=None)
			db=unicode
			user=unicode
			password=unicode
			host=unicode
			port=QtCore.int
			connOpts=unicode

		Derived classes must reimplement this pure virtual function to open a database connection on database db , using user name user , password password , host host , port port and connection options options .
		The function must return true on success and false on failure.
		"""
		res = super(QSqlDriver,self).open(db,user,password,host,port,connOpts)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def primaryIndex(self,tableName):
		"""
		primaryIndex(tableName)
			tableName=unicode

		Returns the primary index for table tableName
		Returns an empty PySide.QtSql.QSqlIndex if the table doesnt have a primary index
		The default implementation returns an empty index.
		"""
		res = super(QSqlDriver,self).primaryIndex(tableName)
		isinstance(res,QtSql.QSqlIndex)
		return res
	#----------------------------------------------------------------------
	def record(self,tableName):
		"""
		record(tableName)
			tableName=unicode

		Returns a PySide.QtSql.QSqlRecord populated with the names of the fields in table tableName
		If no such table exists, an empty record is returned
		The default implementation returns an empty record.
		"""
		res = super(QSqlDriver,self).record(tableName)
		isinstance(res,QtSql.QSqlRecord)
		return res
	#----------------------------------------------------------------------
	def setLastError(self,e):
		"""
		setLastError(e)
			e=QtSql.QSqlError

		This function is used to set the value of the last error, error , that occurred on the database.
		"""
		res = super(QSqlDriver,self).setLastError(e)
		return res
	#----------------------------------------------------------------------
	def setNumericalPrecisionPolicy(self,precisionPolicy):
		"""
		setNumericalPrecisionPolicy(precisionPolicy)
			precisionPolicy=QtSql.QSql.NumericalPrecisionPolicy


		"""
		res = super(QSqlDriver,self).setNumericalPrecisionPolicy(precisionPolicy)
		return res
	#----------------------------------------------------------------------
	def setOpen(self,o):
		"""
		setOpen(o)
			o=QtCore.bool

		This function sets the open state of the database to open
		Derived classes can use this function to report the status of PySide.QtSql.QSqlDriver.open() .
		"""
		res = super(QSqlDriver,self).setOpen(o)
		return res
	#----------------------------------------------------------------------
	def setOpenError(self,e):
		"""
		setOpenError(e)
			e=QtCore.bool

		This function sets the open error state of the database to error
		Derived classes can use this function to report the status of PySide.QtSql.QSqlDriver.open()
		Note that if error is true the open state of the database is set to closed (i.e., PySide.QtSql.QSqlDriver.isOpen() returns false).
		"""
		res = super(QSqlDriver,self).setOpenError(e)
		return res
	#----------------------------------------------------------------------
	def sqlStatement(self,type,tableName,rec,preparedStatement):
		"""
		sqlStatement(type,tableName,rec,preparedStatement)
			type=QtSql.QSqlDriver.StatementType
			tableName=unicode
			rec=QtSql.QSqlRecord
			preparedStatement=QtCore.bool

		Returns a SQL statement of type type for the table tableName with the values from rec
		If preparedStatement is true, the string will contain placeholders instead of values.
		This method can be used to manipulate tables without having to worry about database-dependent SQL dialects
		For non-prepared statements, the values will be properly escaped.
		"""
		res = super(QSqlDriver,self).sqlStatement(type,tableName,rec,preparedStatement)
		return res
	#----------------------------------------------------------------------
	def stripDelimiters(self,identifier,type):
		"""
		stripDelimiters(identifier,type)
			identifier=unicode
			type=QtSql.QSqlDriver.IdentifierType

		Returns the identifier with the leading and trailing delimiters removed, identifier can either be a table name or field name, dependent on type
		If identifier does not have leading and trailing delimiter characters, identifier is returned without modification.
		"""
		res = super(QSqlDriver,self).stripDelimiters(identifier,type)
		return res
	#----------------------------------------------------------------------
	def subscribeToNotification(self,name):
		"""
		subscribeToNotification(name)
			name=unicode

		This function is called to subscribe to event notifications from the database
		name identifies the event notification.
		If successful, return true, otherwise return false.
		The database must be open when this function is called
		When the database is closed by calling PySide.QtSql.QSqlDriver.close() all subscribed event notifications are automatically unsubscribed
		Note that calling PySide.QtSql.QSqlDriver.open() on an already open database may implicitly cause PySide.QtSql.QSqlDriver.close() to be called, which will cause the driver to unsubscribe from all event notifications.
		When an event notification identified by name is posted by the database the PySide.QtSql.QSqlDriver.notification() signal is emitted.
		"""
		res = super(QSqlDriver,self).subscribeToNotification(name)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def tables(self,tableType):
		"""
		tables(tableType)
			tableType=QtSql.QSql.TableType


		"""
		res = super(QSqlDriver,self).tables(tableType)
		return res
	#----------------------------------------------------------------------
	def unsubscribeFromNotification(self,name):
		"""
		unsubscribeFromNotification(name)
			name=unicode

		This function is called to unsubscribe from event notifications from the database
		name identifies the event notification.
		If successful, return true, otherwise return false.
		The database must be open when this function is called
		All subscribed event notifications are automatically unsubscribed from when the PySide.QtSql.QSqlDriver.close() function is called.
		After calling this function the PySide.QtSql.QSqlDriver.notification() signal will no longer be emitted when an event notification identified by name is posted by the database.
		"""
		res = super(QSqlDriver,self).unsubscribeFromNotification(name)
		isinstance(res,bool)
		return res

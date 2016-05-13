from PySide import QtGui, QtCore

class QSqlDatabase(QtSql.QSqlDatabase):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSqlDatabase,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def close(self):
		"""
		Closes the database connection, freeing any resources acquired, and invalidating any existing PySide.QtSql.QSqlQuery objects that are used with the database.
		This will also affect copies of this PySide.QtSql.QSqlDatabase object.
		"""
		res = super(QSqlDatabase,self).close()
		return res
	#----------------------------------------------------------------------
	def commit(self):
		"""
		Commits a transaction to the database if the driver supports transactions and a PySide.QtSql.QSqlDatabase.transaction() has been started
		Returns true if the operation succeeded
		Otherwise it returns false .
		Call PySide.QtSql.QSqlDatabase.lastError() to get information about errors.
		"""
		res = super(QSqlDatabase,self).commit()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def connectOptions(self):
		"""
		Returns the connection options string used for this connection
		The string may be empty.
		"""
		res = super(QSqlDatabase,self).connectOptions()
		return res
	#----------------------------------------------------------------------
	def connectionName(self):
		"""
		Returns the connection name, which may be empty
		Note: The connection name is not the database name .
		"""
		res = super(QSqlDatabase,self).connectionName()
		return res
	#----------------------------------------------------------------------
	def databaseName(self):
		"""
		Returns the connections database name, which may be empty
		Note: The database name is not the connection name.
		"""
		res = super(QSqlDatabase,self).databaseName()
		return res
	#----------------------------------------------------------------------
	def driver(self):
		"""
		Returns the database driver used to access the database connection.
		"""
		res = super(QSqlDatabase,self).driver()
		isinstance(res,QtSql.QSqlDriver)
		return res
	#----------------------------------------------------------------------
	def driverName(self):
		"""
		Returns the connections driver name.
		"""
		res = super(QSqlDatabase,self).driverName()
		return res
	#----------------------------------------------------------------------
	def hostName(self):
		"""
		Returns the connections host name; it may be empty.
		"""
		res = super(QSqlDatabase,self).hostName()
		return res
	#----------------------------------------------------------------------
	def isOpen(self):
		"""
		Returns true if the database connection is currently open; otherwise returns false.
		"""
		res = super(QSqlDatabase,self).isOpen()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isOpenError(self):
		"""
		Returns true if there was an error opening the database connection; otherwise returns false
		Error information can be retrieved using the PySide.QtSql.QSqlDatabase.lastError() function.
		"""
		res = super(QSqlDatabase,self).isOpenError()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if the PySide.QtSql.QSqlDatabase has a valid driver.
		Example:
		"""
		res = super(QSqlDatabase,self).isValid()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def lastError(self):
		"""
		Returns information about the last error that occurred on the database.
		Failures that occur in conjunction with an individual query are reported by QSqlQuery.lastError() .
		"""
		res = super(QSqlDatabase,self).lastError()
		isinstance(res,QtSql.QSqlError)
		return res
	#----------------------------------------------------------------------
	def numericalPrecisionPolicy(self):
		"""
		Returns the current default precision policy for the database connection.
		"""
		res = super(QSqlDatabase,self).numericalPrecisionPolicy()
		isinstance(res,QtSql.QSql.NumericalPrecisionPolicy)
		return res
	#----------------------------------------------------------------------
	def open(self):
		"""
		Opens the database connection using the current connection values
		Returns true on success; otherwise returns false
		Error information can be retrieved using PySide.QtSql.QSqlDatabase.lastError() .
		"""
		res = super(QSqlDatabase,self).open()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def password(self):
		"""
		Returns the connections password
		If the password was not set with PySide.QtSql.QSqlDatabase.setPassword() , and if the password was given in the PySide.QtSql.QSqlDatabase.open() call, or if no password was used, an empty string is returned.
		"""
		res = super(QSqlDatabase,self).password()
		return res
	#----------------------------------------------------------------------
	def port(self):
		"""
		Returns the connections port number
		The value is undefined if the port number has not been set.
		"""
		res = super(QSqlDatabase,self).port()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def rollback(self):
		"""
		Rolls back a transaction on the database, if the driver supports transactions and a PySide.QtSql.QSqlDatabase.transaction() has been started
		Returns true if the operation succeeded
		Otherwise it returns false .
		Call PySide.QtSql.QSqlDatabase.lastError() to get information about errors.
		"""
		res = super(QSqlDatabase,self).rollback()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def transaction(self):
		"""
		Begins a transaction on the database if the driver supports transactions
		Returns true if the operation succeeded
		Otherwise it returns false .
		"""
		res = super(QSqlDatabase,self).transaction()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def userName(self):
		"""
		Returns the connections user name; it may be empty.
		"""
		res = super(QSqlDatabase,self).userName()
		return res
	#----------------------------------------------------------------------
	def exec_(self,query=None):
		"""
		exec_(query=None)
			query=unicode

		Executes a SQL statement on the database and returns a PySide.QtSql.QSqlQuery object
		Use PySide.QtSql.QSqlDatabase.lastError() to retrieve error information
		If query is empty, an empty, invalid query is returned and PySide.QtSql.QSqlDatabase.lastError() is not affected.
		"""
		res = super(QSqlDatabase,self).exec_(query)
		isinstance(res,QtSql.QSqlQuery)
		return res
	#----------------------------------------------------------------------
	def open(self,user,password):
		"""
		open(user,password)
			user=unicode
			password=unicode

		This is an overloaded function.
		Opens the database connection using the given user name and password
		Returns true on success; otherwise returns false
		Error information can be retrieved using the PySide.QtSql.QSqlDatabase.lastError() function.
		This function does not store the password it is given
		Instead, the password is passed directly to the driver for opening the connection and it is then discarded.
		"""
		res = super(QSqlDatabase,self).open(user,password)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def primaryIndex(self,tablename):
		"""
		primaryIndex(tablename)
			tablename=unicode

		Returns the primary index for table tablename
		If no primary index exists an empty PySide.QtSql.QSqlIndex is returned.
		"""
		res = super(QSqlDatabase,self).primaryIndex(tablename)
		isinstance(res,QtSql.QSqlIndex)
		return res
	#----------------------------------------------------------------------
	def record(self,tablename):
		"""
		record(tablename)
			tablename=unicode

		Returns a PySide.QtSql.QSqlRecord populated with the names of all the fields in the table (or view) called tablename
		The order in which the fields appear in the record is undefined
		If no such table (or view) exists, an empty record is returned.
		"""
		res = super(QSqlDatabase,self).record(tablename)
		isinstance(res,QtSql.QSqlRecord)
		return res
	#----------------------------------------------------------------------
	def setConnectOptions(self,options=None):
		"""
		setConnectOptions(options=None)
			options=unicode

		Sets database-specific options
		This must be done before the connection is opened or it has no effect (or you can PySide.QtSql.QSqlDatabase.close() the connection, call this function and PySide.QtSql.QSqlDatabase.open() the connection again).
		The format of the options string is a semicolon separated list of option names or option=value pairs
		The options depend on the database client used:
		Examples:
		Refer to the client library documentation for more information about the different options.
		"""
		res = super(QSqlDatabase,self).setConnectOptions(options)
		return res
	#----------------------------------------------------------------------
	def setDatabaseName(self,name):
		"""
		setDatabaseName(name)
			name=unicode

		Sets the connections database name to name
		To have effect, the database name must be set before the connection is opened
		Alternatively, you can PySide.QtSql.QSqlDatabase.close() the connection, set the database name, and call PySide.QtSql.QSqlDatabase.open() again
		Note: The database name is not the connection name
		The connection name must be passed to PySide.QtSql.QSqlDatabase.addDatabase() at connection object create time.
		For the QOCI (Oracle) driver, the database name is the TNS Service Name.
		For the QODBC driver, the name can either be a DSN, a DSN filename (in which case the file must have a .dsn extension), or a connection string.
		For example, Microsoft Access users can use the following connection string to open an .mdb file directly, instead of having to create a DSN entry in the ODBC manager:
		There is no default value.
		"""
		res = super(QSqlDatabase,self).setDatabaseName(name)
		return res
	#----------------------------------------------------------------------
	def setHostName(self,host):
		"""
		setHostName(host)
			host=unicode

		Sets the connections host name to host
		To have effect, the host name must be set before the connection is opened
		Alternatively, you can PySide.QtSql.QSqlDatabase.close() the connection, set the host name, and call PySide.QtSql.QSqlDatabase.open() again.
		There is no default value.
		"""
		res = super(QSqlDatabase,self).setHostName(host)
		return res
	#----------------------------------------------------------------------
	def setNumericalPrecisionPolicy(self,precisionPolicy):
		"""
		setNumericalPrecisionPolicy(precisionPolicy)
			precisionPolicy=QtSql.QSql.NumericalPrecisionPolicy


		"""
		res = super(QSqlDatabase,self).setNumericalPrecisionPolicy(precisionPolicy)
		return res
	#----------------------------------------------------------------------
	def setPassword(self,password):
		"""
		setPassword(password)
			password=unicode

		Sets the connections password to password
		To have effect, the password must be set before the connection is opened
		Alternatively, you can PySide.QtSql.QSqlDatabase.close() the connection, set the password, and call PySide.QtSql.QSqlDatabase.open() again.
		There is no default value.
		"""
		res = super(QSqlDatabase,self).setPassword(password)
		return res
	#----------------------------------------------------------------------
	def setPort(self,p):
		"""
		setPort(p)
			p=QtCore.int

		Sets the connections port number to port
		To have effect, the port number must be set before the connection is opened
		Alternatively, you can PySide.QtSql.QSqlDatabase.close() the connection, set the port number, and call PySide.QtSql.QSqlDatabase.open() again..
		There is no default value.
		"""
		res = super(QSqlDatabase,self).setPort(p)
		return res
	#----------------------------------------------------------------------
	def setUserName(self,name):
		"""
		setUserName(name)
			name=unicode

		Sets the connections user name to name
		To have effect, the user name must be set before the connection is opened
		Alternatively, you can PySide.QtSql.QSqlDatabase.close() the connection, set the user name, and call PySide.QtSql.QSqlDatabase.open() again.
		There is no default value.
		"""
		res = super(QSqlDatabase,self).setUserName(name)
		return res
	#----------------------------------------------------------------------
	def tables(self,type=None):
		"""
		tables(type=None)
			type=QtSql.QSql.TableType


		"""
		res = super(QSqlDatabase,self).tables(type)
		return res

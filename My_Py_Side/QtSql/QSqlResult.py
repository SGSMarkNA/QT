from PySide import QtGui, QtCore

class QSqlResult(QtSql.QSqlResult):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSqlResult,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def at(self):
		"""
		Returns the current (zero-based) row position of the result
		May return the special values QSql.BeforeFirstRow or QSql.AfterLastRow .
		"""
		res = super(QSqlResult,self).at()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def bindingSyntax(self):
		"""
		Returns the binding syntax used by prepared queries.
		"""
		res = super(QSqlResult,self).bindingSyntax()
		isinstance(res,QtSql.QSqlResult.BindingSyntax)
		return res
	#----------------------------------------------------------------------
	def boundValueCount(self):
		"""
		Returns the number of bound values in the result.
		"""
		res = super(QSqlResult,self).boundValueCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def boundValues(self):
		"""
		Returns a vector of the results bound values for the current record (row).
		"""
		res = super(QSqlResult,self).boundValues()
		return res
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Clears the entire result set and releases any associated resources.
		"""
		res = super(QSqlResult,self).clear()
		return res
	#----------------------------------------------------------------------
	def detachFromResultSet(self):
		"""

		"""
		res = super(QSqlResult,self).detachFromResultSet()
		return res
	#----------------------------------------------------------------------
	def driver(self):
		"""
		Returns the driver associated with the result
		This is the object that was passed to the constructor.
		"""
		res = super(QSqlResult,self).driver()
		isinstance(res,QtSql.QSqlDriver)
		return res
	#----------------------------------------------------------------------
	def exec_(self):
		"""
		Executes the query, returning true if successful; otherwise returns false.
		"""
		res = super(QSqlResult,self).exec_()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def executedQuery(self):
		"""
		Returns the query that was actually executed
		This may differ from the query that was passed, for example if bound values were used with a prepared query and the underlying database doesnt support prepared queries.
		"""
		res = super(QSqlResult,self).executedQuery()
		return res
	#----------------------------------------------------------------------
	def fetchFirst(self):
		"""
		Positions the result to the first record (row 0) in the result.
		This function is only called if the result is in an active state
		Derived classes must reimplement this function and position the result to the first record, and call PySide.QtSql.QSqlResult.setAt() with an appropriate value
		Return true to indicate success, or false to signify failure.
		"""
		res = super(QSqlResult,self).fetchFirst()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def fetchLast(self):
		"""
		Positions the result to the last record (last row) in the result.
		This function is only called if the result is in an active state
		Derived classes must reimplement this function and position the result to the last record, and call PySide.QtSql.QSqlResult.setAt() with an appropriate value
		Return true to indicate success, or false to signify failure.
		"""
		res = super(QSqlResult,self).fetchLast()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def fetchNext(self):
		"""
		Positions the result to the next available record (row) in the result.
		This function is only called if the result is in an active state
		The default implementation calls PySide.QtSql.QSqlResult.fetch() with the next index
		Derived classes can reimplement this function and position the result to the next record in some other way, and call PySide.QtSql.QSqlResult.setAt() with an appropriate value
		Return true to indicate success, or false to signify failure.
		"""
		res = super(QSqlResult,self).fetchNext()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def fetchPrevious(self):
		"""
		Positions the result to the previous record (row) in the result.
		This function is only called if the result is in an active state
		The default implementation calls PySide.QtSql.QSqlResult.fetch() with the previous index
		Derived classes can reimplement this function and position the result to the next record in some other way, and call PySide.QtSql.QSqlResult.setAt() with an appropriate value
		Return true to indicate success, or false to signify failure.
		"""
		res = super(QSqlResult,self).fetchPrevious()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def handle(self):
		"""
		Returns the low-level database handle for this result set wrapped in a PySide.QtCore.QVariant or an invalid PySide.QtCore.QVariant if there is no handle.
		The handle returned here is database-dependent, you should query the type name of the variant before accessing it.
		This example retrieves the handle for a sqlite result:
		This snippet returns the handle for PostgreSQL or MySQL:
		"""
		res = super(QSqlResult,self).handle()
		return res
	#----------------------------------------------------------------------
	def hasOutValues(self):
		"""
		Returns true if at least one of the querys bound values is a QSql::Out or a QSql.InOut ; otherwise returns false.
		"""
		res = super(QSqlResult,self).hasOutValues()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isActive(self):
		"""
		Returns true if the result has records to be retrieved; otherwise returns false.
		"""
		res = super(QSqlResult,self).isActive()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isForwardOnly(self):
		"""
		Returns true if you can only scroll forward through the result set; otherwise returns false.
		"""
		res = super(QSqlResult,self).isForwardOnly()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isSelect(self):
		"""
		Returns true if the current result is from a SELECT statement; otherwise returns false.
		"""
		res = super(QSqlResult,self).isSelect()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if the result is positioned on a valid record (that is, the result is not positioned before the first or after the last record); otherwise returns false.
		"""
		res = super(QSqlResult,self).isValid()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def lastError(self):
		"""
		Returns the last error associated with the result.
		"""
		res = super(QSqlResult,self).lastError()
		isinstance(res,QtSql.QSqlError)
		return res
	#----------------------------------------------------------------------
	def lastInsertId(self):
		"""
		Returns the object ID of the most recent inserted row if the database supports it
		An invalid PySide.QtCore.QVariant will be returned if the query did not insert any value or if the database does not report the id back
		If more than one row was touched by the insert, the behavior is undefined.
		Note that for Oracle databases the rows ROWID will be returned, while for MySQL databases the rows auto-increment field will be returned.
		"""
		res = super(QSqlResult,self).lastInsertId()
		return res
	#----------------------------------------------------------------------
	def lastQuery(self):
		"""
		Returns the current SQL query text, or an empty string if there isnt one.
		"""
		res = super(QSqlResult,self).lastQuery()
		return res
	#----------------------------------------------------------------------
	def nextResult(self):
		"""

		"""
		res = super(QSqlResult,self).nextResult()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def numRowsAffected(self):
		"""
		Returns the number of rows affected by the last query executed, or -1 if it cannot be determined or if the query is a SELECT statement.
		"""
		res = super(QSqlResult,self).numRowsAffected()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def numericalPrecisionPolicy(self):
		"""

		"""
		res = super(QSqlResult,self).numericalPrecisionPolicy()
		isinstance(res,QtSql.QSql.NumericalPrecisionPolicy)
		return res
	#----------------------------------------------------------------------
	def record(self):
		"""
		Returns the current record if the query is active; otherwise returns an empty PySide.QtSql.QSqlRecord .
		The default implementation always returns an empty PySide.QtSql.QSqlRecord .
		"""
		res = super(QSqlResult,self).record()
		isinstance(res,QtSql.QSqlRecord)
		return res
	#----------------------------------------------------------------------
	def resetBindCount(self):
		"""

		"""
		res = super(QSqlResult,self).resetBindCount()
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""
		Returns the size of the SELECT result, or -1 if it cannot be determined or if the query is not a SELECT statement.
		"""
		res = super(QSqlResult,self).size()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def addBindValue(self,val,type):
		"""
		addBindValue(val,type)
			val=object
			type=QtSql.QSql.ParamType


		"""
		res = super(QSqlResult,self).addBindValue(val,type)
		return res
	#----------------------------------------------------------------------
	def bindValue(self,*args,**kwargs):
		"""
		bindValue(placeholder,val,type)
			placeholder=unicode
			val=object
			type=QtSql.QSql.ParamType

		bindValue(pos,val,type)
			pos=QtCore.int
			val=object
			type=QtSql.QSql.ParamType


		"""
		res = super(QSqlResult,self).bindValue(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def bindValueType(self,*args,**kwargs):
		"""
		bindValueType(pos)
			pos=QtCore.int

		bindValueType(placeholder)
			placeholder=unicode

		Returns the parameter type for the value bound at position index .
		"""
		res = super(QSqlResult,self).bindValueType(*args,**kwargs)
		isinstance(res,QtSql.QSql.ParamType)
		return res
	#----------------------------------------------------------------------
	def boundValue(self,*args,**kwargs):
		"""
		boundValue(pos)
			pos=QtCore.int

		boundValue(placeholder)
			placeholder=unicode

		Returns the value bound at position index in the current record (row).
		"""
		res = super(QSqlResult,self).boundValue(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def boundValueName(self,pos):
		"""
		boundValueName(pos)
			pos=QtCore.int

		Returns the name of the bound value at position index in the current record (row).
		"""
		res = super(QSqlResult,self).boundValueName(pos)
		return res
	#----------------------------------------------------------------------
	def data(self,i):
		"""
		data(i)
			i=QtCore.int

		Returns the data for field index in the current row as a PySide.QtCore.QVariant
		This function is only called if the result is in an active state and is positioned on a valid record and index is non-negative
		Derived classes must reimplement this function and return the value of field index , or QVariant() if it cannot be determined.
		"""
		res = super(QSqlResult,self).data(i)
		return res
	#----------------------------------------------------------------------
	def execBatch(self,arrayBind=None):
		"""
		execBatch(arrayBind=None)
			arrayBind=QtCore.bool

		Executes a prepared query in batch mode if the driver supports it, otherwise emulates a batch execution using PySide.QtSql.QSqlResult.bindValue() and exec()
		QSqlDriver.hasFeature() can be used to find out whether a driver supports batch execution.
		Batch execution can be faster for large amounts of data since it reduces network roundtrips.
		For batch executions, bound values have to be provided as lists of variants ( QVariantList ).
		Each list must contain values of the same type
		All lists must contain equal amount of values (rows).
		NULL values are passed in as typed QVariants , for example QVariant(QVariant::Int) for an integer NULL value.
		Example:
		Here, we insert two rows into a SQL table, with each row containing three values.
		"""
		res = super(QSqlResult,self).execBatch(arrayBind)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def fetch(self,i):
		"""
		fetch(i)
			i=QtCore.int

		Positions the result to an arbitrary (zero-based) row index .
		This function is only called if the result is in an active state
		Derived classes must reimplement this function and position the result to the row index , and call PySide.QtSql.QSqlResult.setAt() with an appropriate value
		Return true to indicate success, or false to signify failure.
		"""
		res = super(QSqlResult,self).fetch(i)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isNull(self,i):
		"""
		isNull(i)
			i=QtCore.int

		Returns true if the field at position index in the current row is null; otherwise returns false.
		"""
		res = super(QSqlResult,self).isNull(i)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def prepare(self,query):
		"""
		prepare(query)
			query=unicode

		Prepares the given query for execution; the query will normally use placeholders so that it can be executed repeatedly
		Returns true if the query is prepared successfully; otherwise returns false.
		"""
		res = super(QSqlResult,self).prepare(query)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def reset(self,sqlquery):
		"""
		reset(sqlquery)
			sqlquery=unicode

		Sets the result to use the SQL statement query for subsequent data retrieval.
		Derived classes must reimplement this function and apply the query to the database
		This function is only called after the result is set to an inactive state and is positioned before the first record of the new result
		Derived classes should return true if the query was successful and ready to be used, or false otherwise.
		"""
		res = super(QSqlResult,self).reset(sqlquery)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def savePrepare(self,sqlquery):
		"""
		savePrepare(sqlquery)
			sqlquery=unicode

		Prepares the given query , using the underlying database functionality where possible
		Returns true if the query is prepared successfully; otherwise returns false.
		"""
		res = super(QSqlResult,self).savePrepare(sqlquery)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setActive(self,a):
		"""
		setActive(a)
			a=QtCore.bool

		This function is provided for derived classes to set the internal active state to active .
		"""
		res = super(QSqlResult,self).setActive(a)
		return res
	#----------------------------------------------------------------------
	def setAt(self,at):
		"""
		setAt(at)
			at=QtCore.int

		This function is provided for derived classes to set the internal (zero-based) row position to index .
		"""
		res = super(QSqlResult,self).setAt(at)
		return res
	#----------------------------------------------------------------------
	def setForwardOnly(self,forward):
		"""
		setForwardOnly(forward)
			forward=QtCore.bool

		Sets forward only mode to forward
		If forward is true, only PySide.QtSql.QSqlResult.fetchNext() is allowed for navigating the results
		Forward only mode needs much less memory since results do not have to be cached
		By default, this feature is disabled.
		Setting forward only to false is a suggestion to the database engine, which has the final say on whether a result set is forward only or scrollable
		PySide.QtSql.QSqlResult.isForwardOnly() will always return the correct status of the result set.
		"""
		res = super(QSqlResult,self).setForwardOnly(forward)
		return res
	#----------------------------------------------------------------------
	def setLastError(self,e):
		"""
		setLastError(e)
			e=QtSql.QSqlError

		This function is provided for derived classes to set the last error to error .
		"""
		res = super(QSqlResult,self).setLastError(e)
		return res
	#----------------------------------------------------------------------
	def setNumericalPrecisionPolicy(self,policy):
		"""
		setNumericalPrecisionPolicy(policy)
			policy=QtSql.QSql.NumericalPrecisionPolicy


		"""
		res = super(QSqlResult,self).setNumericalPrecisionPolicy(policy)
		return res
	#----------------------------------------------------------------------
	def setQuery(self,query):
		"""
		setQuery(query)
			query=unicode

		Sets the current query for the result to query
		You must call PySide.QtSql.QSqlResult.reset() to execute the query on the database.
		"""
		res = super(QSqlResult,self).setQuery(query)
		return res
	#----------------------------------------------------------------------
	def setSelect(self,s):
		"""
		setSelect(s)
			s=QtCore.bool

		This function is provided for derived classes to indicate whether or not the current statement is a SQL SELECT statement
		The select parameter should be true if the statement is a SELECT statement; otherwise it should be false.
		"""
		res = super(QSqlResult,self).setSelect(s)
		return res

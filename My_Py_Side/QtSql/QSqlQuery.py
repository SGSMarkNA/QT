from PySide import QtGui, QtCore

class QSqlQuery(QtSql.QSqlQuery):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSqlQuery,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def at(self):
		"""
		Returns the current internal position of the query
		The first record is at position zero
		If the position is invalid, the function returns QSql.BeforeFirstRow or QSql.AfterLastRow , which are special negative values.
		"""
		res = super(QSqlQuery,self).at()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def boundValues(self):
		"""
		Returns a map of the bound values.
		With named binding, the bound values can be examined in the following ways:
		With positional binding, the code becomes:
		"""
		res = super(QSqlQuery,self).boundValues()
		return res
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Clears the result set and releases any resources held by the query
		Sets the query state to inactive
		You should rarely if ever need to call this function.
		"""
		res = super(QSqlQuery,self).clear()
		return res
	#----------------------------------------------------------------------
	def driver(self):
		"""
		Returns the database driver associated with the query.
		"""
		res = super(QSqlQuery,self).driver()
		isinstance(res,QtSql.QSqlDriver)
		return res
	#----------------------------------------------------------------------
	def exec_(self):
		"""
		Executes a previously prepared SQL query
		Returns true if the query executed successfully; otherwise returns false.
		Note that the last error for this query is reset when exec() is called.
		"""
		res = super(QSqlQuery,self).exec_()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def executedQuery(self):
		"""
		Returns the last query that was successfully executed.
		In most cases this function returns the same string as PySide.QtSql.QSqlQuery.lastQuery()
		If a prepared query with placeholders is executed on a DBMS that does not support it, the preparation of this query is emulated
		The placeholders in the original query are replaced with their bound values to form a new query
		This function returns the modified query
		It is mostly useful for debugging purposes.
		"""
		res = super(QSqlQuery,self).executedQuery()
		return res
	#----------------------------------------------------------------------
	def finish(self):
		"""
		Instruct the database driver that no more data will be fetched from this query until it is re-executed
		There is normally no need to call this function, but it may be helpful in order to free resources such as locks or cursors if you intend to re-use the query at a later time.
		Sets the query to inactive
		Bound values retain their values.
		"""
		res = super(QSqlQuery,self).finish()
		return res
	#----------------------------------------------------------------------
	def first(self):
		"""
		Retrieves the first record in the result, if available, and positions the query on the retrieved record
		Note that the result must be in the active state and PySide.QtSql.QSqlQuery.isSelect() must return true before calling this function or it will do nothing and return false
		Returns true if successful
		If unsuccessful the query position is set to an invalid position and false is returned.
		"""
		res = super(QSqlQuery,self).first()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isActive(self):
		"""
		Returns true if the query is active
		An active PySide.QtSql.QSqlQuery is one that has been exec()'d successfully but not yet finished with
		When you are finished with an active query, you can make make the query inactive by calling PySide.QtSql.QSqlQuery.finish() or PySide.QtSql.QSqlQuery.clear() , or you can delete the PySide.QtSql.QSqlQuery instance.
		"""
		res = super(QSqlQuery,self).isActive()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isForwardOnly(self):
		"""
		Returns true if you can only scroll forward through a result set; otherwise returns false.
		"""
		res = super(QSqlQuery,self).isForwardOnly()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isSelect(self):
		"""
		Returns true if the current query is a SELECT statement; otherwise returns false.
		"""
		res = super(QSqlQuery,self).isSelect()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if the query is currently positioned on a valid record; otherwise returns false.
		"""
		res = super(QSqlQuery,self).isValid()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def last(self):
		"""
		Retrieves the last record in the result, if available, and positions the query on the retrieved record
		Note that the result must be in the active state and PySide.QtSql.QSqlQuery.isSelect() must return true before calling this function or it will do nothing and return false
		Returns true if successful
		If unsuccessful the query position is set to an invalid position and false is returned.
		"""
		res = super(QSqlQuery,self).last()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def lastError(self):
		"""
		Returns error information about the last error (if any) that occurred with this query.
		"""
		res = super(QSqlQuery,self).lastError()
		isinstance(res,QtSql.QSqlError)
		return res
	#----------------------------------------------------------------------
	def lastInsertId(self):
		"""
		Returns the object ID of the most recent inserted row if the database supports it
		An invalid PySide.QtCore.QVariant will be returned if the query did not insert any value or if the database does not report the id back
		If more than one row was touched by the insert, the behavior is undefined.
		For MySQL databases the rows auto-increment field will be returned.
		"""
		res = super(QSqlQuery,self).lastInsertId()
		return res
	#----------------------------------------------------------------------
	def lastQuery(self):
		"""
		Returns the text of the current query being used, or an empty string if there is no current query text.
		"""
		res = super(QSqlQuery,self).lastQuery()
		return res
	#----------------------------------------------------------------------
	def next(self):
		"""
		Retrieves the next record in the result, if available, and positions the query on the retrieved record
		Note that the result must be in the active state and PySide.QtSql.QSqlQuery.isSelect() must return true before calling this function or it will do nothing and return false.
		The following rules apply:
		If the record could not be retrieved, the result is positioned after the last record and false is returned
		If the record is successfully retrieved, true is returned.
		"""
		res = super(QSqlQuery,self).next()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def nextResult(self):
		"""
		Discards the current result set and navigates to the next if available.
		Some databases are capable of returning multiple result sets for stored procedures or SQL batches (a query strings that contains multiple statements)
		If multiple result sets are available after executing a query this function can be used to navigate to the next result set(s).
		If a new result set is available this function will return true
		The query will be repositioned on an invalid record in the new result set and must be navigated to a valid record before data values can be retrieved
		If a new result set isnt available the function returns false and the query is set to inactive
		In any case the old result set will be discarded.
		When one of the statements is a non-select statement a count of affected rows may be available instead of a result set.
		Note that some databases, i.e
		Microsoft SQL Server, requires non-scrollable cursors when working with multiple result sets
		Some databases may execute all statements at once while others may delay the execution until the result set is actually accessed, and some databases may have restrictions on which statements are allowed to be used in a SQL batch.
		"""
		res = super(QSqlQuery,self).nextResult()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def numRowsAffected(self):
		"""
		Returns the number of rows affected by the results SQL statement, or -1 if it cannot be determined
		Note that for SELECT statements, the value is undefined; use PySide.QtSql.QSqlQuery.size() instead
		If the query is not active , -1 is returned.
		"""
		res = super(QSqlQuery,self).numRowsAffected()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def numericalPrecisionPolicy(self):
		"""
		Returns the current precision policy.
		"""
		res = super(QSqlQuery,self).numericalPrecisionPolicy()
		isinstance(res,QtSql.QSql.NumericalPrecisionPolicy)
		return res
	#----------------------------------------------------------------------
	def previous(self):
		"""
		Retrieves the previous record in the result, if available, and positions the query on the retrieved record
		Note that the result must be in the active state and PySide.QtSql.QSqlQuery.isSelect() must return true before calling this function or it will do nothing and return false.
		The following rules apply:
		If the record could not be retrieved, the result is positioned before the first record and false is returned
		If the record is successfully retrieved, true is returned.
		"""
		res = super(QSqlQuery,self).previous()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def record(self):
		"""
		Returns a PySide.QtSql.QSqlRecord containing the field information for the current query
		If the query points to a valid row ( PySide.QtSql.QSqlQuery.isValid() returns true), the record is populated with the rows values
		An empty record is returned when there is no active query ( PySide.QtSql.QSqlQuery.isActive() returns false).
		To retrieve values from a query, PySide.QtSql.QSqlQuery.value() should be used since its index-based lookup is faster.
		In the following example, a SELECT * FROM query is executed
		Since the order of the columns is not defined, QSqlRecord.indexOf() is used to obtain the index of a column.
		"""
		res = super(QSqlQuery,self).record()
		isinstance(res,QtSql.QSqlRecord)
		return res
	#----------------------------------------------------------------------
	def result(self):
		"""
		Returns the result associated with the query.
		"""
		res = super(QSqlQuery,self).result()
		isinstance(res,QtSql.QSqlResult)
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""
		Returns the size of the result (number of rows returned), or -1 if the size cannot be determined or if the database does not support reporting information about query sizes
		Note that for non-SELECT statements ( PySide.QtSql.QSqlQuery.isSelect() returns false), PySide.QtSql.QSqlQuery.size() will return -1
		If the query is not active ( PySide.QtSql.QSqlQuery.isActive() returns false), -1 is returned.
		To determine the number of rows affected by a non-SELECT statement, use PySide.QtSql.QSqlQuery.numRowsAffected() .
		"""
		res = super(QSqlQuery,self).size()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def addBindValue(self,val,type=None):
		"""
		addBindValue(val,type=None)
			val=object
			type=QtSql.QSql.ParamType


		"""
		res = super(QSqlQuery,self).addBindValue(val,type)
		return res
	#----------------------------------------------------------------------
	def bindValue(self,*args,**kwargs):
		"""
		bindValue(placeholder,val,type=None)
			placeholder=unicode
			val=object
			type=QtSql.QSql.ParamType

		bindValue(pos,val,type=None)
			pos=QtCore.int
			val=object
			type=QtSql.QSql.ParamType


		"""
		res = super(QSqlQuery,self).bindValue(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def boundValue(self,*args,**kwargs):
		"""
		boundValue(placeholder)
			placeholder=unicode

		boundValue(pos)
			pos=QtCore.int

		Returns the value for the placeholder .
		"""
		res = super(QSqlQuery,self).boundValue(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def execBatch(self,mode=None):
		"""
		execBatch(mode=None)
			mode=QtSql.QSqlQuery.BatchExecutionMode

		Executes a previously prepared SQL query in a batch
		All the bound parameters have to be lists of variants
		If the database doesnt support batch executions, the driver will simulate it using conventional exec() calls.
		Returns true if the query is executed successfully; otherwise returns false.
		Example:
		The example above inserts four new rows into myTable :
		To bind NULL values, a null PySide.QtCore.QVariant of the relevant type has to be added to the bound QVariantList ; for example, QVariant(QVariant::String) should be used if you are using strings.
		The mode parameter indicates how the bound QVariantList will be interpreted
		If mode is ValuesAsRows , every variant within the QVariantList will be interpreted as a value for a new row
		ValuesAsColumns is a special case for the Oracle driver
		In this mode, every entry within a QVariantList will be interpreted as array-value for an IN or OUT value within a stored procedure
		Note that this will only work if the IN or OUT value is a table-type consisting of only one column of a basic type, for example TYPE myType IS TABLE OF VARCHAR(64) INDEX BY BINARY_INTEGER;
		"""
		res = super(QSqlQuery,self).execBatch(mode)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def exec_(self,query):
		"""
		exec_(query)
			query=unicode

		Executes the SQL in query
		Returns true and sets the query state to active if the query was successful; otherwise returns false
		The query string must use syntax appropriate for the SQL database being queried (for example, standard SQL).
		After the query is executed, the query is positioned on an invalid record and must be navigated to a valid record before data values can be retrieved (for example, using PySide.QtSql.QSqlQuery.next() ).
		Note that the last error for this query is reset when exec() is called.
		Example:
		"""
		res = super(QSqlQuery,self).exec_(query)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isNull(self,field):
		"""
		isNull(field)
			field=QtCore.int

		Returns true if the query is active and positioned on a valid record and the field is NULL; otherwise returns false
		Note that for some drivers, PySide.QtSql.QSqlQuery.isNull() will not return accurate information until after an attempt is made to retrieve data.
		"""
		res = super(QSqlQuery,self).isNull(field)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def prepare(self,query):
		"""
		prepare(query)
			query=unicode

		Prepares the SQL query query for execution
		Returns true if the query is prepared successfully; otherwise returns false.
		The query may contain placeholders for binding values
		Both Oracle style colon-name (e.g., :surname ), and ODBC style (? ) placeholders are supported; but they cannot be mixed in the same query
		See the Detailed Description for examples.
		Portability note: Some databases choose to delay preparing a query until it is executed the first time
		In this case, preparing a syntactically wrong query succeeds, but every consecutive exec() will fail.
		Example:
		"""
		res = super(QSqlQuery,self).prepare(query)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def seek(self,i,relative=None):
		"""
		seek(i,relative=None)
			i=QtCore.int
			relative=QtCore.bool

		Retrieves the record at position index , if available, and positions the query on the retrieved record
		The first record is at position 0
		Note that the query must be in an active state and PySide.QtSql.QSqlQuery.isSelect() must return true before calling this function.
		If relative is false (the default), the following rules apply:
		If relative is true, the following rules apply:
		"""
		res = super(QSqlQuery,self).seek(i,relative)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setForwardOnly(self,forward):
		"""
		setForwardOnly(forward)
			forward=QtCore.bool

		Sets forward only mode to forward
		If forward is true, only PySide.QtSql.QSqlQuery.next() and PySide.QtSql.QSqlQuery.seek() with positive values, are allowed for navigating the results.
		Forward only mode can be (depending on the driver) more memory efficient since results do not need to be cached
		It will also improve performance on some databases
		For this to be true, you must call setForwardOnly() before the query is prepared or executed
		Note that the constructor that takes a query and a database may execute the query.
		Forward only mode is off by default.
		Setting forward only to false is a suggestion to the database engine, which has the final say on whether a result set is forward only or scrollable
		PySide.QtSql.QSqlQuery.isForwardOnly() will always return the correct status of the result set.
		"""
		res = super(QSqlQuery,self).setForwardOnly(forward)
		return res
	#----------------------------------------------------------------------
	def setNumericalPrecisionPolicy(self,precisionPolicy):
		"""
		setNumericalPrecisionPolicy(precisionPolicy)
			precisionPolicy=QtSql.QSql.NumericalPrecisionPolicy


		"""
		res = super(QSqlQuery,self).setNumericalPrecisionPolicy(precisionPolicy)
		return res
	#----------------------------------------------------------------------
	def value(self,i):
		"""
		value(i)
			i=QtCore.int

		Returns the value of field index in the current record.
		The fields are numbered from left to right using the text of the SELECT statement, e.g
		in
		field 0 is forename and field 1 is surname
		Using SELECT * is not recommended because the order of the fields in the query is undefined.
		An invalid PySide.QtCore.QVariant is returned if field index does not exist, if the query is inactive, or if the query is positioned on an invalid record.
		"""
		res = super(QSqlQuery,self).value(i)
		return res

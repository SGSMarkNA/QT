from PySide import QtGui, QtCore

class QSqlQueryModel(QtSql.QSqlQueryModel):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSqlQueryModel,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Clears the model and releases any acquired resource.
		"""
		res = super(QSqlQueryModel,self).clear()
		return res
	#----------------------------------------------------------------------
	def lastError(self):
		"""
		Returns information about the last error that occurred on the database.
		"""
		res = super(QSqlQueryModel,self).lastError()
		isinstance(res,QtSql.QSqlError)
		return res
	#----------------------------------------------------------------------
	def query(self):
		"""
		Returns the PySide.QtSql.QSqlQuery associated with this model.
		"""
		res = super(QSqlQueryModel,self).query()
		isinstance(res,QtSql.QSqlQuery)
		return res
	#----------------------------------------------------------------------
	def queryChange(self):
		"""
		This virtual function is called whenever the query changes
		The default implementation does nothing.
		PySide.QtSql.QSqlQueryModel.query() returns the new query.
		"""
		res = super(QSqlQueryModel,self).queryChange()
		return res
	#----------------------------------------------------------------------
	def record(self):
		"""
		This is an overloaded function.
		Returns an empty record containing information about the fields of the current query.
		If the model is not initialized, an empty record will be returned.
		"""
		res = super(QSqlQueryModel,self).record()
		isinstance(res,QtSql.QSqlRecord)
		return res
	#----------------------------------------------------------------------
	def indexInQuery(self,item):
		"""
		indexInQuery(item)
			item=QtCore.QModelIndex

		Returns the index of the value in the database result set for the given item in the model.
		The return value is identical to item if no columns or rows have been inserted, removed, or moved around.
		Returns an invalid model index if item is out of bounds or if item does not point to a value in the result set.
		"""
		res = super(QSqlQueryModel,self).indexInQuery(item)
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def record(self,row):
		"""
		record(row)
			row=QtCore.int

		Returns the record containing information about the fields of the current query
		If row is the index of a valid row, the record will be populated with values from that row.
		If the model is not initialized, an empty record will be returned.
		"""
		res = super(QSqlQueryModel,self).record(row)
		isinstance(res,QtSql.QSqlRecord)
		return res
	#----------------------------------------------------------------------
	def setLastError(self,error):
		"""
		setLastError(error)
			error=QtSql.QSqlError

		Protected function which allows derived classes to set the value of the last error that occurred on the database to error .
		"""
		res = super(QSqlQueryModel,self).setLastError(error)
		return res
	#----------------------------------------------------------------------
	def setQuery(self,*args,**kwargs):
		"""
		setQuery(query)
			query=QtSql.QSqlQuery

		setQuery(query,db=None)
			query=unicode
			db=QtSql.QSqlDatabase

		Resets the model and sets the data provider to be the given query
		Note that the query must be active and must not be isForwardOnly().
		PySide.QtSql.QSqlQueryModel.lastError() can be used to retrieve verbose information if there was an error setting the query.
		"""
		res = super(QSqlQueryModel,self).setQuery(*args,**kwargs)
		return res

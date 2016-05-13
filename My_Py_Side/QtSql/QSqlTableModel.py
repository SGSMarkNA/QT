from PySide import QtGui, QtCore

class QSqlTableModel(QtSql.QSqlTableModel):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSqlTableModel,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def database(self):
		"""
		Returns a pointer to the used PySide.QtSql.QSqlDatabase or 0 if no database was set.
		"""
		res = super(QSqlTableModel,self).database()
		isinstance(res,QtSql.QSqlDatabase)
		return res
	#----------------------------------------------------------------------
	def editStrategy(self):
		"""
		Returns the current edit strategy.
		"""
		res = super(QSqlTableModel,self).editStrategy()
		isinstance(res,QtSql.QSqlTableModel.EditStrategy)
		return res
	#----------------------------------------------------------------------
	def filter(self):
		"""
		Returns the currently set filter.
		"""
		res = super(QSqlTableModel,self).filter()
		return res
	#----------------------------------------------------------------------
	def orderByClause(self):
		"""
		Returns an SQL ORDER BY clause based on the currently set sort order.
		"""
		res = super(QSqlTableModel,self).orderByClause()
		return res
	#----------------------------------------------------------------------
	def primaryKey(self):
		"""
		Returns the primary key for the current table, or an empty PySide.QtSql.QSqlIndex if the table is not set or has no primary key.
		"""
		res = super(QSqlTableModel,self).primaryKey()
		isinstance(res,QtSql.QSqlIndex)
		return res
	#----------------------------------------------------------------------
	def select(self):
		"""
		Populates the model with data from the table that was set via PySide.QtSql.QSqlTableModel.setTable() , using the specified filter and sort condition, and returns true if successful; otherwise returns false.
		"""
		res = super(QSqlTableModel,self).select()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def selectStatement(self):
		"""
		Returns the SQL SELECT statement used internally to populate the model
		The statement includes the filter and the ORDER BY clause.
		"""
		res = super(QSqlTableModel,self).selectStatement()
		return res
	#----------------------------------------------------------------------
	def tableName(self):
		"""
		Returns the name of the currently selected table.
		"""
		res = super(QSqlTableModel,self).tableName()
		return res
	#----------------------------------------------------------------------
	def deleteRowFromTable(self,row):
		"""
		deleteRowFromTable(row)
			row=QtCore.int

		Deletes the given row from the currently active database table.
		This is a low-level method that operates directly on the database and should not be called directly
		Use PySide.QtCore.QAbstractItemModel.removeRow() or PySide.QtSql.QSqlTableModel.removeRows() to delete values
		The model will decide depending on its edit strategy when to modify the database.
		Returns true if the row was deleted; otherwise returns false.
		"""
		res = super(QSqlTableModel,self).deleteRowFromTable(row)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def fieldIndex(self,fieldName):
		"""
		fieldIndex(fieldName)
			fieldName=unicode

		Returns the index of the field fieldName .
		"""
		res = super(QSqlTableModel,self).fieldIndex(fieldName)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def insertRecord(self,row,record):
		"""
		insertRecord(row,record)
			row=QtCore.int
			record=QtSql.QSqlRecord

		Inserts the record after row
		If row is negative, the record will be appended to the end
		Calls PySide.QtSql.QSqlTableModel.insertRows() and PySide.QtSql.QSqlTableModel.setRecord() internally.
		Returns true if the row could be inserted, otherwise false.
		"""
		res = super(QSqlTableModel,self).insertRecord(row,record)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def insertRowIntoTable(self,values):
		"""
		insertRowIntoTable(values)
			values=QtSql.QSqlRecord

		Inserts the values values into the currently active database table.
		This is a low-level method that operates directly on the database and should not be called directly
		Use PySide.QtCore.QAbstractItemModel.insertRow() and PySide.QtSql.QSqlTableModel.setData() to insert values
		The model will decide depending on its edit strategy when to modify the database.
		Returns true if the values could be inserted, otherwise false
		Error information can be retrieved with PySide.QtSql.QSqlQueryModel.lastError() .
		"""
		res = super(QSqlTableModel,self).insertRowIntoTable(values)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isDirty(self,index):
		"""
		isDirty(index)
			index=QtCore.QModelIndex

		Returns true if the value at the index index is dirty, otherwise false
		Dirty values are values that were modified in the model but not yet written into the database.
		If index is invalid or points to a non-existing row, false is returned.
		"""
		res = super(QSqlTableModel,self).isDirty(index)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def revertRow(self,row):
		"""
		revertRow(row)
			row=QtCore.int

		Reverts all changes for the specified row .
		"""
		res = super(QSqlTableModel,self).revertRow(row)
		return res
	#----------------------------------------------------------------------
	def setEditStrategy(self,strategy):
		"""
		setEditStrategy(strategy)
			strategy=QtSql.QSqlTableModel.EditStrategy

		Sets the strategy for editing values in the database to strategy .
		This will revert any pending changes.
		"""
		res = super(QSqlTableModel,self).setEditStrategy(strategy)
		return res
	#----------------------------------------------------------------------
	def setFilter(self,filter):
		"""
		setFilter(filter)
			filter=unicode

		Sets the current filter to filter .
		The filter is a SQL WHERE clause without the keyword WHERE (for example, name='Josephine') .
		If the model is already populated with data from a database, the model re-selects it with the new filter
		Otherwise, the filter will be applied the next time PySide.QtSql.QSqlTableModel.select() is called.
		"""
		res = super(QSqlTableModel,self).setFilter(filter)
		return res
	#----------------------------------------------------------------------
	def setPrimaryKey(self,key):
		"""
		setPrimaryKey(key)
			key=QtSql.QSqlIndex

		Protected method that allows subclasses to set the primary key to key .
		Normally, the primary index is set automatically whenever you call PySide.QtSql.QSqlTableModel.setTable() .
		"""
		res = super(QSqlTableModel,self).setPrimaryKey(key)
		return res
	#----------------------------------------------------------------------
	def setRecord(self,row,record):
		"""
		setRecord(row,record)
			row=QtCore.int
			record=QtSql.QSqlRecord

		Sets the values at the specified row to the values of record
		Returns true if all the values could be set; otherwise returns false.
		"""
		res = super(QSqlTableModel,self).setRecord(row,record)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def setSort(self,column,order):
		"""
		setSort(column,order)
			column=QtCore.int
			order=QtCore.Qt.SortOrder


		"""
		res = super(QSqlTableModel,self).setSort(column,order)
		return res
	#----------------------------------------------------------------------
	def setTable(self,tableName):
		"""
		setTable(tableName)
			tableName=unicode

		Sets the database table on which the model operates to tableName
		Does not select data from the table, but fetches its field information.
		To populate the model with the tables data, call PySide.QtSql.QSqlTableModel.select() .
		Error information can be retrieved with PySide.QtSql.QSqlQueryModel.lastError() .
		"""
		res = super(QSqlTableModel,self).setTable(tableName)
		return res
	#----------------------------------------------------------------------
	def updateRowInTable(self,row,values):
		"""
		updateRowInTable(row,values)
			row=QtCore.int
			values=QtSql.QSqlRecord

		Updates the given row in the currently active database table with the specified values
		Returns true if successful; otherwise returns false.
		This is a low-level method that operates directly on the database and should not be called directly
		Use PySide.QtSql.QSqlTableModel.setData() to update values
		The model will decide depending on its edit strategy when to modify the database.
		Note that only values that have the generated-flag set are updated
		The generated-flag can be set with QSqlRecord.setGenerated() and tested with QSqlRecord.isGenerated() .
		"""
		res = super(QSqlTableModel,self).updateRowInTable(row,values)
		isinstance(res,QtCore.bool)
		return res

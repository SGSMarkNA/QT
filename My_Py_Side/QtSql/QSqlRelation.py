from PySide import QtGui, QtCore

class QSqlRelation(QtSql.QSqlRelation):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSqlRelation,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def displayColumn(self):
		"""
		Returns the column from table PySide.QtSql.QSqlRelation.tableName() that should be presented to the user instead of a foreign key.
		"""
		res = super(QSqlRelation,self).displayColumn()
		return res
	#----------------------------------------------------------------------
	def indexColumn(self):
		"""
		Returns the index column from table PySide.QtSql.QSqlRelation.tableName() to which a foreign key refers.
		"""
		res = super(QSqlRelation,self).indexColumn()
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if the PySide.QtSql.QSqlRelation object is valid; otherwise returns false.
		"""
		res = super(QSqlRelation,self).isValid()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def tableName(self):
		"""
		Returns the name of the table to which a foreign key refers.
		"""
		res = super(QSqlRelation,self).tableName()
		return res

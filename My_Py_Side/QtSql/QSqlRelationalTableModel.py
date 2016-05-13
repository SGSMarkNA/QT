from PySide import QtGui, QtCore

class QSqlRelationalTableModel(QtSql.QSqlRelationalTableModel):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSqlRelationalTableModel,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def relation(self,column):
		"""
		relation(column)
			column=QtCore.int

		Returns the relation for the column column , or an invalid relation if no relation is set.
		"""
		res = super(QSqlRelationalTableModel,self).relation(column)
		isinstance(res,QtSql.QSqlRelation)
		return res
	#----------------------------------------------------------------------
	def relationModel(self,column):
		"""
		relationModel(column)
			column=QtCore.int

		Returns a PySide.QtSql.QSqlTableModel object for accessing the table for which column is a foreign key, or 0 if there is no relation for the given column .
		The returned object is owned by the PySide.QtSql.QSqlRelationalTableModel .
		"""
		res = super(QSqlRelationalTableModel,self).relationModel(column)
		isinstance(res,QtSql.QSqlTableModel)
		return res
	#----------------------------------------------------------------------
	def setRelation(self,column,relation):
		"""
		setRelation(column,relation)
			column=QtCore.int
			relation=QtSql.QSqlRelation

		Lets the specified column be a foreign index specified by relation .
		Example:
		The PySide.QtSql.QSqlRelationalTableModel.setRelation() call specifies that column 2 in table employee is a foreign key that maps with field id of table city , and that the view should present the city s name field to the user.
		Note: The tables primary key may not contain a relation to another table.
		"""
		res = super(QSqlRelationalTableModel,self).setRelation(column,relation)
		return res

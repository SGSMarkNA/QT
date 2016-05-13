from PySide import QtGui, QtCore

class QWebDatabase(QtWebKit.QWebDatabase):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QWebDatabase,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def displayName(self):
		"""
		Returns the name of the database in a format that is suitable for display to the user.
		"""
		res = super(QWebDatabase,self).displayName()
		return res
	#----------------------------------------------------------------------
	def expectedSize(self):
		"""
		Returns the expected size of the database in bytes as defined by the web author.
		"""
		res = super(QWebDatabase,self).expectedSize()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def fileName(self):
		"""
		Returns the file name of the web database.
		The name can be used to access the database through the QtSql database module, for example:
		"""
		res = super(QWebDatabase,self).fileName()
		return res
	#----------------------------------------------------------------------
	def name(self):
		"""
		Returns the name of the database.
		"""
		res = super(QWebDatabase,self).name()
		return res
	#----------------------------------------------------------------------
	def origin(self):
		"""
		Returns the databasess security origin.
		"""
		res = super(QWebDatabase,self).origin()
		isinstance(res,QtWebKit.QWebSecurityOrigin)
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""
		Returns the current size of the database in bytes.
		"""
		res = super(QWebDatabase,self).size()
		isinstance(res,QtCore.qint64)
		return res

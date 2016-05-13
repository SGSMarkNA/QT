from PySide import QtGui, QtCore

class QWebSecurityOrigin(QtWebKit.QWebSecurityOrigin):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QWebSecurityOrigin,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def databaseQuota(self):
		"""
		Returns the quota for the databases in the security origin.
		"""
		res = super(QWebSecurityOrigin,self).databaseQuota()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def databaseUsage(self):
		"""
		Returns the number of bytes all databases in the security origin use on the disk.
		"""
		res = super(QWebSecurityOrigin,self).databaseUsage()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def databases(self):
		"""
		Returns a list of all databases defined in the security origin.
		"""
		res = super(QWebSecurityOrigin,self).databases()
		return res
	#----------------------------------------------------------------------
	def host(self):
		"""
		Returns the host name defining the security origin.
		"""
		res = super(QWebSecurityOrigin,self).host()
		return res
	#----------------------------------------------------------------------
	def port(self):
		"""
		Returns the port number defining the security origin.
		"""
		res = super(QWebSecurityOrigin,self).port()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def scheme(self):
		"""
		Returns the scheme defining the security origin.
		"""
		res = super(QWebSecurityOrigin,self).scheme()
		return res
	#----------------------------------------------------------------------
	def setDatabaseQuota(self,quota):
		"""
		setDatabaseQuota(quota)
			quota=QtCore.qint64

		Sets the quota for the databases in the security origin to quota bytes.
		If the quota is set to a value less than the current usage, the quota will remain and no data will be purged to meet the new quota
		However, no new data can be added to databases in this origin.
		"""
		res = super(QWebSecurityOrigin,self).setDatabaseQuota(quota)
		return res

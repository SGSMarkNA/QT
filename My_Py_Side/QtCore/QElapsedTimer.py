from PySide import QtGui, QtCore

class QElapsedTimer(QtCore.QElapsedTimer):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QElapsedTimer,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def elapsed(self):
		"""

		"""
		res = super(QElapsedTimer,self).elapsed()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def invalidate(self):
		"""

		"""
		res = super(QElapsedTimer,self).invalidate()
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""

		"""
		res = super(QElapsedTimer,self).isValid()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def msecsSinceReference(self):
		"""

		"""
		res = super(QElapsedTimer,self).msecsSinceReference()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def restart(self):
		"""

		"""
		res = super(QElapsedTimer,self).restart()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def start(self):
		"""

		"""
		res = super(QElapsedTimer,self).start()
		return res
	#----------------------------------------------------------------------
	def hasExpired(self,timeout):
		"""
		hasExpired(timeout)
			timeout=QtCore.qint64


		"""
		res = super(QElapsedTimer,self).hasExpired(timeout)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def msecsTo(self,other):
		"""
		msecsTo(other)
			other=QtCore.QElapsedTimer


		"""
		res = super(QElapsedTimer,self).msecsTo(other)
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtCore.QElapsedTimer


		"""
		res = super(QElapsedTimer,self).__ne__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtCore.QElapsedTimer


		"""
		res = super(QElapsedTimer,self).__eq__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def secsTo(self,other):
		"""
		secsTo(other)
			other=QtCore.QElapsedTimer


		"""
		res = super(QElapsedTimer,self).secsTo(other)
		isinstance(res,QtCore.qint64)
		return res

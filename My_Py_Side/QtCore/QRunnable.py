from PySide import QtGui, QtCore

class QRunnable(QtCore.QRunnable):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QRunnable,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def autoDelete(self):
		"""
		Returns true is auto-deletion is enabled; false otherwise.
		If auto-deletion is enabled, PySide.QtCore.QThreadPool will automatically delete this runnable after calling PySide.QtCore.QRunnable.run() ; otherwise, ownership remains with the application programmer.
		"""
		res = super(QRunnable,self).autoDelete()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def run(self):
		"""
		Implement this pure virtual function in your subclass.
		"""
		res = super(QRunnable,self).run()
		return res
	#----------------------------------------------------------------------
	def setAutoDelete(self,_autoDelete):
		"""
		setAutoDelete(_autoDelete)
			_autoDelete=QtCore.bool

		Enables auto-deletion if autoDelete is true; otherwise auto-deletion is disabled.
		If auto-deletion is enabled, PySide.QtCore.QThreadPool will automatically delete this runnable after calling PySide.QtCore.QRunnable.run() ; otherwise, ownership remains with the application programmer.
		Note that this flag must be set before calling QThreadPool.start()
		Calling this function after QThreadPool.start() results in undefined behavior.
		"""
		res = super(QRunnable,self).setAutoDelete(_autoDelete)
		return res

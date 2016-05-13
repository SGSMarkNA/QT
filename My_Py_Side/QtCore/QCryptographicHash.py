from PySide import QtGui, QtCore

class QCryptographicHash(QtCore.QCryptographicHash):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QCryptographicHash,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def reset(self):
		"""
		Resets the object.
		"""
		res = super(QCryptographicHash,self).reset()
		return res
	#----------------------------------------------------------------------
	def result(self):
		"""
		Returns the final hash value.
		"""
		res = super(QCryptographicHash,self).result()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def addData(self,*args,**kwargs):
		"""
		addData(data)
			data=QtCore.QByteArray

		addData(data)
			data=str

		This function overloads PySide.QtCore.QCryptographicHash.addData() .
		"""
		res = super(QCryptographicHash,self).addData(*args,**kwargs)
		return res

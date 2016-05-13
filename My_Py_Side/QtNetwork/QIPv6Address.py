from PySide import QtGui, QtCore

class QIPv6Address(QtNetwork.QIPv6Address):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QIPv6Address,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __getitem__(self):
		"""

		"""
		res = super(QIPv6Address,self).__getitem__()
		return res
	#----------------------------------------------------------------------
	def __len__(self):
		"""

		"""
		res = super(QIPv6Address,self).__len__()
		return res
	#----------------------------------------------------------------------
	def __len__(self):
		"""

		"""
		res = super(QIPv6Address,self).__len__()
		return res
	#----------------------------------------------------------------------
	def __setitem__(self):
		"""

		"""
		res = super(QIPv6Address,self).__setitem__()
		return res
	#----------------------------------------------------------------------
	def PySide.QtNetwork.QIPv6Address.operator[](index)(self):
		"""

		"""
		res = super(QIPv6Address,self).PySide.QtNetwork.QIPv6Address.operator[](index)()
		isinstance(res,QtCore.quint8)
		return res

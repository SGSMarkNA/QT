from PySide import QtGui, QtCore

class QProxyModel(QtGui.QProxyModel):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QProxyModel,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def model(self):
		"""
		Returns the model that contains the data that is available through the proxy model.
		"""
		res = super(QProxyModel,self).model()
		isinstance(res,QtCore.QAbstractItemModel)
		return res
	#----------------------------------------------------------------------
	def connectToModel(self,model):
		"""
		connectToModel(model)
			model=QtCore.QAbstractItemModel

		Connect to all the signals emitted by given model .
		"""
		res = super(QProxyModel,self).connectToModel(model)
		return res
	#----------------------------------------------------------------------
	def disconnectFromModel(self,model):
		"""
		disconnectFromModel(model)
			model=QtCore.QAbstractItemModel

		Disconnect from all the signals emitted by the given model .
		"""
		res = super(QProxyModel,self).disconnectFromModel(model)
		return res
	#----------------------------------------------------------------------
	def setModel(self,model):
		"""
		setModel(model)
			model=QtCore.QAbstractItemModel

		Sets the given model to be processed by the proxy model.
		"""
		res = super(QProxyModel,self).setModel(model)
		return res
	#----------------------------------------------------------------------
	def setProxyModel(self,source_index):
		"""
		setProxyModel(source_index)
			source_index=QtCore.QModelIndex

		Change the model pointer in the given source_index to point to the proxy model.
		"""
		res = super(QProxyModel,self).setProxyModel(source_index)
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def setSourceModel(self,proxy_index):
		"""
		setSourceModel(proxy_index)
			proxy_index=QtCore.QModelIndex

		Change the model pointer in the given proxy_index to point to the source model.
		"""
		res = super(QProxyModel,self).setSourceModel(proxy_index)
		isinstance(res,QtCore.QModelIndex)
		return res

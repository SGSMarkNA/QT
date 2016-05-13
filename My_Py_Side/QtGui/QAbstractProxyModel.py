from PySide import QtGui, QtCore

class QAbstractProxyModel(QtGui.QAbstractProxyModel):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QAbstractProxyModel,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def sourceModel(self):
		"""
		Returns the model that contains the data that is available through the proxy model.
		"""
		res = super(QAbstractProxyModel,self).sourceModel()
		isinstance(res,QtCore.QAbstractItemModel)
		return res
	#----------------------------------------------------------------------
	def mapFromSource(self,sourceIndex):
		"""
		mapFromSource(sourceIndex)
			sourceIndex=QtCore.QModelIndex

		Reimplement this function to return the model index in the proxy model that corresponds to the sourceIndex from the source model.
		"""
		res = super(QAbstractProxyModel,self).mapFromSource(sourceIndex)
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def mapSelectionFromSource(self,selection):
		"""
		mapSelectionFromSource(selection)
			selection=QtGui.QItemSelection

		Returns a proxy selection mapped from the specified sourceSelection .
		Reimplement this method to map source selections to proxy selections.
		"""
		res = super(QAbstractProxyModel,self).mapSelectionFromSource(selection)
		isinstance(res,QtGui.QItemSelection)
		return res
	#----------------------------------------------------------------------
	def mapSelectionToSource(self,selection):
		"""
		mapSelectionToSource(selection)
			selection=QtGui.QItemSelection

		Returns a source selection mapped from the specified proxySelection .
		Reimplement this method to map proxy selections to source selections.
		"""
		res = super(QAbstractProxyModel,self).mapSelectionToSource(selection)
		isinstance(res,QtGui.QItemSelection)
		return res
	#----------------------------------------------------------------------
	def mapToSource(self,proxyIndex):
		"""
		mapToSource(proxyIndex)
			proxyIndex=QtCore.QModelIndex

		Reimplement this function to return the model index in the source model that corresponds to the proxyIndex in the proxy model.
		"""
		res = super(QAbstractProxyModel,self).mapToSource(proxyIndex)
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def setSourceModel(self,sourceModel):
		"""
		setSourceModel(sourceModel)
			sourceModel=QtCore.QAbstractItemModel

		Sets the given sourceModel to be processed by the proxy model.
		"""
		res = super(QAbstractProxyModel,self).setSourceModel(sourceModel)
		return res

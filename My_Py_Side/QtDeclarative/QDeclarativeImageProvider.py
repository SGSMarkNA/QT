from PySide import QtGui, QtCore

class QDeclarativeImageProvider(QtDeclarative.QDeclarativeImageProvider):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDeclarativeImageProvider,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def imageType(self):
		"""

		"""
		res = super(QDeclarativeImageProvider,self).imageType()
		isinstance(res,QtDeclarative.QDeclarativeImageProvider.ImageType)
		return res
	#----------------------------------------------------------------------
	def requestImage(self,id,size,requestedSize):
		"""
		requestImage(id,size,requestedSize)
			id=unicode
			size=QtCore.QSize
			requestedSize=QtCore.QSize


		"""
		res = super(QDeclarativeImageProvider,self).requestImage(id,size,requestedSize)
		isinstance(res,QtGui.QImage)
		return res
	#----------------------------------------------------------------------
	def requestPixmap(self,id,size,requestedSize):
		"""
		requestPixmap(id,size,requestedSize)
			id=unicode
			size=QtCore.QSize
			requestedSize=QtCore.QSize


		"""
		res = super(QDeclarativeImageProvider,self).requestPixmap(id,size,requestedSize)
		isinstance(res,QtGui.QPixmap)
		return res

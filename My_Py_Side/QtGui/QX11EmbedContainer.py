from PySide import QtGui, QtCore

class QX11EmbedContainer(QtGui.QX11EmbedContainer):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QX11EmbedContainer,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def clientClosed(self):
		"""

		"""
		res = super(QX11EmbedContainer,self).clientClosed()
		return res
	#----------------------------------------------------------------------
	def clientIsEmbedded(self):
		"""

		"""
		res = super(QX11EmbedContainer,self).clientIsEmbedded()
		return res
	#----------------------------------------------------------------------
	def clientWinId(self):
		"""
		If the container has an embedded widget, this function returns the X11 window ID of the client; otherwise it returns 0.
		"""
		res = super(QX11EmbedContainer,self).clientWinId()
		return res
	#----------------------------------------------------------------------
	def discardClient(self):
		"""
		Detaches the client from the embedder
		The client will appear as a standalone window on the desktop.
		"""
		res = super(QX11EmbedContainer,self).discardClient()
		return res
	#----------------------------------------------------------------------
	def error(self):
		"""
		Returns the last error that occurred.
		"""
		res = super(QX11EmbedContainer,self).error()
		isinstance(res,QtGui.QX11EmbedContainer.Error)
		return res
	#----------------------------------------------------------------------
	def embedClient(self,id):
		"""
		embedClient(id)
			id=long


		"""
		res = super(QX11EmbedContainer,self).embedClient(id)
		return res
	#----------------------------------------------------------------------
	def error(self,arg__1):
		"""
		error(arg__1)
			arg__1=QtGui.QX11EmbedContainer.Error


		"""
		res = super(QX11EmbedContainer,self).error(arg__1)
		return res

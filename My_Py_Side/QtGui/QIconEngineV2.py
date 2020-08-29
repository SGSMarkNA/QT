from PySide import QtGui, QtCore

class QIconEngineV2(QtGui.QIconEngineV2):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QIconEngineV2,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def clone(self):
		"""
		Returns a clone of this icon engine.
		"""
		res = super(QIconEngineV2,self).clone()
		isinstance(res,QtGui.QIconEngineV2)
		return res
	#----------------------------------------------------------------------
	def iconName(self):
		"""
		Returns the name used to create the engine, if available.
		"""
		res = super(QIconEngineV2,self).iconName()
		return res
	#----------------------------------------------------------------------
	def key(self):
		"""
		Returns a key that identifies this icon engine.
		"""
		res = super(QIconEngineV2,self).key()
		return res
	#----------------------------------------------------------------------
	def availableSizes(self,mode=None,state=None):
		"""
		availableSizes(mode=None,state=None)
			mode=QtGui.QIcon.Mode
			state=QtGui.QIcon.State


		"""
		res = super(QIconEngineV2,self).availableSizes(mode,state)
		return res
	#----------------------------------------------------------------------
	def read(self,in):
		"""
		read(in)
			in=QtCore.QDataStream

		Reads icon engine contents from the PySide.QtCore.QDataStream in
		Returns true if the contents were read; otherwise returns false.
		PySide.QtGui.QIconEngineV2 s default implementation always return false.
		"""
		res = super(QIconEngineV2,self).read(in)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def write(self,out):
		"""
		write(out)
			out=QtCore.QDataStream

		Writes the contents of this engine to the PySide.QtCore.QDataStream out
		Returns true if the contents were written; otherwise returns false.
		PySide.QtGui.QIconEngineV2 s default implementation always return false.
		"""
		res = super(QIconEngineV2,self).write(out)
		isinstance(res,bool)
		return res

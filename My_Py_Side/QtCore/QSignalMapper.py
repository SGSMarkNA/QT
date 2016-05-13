from PySide import QtGui, QtCore

class QSignalMapper(QtCore.QSignalMapper):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSignalMapper,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def mapping(self,*args,**kwargs):
		"""
		mapping(id)
			id=QtCore.int

		mapping(text)
			text=unicode

		mapping(widget)
			widget=QtGui.QWidget

		mapping(object)
			object=QtCore.QObject

		Returns the sender PySide.QtCore.QObject that is associated with the id .
		"""
		res = super(QSignalMapper,self).mapping(*args,**kwargs)
		isinstance(res,QtCore.QObject)
		return res
	#----------------------------------------------------------------------
	def removeMappings(self,sender):
		"""
		removeMappings(sender)
			sender=QtCore.QObject

		Removes all mappings for sender .
		This is done automatically when mapped objects are destroyed.
		"""
		res = super(QSignalMapper,self).removeMappings(sender)
		return res
	#----------------------------------------------------------------------
	def setMapping(self,*args,**kwargs):
		"""
		setMapping(sender,text)
			sender=QtCore.QObject
			text=unicode

		setMapping(sender,widget)
			sender=QtCore.QObject
			widget=QtGui.QWidget

		setMapping(sender,object)
			sender=QtCore.QObject
			object=QtCore.QObject

		setMapping(sender,id)
			sender=QtCore.QObject
			id=QtCore.int

		Adds a mapping so that when PySide.QtCore.QSignalMapper.map() is signalled from the sender , the signal mapped(text ) is emitted.
		There may be at most one text for each sender.
		"""
		res = super(QSignalMapper,self).setMapping(*args,**kwargs)
		return res

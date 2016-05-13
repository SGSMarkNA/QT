from PySide import QtGui, QtCore

class QDeclarativeScriptString(QtDeclarative.QDeclarativeScriptString):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDeclarativeScriptString,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def context(self):
		"""
		Returns the context for the script.
		"""
		res = super(QDeclarativeScriptString,self).context()
		isinstance(res,QtDeclarative.QDeclarativeContext)
		return res
	#----------------------------------------------------------------------
	def scopeObject(self):
		"""
		Returns the scope object for the script.
		"""
		res = super(QDeclarativeScriptString,self).scopeObject()
		isinstance(res,QtCore.QObject)
		return res
	#----------------------------------------------------------------------
	def script(self):
		"""
		Returns the script text.
		"""
		res = super(QDeclarativeScriptString,self).script()
		return res
	#----------------------------------------------------------------------
	def setContext(self,arg__1):
		"""
		setContext(arg__1)
			arg__1=QtDeclarative.QDeclarativeContext

		Sets the context for the script.
		"""
		res = super(QDeclarativeScriptString,self).setContext(arg__1)
		return res
	#----------------------------------------------------------------------
	def setScopeObject(self,arg__1):
		"""
		setScopeObject(arg__1)
			arg__1=QtCore.QObject

		Sets the scope object for the script.
		"""
		res = super(QDeclarativeScriptString,self).setScopeObject(arg__1)
		return res
	#----------------------------------------------------------------------
	def setScript(self,arg__1):
		"""
		setScript(arg__1)
			arg__1=unicode

		Sets the script text.
		"""
		res = super(QDeclarativeScriptString,self).setScript(arg__1)
		return res

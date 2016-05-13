from PySide import QtGui, QtCore

class QScriptExtensionPlugin(QtScript.QScriptExtensionPlugin):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QScriptExtensionPlugin,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def setupPackage(self,key,engine):
		"""
		setupPackage(key,engine)
			key=unicode
			engine=QtScript.QScriptEngine

		This function is provided for convenience when reimplementing PySide.QtScript.QScriptExtensionPlugin.initialize()
		It splits the given key on '.' (dot), and ensures that theres a corresponding path of objects in the environment of the given engine , creating new objects to complete the path if necessary
		E.g
		if the key is com.trolltech, after the call to PySide.QtScript.QScriptExtensionPlugin.setupPackage() the script expression com.trolltech will evaluate to an object
		More specifically, the engines Global Object will have a property called com, which in turn has a property called trolltech.
		Use this function to avoid global namespace pollution when installing your extensions in the engine.
		"""
		res = super(QScriptExtensionPlugin,self).setupPackage(key,engine)
		isinstance(res,QtScript.QScriptValue)
		return res

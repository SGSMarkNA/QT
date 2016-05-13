from PySide import QtGui, QtCore

class QProcessEnvironment(QtCore.QProcessEnvironment):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QProcessEnvironment,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Removes all key=value pairs from this PySide.QtCore.QProcessEnvironment object, making it empty.
		"""
		res = super(QProcessEnvironment,self).clear()
		return res
	#----------------------------------------------------------------------
	def isEmpty(self):
		"""
		Returns true if this PySide.QtCore.QProcessEnvironment object is empty: that is there are no key=value pairs set.
		"""
		res = super(QProcessEnvironment,self).isEmpty()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def toStringList(self):
		"""
		Converts this PySide.QtCore.QProcessEnvironment object into a list of strings, one for each environment variable that is set
		The environment variables name and its value are separated by an equal character (=).
		The PySide.QtCore.QStringList contents returned by this function are suitable for use with the QProcess::setEnvironment function
		However, it is recommended to use QProcess::setProcessEnvironment instead since that will avoid unnecessary copying of the data.
		"""
		res = super(QProcessEnvironment,self).toStringList()
		return res
	#----------------------------------------------------------------------
	def contains(self,name):
		"""
		contains(name)
			name=unicode

		Returns true if the environment variable of name name is found in this PySide.QtCore.QProcessEnvironment object.
		On Windows, variable names are case-insensitive, so the key is converted to uppercase before searching
		On other systems, names are case-sensitive so no trasformation is applied.
		"""
		res = super(QProcessEnvironment,self).contains(name)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def insert(self,name,value):
		"""
		insert(name,value)
			name=unicode
			value=unicode

		Inserts the environment variable of name name and contents value into this PySide.QtCore.QProcessEnvironment object
		If that variable already existed, it is replaced by the new value.
		On Windows, variable names are case-insensitive, so this function always uppercases the variable name before inserting
		On other systems, names are case-sensitive, so no transformation is applied.
		On most systems, inserting a variable with no contents will have the same effect for applications as if the variable had not been set at all
		However, to guarantee that there are no incompatibilities, to remove a variable, please use the PySide.QtCore.QProcessEnvironment.remove() function.
		"""
		res = super(QProcessEnvironment,self).insert(name,value)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtCore.QProcessEnvironment

		Returns true if this and the otherPySide.QtCore.QProcessEnvironment objects are different.
		"""
		res = super(QProcessEnvironment,self).__ne__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtCore.QProcessEnvironment

		Returns true if this and the otherPySide.QtCore.QProcessEnvironment objects are equal.
		Two PySide.QtCore.QProcessEnvironment objects are considered equal if they have the same set of key=value pairs
		The comparison of keys is done case-sensitive on platforms where the environment is case-sensitive.
		"""
		res = super(QProcessEnvironment,self).__eq__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def remove(self,name):
		"""
		remove(name)
			name=unicode

		Removes the environment variable identified by name from this PySide.QtCore.QProcessEnvironment object
		If that variable did not exist before, nothing happens.
		On Windows, variable names are case-insensitive, so the key is converted to uppercase before searching
		On other systems, names are case-sensitive so no trasformation is applied.
		"""
		res = super(QProcessEnvironment,self).remove(name)
		return res
	#----------------------------------------------------------------------
	def value(self,name,defaultValue=None):
		"""
		value(name,defaultValue=None)
			name=unicode
			defaultValue=unicode

		Searches this PySide.QtCore.QProcessEnvironment object for a variable identified by name and returns its value
		If the variable is not found in this object, then defaultValue is returned instead.
		On Windows, variable names are case-insensitive, so the key is converted to uppercase before searching
		On other systems, names are case-sensitive so no trasformation is applied.
		"""
		res = super(QProcessEnvironment,self).value(name,defaultValue)
		return res

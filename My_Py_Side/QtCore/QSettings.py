from PySide import QtGui, QtCore

class QSettings(QtCore.QSettings):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSettings,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def allKeys(self):
		"""
		Returns a list of all keys, including subkeys, that can be read using the PySide.QtCore.QSettings object.
		Example:
		If a group is set using PySide.QtCore.QSettings.beginGroup() , only the keys in the group are returned, without the group prefix:
		"""
		res = super(QSettings,self).allKeys()
		return res
	#----------------------------------------------------------------------
	def applicationName(self):
		"""
		Returns the application name used for storing the settings.
		"""
		res = super(QSettings,self).applicationName()
		return res
	#----------------------------------------------------------------------
	def childGroups(self):
		"""
		Returns a list of all key top-level groups that contain keys that can be read using the PySide.QtCore.QSettings object.
		Example:
		If a group is set using PySide.QtCore.QSettings.beginGroup() , the first-level keys in that group are returned, without the group prefix.
		You can navigate through the entire setting hierarchy using PySide.QtCore.QSettings.childKeys() and PySide.QtCore.QSettings.childGroups() recursively.
		"""
		res = super(QSettings,self).childGroups()
		return res
	#----------------------------------------------------------------------
	def childKeys(self):
		"""
		Returns a list of all top-level keys that can be read using the PySide.QtCore.QSettings object.
		Example:
		If a group is set using PySide.QtCore.QSettings.beginGroup() , the top-level keys in that group are returned, without the group prefix:
		You can navigate through the entire setting hierarchy using PySide.QtCore.QSettings.childKeys() and PySide.QtCore.QSettings.childGroups() recursively.
		"""
		res = super(QSettings,self).childKeys()
		return res
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Removes all entries in the primary location associated to this PySide.QtCore.QSettings object.
		Entries in fallback locations are not removed.
		If you only want to remove the entries in the current PySide.QtCore.QSettings.group() , use remove() instead.
		"""
		res = super(QSettings,self).clear()
		return res
	#----------------------------------------------------------------------
	def endArray(self):
		"""
		Closes the array that was started using PySide.QtCore.QSettings.beginReadArray() or PySide.QtCore.QSettings.beginWriteArray() .
		"""
		res = super(QSettings,self).endArray()
		return res
	#----------------------------------------------------------------------
	def endGroup(self):
		"""
		Resets the group to what it was before the corresponding PySide.QtCore.QSettings.beginGroup() call.
		Example:
		"""
		res = super(QSettings,self).endGroup()
		return res
	#----------------------------------------------------------------------
	def fallbacksEnabled(self):
		"""
		Returns true if fallbacks are enabled; returns false otherwise.
		By default, fallbacks are enabled.
		"""
		res = super(QSettings,self).fallbacksEnabled()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def fileName(self):
		"""
		Returns the path where settings written using this PySide.QtCore.QSettings object are stored.
		On Windows, if the format is QSettings.NativeFormat , the return value is a system registry path, not a file path.
		"""
		res = super(QSettings,self).fileName()
		return res
	#----------------------------------------------------------------------
	def format(self):
		"""
		Returns the format used for storing the settings.
		"""
		res = super(QSettings,self).format()
		isinstance(res,QtCore.QSettings.Format)
		return res
	#----------------------------------------------------------------------
	def group(self):
		"""
		Returns the current group.
		"""
		res = super(QSettings,self).group()
		return res
	#----------------------------------------------------------------------
	def iniCodec(self):
		"""
		Returns the codec that is used for accessing INI files
		By default, no codec is used, so a null pointer is returned.
		"""
		res = super(QSettings,self).iniCodec()
		isinstance(res,QtCore.QTextCodec)
		return res
	#----------------------------------------------------------------------
	def isWritable(self):
		"""
		Returns true if settings can be written using this PySide.QtCore.QSettings object; returns false otherwise.
		One reason why PySide.QtCore.QSettings.isWritable() might return false is if PySide.QtCore.QSettings operates on a read-only file.
		"""
		res = super(QSettings,self).isWritable()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def organizationName(self):
		"""
		Returns the organization name used for storing the settings.
		"""
		res = super(QSettings,self).organizationName()
		return res
	#----------------------------------------------------------------------
	def scope(self):
		"""
		Returns the scope used for storing the settings.
		"""
		res = super(QSettings,self).scope()
		isinstance(res,QtCore.QSettings.Scope)
		return res
	#----------------------------------------------------------------------
	def status(self):
		"""
		Returns a status code indicating the first error that was met by PySide.QtCore.QSettings , or QSettings.NoError if no error occurred.
		Be aware that PySide.QtCore.QSettings delays performing some operations
		For this reason, you might want to call PySide.QtCore.QSettings.sync() to ensure that the data stored in PySide.QtCore.QSettings is written to disk before calling PySide.QtCore.QSettings.status() .
		"""
		res = super(QSettings,self).status()
		isinstance(res,QtCore.QSettings.Status)
		return res
	#----------------------------------------------------------------------
	def sync(self):
		"""
		Writes any unsaved changes to permanent storage, and reloads any settings that have been changed in the meantime by another application.
		This function is called automatically from PySide.QtCore.QSettings s destructor and by the event loop at regular intervals, so you normally dont need to call it yourself.
		"""
		res = super(QSettings,self).sync()
		return res
	#----------------------------------------------------------------------
	def beginGroup(self,prefix):
		"""
		beginGroup(prefix)
			prefix=unicode

		Appends prefix to the current group.
		The current group is automatically prepended to all keys specified to PySide.QtCore.QSettings
		In addition, query functions such as PySide.QtCore.QSettings.childGroups() , PySide.QtCore.QSettings.childKeys() , and PySide.QtCore.QSettings.allKeys() are based on the group
		By default, no group is set.
		Groups are useful to avoid typing in the same setting paths over and over
		For example:
		This will set the value of three settings:
		Call PySide.QtCore.QSettings.endGroup() to reset the current group to what it was before the corresponding PySide.QtCore.QSettings.beginGroup() call
		Groups can be nested.
		"""
		res = super(QSettings,self).beginGroup(prefix)
		return res
	#----------------------------------------------------------------------
	def beginReadArray(self,prefix):
		"""
		beginReadArray(prefix)
			prefix=unicode

		Adds prefix to the current group and starts reading from an array
		Returns the size of the array.
		Example:
		Use PySide.QtCore.QSettings.beginWriteArray() to write the array in the first place.
		"""
		res = super(QSettings,self).beginReadArray(prefix)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def beginWriteArray(self,prefix,size=None):
		"""
		beginWriteArray(prefix,size=None)
			prefix=unicode
			size=QtCore.int

		Adds prefix to the current group and starts writing an array of size size
		If size is -1 (the default), it is automatically determined based on the indexes of the entries written.
		If you have many occurrences of a certain set of keys, you can use arrays to make your life easier
		For example, lets suppose that you want to save a variable-length list of user names and passwords
		You could then write:
		The generated keys will have the form
		To read back an array, use PySide.QtCore.QSettings.beginReadArray() .
		"""
		res = super(QSettings,self).beginWriteArray(prefix,size)
		return res
	#----------------------------------------------------------------------
	def contains(self,key):
		"""
		contains(key)
			key=unicode

		Returns true if there exists a setting called key ; returns false otherwise.
		If a group is set using PySide.QtCore.QSettings.beginGroup() , key is taken to be relative to that group.
		Note that the Windows registry and INI files use case-insensitive keys, whereas the Carbon Preferences API on Mac OS X uses case-sensitive keys
		To avoid portability problems, see the Section and Key Syntax rules.
		"""
		res = super(QSettings,self).contains(key)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def remove(self,key):
		"""
		remove(key)
			key=unicode

		Removes the setting key and any sub-settings of key .
		Example:
		Be aware that if one of the fallback locations contains a setting with the same key, that setting will be visible after calling PySide.QtCore.QSettings.remove() .
		If key is an empty string, all keys in the current PySide.QtCore.QSettings.group() are removed
		For example:
		Note that the Windows registry and INI files use case-insensitive keys, whereas the Carbon Preferences API on Mac OS X uses case-sensitive keys
		To avoid portability problems, see the Section and Key Syntax rules.
		"""
		res = super(QSettings,self).remove(key)
		return res
	#----------------------------------------------------------------------
	def setArrayIndex(self,i):
		"""
		setArrayIndex(i)
			i=QtCore.int

		Sets the current array index to i
		Calls to functions such as PySide.QtCore.QSettings.setValue() , PySide.QtCore.QSettings.value() , PySide.QtCore.QSettings.remove() , and PySide.QtCore.QSettings.contains() will operate on the array entry at that index.
		You must call PySide.QtCore.QSettings.beginReadArray() or PySide.QtCore.QSettings.beginWriteArray() before you can call this function.
		"""
		res = super(QSettings,self).setArrayIndex(i)
		return res
	#----------------------------------------------------------------------
	def setFallbacksEnabled(self,b):
		"""
		setFallbacksEnabled(b)
			b=QtCore.bool

		Sets whether fallbacks are enabled to b .
		By default, fallbacks are enabled.
		"""
		res = super(QSettings,self).setFallbacksEnabled(b)
		return res
	#----------------------------------------------------------------------
	def setIniCodec(self,*args,**kwargs):
		"""
		setIniCodec(codec)
			codec=QtCore.QTextCodec

		setIniCodec(codecName)
			codecName=str

		Sets the codec for accessing INI files (including .conf files on Unix) to codec
		The codec is used for decoding any data that is read from the INI file, and for encoding any data that is written to the file
		By default, no codec is used, and non-ASCII characters are encoded using standard INI escape sequences.
		"""
		res = super(QSettings,self).setIniCodec(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setValue(self,key,value):
		"""
		setValue(key,value)
			key=unicode
			value=object

		Sets the value of setting key to value
		If the key already exists, the previous value is overwritten.
		Note that the Windows registry and INI files use case-insensitive keys, whereas the Carbon Preferences API on Mac OS X uses case-sensitive keys
		To avoid portability problems, see the Section and Key Syntax rules.
		Example:
		"""
		res = super(QSettings,self).setValue(key,value)
		return res
	#----------------------------------------------------------------------
	def value(self,key,defaultValue=None):
		"""
		value(key,defaultValue=None)
			key=unicode
			defaultValue=object

		Returns the value for setting key
		If the setting doesnt exist, returns defaultValue .
		If no default value is specified, a default PySide.QtCore.QVariant is returned.
		Note that the Windows registry and INI files use case-insensitive keys, whereas the Carbon Preferences API on Mac OS X uses case-sensitive keys
		To avoid portability problems, see the Section and Key Syntax rules.
		Example:
		"""
		res = super(QSettings,self).value(key,defaultValue)
		return res

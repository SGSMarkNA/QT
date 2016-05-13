from PySide import QtGui, QtCore

class QNetworkConfigurationManager(QtNetwork.QNetworkConfigurationManager):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QNetworkConfigurationManager,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def capabilities(self):
		"""
		Returns the capabilities supported by the current platform.
		"""
		res = super(QNetworkConfigurationManager,self).capabilities()
		isinstance(res,QtNetwork.QNetworkConfigurationManager.Capabilities)
		return res
	#----------------------------------------------------------------------
	def defaultConfiguration(self):
		"""
		Returns the default configuration to be used
		This function always returns a discovered configuration; otherwise an invalid configuration.
		In some cases it may be required to call PySide.QtNetwork.QNetworkConfigurationManager.updateConfigurations() and wait for the PySide.QtNetwork.QNetworkConfigurationManager.updateCompleted() signal before calling this function.
		"""
		res = super(QNetworkConfigurationManager,self).defaultConfiguration()
		isinstance(res,QtNetwork.QNetworkConfiguration)
		return res
	#----------------------------------------------------------------------
	def isOnline(self):
		"""
		Returns true if the system is considered to be connected to another device via an active network interface; otherwise returns false.
		This is equivalent to the following code snippet:
		"""
		res = super(QNetworkConfigurationManager,self).isOnline()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def updateCompleted(self):
		"""

		"""
		res = super(QNetworkConfigurationManager,self).updateCompleted()
		return res
	#----------------------------------------------------------------------
	def updateConfigurations(self):
		"""
		Initiates an update of all configurations
		This may be used to initiate WLAN scans or other time consuming updates which may be required to obtain the correct state for configurations.
		This call is asynchronous
		On completion of this update the PySide.QtNetwork.QNetworkConfigurationManager.updateCompleted() signal is emitted
		If new configurations are discovered or old ones were removed or changed the update process may trigger the emission of one or multiple PySide.QtNetwork.QNetworkConfigurationManager.configurationAdded() , PySide.QtNetwork.QNetworkConfigurationManager.configurationRemoved() and PySide.QtNetwork.QNetworkConfigurationManager.configurationChanged() signals.
		If a configuration state changes as a result of this update all existing PySide.QtNetwork.QNetworkConfiguration instances are updated automatically.
		"""
		res = super(QNetworkConfigurationManager,self).updateConfigurations()
		return res
	#----------------------------------------------------------------------
	def allConfigurations(self,flags=None):
		"""
		allConfigurations(flags=None)
			flags=QtNetwork.QNetworkConfiguration.StateFlags


		"""
		res = super(QNetworkConfigurationManager,self).allConfigurations(flags)
		return res
	#----------------------------------------------------------------------
	def configurationFromIdentifier(self,identifier):
		"""
		configurationFromIdentifier(identifier)
			identifier=unicode

		Returns the PySide.QtNetwork.QNetworkConfiguration for identifier ; otherwise returns an invalid PySide.QtNetwork.QNetworkConfiguration .
		"""
		res = super(QNetworkConfigurationManager,self).configurationFromIdentifier(identifier)
		isinstance(res,QtNetwork.QNetworkConfiguration)
		return res

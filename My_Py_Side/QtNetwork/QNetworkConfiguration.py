from PySide import QtGui, QtCore

class QNetworkConfiguration(QtNetwork.QNetworkConfiguration):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QNetworkConfiguration,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def bearerName(self):
		"""
		This function is deprecated
		It is equivalent to calling PySide.QtNetwork.QNetworkConfiguration.bearerTypeName() , however PySide.QtNetwork.QNetworkConfiguration.bearerType() should be used in preference.
		"""
		res = super(QNetworkConfiguration,self).bearerName()
		return res
	#----------------------------------------------------------------------
	def bearerType(self):
		"""
		Returns the type of bearer used by this network configuration.
		If the bearer type is unknown the PySide.QtNetwork.QNetworkConfiguration.bearerTypeName() function can be used to retrieve a textural type name for the bearer.
		An invalid network configuration always returns the BearerUnknown value.
		"""
		res = super(QNetworkConfiguration,self).bearerType()
		isinstance(res,QtNetwork.QNetworkConfiguration.BearerType)
		return res
	#----------------------------------------------------------------------
	def bearerTypeName(self):
		"""
		Returns the type of bearer used by this network configuration as a string.
		The string is not translated and therefore can not be shown to the user
		The subsequent table shows the fixed mappings between QNetworkConfiguration.BearerType and the bearer type name for known types
		If the QNetworkConfiguration.BearerType is unknown this function may return additional information if it is available; otherwise an empty string will be returned.
		This function returns an empty string if this is an invalid configuration, a network configuration of type QNetworkConfiguration.ServiceNetwork or QNetworkConfiguration.UserChoice .
		"""
		res = super(QNetworkConfiguration,self).bearerTypeName()
		return res
	#----------------------------------------------------------------------
	def children(self):
		"""
		Returns all sub configurations of this network configuration in priority order
		The first sub configuration in the list has the highest priority.
		Only network configurations of type ServiceNetwork can have children
		Otherwise this function returns an empty list.
		"""
		res = super(QNetworkConfiguration,self).children()
		return res
	#----------------------------------------------------------------------
	def identifier(self):
		"""
		Returns the unique and platform specific identifier for this network configuration; otherwise an empty string.
		"""
		res = super(QNetworkConfiguration,self).identifier()
		return res
	#----------------------------------------------------------------------
	def isRoamingAvailable(self):
		"""
		Returns true if this configuration supports roaming; otherwise false.
		"""
		res = super(QNetworkConfiguration,self).isRoamingAvailable()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if this PySide.QtNetwork.QNetworkConfiguration object is valid
		A configuration may become invalid if the user deletes the configuration or the configuration was default-constructed.
		The addition and removal of configurations can be monitored via the PySide.QtNetwork.QNetworkConfigurationManager .
		"""
		res = super(QNetworkConfiguration,self).isValid()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def name(self):
		"""
		Returns the user visible name of this configuration.
		The name may either be the name of the underlying access point or the name for service network that this configuration represents.
		"""
		res = super(QNetworkConfiguration,self).name()
		return res
	#----------------------------------------------------------------------
	def purpose(self):
		"""
		Returns the purpose of this configuration.
		The purpose field may be used to programmatically determine the purpose of a configuration
		Such information is usually part of the access point or service network meta data.
		"""
		res = super(QNetworkConfiguration,self).purpose()
		isinstance(res,QtNetwork.QNetworkConfiguration.Purpose)
		return res
	#----------------------------------------------------------------------
	def state(self):
		"""
		Returns the current state of the configuration.
		"""
		res = super(QNetworkConfiguration,self).state()
		isinstance(res,QtNetwork.QNetworkConfiguration.StateFlags)
		return res
	#----------------------------------------------------------------------
	def type(self):
		"""
		Returns the type of the configuration.
		A configuration can represent a single access point configuration or a set of access point configurations
		Such a set is called service network
		A configuration that is based on a service network can potentially support roaming of network sessions.
		"""
		res = super(QNetworkConfiguration,self).type()
		isinstance(res,QtNetwork.QNetworkConfiguration.Type)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,cp):
		"""
		__ne__(cp)
			cp=QtNetwork.QNetworkConfiguration

		Returns true if this configuration is not the same as the other configuration given; otherwise returns false.
		"""
		res = super(QNetworkConfiguration,self).__ne__(cp)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,cp):
		"""
		__eq__(cp)
			cp=QtNetwork.QNetworkConfiguration

		Returns true, if this configuration is the same as the other configuration given; otherwise returns false.
		"""
		res = super(QNetworkConfiguration,self).__eq__(cp)
		isinstance(res,QtCore.bool)
		return res

from PySide import QtGui, QtCore

class QNetworkInterface(QtNetwork.QNetworkInterface):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QNetworkInterface,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def addressEntries(self):
		"""
		Returns the list of IP addresses that this interface possesses along with their associated netmasks and broadcast addresses.
		If the netmask or broadcast address information is not necessary, you can call the PySide.QtNetwork.QNetworkInterface.allAddresses() function to obtain just the IP addresses.
		"""
		res = super(QNetworkInterface,self).addressEntries()
		return res
	#----------------------------------------------------------------------
	def flags(self):
		"""
		Returns the flags associated with this network interface.
		"""
		res = super(QNetworkInterface,self).flags()
		isinstance(res,QtNetwork.QNetworkInterface.InterfaceFlags)
		return res
	#----------------------------------------------------------------------
	def hardwareAddress(self):
		"""
		Returns the low-level hardware address for this interface
		On Ethernet interfaces, this will be a MAC address in string representation, separated by colons.
		Other interface types may have other types of hardware addresses
		Implementations should not depend on this function returning a valid MAC address.
		"""
		res = super(QNetworkInterface,self).hardwareAddress()
		return res
	#----------------------------------------------------------------------
	def humanReadableName(self):
		"""
		Returns the human-readable name of this network interface on Windows, such as Local Area Connection, if the name could be determined
		If it couldnt, this function returns the same as PySide.QtNetwork.QNetworkInterface.name()
		The human-readable name is a name that the user can modify in the Windows Control Panel, so it may change during the execution of the program.
		On Unix, this function currently always returns the same as PySide.QtNetwork.QNetworkInterface.name() , since Unix systems dont store a configuration for human-readable names.
		"""
		res = super(QNetworkInterface,self).humanReadableName()
		return res
	#----------------------------------------------------------------------
	def index(self):
		"""
		Returns the interface system index, if known
		This is an integer assigned by the operating system to identify this interface and it generally doesnt change
		It matches the scope ID field in IPv6 addresses.
		If the index isnt known, this function returns 0.
		"""
		res = super(QNetworkInterface,self).index()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if this PySide.QtNetwork.QNetworkInterface object contains valid information about a network interface.
		"""
		res = super(QNetworkInterface,self).isValid()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def name(self):
		"""
		Returns the name of this network interface
		On Unix systems, this is a string containing the type of the interface and optionally a sequence number, such as eth0, lo or pcn0
		On Windows, its an internal ID that cannot be changed by the user.
		"""
		res = super(QNetworkInterface,self).name()
		return res

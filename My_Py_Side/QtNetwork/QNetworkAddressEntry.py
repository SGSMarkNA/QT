from PySide import QtGui, QtCore

class QNetworkAddressEntry(QtNetwork.QNetworkAddressEntry):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QNetworkAddressEntry,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def broadcast(self):
		"""
		Returns the broadcast address associated with the IPv4 address and netmask
		It can usually be derived from those two by setting to 1 the bits of the IP address where the netmask contains a 0
		(In other words, by bitwise-ORing the IP address with the inverse of the netmask)
		This member is always empty for IPv6 addresses, since the concept of broadcast has been abandoned in that system in favor of multicast
		In particular, the group of hosts corresponding to all the nodes in the local network can be reached by the all-nodes special multicast group (address FF02::1).
		"""
		res = super(QNetworkAddressEntry,self).broadcast()
		isinstance(res,QtNetwork.QHostAddress)
		return res
	#----------------------------------------------------------------------
	def ip(self):
		"""
		This function returns one IPv4 or IPv6 address found, that was found in a network interface.
		"""
		res = super(QNetworkAddressEntry,self).ip()
		isinstance(res,QtNetwork.QHostAddress)
		return res
	#----------------------------------------------------------------------
	def netmask(self):
		"""
		Returns the netmask associated with the IP address
		The netmask is expressed in the form of an IP address, such as 255.255.0.0.
		For IPv6 addresses, the prefix length is converted to an address where the number of bits set to 1 is equal to the prefix length
		For a prefix length of 64 bits (the most common value), the netmask will be expressed as a PySide.QtNetwork.QHostAddress holding the address FFFF:FFFF:FFFF:FFFF:
		"""
		res = super(QNetworkAddressEntry,self).netmask()
		isinstance(res,QtNetwork.QHostAddress)
		return res
	#----------------------------------------------------------------------
	def prefixLength(self):
		"""
		Returns the prefix length of this IP address
		The prefix length matches the number of bits set to 1 in the netmask (see PySide.QtNetwork.QNetworkAddressEntry.netmask() )
		For IPv4 addresses, the value is between 0 and 32
		For IPv6 addresses, its contained between 0 and 128 and is the preferred form of representing addresses.
		This function returns -1 if the prefix length could not be determined (i.e., PySide.QtNetwork.QNetworkAddressEntry.netmask() returns a null QHostAddress()).
		"""
		res = super(QNetworkAddressEntry,self).prefixLength()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtNetwork.QNetworkAddressEntry

		Returns true if this network address entry is different from other .
		"""
		res = super(QNetworkAddressEntry,self).__ne__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtNetwork.QNetworkAddressEntry

		Returns true if this network address entry is the same as other .
		"""
		res = super(QNetworkAddressEntry,self).__eq__(other)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def setBroadcast(self,newBroadcast):
		"""
		setBroadcast(newBroadcast)
			newBroadcast=QtNetwork.QHostAddress

		Sets the broadcast IP address of this PySide.QtNetwork.QNetworkAddressEntry object to newBroadcast .
		"""
		res = super(QNetworkAddressEntry,self).setBroadcast(newBroadcast)
		return res
	#----------------------------------------------------------------------
	def setIp(self,newIp):
		"""
		setIp(newIp)
			newIp=QtNetwork.QHostAddress

		Sets the IP address the PySide.QtNetwork.QNetworkAddressEntry object contains to newIp .
		"""
		res = super(QNetworkAddressEntry,self).setIp(newIp)
		return res
	#----------------------------------------------------------------------
	def setNetmask(self,newNetmask):
		"""
		setNetmask(newNetmask)
			newNetmask=QtNetwork.QHostAddress

		Sets the netmask that this PySide.QtNetwork.QNetworkAddressEntry object contains to newNetmask
		Setting the netmask also sets the prefix length to match the new netmask.
		"""
		res = super(QNetworkAddressEntry,self).setNetmask(newNetmask)
		return res
	#----------------------------------------------------------------------
	def setPrefixLength(self,length):
		"""
		setPrefixLength(length)
			length=QtCore.int

		Sets the prefix length of this IP address to length
		The value of length must be valid for this type of IP address: between 0 and 32 for IPv4 addresses, between 0 and 128 for IPv6 addresses
		Setting to any invalid value is equivalent to setting to -1, which means no prefix length.
		Setting the prefix length also sets the netmask (see PySide.QtNetwork.QNetworkAddressEntry.netmask() ).
		"""
		res = super(QNetworkAddressEntry,self).setPrefixLength(length)
		return res

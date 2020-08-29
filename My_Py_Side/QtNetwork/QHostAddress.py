from PySide import QtGui, QtCore

class QHostAddress(QtNetwork.QHostAddress):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QHostAddress,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Sets the host address to 0.0.0.0.
		"""
		res = super(QHostAddress,self).clear()
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if this host address is null (INADDR_ANY or in6addr_any)
		The default constructor creates a null address, and that address is not valid for any host or interface.
		"""
		res = super(QHostAddress,self).isNull()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def protocol(self):
		"""
		Returns the network layer protocol of the host address.
		"""
		res = super(QHostAddress,self).protocol()
		isinstance(res,QtNetwork.QAbstractSocket.NetworkLayerProtocol)
		return res
	#----------------------------------------------------------------------
	def scopeId(self):
		"""
		Returns the scope ID of an IPv6 address
		For IPv4 addresses, or if the address does not contain a scope ID, an empty PySide.QtCore.QString is returned.
		The IPv6 scope ID specifies the scope of reachability for non-global IPv6 addresses, limiting the area in which the address can be used
		All IPv6 addresses are associated with such a reachability scope
		The scope ID is used to disambiguate addresses that are not guaranteed to be globally unique.
		IPv6 specifies the following four levels of reachability:
		When using a link-local or site-local address for IPv6 connections, you must specify the scope ID
		The scope ID for a link-local address is usually the same as the interface name (e.g., eth0, en1) or number (e.g., 1, 2).
		"""
		res = super(QHostAddress,self).scopeId()
		return res
	#----------------------------------------------------------------------
	def toIPv4Address(self):
		"""
		Returns the IPv4 address as a number.
		For example, if the address is 127.0.0.1, the returned value is 2130706433 (i.e
		0x7f000001).
		This value is only valid if the Protocol() is IPv4Protocol .
		"""
		res = super(QHostAddress,self).toIPv4Address()
		isinstance(res,QtCore.quint32)
		return res
	#----------------------------------------------------------------------
	def toIPv6Address(self):
		"""
		Returns the IPv6 address as a Q_IPV6ADDR structure
		The structure consists of 16 unsigned characters.
		This value is only valid if the PySide.QtNetwork.QHostAddress.protocol() is IPv6Protocol .
		"""
		res = super(QHostAddress,self).toIPv6Address()
		isinstance(res,QtNetwork.QIPv6Address)
		return res
	#----------------------------------------------------------------------
	def toString(self):
		"""
		Returns the address as a string.
		For example, if the address is the IPv4 address 127.0.0.1, the returned string is 127.0.0.1.
		"""
		res = super(QHostAddress,self).toString()
		return res
	#----------------------------------------------------------------------
	def isInSubnet(self,*args,**kwargs):
		"""
		isInSubnet(subnet)
			subnet=unKnown

		isInSubnet(subnet,netmask)
			subnet=QtNetwork.QHostAddress
			netmask=QtCore.int


		"""
		res = super(QHostAddress,self).isInSubnet(*args,**kwargs)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,*args,**kwargs):
		"""
		__ne__(address)
			address=QtNetwork.QHostAddress.SpecialAddress

		__ne__(address)
			address=QtNetwork.QHostAddress

		Returns true if this host address is not the same as the other address given; otherwise returns false.
		"""
		res = super(QHostAddress,self).__ne__(*args,**kwargs)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,*args,**kwargs):
		"""
		__eq__(address)
			address=QtNetwork.QHostAddress

		__eq__(address)
			address=QtNetwork.QHostAddress.SpecialAddress

		Returns true if this host address is the same as the other address given; otherwise returns false.
		"""
		res = super(QHostAddress,self).__eq__(*args,**kwargs)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setAddress(self,*args,**kwargs):
		"""
		setAddress(ip6Addr)
			ip6Addr=QtCore.quint8

		setAddress(ip4Addr)
			ip4Addr=QtCore.quint32

		setAddress(ip6Addr)
			ip6Addr=QtNetwork.QIPv6Address

		setAddress(address)
			address=unicode

		This is an overloaded function.
		Set the IPv6 address specified by ip6Addr .
		ip6Addr must be an array of 16 bytes in network byte order (high-order byte first).
		"""
		res = super(QHostAddress,self).setAddress(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setScopeId(self,id):
		"""
		setScopeId(id)
			id=unicode

		Sets the IPv6 scope ID of the address to id
		If the address protocol is not IPv6, this function does nothing.
		"""
		res = super(QHostAddress,self).setScopeId(id)
		return res

from PySide import QtGui, QtCore

class QNetworkSession(QtNetwork.QNetworkSession):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QNetworkSession,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def activeTime(self):
		"""
		Returns the number of seconds that the session has been active.
		"""
		res = super(QNetworkSession,self).activeTime()
		isinstance(res,QtCore.quint64)
		return res
	#----------------------------------------------------------------------
	def bytesReceived(self):
		"""
		Returns the amount of data received in bytes; otherwise 0.
		This field value includes the usage across all open network sessions which use the same network interface.
		If the session is based on a service network configuration the number of sent bytes across all active member configurations are returned.
		This function may not always be supported on all platforms and returns 0
		The platform capability can be detected via QNetworkConfigurationManager.DataStatistics .
		"""
		res = super(QNetworkSession,self).bytesReceived()
		isinstance(res,QtCore.quint64)
		return res
	#----------------------------------------------------------------------
	def bytesWritten(self):
		"""
		Returns the amount of data sent in bytes; otherwise 0.
		This field value includes the usage across all open network sessions which use the same network interface.
		If the session is based on a service network configuration the number of sent bytes across all active member configurations are returned.
		This function may not always be supported on all platforms and returns 0
		The platform capability can be detected via QNetworkConfigurationManager.DataStatistics .
		"""
		res = super(QNetworkSession,self).bytesWritten()
		isinstance(res,QtCore.quint64)
		return res
	#----------------------------------------------------------------------
	def closed(self):
		"""

		"""
		res = super(QNetworkSession,self).closed()
		return res
	#----------------------------------------------------------------------
	def configuration(self):
		"""
		Returns the PySide.QtNetwork.QNetworkConfiguration that this network session object is based on.
		"""
		res = super(QNetworkSession,self).configuration()
		isinstance(res,QtNetwork.QNetworkConfiguration)
		return res
	#----------------------------------------------------------------------
	def error(self):
		"""
		Returns the type of error that last occurred.
		"""
		res = super(QNetworkSession,self).error()
		isinstance(res,QtNetwork.QNetworkSession.SessionError)
		return res
	#----------------------------------------------------------------------
	def errorString(self):
		"""
		Returns a human-readable description of the last device error that occurred.
		"""
		res = super(QNetworkSession,self).errorString()
		return res
	#----------------------------------------------------------------------
	def interface(self):
		"""
		Returns the network interface that is used by this session.
		This function only returns a valid PySide.QtNetwork.QNetworkInterface when this session is Connected .
		The returned interface may change as a result of a roaming process.
		Note: this function does not work in Symbian emulator due to the way the connectivity is emulated on Windows.
		"""
		res = super(QNetworkSession,self).interface()
		isinstance(res,QtNetwork.QNetworkInterface)
		return res
	#----------------------------------------------------------------------
	def isOpen(self):
		"""
		Returns true if this session is open
		If the number of all open sessions is greater than zero the underlying network interface will remain connected/up.
		The session can be controlled via PySide.QtNetwork.QNetworkSession.open() and PySide.QtNetwork.QNetworkSession.close() .
		"""
		res = super(QNetworkSession,self).isOpen()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def newConfigurationActivated(self):
		"""

		"""
		res = super(QNetworkSession,self).newConfigurationActivated()
		return res
	#----------------------------------------------------------------------
	def opened(self):
		"""

		"""
		res = super(QNetworkSession,self).opened()
		return res
	#----------------------------------------------------------------------
	def state(self):
		"""
		Returns the state of the session.
		If the session is based on a single access point configuration the state of the session is the same as the state of the associated network interface
		Therefore a network session object can be used to monitor network interfaces.
		A QNetworkConfiguration.ServiceNetwork based session summarizes the state of all its children and therefore returns the Connected state if at least one of the service networks PySide.QtNetwork.QNetworkConfiguration.children() configurations is active.
		Note that it is not required to hold an open session in order to obtain the network interface state
		A connected but closed session may be used to monitor network interfaces whereas an open and connected session object may prevent the network interface from being shut down.
		"""
		res = super(QNetworkSession,self).state()
		isinstance(res,QtNetwork.QNetworkSession.State)
		return res
	#----------------------------------------------------------------------
	def error(self,arg__1):
		"""
		error(arg__1)
			arg__1=QtNetwork.QNetworkSession.SessionError


		"""
		res = super(QNetworkSession,self).error(arg__1)
		return res
	#----------------------------------------------------------------------
	def sessionProperty(self,key):
		"""
		sessionProperty(key)
			key=unicode

		Returns the value for property key .
		A network session can have properties attached which may describe the session in more details
		This function can be used to gain access to those properties.
		The following property keys are guaranteed to be specified on all platforms:
		"""
		res = super(QNetworkSession,self).sessionProperty(key)
		return res
	#----------------------------------------------------------------------
	def setSessionProperty(self,key,value):
		"""
		setSessionProperty(key,value)
			key=unicode
			value=object

		Sets the property value on the session
		The property is identified using key
		Removing an already set property can be achieved by passing an invalid PySide.QtCore.QVariant .
		Note that the UserChoiceConfiguration and ActiveConfiguration properties are read only and cannot be changed using this method.
		"""
		res = super(QNetworkSession,self).setSessionProperty(key,value)
		return res
	#----------------------------------------------------------------------
	def waitForOpened(self,msecs=None):
		"""
		waitForOpened(msecs=None)
			msecs=QtCore.int

		Waits until the session has been opened, up to msecs milliseconds
		If the session has been opened, this function returns true; otherwise it returns false
		In the case where it returns false, you can call PySide.QtNetwork.QNetworkSession.error() to determine the cause of the error.
		The following example waits up to one second for the session to be opened:
		If msecs is -1, this function will not time out.
		"""
		res = super(QNetworkSession,self).waitForOpened(msecs)
		isinstance(res,QtCore.bool)
		return res

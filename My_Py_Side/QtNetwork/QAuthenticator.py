from PySide import QtGui, QtCore

class QAuthenticator(QtNetwork.QAuthenticator):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QAuthenticator,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if the authenticator is null.
		"""
		res = super(QAuthenticator,self).isNull()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def options(self):
		"""
		Returns all incoming options set in this PySide.QtNetwork.QAuthenticator object by parsing the server reply
		See QAuthenticator#Options for more information on incoming options.
		"""
		res = super(QAuthenticator,self).options()
		return res
	#----------------------------------------------------------------------
	def password(self):
		"""
		returns the password used for authentication.
		"""
		res = super(QAuthenticator,self).password()
		return res
	#----------------------------------------------------------------------
	def realm(self):
		"""
		returns the realm requiring authentication.
		"""
		res = super(QAuthenticator,self).realm()
		return res
	#----------------------------------------------------------------------
	def user(self):
		"""
		returns the user used for authentication.
		"""
		res = super(QAuthenticator,self).user()
		return res
	#----------------------------------------------------------------------
	def __ne__(self,other):
		"""
		__ne__(other)
			other=QtNetwork.QAuthenticator

		Returns true if this authenticator is different from other ; otherwise returns false.
		"""
		res = super(QAuthenticator,self).__ne__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,other):
		"""
		__eq__(other)
			other=QtNetwork.QAuthenticator

		Returns true if this authenticator is identical to other ; otherwise returns false.
		"""
		res = super(QAuthenticator,self).__eq__(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def option(self,opt):
		"""
		option(opt)
			opt=unicode

		Returns the value related to option opt if it was set by the server
		See QAuthenticator#Options for more information on incoming options
		If option opt isnt found, an invalid PySide.QtCore.QVariant will be returned.
		"""
		res = super(QAuthenticator,self).option(opt)
		return res
	#----------------------------------------------------------------------
	def setOption(self,opt,value):
		"""
		setOption(opt,value)
			opt=unicode
			value=object

		Sets the outgoing option opt to value value
		See QAuthenticator#Options for more information on outgoing options.
		"""
		res = super(QAuthenticator,self).setOption(opt,value)
		return res
	#----------------------------------------------------------------------
	def setPassword(self,password):
		"""
		setPassword(password)
			password=unicode

		Sets the password used for authentication.
		"""
		res = super(QAuthenticator,self).setPassword(password)
		return res
	#----------------------------------------------------------------------
	def setUser(self,user):
		"""
		setUser(user)
			user=unicode

		Sets the user used for authentication.
		"""
		res = super(QAuthenticator,self).setUser(user)
		return res

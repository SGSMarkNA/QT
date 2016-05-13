from PySide import QtGui, QtCore

class QFtp(QtNetwork.QFtp):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QFtp,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def bytesAvailable(self):
		"""
		Returns the number of bytes that can be read from the data socket at the moment.
		"""
		res = super(QFtp,self).bytesAvailable()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def clearPendingCommands(self):
		"""
		Deletes all pending commands from the list of scheduled commands
		This does not affect the command that is being executed
		If you want to stop this as well, use PySide.QtNetwork.QFtp.abort() .
		"""
		res = super(QFtp,self).clearPendingCommands()
		return res
	#----------------------------------------------------------------------
	def close(self):
		"""
		Closes the connection to the FTP server.
		The PySide.QtNetwork.QFtp.stateChanged() signal is emitted when the state of the connecting process changes, e.g
		to Closing , then Unconnected .
		The function does not block and returns immediately
		The command is scheduled, and its execution is performed asynchronously
		The function returns a unique identifier which is passed by PySide.QtNetwork.QFtp.commandStarted() and PySide.QtNetwork.QFtp.commandFinished() .
		When the command is started the PySide.QtNetwork.QFtp.commandStarted() signal is emitted
		When it is finished the PySide.QtNetwork.QFtp.commandFinished() signal is emitted.
		"""
		res = super(QFtp,self).close()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def currentCommand(self):
		"""
		Returns the command type of the FTP command being executed or None if there is no command being executed.
		"""
		res = super(QFtp,self).currentCommand()
		isinstance(res,QtNetwork.QFtp.Command)
		return res
	#----------------------------------------------------------------------
	def currentDevice(self):
		"""
		Returns the PySide.QtCore.QIODevice pointer that is used by the FTP command to read data from or store data to
		If there is no current FTP command being executed or if the command does not use an IO device, this function returns 0.
		This function can be used to delete the PySide.QtCore.QIODevice in the slot connected to the PySide.QtNetwork.QFtp.commandFinished() signal.
		"""
		res = super(QFtp,self).currentDevice()
		isinstance(res,QtCore.QIODevice)
		return res
	#----------------------------------------------------------------------
	def currentId(self):
		"""
		Returns the identifier of the FTP command that is being executed or 0 if there is no command being executed.
		"""
		res = super(QFtp,self).currentId()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def error(self):
		"""
		Returns the last error that occurred
		This is useful to find out what went wrong when receiving a PySide.QtNetwork.QFtp.commandFinished() or a PySide.QtNetwork.QFtp.done() signal with the error argument set to true .
		If you start a new command, the error status is reset to NoError .
		"""
		res = super(QFtp,self).error()
		isinstance(res,QtNetwork.QFtp.Error)
		return res
	#----------------------------------------------------------------------
	def errorString(self):
		"""
		Returns a human-readable description of the last error that occurred
		This is useful for presenting a error message to the user when receiving a PySide.QtNetwork.QFtp.commandFinished() or a PySide.QtNetwork.QFtp.done() signal with the error argument set to true .
		The error string is often (but not always) the reply from the server, so it is not always possible to translate the string
		If the message comes from Qt, the string has already passed through tr() .
		"""
		res = super(QFtp,self).errorString()
		return res
	#----------------------------------------------------------------------
	def hasPendingCommands(self):
		"""
		Returns true if there are any commands scheduled that have not yet been executed; otherwise returns false.
		The command that is being executed is not considered as a scheduled command.
		"""
		res = super(QFtp,self).hasPendingCommands()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def readAll(self):
		"""
		Reads all the bytes available from the data socket and returns them.
		"""
		res = super(QFtp,self).readAll()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def readyRead(self):
		"""

		"""
		res = super(QFtp,self).readyRead()
		return res
	#----------------------------------------------------------------------
	def state(self):
		"""
		Returns the current state of the object
		When the state changes, the PySide.QtNetwork.QFtp.stateChanged() signal is emitted.
		"""
		res = super(QFtp,self).state()
		isinstance(res,QtNetwork.QFtp.State)
		return res
	#----------------------------------------------------------------------
	def cd(self,dir):
		"""
		cd(dir)
			dir=unicode

		Changes the working directory of the server to dir .
		The function does not block and returns immediately
		The command is scheduled, and its execution is performed asynchronously
		The function returns a unique identifier which is passed by PySide.QtNetwork.QFtp.commandStarted() and PySide.QtNetwork.QFtp.commandFinished() .
		When the command is started the PySide.QtNetwork.QFtp.commandStarted() signal is emitted
		When it is finished the PySide.QtNetwork.QFtp.commandFinished() signal is emitted.
		"""
		res = super(QFtp,self).cd(dir)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def connectToHost(self,host,port=None):
		"""
		connectToHost(host,port=None)
			host=unicode
			port=QtCore.quint16

		Connects to the FTP server host using port port .
		The PySide.QtNetwork.QFtp.stateChanged() signal is emitted when the state of the connecting process changes, e.g
		to HostLookup , then Connecting , then Connected .
		The function does not block and returns immediately
		The command is scheduled, and its execution is performed asynchronously
		The function returns a unique identifier which is passed by PySide.QtNetwork.QFtp.commandStarted() and PySide.QtNetwork.QFtp.commandFinished() .
		When the command is started the PySide.QtNetwork.QFtp.commandStarted() signal is emitted
		When it is finished the PySide.QtNetwork.QFtp.commandFinished() signal is emitted.
		"""
		res = super(QFtp,self).connectToHost(host,port)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def get(self,file,dev=None,type=None):
		"""
		get(file,dev=None,type=None)
			file=unicode
			dev=QtCore.QIODevice
			type=QtNetwork.QFtp.TransferType

		Downloads the file file from the server.
		If dev is 0, then the PySide.QtNetwork.QFtp.readyRead() signal is emitted when there is data available to read
		You can then read the data with the PySide.QtNetwork.QFtp.read() or PySide.QtNetwork.QFtp.readAll() functions.
		If dev is not 0, the data is written directly to the device dev
		Make sure that the dev pointer is valid for the duration of the operation (it is safe to delete it when the PySide.QtNetwork.QFtp.commandFinished() signal is emitted)
		In this case the PySide.QtNetwork.QFtp.readyRead() signal is not emitted and you cannot read data with the PySide.QtNetwork.QFtp.read() or PySide.QtNetwork.QFtp.readAll() functions.
		If you dont read the data immediately it becomes available, i.e
		when the PySide.QtNetwork.QFtp.readyRead() signal is emitted, it is still available until the next command is started.
		For example, if you want to present the data to the user as soon as there is something available, connect to the PySide.QtNetwork.QFtp.readyRead() signal and read the data immediately
		On the other hand, if you only want to work with the complete data, you can connect to the PySide.QtNetwork.QFtp.commandFinished() signal and read the data when the PySide.QtNetwork.QFtp.get() command is finished.
		The data is transferred as Binary or Ascii depending on the value of type .
		The function does not block and returns immediately
		The command is scheduled, and its execution is performed asynchronously
		The function returns a unique identifier which is passed by PySide.QtNetwork.QFtp.commandStarted() and PySide.QtNetwork.QFtp.commandFinished() .
		When the command is started the PySide.QtNetwork.QFtp.commandStarted() signal is emitted
		When it is finished the PySide.QtNetwork.QFtp.commandFinished() signal is emitted.
		PySide.QtNetwork.QFtp.commandFinished()
		"""
		res = super(QFtp,self).get(file,dev,type)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def list(self,dir=None):
		"""
		list(dir=None)
			dir=unicode

		Lists the contents of directory dir on the FTP server
		If dir is empty, it lists the contents of the current directory.
		The PySide.QtNetwork.QFtp.listInfo() signal is emitted for each directory entry found.
		The function does not block and returns immediately
		The command is scheduled, and its execution is performed asynchronously
		The function returns a unique identifier which is passed by PySide.QtNetwork.QFtp.commandStarted() and PySide.QtNetwork.QFtp.commandFinished() .
		When the command is started the PySide.QtNetwork.QFtp.commandStarted() signal is emitted
		When it is finished the PySide.QtNetwork.QFtp.commandFinished() signal is emitted.
		"""
		res = super(QFtp,self).list(dir)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def login(self,user=None,password=None):
		"""
		login(user=None,password=None)
			user=unicode
			password=unicode

		Logs in to the FTP server with the username user and the password password .
		The PySide.QtNetwork.QFtp.stateChanged() signal is emitted when the state of the connecting process changes, e.g
		to LoggedIn .
		The function does not block and returns immediately
		The command is scheduled, and its execution is performed asynchronously
		The function returns a unique identifier which is passed by PySide.QtNetwork.QFtp.commandStarted() and PySide.QtNetwork.QFtp.commandFinished() .
		When the command is started the PySide.QtNetwork.QFtp.commandStarted() signal is emitted
		When it is finished the PySide.QtNetwork.QFtp.commandFinished() signal is emitted.
		"""
		res = super(QFtp,self).login(user,password)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def mkdir(self,dir):
		"""
		mkdir(dir)
			dir=unicode

		Creates a directory called dir on the server.
		The function does not block and returns immediately
		The command is scheduled, and its execution is performed asynchronously
		The function returns a unique identifier which is passed by PySide.QtNetwork.QFtp.commandStarted() and PySide.QtNetwork.QFtp.commandFinished() .
		When the command is started the PySide.QtNetwork.QFtp.commandStarted() signal is emitted
		When it is finished the PySide.QtNetwork.QFtp.commandFinished() signal is emitted.
		"""
		res = super(QFtp,self).mkdir(dir)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def put(self,*args,**kwargs):
		"""
		put(dev,file,type=None)
			dev=QtCore.QIODevice
			file=unicode
			type=QtNetwork.QFtp.TransferType

		put(data,file,type=None)
			data=QtCore.QByteArray
			file=unicode
			type=QtNetwork.QFtp.TransferType

		Reads the data from the IO device dev , and writes it to the file called file on the server
		The data is read in chunks from the IO device, so this overload allows you to transmit large amounts of data without the need to read all the data into memory at once.
		The data is transferred as Binary or Ascii depending on the value of type .
		Make sure that the dev pointer is valid for the duration of the operation (it is safe to delete it when the PySide.QtNetwork.QFtp.commandFinished() is emitted).
		"""
		res = super(QFtp,self).put(*args,**kwargs)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def rawCommand(self,command):
		"""
		rawCommand(command)
			command=unicode

		Sends the raw FTP command command to the FTP server
		This is useful for low-level FTP access
		If the operation you wish to perform has an equivalent PySide.QtNetwork.QFtp function, we recommend using the function instead of raw FTP commands since the functions are easier and safer.
		The function does not block and returns immediately
		The command is scheduled, and its execution is performed asynchronously
		The function returns a unique identifier which is passed by PySide.QtNetwork.QFtp.commandStarted() and PySide.QtNetwork.QFtp.commandFinished() .
		When the command is started the PySide.QtNetwork.QFtp.commandStarted() signal is emitted
		When it is finished the PySide.QtNetwork.QFtp.commandFinished() signal is emitted.
		"""
		res = super(QFtp,self).rawCommand(command)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def read(self,maxlen):
		"""
		read(maxlen)
			maxlen=QtCore.qint64

		Reads maxlen bytes from the data socket into data and returns the number of bytes read
		Returns -1 if an error occurred.
		"""
		res = super(QFtp,self).read(maxlen)
		return res
	#----------------------------------------------------------------------
	def remove(self,file):
		"""
		remove(file)
			file=unicode

		Deletes the file called file from the server.
		The function does not block and returns immediately
		The command is scheduled, and its execution is performed asynchronously
		The function returns a unique identifier which is passed by PySide.QtNetwork.QFtp.commandStarted() and PySide.QtNetwork.QFtp.commandFinished() .
		When the command is started the PySide.QtNetwork.QFtp.commandStarted() signal is emitted
		When it is finished the PySide.QtNetwork.QFtp.commandFinished() signal is emitted.
		"""
		res = super(QFtp,self).remove(file)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def rename(self,oldname,newname):
		"""
		rename(oldname,newname)
			oldname=unicode
			newname=unicode

		Renames the file called oldname to newname on the server.
		The function does not block and returns immediately
		The command is scheduled, and its execution is performed asynchronously
		The function returns a unique identifier which is passed by PySide.QtNetwork.QFtp.commandStarted() and PySide.QtNetwork.QFtp.commandFinished() .
		When the command is started the PySide.QtNetwork.QFtp.commandStarted() signal is emitted
		When it is finished the PySide.QtNetwork.QFtp.commandFinished() signal is emitted.
		"""
		res = super(QFtp,self).rename(oldname,newname)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def rmdir(self,dir):
		"""
		rmdir(dir)
			dir=unicode

		Removes the directory called dir from the server.
		The function does not block and returns immediately
		The command is scheduled, and its execution is performed asynchronously
		The function returns a unique identifier which is passed by PySide.QtNetwork.QFtp.commandStarted() and PySide.QtNetwork.QFtp.commandFinished() .
		When the command is started the PySide.QtNetwork.QFtp.commandStarted() signal is emitted
		When it is finished the PySide.QtNetwork.QFtp.commandFinished() signal is emitted.
		"""
		res = super(QFtp,self).rmdir(dir)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def setProxy(self,host,port):
		"""
		setProxy(host,port)
			host=unicode
			port=QtCore.quint16

		Enables use of the FTP proxy on host host and port port
		Calling this function with host empty disables proxying.
		PySide.QtNetwork.QFtp does not support FTP-over-HTTP proxy servers
		Use PySide.QtNetwork.QNetworkAccessManager for this.
		"""
		res = super(QFtp,self).setProxy(host,port)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def setTransferMode(self,mode):
		"""
		setTransferMode(mode)
			mode=QtNetwork.QFtp.TransferMode

		Sets the current FTP transfer mode to mode
		The default is QFtp.Passive .
		"""
		res = super(QFtp,self).setTransferMode(mode)
		isinstance(res,QtCore.int)
		return res

from PySide import QtGui, QtCore

class QProcess(QtCore.QProcess):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QProcess,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def closeWriteChannel(self):
		"""
		Schedules the write channel of PySide.QtCore.QProcess to be closed
		The channel will close once all data has been written to the process
		After calling this function, any attempts to write to the process will fail.
		Closing the write channel is necessary for programs that read input data until the channel has been closed
		For example, the program more is used to display text data in a console on both Unix and Windows
		But it will not display the text data until PySide.QtCore.QProcess s write channel has been closed
		Example:
		The write channel is implicitly opened when PySide.QtCore.QProcess.start() is called.
		"""
		res = super(QProcess,self).closeWriteChannel()
		return res
	#----------------------------------------------------------------------
	def environment(self):
		"""
		Returns the environment that PySide.QtCore.QProcess will use when starting a process, or an empty PySide.QtCore.QStringList if no environment has been set using PySide.QtCore.QProcess.setEnvironment() or setEnvironmentHash()
		If no environment has been set, the environment of the calling process will be used.
		"""
		res = super(QProcess,self).environment()
		return res
	#----------------------------------------------------------------------
	def error(self):
		"""
		Returns the type of error that occurred last.
		"""
		res = super(QProcess,self).error()
		isinstance(res,QtCore.QProcess.ProcessError)
		return res
	#----------------------------------------------------------------------
	def exitCode(self):
		"""
		Returns the exit code of the last process that finished.
		"""
		res = super(QProcess,self).exitCode()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def exitStatus(self):
		"""
		Returns the exit status of the last process that finished.
		On Windows, if the process was terminated with TerminateProcess() from another application this function will still return NormalExit unless the exit code is less than 0.
		"""
		res = super(QProcess,self).exitStatus()
		isinstance(res,QtCore.QProcess.ExitStatus)
		return res
	#----------------------------------------------------------------------
	def processChannelMode(self):
		"""
		Returns the channel mode of the PySide.QtCore.QProcess standard output and standard error channels.
		"""
		res = super(QProcess,self).processChannelMode()
		isinstance(res,QtCore.QProcess.ProcessChannelMode)
		return res
	#----------------------------------------------------------------------
	def processEnvironment(self):
		"""
		Returns the environment that PySide.QtCore.QProcess will use when starting a process, or an empty object if no environment has been set using PySide.QtCore.QProcess.setEnvironment() or PySide.QtCore.QProcess.setProcessEnvironment()
		If no environment has been set, the environment of the calling process will be used.
		"""
		res = super(QProcess,self).processEnvironment()
		isinstance(res,QtCore.QProcessEnvironment)
		return res
	#----------------------------------------------------------------------
	def readAllStandardError(self):
		"""
		Regardless of the current read channel, this function returns all data available from the standard error of the process as a PySide.QtCore.QByteArray .
		"""
		res = super(QProcess,self).readAllStandardError()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def readAllStandardOutput(self):
		"""
		Regardless of the current read channel, this function returns all data available from the standard output of the process as a PySide.QtCore.QByteArray .
		"""
		res = super(QProcess,self).readAllStandardOutput()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def readChannel(self):
		"""
		Returns the current read channel of the PySide.QtCore.QProcess .
		"""
		res = super(QProcess,self).readChannel()
		isinstance(res,QtCore.QProcess.ProcessChannel)
		return res
	#----------------------------------------------------------------------
	def readyReadStandardError(self):
		"""

		"""
		res = super(QProcess,self).readyReadStandardError()
		return res
	#----------------------------------------------------------------------
	def readyReadStandardOutput(self):
		"""

		"""
		res = super(QProcess,self).readyReadStandardOutput()
		return res
	#----------------------------------------------------------------------
	def setupChildProcess(self):
		"""
		This function is called in the child process context just before the program is executed on Unix or Mac OS X (i.e., after fork() , but before execve() )
		Reimplement this function to do last minute initialization of the child process
		Example:
		You cannot exit the process (by calling exit(), for instance) from this function
		If you need to stop the program before it starts execution, your workaround is to emit PySide.QtCore.QProcess.finished() and then call exit().
		"""
		res = super(QProcess,self).setupChildProcess()
		return res
	#----------------------------------------------------------------------
	def started(self):
		"""

		"""
		res = super(QProcess,self).started()
		return res
	#----------------------------------------------------------------------
	def state(self):
		"""
		Returns the current state of the process.
		"""
		res = super(QProcess,self).state()
		isinstance(res,QtCore.QProcess.ProcessState)
		return res
	#----------------------------------------------------------------------
	def workingDirectory(self):
		"""
		If PySide.QtCore.QProcess has been assigned a working directory, this function returns the working directory that the PySide.QtCore.QProcess will enter before the program has started
		Otherwise, (i.e., no directory has been assigned,) an empty string is returned, and PySide.QtCore.QProcess will use the applications current working directory instead.
		"""
		res = super(QProcess,self).workingDirectory()
		return res
	#----------------------------------------------------------------------
	def closeReadChannel(self,channel):
		"""
		closeReadChannel(channel)
			channel=QtCore.QProcess.ProcessChannel

		Closes the read channel channel
		After calling this function, PySide.QtCore.QProcess will no longer receive data on the channel
		Any data that has already been received is still available for reading.
		Call this function to save memory, if you are not interested in the output of the process.
		"""
		res = super(QProcess,self).closeReadChannel(channel)
		return res
	#----------------------------------------------------------------------
	def error(self,error):
		"""
		error(error)
			error=QtCore.QProcess.ProcessError


		"""
		res = super(QProcess,self).error(error)
		return res
	#----------------------------------------------------------------------
	def setEnvironment(self,environment):
		"""
		setEnvironment(environment)
			environment=list

		Sets the environment that PySide.QtCore.QProcess will use when starting a process to the environment specified which consists of a list of key=value pairs.
		For example, the following code adds the C:\\BIN directory to the list of executable paths (PATHS ) on Windows:
		"""
		res = super(QProcess,self).setEnvironment(environment)
		return res
	#----------------------------------------------------------------------
	def setProcessChannelMode(self,mode):
		"""
		setProcessChannelMode(mode)
			mode=QtCore.QProcess.ProcessChannelMode

		Sets the channel mode of the PySide.QtCore.QProcess standard output and standard error channels to the mode specified
		This mode will be used the next time PySide.QtCore.QProcess.start() is called
		For example:
		"""
		res = super(QProcess,self).setProcessChannelMode(mode)
		return res
	#----------------------------------------------------------------------
	def setProcessEnvironment(self,environment):
		"""
		setProcessEnvironment(environment)
			environment=QtCore.QProcessEnvironment

		Sets the environment that PySide.QtCore.QProcess will use when starting a process to the environment object.
		For example, the following code adds the C:\\BIN directory to the list of executable paths (PATHS ) on Windows and sets TMPDIR :
		Note how, on Windows, environment variable names are case-insensitive.
		"""
		res = super(QProcess,self).setProcessEnvironment(environment)
		return res
	#----------------------------------------------------------------------
	def setProcessState(self,state):
		"""
		setProcessState(state)
			state=QtCore.QProcess.ProcessState

		Sets the current state of the PySide.QtCore.QProcess to the state specified.
		"""
		res = super(QProcess,self).setProcessState(state)
		return res
	#----------------------------------------------------------------------
	def setReadChannel(self,channel):
		"""
		setReadChannel(channel)
			channel=QtCore.QProcess.ProcessChannel

		Sets the current read channel of the PySide.QtCore.QProcess to the given channel
		The current input channel is used by the functions PySide.QtCore.QIODevice.read() , PySide.QtCore.QIODevice.readAll() , PySide.QtCore.QIODevice.readLine() , and PySide.QtCore.QIODevice.getChar()
		It also determines which channel triggers PySide.QtCore.QProcess to emit PySide.QtCore.QIODevice.readyRead() .
		"""
		res = super(QProcess,self).setReadChannel(channel)
		return res
	#----------------------------------------------------------------------
	def setStandardErrorFile(self,fileName,mode=None):
		"""
		setStandardErrorFile(fileName,mode=None)
			fileName=unicode
			mode=QtCore.QIODevice.OpenMode


		"""
		res = super(QProcess,self).setStandardErrorFile(fileName,mode)
		return res
	#----------------------------------------------------------------------
	def setStandardInputFile(self,fileName):
		"""
		setStandardInputFile(fileName)
			fileName=unicode

		Redirects the process standard input to the file indicated by fileName
		When an input redirection is in place, the PySide.QtCore.QProcess object will be in read-only mode (calling PySide.QtCore.QIODevice.write() will result in error).
		If the file fileName does not exist at the moment PySide.QtCore.QProcess.start() is called or is not readable, starting the process will fail.
		Calling PySide.QtCore.QProcess.setStandardInputFile() after the process has started has no effect.
		"""
		res = super(QProcess,self).setStandardInputFile(fileName)
		return res
	#----------------------------------------------------------------------
	def setStandardOutputFile(self,fileName,mode=None):
		"""
		setStandardOutputFile(fileName,mode=None)
			fileName=unicode
			mode=QtCore.QIODevice.OpenMode


		"""
		res = super(QProcess,self).setStandardOutputFile(fileName,mode)
		return res
	#----------------------------------------------------------------------
	def setStandardOutputProcess(self,destination):
		"""
		setStandardOutputProcess(destination)
			destination=QtCore.QProcess

		Pipes the standard output stream of this process to the destination process standard input.
		The following shell command:
		Can be accomplished with QProcesses with the following code:
		"""
		res = super(QProcess,self).setStandardOutputProcess(destination)
		return res
	#----------------------------------------------------------------------
	def setWorkingDirectory(self,dir):
		"""
		setWorkingDirectory(dir)
			dir=unicode

		Sets the working directory to dir
		PySide.QtCore.QProcess will start the process in this directory
		The default behavior is to start the process in the working directory of the calling process.
		"""
		res = super(QProcess,self).setWorkingDirectory(dir)
		return res
	#----------------------------------------------------------------------
	def start(self,*args,**kwargs):
		"""
		start(program,mode=None)
			program=unicode
			mode=QtCore.QIODevice.OpenMode

		start(program,arguments,mode=None)
			program=unicode
			arguments=list
			mode=QtCore.QIODevice.OpenMode


		"""
		res = super(QProcess,self).start(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def waitForFinished(self,msecs=None):
		"""
		waitForFinished(msecs=None)
			msecs=QtCore.int

		Blocks until the process has finished and the PySide.QtCore.QProcess.finished() signal has been emitted, or until msecs milliseconds have passed.
		Returns true if the process finished; otherwise returns false (if the operation timed out, if an error occurred, or if this PySide.QtCore.QProcess is already finished).
		This function can operate without an event loop
		It is useful when writing non-GUI applications and when performing I/O operations in a non-GUI thread.
		If msecs is -1, this function will not time out.
		"""
		res = super(QProcess,self).waitForFinished(msecs)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def waitForStarted(self,msecs=None):
		"""
		waitForStarted(msecs=None)
			msecs=QtCore.int

		Blocks until the process has started and the PySide.QtCore.QProcess.started() signal has been emitted, or until msecs milliseconds have passed.
		Returns true if the process was started successfully; otherwise returns false (if the operation timed out or if an error occurred).
		This function can operate without an event loop
		It is useful when writing non-GUI applications and when performing I/O operations in a non-GUI thread.
		If msecs is -1, this function will not time out.
		"""
		res = super(QProcess,self).waitForStarted(msecs)
		isinstance(res,bool)
		return res

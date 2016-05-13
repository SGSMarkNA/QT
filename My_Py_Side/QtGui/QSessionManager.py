from PySide import QtGui, QtCore

class QSessionManager(QtGui.QSessionManager):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSessionManager,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def allowsErrorInteraction(self):
		"""
		Returns true if error interaction is permitted; otherwise returns false.
		This is similar to PySide.QtGui.QSessionManager.allowsInteraction() , but also enables the application to tell the user about any errors that occur
		Session managers may give error interaction requests higher priority, which means that it is more likely that an error interaction is permitted
		However, you are still not guaranteed that the session manager will allow interaction.
		"""
		res = super(QSessionManager,self).allowsErrorInteraction()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def allowsInteraction(self):
		"""
		Asks the session manager for permission to interact with the user
		Returns true if interaction is permitted; otherwise returns false.
		The rationale behind this mechanism is to make it possible to synchronize user interaction during a shutdown
		Advanced session managers may ask all applications simultaneously to commit their data, resulting in a much faster shutdown.
		When the interaction is completed we strongly recommend releasing the user interaction semaphore with a call to PySide.QtGui.QSessionManager.release()
		This way, other applications may get the chance to interact with the user while your application is still busy saving data
		(The semaphore is implicitly released when the application exits.)
		If the user decides to cancel the shutdown process during the interaction phase, you must tell the session manager that this has happened by calling PySide.QtGui.QSessionManager.cancel() .
		Heres an example of how an applications QApplication.commitData() might be implemented:
		If an error occurred within the application while saving its data, you may want to try PySide.QtGui.QSessionManager.allowsErrorInteraction() instead.
		"""
		res = super(QSessionManager,self).allowsInteraction()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def cancel(self):
		"""
		Tells the session manager to cancel the shutdown process
		Applications should not call this function without asking the user first.
		"""
		res = super(QSessionManager,self).cancel()
		return res
	#----------------------------------------------------------------------
	def discardCommand(self):
		"""
		Returns the currently set discard command.
		To iterate over the list, you can use the foreach pseudo-keyword:
		"""
		res = super(QSessionManager,self).discardCommand()
		return res
	#----------------------------------------------------------------------
	def isPhase2(self):
		"""
		Returns true if the session manager is currently performing a second session management phase; otherwise returns false.
		"""
		res = super(QSessionManager,self).isPhase2()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def release(self):
		"""
		Releases the session managers interaction semaphore after an interaction phase.
		"""
		res = super(QSessionManager,self).release()
		return res
	#----------------------------------------------------------------------
	def requestPhase2(self):
		"""
		Requests a second session management phase for the application
		The application may then return immediately from the QApplication.commitData() or QApplication.saveState() function, and they will be called again once most or all other applications have finished their session management.
		The two phases are useful for applications such as the X11 window manager that need to store information about another applications windows and therefore have to wait until these applications have completed their respective session management tasks.
		"""
		res = super(QSessionManager,self).requestPhase2()
		return res
	#----------------------------------------------------------------------
	def restartCommand(self):
		"""
		Returns the currently set restart command.
		To iterate over the list, you can use the foreach pseudo-keyword:
		"""
		res = super(QSessionManager,self).restartCommand()
		return res
	#----------------------------------------------------------------------
	def restartHint(self):
		"""
		Returns the applications current restart hint
		The default is RestartIfRunning .
		"""
		res = super(QSessionManager,self).restartHint()
		isinstance(res,QtGui.QSessionManager.RestartHint)
		return res
	#----------------------------------------------------------------------
	def sessionId(self):
		"""
		Returns the identifier of the current session.
		If the application has been restored from an earlier session, this identifier is the same as it was in the earlier session.
		"""
		res = super(QSessionManager,self).sessionId()
		return res
	#----------------------------------------------------------------------
	def sessionKey(self):
		"""
		Returns the session key in the current session.
		If the application has been restored from an earlier session, this key is the same as it was when the previous session ended.
		The session key changes with every call of commitData() or saveState().
		"""
		res = super(QSessionManager,self).sessionKey()
		return res
	#----------------------------------------------------------------------
	def setDiscardCommand(self,arg__1):
		"""
		setDiscardCommand(arg__1)
			arg__1=list

		Sets the discard command to the given list .
		"""
		res = super(QSessionManager,self).setDiscardCommand(arg__1)
		return res
	#----------------------------------------------------------------------
	def setManagerProperty(self,*args,**kwargs):
		"""
		setManagerProperty(name,value)
			name=unicode
			value=list

		setManagerProperty(name,value)
			name=unicode
			value=unicode

		Low-level write access to the applications identification and state record are kept in the session manager.
		The property called name has its value set to the string list value .
		"""
		res = super(QSessionManager,self).setManagerProperty(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setRestartCommand(self,arg__1):
		"""
		setRestartCommand(arg__1)
			arg__1=list

		If the session manager is capable of restoring sessions it will execute command in order to restore the application
		The command defaults to
		The -session option is mandatory; otherwise PySide.QtGui.QApplication cannot tell whether it has been restored or what the current session identifier is
		See QApplication.isSessionRestored() and QApplication.sessionId() for details.
		If your application is very simple, it may be possible to store the entire application state in additional command line options
		This is usually a very bad idea because command lines are often limited to a few hundred bytes
		Instead, use PySide.QtCore.QSettings , temporary files, or a database for this purpose
		By marking the data with the unique PySide.QtGui.QSessionManager.sessionId() , you will be able to restore the application in a future session.
		"""
		res = super(QSessionManager,self).setRestartCommand(arg__1)
		return res
	#----------------------------------------------------------------------
	def setRestartHint(self,arg__1):
		"""
		setRestartHint(arg__1)
			arg__1=QtGui.QSessionManager.RestartHint

		Sets the applications restart hint to hint
		On application startup, the hint is set to RestartIfRunning .
		We recommend setting the restart hint in QApplication.saveState() because most session managers perform a checkpoint shortly after an applications startup.
		"""
		res = super(QSessionManager,self).setRestartHint(arg__1)
		return res

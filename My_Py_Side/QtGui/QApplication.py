from PySide import QtGui, QtCore

class QApplication(QtGui.QApplication):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QApplication,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def fontDatabaseChanged(self):
		"""

		"""
		res = super(QApplication,self).fontDatabaseChanged()
		return res
	#----------------------------------------------------------------------
	def inputContext(self):
		"""
		Returns the PySide.QtGui.QInputContext instance used by the application.
		"""
		res = super(QApplication,self).inputContext()
		isinstance(res,QtGui.QInputContext)
		return res
	#----------------------------------------------------------------------
	def isSessionRestored(self):
		"""
		Returns true if the application has been restored from an earlier session ; otherwise returns false.
		"""
		res = super(QApplication,self).isSessionRestored()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def lastWindowClosed(self):
		"""

		"""
		res = super(QApplication,self).lastWindowClosed()
		return res
	#----------------------------------------------------------------------
	def sessionId(self):
		"""
		Returns the current sessions identifier.
		If the application has been restored from an earlier session, this identifier is the same as it was in that previous session
		The session identifier is guaranteed to be unique both for different applications and for different instances of the same application.
		"""
		res = super(QApplication,self).sessionId()
		return res
	#----------------------------------------------------------------------
	def sessionKey(self):
		"""
		Returns the session key in the current session .
		If the application has been restored from an earlier session, this key is the same as it was when the previous session ended.
		The session key changes with every call of PySide.QtGui.QApplication.commitData() or PySide.QtGui.QApplication.saveState() .
		"""
		res = super(QApplication,self).sessionKey()
		return res
	#----------------------------------------------------------------------
	def styleSheet(self):
		"""
		This property holds the application style sheet.
		By default, this property returns an empty string unless the user specifies the -stylesheet option on the command line when running the application.
		"""
		res = super(QApplication,self).styleSheet()
		return res
	#----------------------------------------------------------------------
	def commitData(self,sm):
		"""
		commitData(sm)
			sm=QtGui.QSessionManager

		This function deals with session management
		It is invoked when the PySide.QtGui.QSessionManager wants the application to commit all its data.
		Usually this means saving all open files, after getting permission from the user
		Furthermore you may want to provide a means by which the user can cancel the shutdown.
		You should not exit the application within this function
		Instead, the session manager may or may not do this afterwards, depending on the context.
		The default implementation requests interaction and sends a close event to all visible top-level widgets
		If any event was rejected, the shutdown is canceled.
		"""
		res = super(QApplication,self).commitData(sm)
		return res
	#----------------------------------------------------------------------
	def saveState(self,sm):
		"""
		saveState(sm)
			sm=QtGui.QSessionManager

		This function deals with session management
		It is invoked when the session manager wants the application to preserve its state for a future session.
		For example, a text editor would create a temporary file that includes the current contents of its edit buffers, the location of the cursor and other aspects of the current editing session.
		You should never exit the application within this function
		Instead, the session manager may or may not do this afterwards, depending on the context
		Futhermore, most session managers will very likely request a saved state immediately after the application has been started
		This permits the session manager to learn about the applications restart policy.
		"""
		res = super(QApplication,self).saveState(sm)
		return res
	#----------------------------------------------------------------------
	def setInputContext(self,arg__1):
		"""
		setInputContext(arg__1)
			arg__1=QtGui.QInputContext

		This function replaces the PySide.QtGui.QInputContext instance used by the application with inputContext .
		Qt takes ownership of the given inputContext .
		"""
		res = super(QApplication,self).setInputContext(arg__1)
		return res

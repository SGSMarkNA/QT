from PySide import QtGui, QtCore

class QScriptEngineDebugger(QtScriptTools.QScriptEngineDebugger):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QScriptEngineDebugger,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def autoShowStandardWindow(self):
		"""
		Returns whether the standard debugger window is automatically shown when evaluation is suspended.
		The default is true.
		"""
		res = super(QScriptEngineDebugger,self).autoShowStandardWindow()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def evaluationResumed(self):
		"""

		"""
		res = super(QScriptEngineDebugger,self).evaluationResumed()
		return res
	#----------------------------------------------------------------------
	def evaluationSuspended(self):
		"""

		"""
		res = super(QScriptEngineDebugger,self).evaluationSuspended()
		return res
	#----------------------------------------------------------------------
	def standardWindow(self):
		"""
		Returns a main window with a standard configuration of the debuggers components.
		"""
		res = super(QScriptEngineDebugger,self).standardWindow()
		isinstance(res,QtGui.QMainWindow)
		return res
	#----------------------------------------------------------------------
	def state(self):
		"""
		Returns the current state of the debugger.
		"""
		res = super(QScriptEngineDebugger,self).state()
		isinstance(res,QtScriptTools.QScriptEngineDebugger.DebuggerState)
		return res
	#----------------------------------------------------------------------
	def action(self,action):
		"""
		action(action)
			action=QtScriptTools.QScriptEngineDebugger.DebuggerAction

		Returns a pointer to the specified action
		The actions available are given by the QScriptEngineDebugger.DebuggerAction enum.
		With this function, you can add the actions to your own widgets, toolbars, and menus
		It is also convenient if you, for example, wish to spice things up with your own groovy icons
		The code example below shows how to add actions to a PySide.QtGui.QToolBar .
		Note that PySide.QtScriptTools.QScriptEngineDebugger has already added the actions to its standard widgets and standard window .
		"""
		res = super(QScriptEngineDebugger,self).action(action)
		isinstance(res,QtGui.QAction)
		return res
	#----------------------------------------------------------------------
	def attachTo(self,engine):
		"""
		attachTo(engine)
			engine=QtScript.QScriptEngine

		Attaches to the given engine .
		The debugger will install a custom agent (using QScriptEngine.setAgent() ) to monitor the engine
		While the debugger is attached, you should not change the agent; however, if you do have to perform additional monitoring, you must set a proxy agent that forwards all events to the debuggers agent.
		"""
		res = super(QScriptEngineDebugger,self).attachTo(engine)
		return res
	#----------------------------------------------------------------------
	def createStandardMenu(self,parent=None):
		"""
		createStandardMenu(parent=None)
			parent=QtGui.QWidget

		Creates a standard debugger menu with the given parent
		Returns the new menu object.
		"""
		res = super(QScriptEngineDebugger,self).createStandardMenu(parent)
		isinstance(res,QtGui.QMenu)
		return res
	#----------------------------------------------------------------------
	def createStandardToolBar(self,parent=None):
		"""
		createStandardToolBar(parent=None)
			parent=QtGui.QWidget

		Creates a standard debugger toolbar with the given parent
		Returns the new toolbar object.
		"""
		res = super(QScriptEngineDebugger,self).createStandardToolBar(parent)
		isinstance(res,QtGui.QToolBar)
		return res
	#----------------------------------------------------------------------
	def setAutoShowStandardWindow(self,autoShow):
		"""
		setAutoShowStandardWindow(autoShow)
			autoShow=QtCore.bool

		Sets whether the standard debugger window is automatically shown when evaluation is suspended
		If autoShow is true, the window will be automatically shown, otherwise it will not.
		"""
		res = super(QScriptEngineDebugger,self).setAutoShowStandardWindow(autoShow)
		return res
	#----------------------------------------------------------------------
	def widget(self,widget):
		"""
		widget(widget)
			widget=QtScriptTools.QScriptEngineDebugger.DebuggerWidget

		Returns a pointer to the instance of the specified standard widget
		The widgets available are defined by the QScriptEngineDebugger.DebuggerWidget enum.
		A main window containing all widgets is returned by PySide.QtScriptTools.QScriptEngineDebugger.standardWindow()
		If you do not want to use this window, you can fetch the individual widgets with this function
		For instance, the code example below shows how to set up a layout containing a code window and a stack widget .
		Note that you need to set PySide.QtScriptTools.QScriptEngineDebugger.setAutoShowStandardWindow() to false; if not, the standard window will be shown regardless.
		"""
		res = super(QScriptEngineDebugger,self).widget(widget)
		isinstance(res,QtGui.QWidget)
		return res

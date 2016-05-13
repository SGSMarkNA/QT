from PySide import QtGui, QtCore

class QWidgetAction(QtGui.QWidgetAction):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QWidgetAction,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def createdWidgets(self):
		"""
		Returns the list of widgets that have been using PySide.QtGui.QWidgetAction.createWidget() and are currently in use by widgets the action has been added to.
		"""
		res = super(QWidgetAction,self).createdWidgets()
		return res
	#----------------------------------------------------------------------
	def defaultWidget(self):
		"""
		Returns the default widget.
		"""
		res = super(QWidgetAction,self).defaultWidget()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def createWidget(self,parent):
		"""
		createWidget(parent)
			parent=QtGui.QWidget

		This function is called whenever the action is added to a container widget that supports custom widgets
		If you dont want a custom widget to be used as representation of the action in the specified parent widget then 0 should be returned.
		"""
		res = super(QWidgetAction,self).createWidget(parent)
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def deleteWidget(self,widget):
		"""
		deleteWidget(widget)
			widget=QtGui.QWidget

		This function is called whenever the action is removed from a container widget that displays the action using a custom widget previously created using PySide.QtGui.QWidgetAction.createWidget()
		The default implementation hides the widget and schedules it for deletion using QObject.deleteLater() .
		"""
		res = super(QWidgetAction,self).deleteWidget(widget)
		return res
	#----------------------------------------------------------------------
	def releaseWidget(self,widget):
		"""
		releaseWidget(widget)
			widget=QtGui.QWidget

		Releases the specified widget .
		Container widgets that support actions call this function when a widget action is removed.
		"""
		res = super(QWidgetAction,self).releaseWidget(widget)
		return res
	#----------------------------------------------------------------------
	def requestWidget(self,parent):
		"""
		requestWidget(parent)
			parent=QtGui.QWidget

		Returns a widget that represents the action, with the given parent .
		Container widgets that support actions can call this function to request a widget as visual representation of the action.
		"""
		res = super(QWidgetAction,self).requestWidget(parent)
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def setDefaultWidget(self,w):
		"""
		setDefaultWidget(w)
			w=QtGui.QWidget

		Sets widget to be the default widget
		The ownership is transferred to PySide.QtGui.QWidgetAction
		Unless PySide.QtGui.QWidgetAction.createWidget() is reimplemented by a subclass to return a new widget the default widget is used when a container widget requests a widget through PySide.QtGui.QWidgetAction.requestWidget() .
		"""
		res = super(QWidgetAction,self).setDefaultWidget(w)
		return res

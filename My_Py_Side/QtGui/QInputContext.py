from PySide import QtGui, QtCore

class QInputContext(QtGui.QInputContext):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QInputContext,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def actions(self):
		"""
		This is a preliminary interface for Qt 4.
		"""
		res = super(QInputContext,self).actions()
		return res
	#----------------------------------------------------------------------
	def focusWidget(self):
		"""
		Returns the widget that has an input focus for this input context.
		The return value may differ from holderWidget() if the input context is shared between several text widgets.
		"""
		res = super(QInputContext,self).focusWidget()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def font(self):
		"""
		Returns the font of the current input widget
		"""
		res = super(QInputContext,self).font()
		isinstance(res,QtGui.QFont)
		return res
	#----------------------------------------------------------------------
	def identifierName(self):
		"""
		This function must be implemented in any subclasses to return the identifier name of the input method.
		Return value is the name to identify and specify input methods for the input method switching mechanism and so on
		The name has to be consistent with QInputContextPlugin.keys()
		The name has to consist of ASCII characters only.
		There are two different names with different responsibility in the input method domain
		This function returns one of them
		Another name is called display name that stands for the name for endusers appeared in a menu and so on.
		"""
		res = super(QInputContext,self).identifierName()
		return res
	#----------------------------------------------------------------------
	def isComposing(self):
		"""
		This function indicates whether InputMethodStart event had been sent to the current focus widget
		It is ensured that an input context can send InputMethodCompose or InputMethodEnd event safely if this function returned true.
		The state is automatically being tracked through PySide.QtGui.QInputContext.sendEvent() .
		"""
		res = super(QInputContext,self).isComposing()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def language(self):
		"""
		This function must be implemented in any subclasses to return a language code (e.g
		zh_CN, zh_TW, zh_HK, ja, ko, ...) of the input context
		If the input context can handle multiple languages, return the currently used one
		The name has to be consistent with QInputContextPlugin::language().
		This information will be used by language tagging feature in PySide.QtGui.QInputMethodEvent
		It is required to distinguish unified han characters correctly
		It enables proper font and character code handling
		Suppose CJK-awared multilingual web browser (that automatically modifies fonts in CJK-mixed text) and XML editor (that automatically inserts lang attr).
		"""
		res = super(QInputContext,self).language()
		return res
	#----------------------------------------------------------------------
	def reset(self):
		"""
		This function can be reimplemented in a subclass to reset the state of the input method.
		This function is called by several widgets to reset input state
		For example, a text widget call this function before inserting a text to make widget ready to accept a text.
		Default implementation is sufficient for simple input method
		You can override this function to reset external input method engines in complex input method
		In the case, call QInputContext.reset() to ensure proper termination of inputting.
		You must not send any PySide.QtGui.QInputMethodEvent except empty InputMethodEnd event using QInputContext.reset() at reimplemented PySide.QtGui.QInputContext.reset()
		It will break input state consistency.
		"""
		res = super(QInputContext,self).reset()
		return res
	#----------------------------------------------------------------------
	def update(self):
		"""
		This virtual function is called when a state in the focus widget has changed
		PySide.QtGui.QInputContext can then use QWidget.inputMethodQuery() to query the new state of the widget.
		"""
		res = super(QInputContext,self).update()
		return res
	#----------------------------------------------------------------------
	def filterEvent(self,event):
		"""
		filterEvent(event)
			event=QtCore.QEvent

		This function can be reimplemented in a subclass to filter input events.
		Return true if the event has been consumed
		Otherwise, the unfiltered event will be forwarded to widgets as ordinary way
		Although the input events have accept() and ignore() methods, leave it untouched.
		event is currently restricted to events of these types:
		But some input method related events such as PySide.QtGui.QWheelEvent or PySide.QtGui.QTabletEvent may be added in future.
		The filtering opportunity is always given to the input context as soon as possible
		It has to be taken place before any other key event consumers such as eventfilters and accelerators because some input methods require quite various key combination and sequences
		It often conflicts with accelerators and so on, so we must give the input context the filtering opportunity first to ensure all input methods work properly regardless of application design.
		Ordinary input methods require discrete key events to work properly, so Qts key compression is always disabled for any input contexts.
		"""
		res = super(QInputContext,self).filterEvent(event)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def mouseHandler(self,x,event):
		"""
		mouseHandler(x,event)
			x=QtCore.int
			event=QtGui.QMouseEvent

		This function can be reimplemented in a subclass to handle mouse press, release, double-click, and move events within the preedit text
		You can use the function to implement mouse-oriented user interface such as text selection or popup menu for candidate selection.
		The x parameter is the offset within the string that was sent with the InputMethodCompose event
		The alteration boundary of x is ensured as character boundary of preedit string accurately.
		The event parameter is the event that was sent to the editor widget
		The event type is QEvent.MouseButtonPress , QEvent.MouseButtonRelease , QEvent.MouseButtonDblClick or QEvent.MouseMove
		The events button and state indicate the kind of operation that was performed.
		"""
		res = super(QInputContext,self).mouseHandler(x,event)
		return res
	#----------------------------------------------------------------------
	def sendEvent(self,event):
		"""
		sendEvent(event)
			event=QtGui.QInputMethodEvent

		Sends an input method event specified by event to the current focus widget
		Implementations of PySide.QtGui.QInputContext should call this method to send the generated input method events and not QApplication.sendEvent() , as the events might have to get dispatched to a different application on some platforms.
		Some complex input methods route the handling to several child contexts (e.g
		to enable language switching)
		To account for this, PySide.QtGui.QInputContext will check if the parent object is a PySide.QtGui.QInputContext
		If yes, it will call the parents PySide.QtGui.QInputContext.sendEvent() implementation instead of sending the event directly.
		"""
		res = super(QInputContext,self).sendEvent(event)
		return res
	#----------------------------------------------------------------------
	def setFocusWidget(self,w):
		"""
		setFocusWidget(w)
			w=QtGui.QWidget

		Sets the widget that has an input focus for this input context.
		"""
		res = super(QInputContext,self).setFocusWidget(w)
		return res
	#----------------------------------------------------------------------
	def standardFormat(self,s):
		"""
		standardFormat(s)
			s=QtGui.QInputContext.StandardFormat

		Returns a PySide.QtGui.QTextFormat object that specifies the format for component s .
		"""
		res = super(QInputContext,self).standardFormat(s)
		isinstance(res,QtGui.QTextFormat)
		return res
	#----------------------------------------------------------------------
	def widgetDestroyed(self,w):
		"""
		widgetDestroyed(w)
			w=QtGui.QWidget

		This virtual function is called when the specified widget is destroyed
		The widget is a widget on which this input context is installed.
		"""
		res = super(QInputContext,self).widgetDestroyed(w)
		return res

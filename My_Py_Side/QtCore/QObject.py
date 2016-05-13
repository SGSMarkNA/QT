from Qt_Tools import QtGui, QtCore
_property = property
class QObject(QtCore.QObject):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QObject,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def children(self):
		"""
		Returns a list of child objects
		The QObjectList class is defined in the <QObject> header file as the following:
		The first child added is the QList.first() object in the list and the last child added is the QList.last() object in the list, i.e
		new children are appended at the end.
		Note that the list order changes when PySide.QtGui.QWidget children are raised or lowered
		A widget that is raised becomes the last object in the list, and a widget that is lowered becomes the first object in the list.
		"""
		res = super(QObject,self).children()
		return res
	#----------------------------------------------------------------------
	def dumpObjectInfo(self):
		"""
		Dumps information about signal connections, etc
		for this object to the debug output.
		This function is useful for debugging, but does nothing if the library has been compiled in release mode (i.e
		without debugging information).
		"""
		res = super(QObject,self).dumpObjectInfo()
		return res
	#----------------------------------------------------------------------
	def dumpObjectTree(self):
		"""
		Dumps a tree of children to the debug output.
		This function is useful for debugging, but does nothing if the library has been compiled in release mode (i.e
		without debugging information).
		"""
		res = super(QObject,self).dumpObjectTree()
		return res
	#----------------------------------------------------------------------
	def dynamicPropertyNames(self):
		"""
		Returns the names of all properties that were dynamically added to the object using PySide.QtCore.QObject.setProperty() .
		"""
		res = super(QObject,self).dynamicPropertyNames()
		return res
	#----------------------------------------------------------------------
	def isWidgetType(self):
		"""
		Returns true if the object is a widget; otherwise returns false.
		Calling this function is equivalent to calling inherits( PySide.QtGui.QWidget ), except that it is much faster.
		"""
		res = super(QObject,self).isWidgetType()

		return res
	#----------------------------------------------------------------------
	def metaObject(self):
		"""
		Returns a pointer to the meta-object of this object.
		A meta-object contains information about a class that inherits PySide.QtCore.QObject , e.g
		class name, superclass name, properties, signals and slots
		Every PySide.QtCore.QObject subclass that contains the Q_OBJECT() macro will have a meta-object.
		The meta-object information is required by the signal/slot connection mechanism and the property system
		The PySide.QtCore.QObject.inherits() function also makes use of the meta-object.
		If you have no pointer to an actual object instance but still want to access the meta-object of a class, you can use staticMetaObject .
		Example:
		"""
		res = super(QObject,self).metaObject()
		isinstance(res,QtCore.QMetaObject)
		return res
	#----------------------------------------------------------------------
	def objectName(self):
		"""
		This property holds the name of this object.
		You can find an object by name (and type) using PySide.QtCore.QObject.findChild()
		You can find a set of objects with PySide.QtCore.QObject.findChildren() .
		By default, this property contains an empty string.
		"""
		res = super(QObject,self).objectName()
		return res
	#----------------------------------------------------------------------
	def parent(self):
		"""
		Returns a pointer to the parent object.
		"""
		res = super(QObject,self).parent()
		isinstance(res,QtCore.QObject)
		return res
	#----------------------------------------------------------------------
	def sender(self):
		"""
		Returns a pointer to the object that sent the signal, if called in a slot activated by a signal; otherwise it returns 0
		The pointer is valid only during the execution of the slot that calls this function from this objects thread context.
		The pointer returned by this function becomes invalid if the sender is destroyed, or if the slot is disconnected from the senders signal.
		"""
		res = super(QObject,self).sender()
		isinstance(res,QtCore.QObject)
		return res
	#----------------------------------------------------------------------
	def signalsBlocked(self):
		"""
		Returns true if signals are blocked; otherwise returns false.
		Signals are not blocked by default.
		"""
		res = super(QObject,self).signalsBlocked()

		return res
	#----------------------------------------------------------------------
	def thread(self):
		"""
		Returns the thread in which the object lives.
		"""
		res = super(QObject,self).thread()
		isinstance(res,QtCore.QThread)
		return res
	#----------------------------------------------------------------------
	def blockSignals(self,b):
		"""
		blockSignals(b)
			b=QtCore.bool

		If block is true, signals emitted by this object are blocked (i.e., emitting a signal will not invoke anything connected to it)
		If block is false, no such blocking will occur.
		The return value is the previous value of PySide.QtCore.QObject.signalsBlocked() .
		Note that the PySide.QtCore.QObject.destroyed() signal will be emitted even if the signals for this object have been blocked.
		"""
		res = super(QObject,self).blockSignals(b)

		return res
	#----------------------------------------------------------------------
	def childEvent(self,arg__1):
		"""
		childEvent(arg__1)
			arg__1=QtCore.QChildEvent

		This event handler can be reimplemented in a subclass to receive child events
		The event is passed in the event parameter.
		QEvent.ChildAdded and QEvent.ChildRemoved events are sent to objects when children are added or removed
		In both cases you can only rely on the child being a PySide.QtCore.QObject , or if PySide.QtCore.QObject.isWidgetType() returns true, a PySide.QtGui.QWidget
		(This is because, in the ChildAdded case, the child is not yet fully constructed, and in the ChildRemoved case it might have been destructed already).
		QEvent.ChildPolished events are sent to widgets when children are polished, or when polished children are added
		If you receive a child polished event, the childs construction is usually completed
		However, this is not guaranteed, and multiple polish events may be delivered during the execution of a widgets constructor.
		For every child widget, you receive one ChildAdded event, zero or more ChildPolished events, and one ChildRemoved event.
		The ChildPolished event is omitted if a child is removed immediately after it is added
		If a child is polished several times during construction and destruction, you may receive several child polished events for the same child, each time with a different virtual table.
		"""
		res = super(QObject,self).childEvent(arg__1)
		return res
	#----------------------------------------------------------------------
	def connect(self,*args,**kwargs):
		"""
		connect(arg__1,arg__2,arg__3,type=None)
			arg__1=str
			arg__2=QtCore.QObject
			arg__3=str
			type=QtCore.Qt.ConnectionType

		connect(arg__1,arg__2,type=None)
			arg__1=str
			arg__2=Callable
			type=QtCore.Qt.ConnectionType

		connect(sender,signal,member,type=None)
			sender=QtCore.QObject
			signal=str
			member=str
			type=QtCore.Qt.ConnectionType


		"""
		res = super(QObject,self).connect(*args,**kwargs)

		return res
	#----------------------------------------------------------------------
	def connectNotify(self,signal):
		"""
		connectNotify(signal)
			signal=str

		This virtual function is called when something has been connected to signal in this object.
		If you want to compare signal with a specific signal, use QLatin1String and the SIGNAL() macro as follows:
		If the signal contains multiple parameters or parameters that contain spaces, call QMetaObject.normalizedSignature() on the result of the SIGNAL() macro.
		"""
		res = super(QObject,self).connectNotify(signal)
		return res
	#----------------------------------------------------------------------
	def customEvent(self,arg__1):
		"""
		customEvent(arg__1)
			arg__1=QtCore.QEvent

		This event handler can be reimplemented in a subclass to receive custom events
		Custom events are user-defined events with a type value at least as large as the QEvent.User item of the QEvent.Type enum, and is typically a PySide.QtCore.QEvent subclass
		The event is passed in the event parameter.
		"""
		res = super(QObject,self).customEvent(arg__1)
		return res
	#----------------------------------------------------------------------
	def disconnect(self,*args,**kwargs):
		"""
		disconnect(signal,receiver,member)
			signal=str
			receiver=QtCore.QObject
			member=str

		disconnect(arg__1,arg__2)
			arg__1=str
			arg__2=Callable

		disconnect(receiver,member=None)
			receiver=QtCore.QObject
			member=str

		This function overloads PySide.QtCore.QObject.disconnect() .
		Disconnects signal from method of receiver .
		A signal-slot connection is removed when either of the objects involved are destroyed.
		"""
		res = super(QObject,self).disconnect(*args,**kwargs)

		return res
	#----------------------------------------------------------------------
	def disconnectNotify(self,signal):
		"""
		disconnectNotify(signal)
			signal=str

		This virtual function is called when something has been disconnected from signal in this object.
		See PySide.QtCore.QObject.connectNotify() for an example of how to compare signal with a specific signal.
		"""
		res = super(QObject,self).disconnectNotify(signal)
		return res
	#----------------------------------------------------------------------
	def emit(self,arg__1,arg__2):
		"""
		emit(arg__1,arg__2)
			arg__1=str
			arg__2=unKnown


		"""
		res = super(QObject,self).emit(arg__1,arg__2)

		return res
	#----------------------------------------------------------------------
	def event(self,arg__1):
		"""
		event(arg__1)
			arg__1=QtCore.QEvent

		This virtual function receives events to an object and should return true if the event e was recognized and processed.
		The PySide.QtCore.QObject.event() function can be reimplemented to customize the behavior of an object.
		"""
		res = super(QObject,self).event(arg__1)

		return res
	#----------------------------------------------------------------------
	def eventFilter(self,arg__1,arg__2):
		"""
		eventFilter(arg__1,arg__2)
			arg__1=QtCore.QObject
			arg__2=QtCore.QEvent

		Filters events if this object has been installed as an event filter for the watched object.
		In your reimplementation of this function, if you want to filter the event out, i.e
		stop it being handled further, return true; otherwise return false.
		Example:
		Notice in the example above that unhandled events are passed to the base classs PySide.QtCore.QObject.eventFilter() function, since the base class might have reimplemented PySide.QtCore.QObject.eventFilter() for its own internal purposes.
		"""
		res = super(QObject,self).eventFilter(arg__1,arg__2)

		return res
	#----------------------------------------------------------------------
	def findChild(self,arg__1,arg__2=None):
		"""
		findChild(arg__1,arg__2=None)
			arg__1=TypeObject
			arg__2=unicode


		"""
		res = super(QObject,self).findChild(arg__1,arg__2)
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def findChildren(self,*args,**kwargs):
		"""
		findChildren(arg__1,arg__2)
			arg__1=TypeObject
			arg__2=QtCore.QRegExp

		findChildren(arg__1,arg__2=None)
			arg__1=TypeObject
			arg__2=unicode


		"""
		res = super(QObject,self).findChildren(*args,**kwargs)

		return res
	#----------------------------------------------------------------------
	def inherits(self,classname):
		"""
		inherits(classname)
			classname=str

		Returns true if this object is an instance of a class that inherits className or a PySide.QtCore.QObject subclass that inherits className ; otherwise returns false.
		A class is considered to inherit itself.
		Example:
		If you need to determine whether an object is an instance of a particular class for the purpose of casting it, consider using qobject_cast<Type *>(object) instead.
		"""
		res = super(QObject,self).inherits(classname)

		return res
	#----------------------------------------------------------------------
	def installEventFilter(self,arg__1):
		"""
		installEventFilter(arg__1)
			arg__1=QtCore.QObject

		Installs an event filter filterObj on this object
		For example:
		An event filter is an object that receives all events that are sent to this object
		The filter can either stop the event or forward it to this object
		The event filter filterObj receives events via its PySide.QtCore.QObject.eventFilter() function
		The PySide.QtCore.QObject.eventFilter() function must return true if the event should be filtered, (i.e
		stopped); otherwise it must return false.
		If multiple event filters are installed on a single object, the filter that was installed last is activated first.
		Heres a KeyPressEater class that eats the key presses of its monitored objects:
		And heres how to install it on two widgets:
		The PySide.QtGui.QShortcut class, for example, uses this technique to intercept shortcut key presses.
		Note that the filtering object must be in the same thread as this object
		If filterObj is in a different thread, this function does nothing
		If either filterObj or this object are moved to a different thread after calling this function, the event filter will not be called until both objects have the same thread affinity again (it is not removed).
		"""
		res = super(QObject,self).installEventFilter(arg__1)
		return res
	#----------------------------------------------------------------------
	def killTimer(self,id):
		"""
		killTimer(id)
			id=QtCore.int

		Kills the timer with timer identifier, id .
		The timer identifier is returned by PySide.QtCore.QObject.startTimer() when a timer event is started.
		"""
		res = super(QObject,self).killTimer(id)
		return res
	#----------------------------------------------------------------------
	def moveToThread(self,thread):
		"""
		moveToThread(thread)
			thread=QtCore.QThread

		Changes the thread affinity for this object and its children
		The object cannot be moved if it has a parent
		Event processing will continue in the targetThread .
		To move an object to the main thread, use QApplication.instance() to retrieve a pointer to the current application, and then use QApplication.thread() to retrieve the thread in which the application lives
		For example:
		If targetThread is zero, all event processing for this object and its children stops.
		Note that all active timers for the object will be reset
		The timers are first stopped in the current thread and restarted (with the same interval) in the targetThread
		As a result, constantly moving an object between threads can postpone timer events indefinitely.
		A QEvent.ThreadChange event is sent to this object just before the thread affinity is changed
		You can handle this event to perform any special processing
		Note that any new events that are posted to this object will be handled in the targetThread .
		"""
		res = super(QObject,self).moveToThread(thread)
		return res
	#----------------------------------------------------------------------
	def property(self,name):
		"""
		property(name)
			name=str

		Returns the value of the objects name property.
		If no such property exists, the returned variant is invalid.
		Information about all available properties is provided through the PySide.QtCore.QObject.metaObject() and PySide.QtCore.QObject.dynamicPropertyNames() .
		"""
		res = super(QObject,self).property(name)
		return res
	#----------------------------------------------------------------------
	def receivers(self,signal):
		"""
		receivers(signal)
			signal=str

		Returns the number of receivers connected to the signal .
		Since both slots and signals can be used as receivers for signals, and the same connections can be made many times, the number of receivers is the same as the number of connections made from this signal.
		When calling this function, you can use the SIGNAL() macro to pass a specific signal:
		As the code snippet above illustrates, you can use this function to avoid emitting a signal that nobody listens to.
		"""
		res = super(QObject,self).receivers(signal)

		return res
	#----------------------------------------------------------------------
	def removeEventFilter(self,arg__1):
		"""
		removeEventFilter(arg__1)
			arg__1=QtCore.QObject

		Removes an event filter object obj from this object
		The request is ignored if such an event filter has not been installed.
		All event filters for this object are automatically removed when this object is destroyed.
		It is always safe to remove an event filter, even during event filter activation (i.e
		from the PySide.QtCore.QObject.eventFilter() function).
		"""
		res = super(QObject,self).removeEventFilter(arg__1)
		return res
	#----------------------------------------------------------------------
	def setObjectName(self,name):
		"""
		setObjectName(name)
			name=unicode

		This property holds the name of this object.
		You can find an object by name (and type) using PySide.QtCore.QObject.findChild()
		You can find a set of objects with PySide.QtCore.QObject.findChildren() .
		By default, this property contains an empty string.
		"""
		res = super(QObject,self).setObjectName(name)
		return res
	#----------------------------------------------------------------------
	def setParent(self,arg__1):
		"""
		setParent(arg__1)
			arg__1=QtCore.QObject

		Makes the object a child of parent .
		"""
		res = super(QObject,self).setParent(arg__1)
		return res
	#----------------------------------------------------------------------
	def setProperty(self,name,value):
		"""
		setProperty(name,value)
			name=str
			value=object

		Sets the value of the objects name property to value .
		If the property is defined in the class using Q_PROPERTY then true is returned on success and false otherwise
		If the property is not defined using Q_PROPERTY, and therefore not listed in the meta-object, it is added as a dynamic property and false is returned.
		Information about all available properties is provided through the PySide.QtCore.QObject.metaObject() and PySide.QtCore.QObject.dynamicPropertyNames() .
		Dynamic properties can be queried again using PySide.QtCore.QObject.property() and can be removed by setting the property value to an invalid PySide.QtCore.QVariant
		Changing the value of a dynamic property causes a PySide.QtCore.QDynamicPropertyChangeEvent to be sent to the object.
		"""
		res = super(QObject,self).setProperty(name,value)

		return res
	#----------------------------------------------------------------------
	def startTimer(self,interval):
		"""
		startTimer(interval)
			interval=QtCore.int

		Starts a timer and returns a timer identifier, or returns zero if it could not start a timer.
		A timer event will occur every interval milliseconds until PySide.QtCore.QObject.killTimer() is called
		If interval is 0, then the timer event occurs once every time there are no more window system events to process.
		The virtual PySide.QtCore.QObject.timerEvent() function is called with the PySide.QtCore.QTimerEvent event parameter class when a timer event occurs
		Reimplement this function to get timer events.
		If multiple timers are running, the QTimerEvent.timerId() can be used to find out which timer was activated.
		Example:
		Note that PySide.QtCore.QTimer s accuracy depends on the underlying operating system and hardware
		Most platforms support an accuracy of 20 milliseconds; some provide more
		If Qt is unable to deliver the requested number of timer events, it will silently discard some.
		The PySide.QtCore.QTimer class provides a high-level programming interface with single-shot timers and timer signals instead of events
		There is also a PySide.QtCore.QBasicTimer class that is more lightweight than PySide.QtCore.QTimer and less clumsy than using timer IDs directly.
		"""
		res = super(QObject,self).startTimer(interval)

		return res
	#----------------------------------------------------------------------
	def timerEvent(self,arg__1):
		"""
		timerEvent(arg__1)
			arg__1=QtCore.QTimerEvent

		This event handler can be reimplemented in a subclass to receive timer events for the object.
		PySide.QtCore.QTimer provides a higher-level interface to the timer functionality, and also more general information about timers
		The timer event is passed in the event parameter.
		"""
		res = super(QObject,self).timerEvent(arg__1)
		return res
	#----------------------------------------------------------------------
	def tr(self,arg__1,arg__2=None,arg__3=None):
		"""
		tr(arg__1,arg__2=None,arg__3=None)
			arg__1=str
			arg__2=str
			arg__3=QtCore.int

		Returns a translated version of sourceText , optionally based on a disambiguation string and value of n for strings containing plurals; otherwise returns sourceText itself if no appropriate translated string is available.
		Example:
		If the same sourceText is used in different roles within the same context, an additional identifying string may be passed in disambiguation (0 by default)
		In Qt 4.4 and earlier, this was the preferred way to pass comments to translators.
		Example:
		See Writing Source Code for Translation for a detailed description of Qts translation mechanisms in general, and the Disambiguation section for information on disambiguation.
		"""
		res = super(QObject,self).tr(arg__1,arg__2,arg__3)
		return res
	#----------------------------------------------------------------------
	def trUtf8(self,*args,**kwargs):
		"""
		trUtf8(arg__1,arg__2=None,arg__3=None)
			arg__1=Unicode
			arg__2=str
			arg__3=QtCore.int

		trUtf8(arg__1,arg__2=None,arg__3=None)
			arg__1=str
			arg__2=str
			arg__3=QtCore.int


		"""
		res = super(QObject,self).trUtf8(*args,**kwargs)
		return res

	Children = _property(children)
	Dump_Object_Info = _property(dumpObjectInfo)
	Dump_Object_Tree = _property(dumpObjectTree)
	Dynamic_Property_Names = _property(dynamicPropertyNames)
	Is_WidgetType = _property(isWidgetType)
	Meta_Object = _property(metaObject)
	Object_Name = _property(objectName)
	Parent = _property(parent)
	Sender = _property(sender)
	Signals_Blocked = _property(signalsBlocked)
	Thread = _property(thread)
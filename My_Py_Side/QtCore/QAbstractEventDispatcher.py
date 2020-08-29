from PySide import QtGui, QtCore

class QAbstractEventDispatcher(QtCore.QAbstractEventDispatcher):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QAbstractEventDispatcher,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def aboutToBlock(self):
		"""

		"""
		res = super(QAbstractEventDispatcher,self).aboutToBlock()
		return res
	#----------------------------------------------------------------------
	def awake(self):
		"""

		"""
		res = super(QAbstractEventDispatcher,self).awake()
		return res
	#----------------------------------------------------------------------
	def closingDown(self):
		"""

		"""
		res = super(QAbstractEventDispatcher,self).closingDown()
		return res
	#----------------------------------------------------------------------
	def flush(self):
		"""
		Flushes the event queue
		This normally returns almost immediately
		Does nothing on platforms other than X11.
		"""
		res = super(QAbstractEventDispatcher,self).flush()
		return res
	#----------------------------------------------------------------------
	def hasPendingEvents(self):
		"""
		Returns true if there is an event waiting; otherwise returns false.
		"""
		res = super(QAbstractEventDispatcher,self).hasPendingEvents()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def interrupt(self):
		"""
		Interrupts event dispatching; i.e
		the event dispatcher will return from PySide.QtCore.QAbstractEventDispatcher.processEvents() as soon as possible.
		"""
		res = super(QAbstractEventDispatcher,self).interrupt()
		return res
	#----------------------------------------------------------------------
	def startingUp(self):
		"""

		"""
		res = super(QAbstractEventDispatcher,self).startingUp()
		return res
	#----------------------------------------------------------------------
	def wakeUp(self):
		"""
		Wakes up the event loop.
		"""
		res = super(QAbstractEventDispatcher,self).wakeUp()
		return res
	#----------------------------------------------------------------------
	def processEvents(self,flags):
		"""
		processEvents(flags)
			flags=QtCore.QEventLoop.ProcessEventsFlags


		"""
		res = super(QAbstractEventDispatcher,self).processEvents(flags)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def registerSocketNotifier(self,notifier):
		"""
		registerSocketNotifier(notifier)
			notifier=QtCore.QSocketNotifier

		Registers notifier with the event loop
		Subclasses must implement this method to tie a socket notifier into another event loop.
		"""
		res = super(QAbstractEventDispatcher,self).registerSocketNotifier(notifier)
		return res
	#----------------------------------------------------------------------
	def registerTimer(self,*args,**kwargs):
		"""
		registerTimer(timerId,interval,object)
			timerId=QtCore.int
			interval=QtCore.int
			object=QtCore.QObject

		registerTimer(interval,object)
			interval=QtCore.int
			object=QtCore.QObject

		Register a timer with the specified timerId and interval for the given object .
		"""
		res = super(QAbstractEventDispatcher,self).registerTimer(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def registeredTimers(self,object):
		"""
		registeredTimers(object)
			object=QtCore.QObject

		Returns a list of registered timers for object
		The timer ID is the first member in each pair; the interval is the second.
		"""
		res = super(QAbstractEventDispatcher,self).registeredTimers(object)
		return res
	#----------------------------------------------------------------------
	def unregisterSocketNotifier(self,notifier):
		"""
		unregisterSocketNotifier(notifier)
			notifier=QtCore.QSocketNotifier

		Unregisters notifier from the event dispatcher
		Subclasses must reimplement this method to tie a socket notifier into another event loop
		Reimplementations must call the base implementation.
		"""
		res = super(QAbstractEventDispatcher,self).unregisterSocketNotifier(notifier)
		return res
	#----------------------------------------------------------------------
	def unregisterTimer(self,timerId):
		"""
		unregisterTimer(timerId)
			timerId=QtCore.int

		Unregisters the timer with the given timerId
		Returns true if successful; otherwise returns false.
		"""
		res = super(QAbstractEventDispatcher,self).unregisterTimer(timerId)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def unregisterTimers(self,object):
		"""
		unregisterTimers(object)
			object=QtCore.QObject

		Unregisters all the timers associated with the given object
		Returns true if all timers were successful removed; otherwise returns false.
		"""
		res = super(QAbstractEventDispatcher,self).unregisterTimers(object)
		isinstance(res,bool)
		return res

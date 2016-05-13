import os, inspect
from itertools import count
QT_PACKAGE = os.environ.get("QT_PACKAGE")

########################################################################
class Counter(object):
	#----------------------------------------------------------------------
	def __init__(self,start=1):
		self.num = count(start)
	#----------------------------------------------------------------------
	def __call__(self):
		return self.num.next()


def set_PyQt4_API():
	import sip
	try:
		sip.setapi('QString', 2)
		sip.setapi('QVariant', 2)
		sip.setapi('QTime',2)
		sip.setapi('QTextStream ',2)
		sip.setapi('QDateTime',2)
		sip.setapi('QDate',2)
		sip.setapi('QUrl',2)
	except:
		pass
	return sip
	

if QT_PACKAGE == "PySide":
	#from PySide import QtCore, QtGui, QtUiTools, QtWebKit
	import PySide.QtCore
	import PySide.QtGui
	import PySide.QtUiTools
	import PySide.QtWebKit
	import UI.UI_Reader
	import UI.UI_Loader
	import UI.UI_Compiler
	QtCore    = PySide.QtCore
	QtGui     = PySide.QtGui
	QtUiTools = PySide.QtUiTools
	QtWebKit  = PySide.QtWebKit
	try:
		import PySide.shiboken as shiboken
	except:
		try:
			import shiboken
		except:
			shiboken = None
	if shiboken is not None:
		sip        = shiboken
		wraperfn   = shiboken.wrapInstance
	uic            = UI.UI_Reader
	ui_Loader      = UI.UI_Loader.UI_Loader()
	build_ui_files = UI.UI_Compiler.build_ui_files
	Qt             = QtCore.Qt
	QtSlot         = QtCore.Slot
	QtSignal       = QtCore.Signal
	QtProperty     = QtCore.Property

elif QT_PACKAGE == "PyQt4":
	sip = set_PyQt4_API()
	from PyQt4 import  QtCore, QtGui
	import UI.UI_Reader
	wraperfn   = sip.wrapinstance
	Qt         = QtCore.Qt
	uic        = UI.UI_Reader
	QtSlot     = QtCore.pyqtSlot
	QtSignal   = QtCore.pyqtSignal
	QtProperty = QtCore.pyqtProperty

else:
	#----------------------------------------------------------------------
	try:
		QT_PACKAGE = "PySide"
		from PySide import QtCore, QtGui, QtUiTools, QtWebKit
		try:
			import PySide.shiboken as shiboken
		except:
			import shiboken
		os.environ["QT_PACKAGE"] = QT_PACKAGE
		
		import UI.UI_Reader
		import UI.UI_Loader
		ui_Loader  = UI.UI_Loader.UI_Loader()
		sip        = shiboken
		wraperfn   = shiboken.wrapInstance
		Qt         = QtCore.Qt
		uic        = UI.UI_Reader
		QtSlot     = QtCore.Slot
		QtSignal   = QtCore.Signal
		QtProperty = QtCore.Property
		
	#----------------------------------------------------------------------
	except ImportError:
		#----------------------------------------------------------------------
		QT_PACKAGE               = "PyQt4"
		sip = set_PyQt4_API()
		from PyQt4 import  QtCore, QtGui
		os.environ["QT_PACKAGE"] = "PyQt4"
		
		import UI.UI_Reader
		wraperfn   = sip.wrapinstance
		Qt         = QtCore.Qt
		uic        = UI.UI_Reader
		QtSlot     = QtCore.pyqtSlot
		QtSignal   = QtCore.pyqtSignal
		QtProperty = QtCore.pyqtProperty



if not hasattr(Qt, 'MiddleButton'):
	Qt.MiddleButton = Qt.MidButton # some Qt code uses MidButton and other places it uses MiddleButton

_userRole_counter    = Counter(QtCore.Qt.UserRole)
_user_type_counter   = Counter(QtGui.QStandardItem.UserType)

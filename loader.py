
import inspect
from itertools import count
import os	
QT_PACKAGE = os.environ.get("QT_PACKAGE")
try:
        import maya.cmds as cmds
	MAYA_VERSION    = int(cmds.about(version=True))
except:
	MAYA_VERSION = 2015

if QT_PACKAGE is None:
	if MAYA_VERSION >= 2017:
		QT_PACKAGE =  "PySide2"
		os.environ["QT_PACKAGE"] = "PySide2"
	elif MAYA_VERSION >= 2013:
		QT_PACKAGE =  "PySide"
		os.environ["QT_PACKAGE"] = "PySide"
	
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
	

if QT_PACKAGE == "PySide2":
	from PySide2 import QtCore, QtGui, QtUiTools, QtWidgets
	from PySide2.QtCore import *
	from PySide2.QtGui import *
	from PySide2.QtUiTools import *
	from PySide2.QtWidgets import *
	# import UI.UI_Reader
	# import UI.UI_Loader
	# import UI.UI_Compiler
	# QtCore    = PySide.QtCore
	# QtGui     = PySide.QtGui
	# QtUiTools = PySide.QtUiTools
	# QtWebKit  = PySide.QtWebKit
	import shiboken2 as sip
	wraperfn       = sip.wrapInstance
	Qt             = QtCore.Qt
	QtSlot         = QtCore.Slot
	QtSignal       = QtCore.Signal
	QtProperty     = QtCore.Property

elif QT_PACKAGE == "PySide":
	from PySide import QtCore, QtGui, QtUiTools, QtWebKit
	from PySide.QtCore import *
	from PySide.QtGui import *
	from PySide.QtUiTools import *
	from PySide.QtWebKit import *
	# QtCore    = PySide.QtCore
	# QtGui     = PySide.QtGui
	# QtUiTools = PySide.QtUiTools
	# QtWebKit  = PySide.QtWebKit
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
	Qt             = QtCore.Qt
	QtSlot         = QtCore.Slot
	QtSignal       = QtCore.Signal
	QtProperty     = QtCore.Property

import UI.UI_Reader
import UI.UI_Loader
import UI.UI_Compiler
uic            = UI.UI_Reader
ui_Loader      = UI.UI_Loader.UI_Loader()
build_ui_files = UI.UI_Compiler.build_ui_files


if not hasattr(Qt, 'MiddleButton'):
	Qt.MiddleButton = Qt.MidButton # some Qt code uses MidButton and other places it uses MiddleButton

_userRole_counter    = Counter(QtCore.Qt.UserRole)
_user_type_counter   = Counter(QtGui.QStandardItem.UserType)

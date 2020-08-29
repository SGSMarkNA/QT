import loader
import os

QT_PACKAGE = os.environ.get("QT_PACKAGE")

if QT_PACKAGE == "PySide2":
	import PySide2.QtGui
	import PySide2.QtCore
	import PySide2.QtWidgets
	import PySide2.QtNetwork
	from PySide2.QtGui import *
	from PySide2.QtCore import *
	from PySide2.QtWidgets import *
	from PySide2.QtNetwork import *
else:
	import PySide.QtGui
	import PySide.QtCore
	from PySide.QtGui import *
	from PySide.QtCore import *	
	
userRole_counter  = loader._userRole_counter
user_type_counter = loader._user_type_counter
QtCore            = loader.QtCore
QtGui             = loader.QtGui
Qt                = loader.Qt
QtSlot            = loader.QtSlot
QtSignal          = loader.QtSignal
QtProperty        = loader.QtProperty
try:
	ui_Loader     = loader.ui_Loader
except:
	pass
try:
	uic               = loader.uic
	wraperfn          = loader.wraperfn
except:
	pass

try:
	import DataModels
except:
	pass
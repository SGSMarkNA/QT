import loader
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


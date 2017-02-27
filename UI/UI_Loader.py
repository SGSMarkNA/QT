import os
if os.environ["QT_PACKAGE"] == "PySide2":
	from PySide2.QtUiTools import QUiLoader
	from PySide2.QtCore import *
	from PySide2.QtGui import *
	from PySide2.QtWidgets import *

if os.environ["QT_PACKAGE"] == "PySide":
	from PySide.QtUiTools import QUiLoader
	from PySide.QtCore import *

############################################################################
class UI_Loader(object):
	#----------------------------------------------------------------------
	def __new__(type, *args, **kwargs):
		if not '_the_instance' in type.__dict__:
			type._the_instance = object.__new__(type)
		return type._the_instance
	#----------------------------------------------------------------------
	def __init__(self):
		""""""
		self.loader = QUiLoader()

	#----------------------------------------------------------------------
	def registerCustomWidget(self, wig):
		""""""
		self.loader.registerCustomWidget(wig)

	#----------------------------------------------------------------------
	def load(self, file_path, parent_widget=None):
		""""""
		Qfile = QFile(file_path)
		Qfile.open(QFile.ReadOnly)
		ui_wig = self.loader.load(Qfile,parent_widget)
		Qfile.close()
		return ui_wig

from PySide.QtUiTools import QUiLoader
from PySide import QtCore
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
		Qfile = QtCore.QFile(file_path)
		Qfile.open(QtCore.QFile.ReadOnly)
		ui_wig = self.loader.load(Qfile,parent_widget)
		Qfile.close()
		return ui_wig
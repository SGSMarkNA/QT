from PySide import QtGui, QtCore

class QPrinterInfo(QtGui.QPrinterInfo):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QPrinterInfo,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def isDefault(self):
		"""
		Returns whether this printer is the default printer.
		"""
		res = super(QPrinterInfo,self).isDefault()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns whether this PySide.QtGui.QPrinterInfo object holds a printer definition.
		An empty PySide.QtGui.QPrinterInfo object could result for example from calling PySide.QtGui.QPrinterInfo.defaultPrinter() when there are no printers on the system.
		"""
		res = super(QPrinterInfo,self).isNull()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def printerName(self):
		"""
		Returns the name of the printer.
		"""
		res = super(QPrinterInfo,self).printerName()
		return res
	#----------------------------------------------------------------------
	def supportedPaperSizes(self):
		"""
		Returns a list of supported paper sizes by the printer.
		Not all printer drivers support this query, so the list may be empty
		On Mac OS X 10.3, this function always returns an empty list.
		"""
		res = super(QPrinterInfo,self).supportedPaperSizes()
		return res

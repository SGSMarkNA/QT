from PySide import QtGui, QtCore

class QAbstractPrintDialog(QtGui.QAbstractPrintDialog):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QAbstractPrintDialog,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def enabledOptions(self):
		"""
		Use QPrintDialog.options() instead.
		"""
		res = super(QAbstractPrintDialog,self).enabledOptions()
		isinstance(res,QtGui.QAbstractPrintDialog.PrintDialogOptions)
		return res
	#----------------------------------------------------------------------
	def fromPage(self):
		"""
		Returns the first page to be printed By default, this value is set to 0.
		"""
		res = super(QAbstractPrintDialog,self).fromPage()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def maxPage(self):
		"""
		Returns the maximum page in the page range
		As of Qt 4.4, this function returns INT_MAX by default
		Previous versions returned 1 by default.
		"""
		res = super(QAbstractPrintDialog,self).maxPage()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def minPage(self):
		"""
		Returns the minimum page in the page range
		By default, this value is set to 1.
		"""
		res = super(QAbstractPrintDialog,self).minPage()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def printRange(self):
		"""
		Returns the print range.
		"""
		res = super(QAbstractPrintDialog,self).printRange()
		isinstance(res,QtGui.QAbstractPrintDialog.PrintRange)
		return res
	#----------------------------------------------------------------------
	def printer(self):
		"""
		Returns the printer that this printer dialog operates on.
		"""
		res = super(QAbstractPrintDialog,self).printer()
		isinstance(res,QtGui.QPrinter)
		return res
	#----------------------------------------------------------------------
	def toPage(self):
		"""
		Returns the last page to be printed
		By default, this value is set to 0.
		"""
		res = super(QAbstractPrintDialog,self).toPage()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def addEnabledOption(self,option):
		"""
		addEnabledOption(option)
			option=QtGui.QAbstractPrintDialog.PrintDialogOption

		Use QPrintDialog::setOption(option , true) instead.
		"""
		res = super(QAbstractPrintDialog,self).addEnabledOption(option)
		return res
	#----------------------------------------------------------------------
	def isOptionEnabled(self,option):
		"""
		isOptionEnabled(option)
			option=QtGui.QAbstractPrintDialog.PrintDialogOption

		Use QPrintDialog::testOption(option ) instead.
		"""
		res = super(QAbstractPrintDialog,self).isOptionEnabled(option)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def setEnabledOptions(self,options):
		"""
		setEnabledOptions(options)
			options=QtGui.QAbstractPrintDialog.PrintDialogOptions


		"""
		res = super(QAbstractPrintDialog,self).setEnabledOptions(options)
		return res
	#----------------------------------------------------------------------
	def setFromTo(self,fromPage,toPage):
		"""
		setFromTo(fromPage,toPage)
			fromPage=QtCore.int
			toPage=QtCore.int

		Sets the range in the print dialog to be from from to to .
		"""
		res = super(QAbstractPrintDialog,self).setFromTo(fromPage,toPage)
		return res
	#----------------------------------------------------------------------
	def setMinMax(self,min,max):
		"""
		setMinMax(min,max)
			min=QtCore.int
			max=QtCore.int

		Sets the page range in this dialog to be from min to max
		This also enables the PrintPageRange option.
		"""
		res = super(QAbstractPrintDialog,self).setMinMax(min,max)
		return res
	#----------------------------------------------------------------------
	def setOptionTabs(self,tabs):
		"""
		setOptionTabs(tabs)
			tabs=unKnown


		"""
		res = super(QAbstractPrintDialog,self).setOptionTabs(tabs)
		return res
	#----------------------------------------------------------------------
	def setPrintRange(self,range):
		"""
		setPrintRange(range)
			range=QtGui.QAbstractPrintDialog.PrintRange

		Sets the print range option in to be range .
		"""
		res = super(QAbstractPrintDialog,self).setPrintRange(range)
		return res

from PySide import QtGui, QtCore

class QPrinter(QtGui.QPrinter):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QPrinter,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def abort(self):
		"""
		Aborts the current print run
		Returns true if the print run was successfully aborted and PySide.QtGui.QPrinter.printerState() will return QPrinter.Aborted ; otherwise returns false.
		It is not always possible to abort a print job
		For example, all the data has gone to the printer but the printer cannot or will not cancel the job when asked to.
		"""
		res = super(QPrinter,self).abort()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def actualNumCopies(self):
		"""
		Returns the number of copies that will be printed
		The default value is 1.
		This function always returns the actual value specified in the print dialog or using PySide.QtGui.QPrinter.setNumCopies() .
		Use PySide.QtGui.QPrinter.copyCount() instead.
		"""
		res = super(QPrinter,self).actualNumCopies()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def collateCopies(self):
		"""
		Returns true if collation is turned on when multiple copies is selected
		Returns false if it is turned off when multiple copies is selected
		When collating is turned off the printing of each individual page will be repeated the PySide.QtGui.QPrinter.numCopies() amount before the next page is started
		With collating turned on all pages are printed before the next copy of those pages is started.
		"""
		res = super(QPrinter,self).collateCopies()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def colorMode(self):
		"""
		Returns the current color mode.
		"""
		res = super(QPrinter,self).colorMode()
		isinstance(res,QtGui.QPrinter.ColorMode)
		return res
	#----------------------------------------------------------------------
	def copyCount(self):
		"""
		Returns the number of copies that will be printed
		The default value is 1.
		"""
		res = super(QPrinter,self).copyCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def creator(self):
		"""
		Returns the name of the application that created the document.
		"""
		res = super(QPrinter,self).creator()
		return res
	#----------------------------------------------------------------------
	def docName(self):
		"""
		Returns the document name.
		"""
		res = super(QPrinter,self).docName()
		return res
	#----------------------------------------------------------------------
	def doubleSidedPrinting(self):
		"""
		Returns true if double side printing is enabled.
		Currently this option is only supported on X11.
		"""
		res = super(QPrinter,self).doubleSidedPrinting()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def duplex(self):
		"""
		Returns the current duplex mode.
		Currently this option is only supported on X11.
		"""
		res = super(QPrinter,self).duplex()
		isinstance(res,QtGui.QPrinter.DuplexMode)
		return res
	#----------------------------------------------------------------------
	def fontEmbeddingEnabled(self):
		"""
		Returns true if font embedding is enabled.
		Currently this option is only supported on X11.
		"""
		res = super(QPrinter,self).fontEmbeddingEnabled()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def fromPage(self):
		"""
		Returns the number of the first page in a range of pages to be printed (the from page setting)
		Pages in a document are numbered according to the convention that the first page is page 1.
		By default, this function returns a special value of 0, meaning that the from page setting is unset.
		"""
		res = super(QPrinter,self).fromPage()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def fullPage(self):
		"""
		Returns true if the origin of the printers coordinate system is at the corner of the page and false if it is at the edge of the printable area.
		See PySide.QtGui.QPrinter.setFullPage() for details and caveats.
		"""
		res = super(QPrinter,self).fullPage()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if the printer currently selected is a valid printer in the system, or a pure PDF/PostScript printer; otherwise returns false.
		To detect other failures check the output of QPainter.begin() or QPrinter.newPage() .
		"""
		res = super(QPrinter,self).isValid()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def newPage(self):
		"""
		Tells the printer to eject the current page and to continue printing on a new page
		Returns true if this was successful; otherwise returns false.
		Calling PySide.QtGui.QPrinter.newPage() on an inactive PySide.QtGui.QPrinter object will always fail.
		"""
		res = super(QPrinter,self).newPage()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def numCopies(self):
		"""
		Returns the number of copies to be printed
		The default value is 1.
		On Windows, Mac OS X and X11 systems that support CUPS, this will always return 1 as these operating systems can internally handle the number of copies.
		On X11, this value will return the number of times the application is required to print in order to match the number specified in the printer setup dialog
		This has been done since some printer drivers are not capable of buffering up the copies and in those cases the application must make an explicit call to the print code for each copy.
		Use PySide.QtGui.QPrinter.copyCount() in conjunction with PySide.QtGui.QPrinter.supportsMultipleCopies() instead.
		"""
		res = super(QPrinter,self).numCopies()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def orientation(self):
		"""
		Returns the orientation setting
		This is driver-dependent, but is usually QPrinter.Portrait .
		"""
		res = super(QPrinter,self).orientation()
		isinstance(res,QtGui.QPrinter.Orientation)
		return res
	#----------------------------------------------------------------------
	def outputFileName(self):
		"""
		Returns the name of the output file
		By default, this is an empty string (indicating that the printer shouldnt print to file).
		"""
		res = super(QPrinter,self).outputFileName()
		return res
	#----------------------------------------------------------------------
	def outputFormat(self):
		"""
		Returns the output format for this printer.
		"""
		res = super(QPrinter,self).outputFormat()
		isinstance(res,QtGui.QPrinter.OutputFormat)
		return res
	#----------------------------------------------------------------------
	def pageOrder(self):
		"""
		Returns the current page order.
		The default page order is FirstPageFirst .
		"""
		res = super(QPrinter,self).pageOrder()
		isinstance(res,QtGui.QPrinter.PageOrder)
		return res
	#----------------------------------------------------------------------
	def pageRect(self):
		"""
		Returns the pages rectangle; this is usually smaller than the PySide.QtGui.QPrinter.paperRect() since the page normally has margins between its borders and the paper.
		The unit of the returned rectangle is DevicePixel .
		"""
		res = super(QPrinter,self).pageRect()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def pageSize(self):
		"""
		Returns the printer page size
		The default value is driver-dependent.
		Use PySide.QtGui.QPrinter.paperSize() instead.
		"""
		res = super(QPrinter,self).pageSize()
		isinstance(res,QtGui.QPrinter.PageSize)
		return res
	#----------------------------------------------------------------------
	def paperRect(self):
		"""
		Returns the papers rectangle; this is usually larger than the PySide.QtGui.QPrinter.pageRect() .
		The unit of the returned rectangle is DevicePixel .
		"""
		res = super(QPrinter,self).paperRect()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def paperSize(self):
		"""
		Returns the printer paper size
		The default value is driver-dependent.
		"""
		res = super(QPrinter,self).paperSize()
		isinstance(res,QtGui.QPrinter.PageSize)
		return res
	#----------------------------------------------------------------------
	def paperSource(self):
		"""
		Returns the printers paper source
		This is Manual or a printer tray or paper cassette.
		"""
		res = super(QPrinter,self).paperSource()
		isinstance(res,QtGui.QPrinter.PaperSource)
		return res
	#----------------------------------------------------------------------
	def printEngine(self):
		"""
		Returns the print engine used by the printer.
		"""
		res = super(QPrinter,self).printEngine()
		isinstance(res,QtGui.QPrintEngine)
		return res
	#----------------------------------------------------------------------
	def printProgram(self):
		"""
		Returns the name of the program that sends the print output to the printer.
		The default is to return an empty string; meaning that PySide.QtGui.QPrinter will try to be smart in a system-dependent way
		On X11 only, you can set it to something different to use a specific print program
		On the other platforms, this returns an empty string.
		"""
		res = super(QPrinter,self).printProgram()
		return res
	#----------------------------------------------------------------------
	def printRange(self):
		"""
		Returns the page range of the PySide.QtGui.QPrinter
		After the print setup dialog has been opened, this function returns the value selected by the user.
		"""
		res = super(QPrinter,self).printRange()
		isinstance(res,QtGui.QPrinter.PrintRange)
		return res
	#----------------------------------------------------------------------
	def printerName(self):
		"""
		Returns the printer name
		This value is initially set to the name of the default printer.
		"""
		res = super(QPrinter,self).printerName()
		return res
	#----------------------------------------------------------------------
	def printerState(self):
		"""
		Returns the current state of the printer
		This may not always be accurate (for example if the printer doesnt have the capability of reporting its state to the operating system).
		"""
		res = super(QPrinter,self).printerState()
		isinstance(res,QtGui.QPrinter.PrinterState)
		return res
	#----------------------------------------------------------------------
	def resolution(self):
		"""
		Returns the current assumed resolution of the printer, as set by PySide.QtGui.QPrinter.setResolution() or by the printer driver.
		"""
		res = super(QPrinter,self).resolution()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def supportedResolutions(self):
		"""
		Returns a list of the resolutions (a list of dots-per-inch integers) that the printer says it supports.
		For X11 where all printing is directly to postscript, this function will always return a one item list containing only the postscript resolution, i.e., 72 (72 dpi  but see QPrinter.PrinterMode ).
		"""
		res = super(QPrinter,self).supportedResolutions()
		return res
	#----------------------------------------------------------------------
	def supportsMultipleCopies(self):
		"""
		Returns true if the printer supports printing multiple copies of the same document in one job; otherwise false is returned.
		On most systems this function will return true
		However, on X11 systems that do not support CUPS, this function will return false
		That means the application has to handle the number of copies by printing the same document the required number of times.
		"""
		res = super(QPrinter,self).supportsMultipleCopies()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def toPage(self):
		"""
		Returns the number of the last page in a range of pages to be printed (the to page setting)
		Pages in a document are numbered according to the convention that the first page is page 1.
		By default, this function returns a special value of 0, meaning that the to page setting is unset.
		The programmer is responsible for reading this setting and printing accordingly.
		"""
		res = super(QPrinter,self).toPage()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def getPageMargins(self,unit):
		"""
		getPageMargins(unit)
			unit=QtGui.QPrinter.Unit

		Returns the page margins for this printer in left , top , right , bottom
		The unit of the returned margins are specified with the unit parameter.
		"""
		res = super(QPrinter,self).getPageMargins(unit)
		return res
	#----------------------------------------------------------------------
	def init(self,mode):
		"""
		init(mode)
			mode=QtGui.QPrinter.PrinterMode


		"""
		res = super(QPrinter,self).init(mode)
		return res
	#----------------------------------------------------------------------
	def pageRect(self,arg__1):
		"""
		pageRect(arg__1)
			arg__1=QtGui.QPrinter.Unit

		Returns the pages rectangle in unit ; this is usually smaller than the PySide.QtGui.QPrinter.paperRect() since the page normally has margins between its borders and the paper.
		"""
		res = super(QPrinter,self).pageRect(arg__1)
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def paperRect(self,arg__1):
		"""
		paperRect(arg__1)
			arg__1=QtGui.QPrinter.Unit

		Returns the papers rectangle in unit ; this is usually larger than the PySide.QtGui.QPrinter.pageRect() .
		"""
		res = super(QPrinter,self).paperRect(arg__1)
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def paperSize(self,unit):
		"""
		paperSize(unit)
			unit=QtGui.QPrinter.Unit

		Returns the paper size in unit .
		"""
		res = super(QPrinter,self).paperSize(unit)
		isinstance(res,QtCore.QSizeF)
		return res
	#----------------------------------------------------------------------
	def setCollateCopies(self,collate):
		"""
		setCollateCopies(collate)
			collate=QtCore.bool

		Sets the default value for collation checkbox when the print dialog appears
		If collate is true, it will enable setCollateCopiesEnabled()
		The default value is false
		This value will be changed by what the user presses in the print dialog.
		"""
		res = super(QPrinter,self).setCollateCopies(collate)
		return res
	#----------------------------------------------------------------------
	def setColorMode(self,arg__1):
		"""
		setColorMode(arg__1)
			arg__1=QtGui.QPrinter.ColorMode

		Sets the printers color mode to newColorMode , which can be either Color or GrayScale .
		"""
		res = super(QPrinter,self).setColorMode(arg__1)
		return res
	#----------------------------------------------------------------------
	def setCopyCount(self,arg__1):
		"""
		setCopyCount(arg__1)
			arg__1=QtCore.int

		Sets the number of copies to be printed to count .
		The printer driver reads this setting and prints the specified number of copies.
		"""
		res = super(QPrinter,self).setCopyCount(arg__1)
		return res
	#----------------------------------------------------------------------
	def setCreator(self,arg__1):
		"""
		setCreator(arg__1)
			arg__1=unicode

		Sets the name of the application that created the document to creator .
		This function is only applicable to the X11 version of Qt
		If no creator name is specified, the creator will be set to Qt followed by some version number.
		"""
		res = super(QPrinter,self).setCreator(arg__1)
		return res
	#----------------------------------------------------------------------
	def setDocName(self,arg__1):
		"""
		setDocName(arg__1)
			arg__1=unicode

		Sets the document name to name .
		On X11, the document name is for example used as the default output filename in PySide.QtGui.QPrintDialog
		Note that the document name does not affect the file name if the printer is printing to a file
		Use the setOutputFile() function for this.
		"""
		res = super(QPrinter,self).setDocName(arg__1)
		return res
	#----------------------------------------------------------------------
	def setDoubleSidedPrinting(self,enable):
		"""
		setDoubleSidedPrinting(enable)
			enable=QtCore.bool

		Enables double sided printing if doubleSided is true; otherwise disables it.
		Currently this option is only supported on X11.
		"""
		res = super(QPrinter,self).setDoubleSidedPrinting(enable)
		return res
	#----------------------------------------------------------------------
	def setDuplex(self,duplex):
		"""
		setDuplex(duplex)
			duplex=QtGui.QPrinter.DuplexMode

		Enables double sided printing based on the duplex mode.
		Currently this option is only supported on X11.
		"""
		res = super(QPrinter,self).setDuplex(duplex)
		return res
	#----------------------------------------------------------------------
	def setEngines(self,printEngine,paintEngine):
		"""
		setEngines(printEngine,paintEngine)
			printEngine=QtGui.QPrintEngine
			paintEngine=QtGui.QPaintEngine

		This function is used by subclasses of PySide.QtGui.QPrinter to specify custom print and paint engines (printEngine and paintEngine , respectively).
		PySide.QtGui.QPrinter does not take ownership of the engines, so you need to manage these engine instances yourself.
		Note that changing the engines will reset the printer state and all its properties.
		"""
		res = super(QPrinter,self).setEngines(printEngine,paintEngine)
		return res
	#----------------------------------------------------------------------
	def setFontEmbeddingEnabled(self,enable):
		"""
		setFontEmbeddingEnabled(enable)
			enable=QtCore.bool

		Enabled or disables font embedding depending on enable .
		Currently this option is only supported on X11.
		"""
		res = super(QPrinter,self).setFontEmbeddingEnabled(enable)
		return res
	#----------------------------------------------------------------------
	def setFromTo(self,fromPage,toPage):
		"""
		setFromTo(fromPage,toPage)
			fromPage=QtCore.int
			toPage=QtCore.int

		Sets the range of pages to be printed to cover the pages with numbers specified by from and to , where from corresponds to the first page in the range and to corresponds to the last.
		This function is mostly used to set a default value that the user can override in the print dialog when you call setup() .
		"""
		res = super(QPrinter,self).setFromTo(fromPage,toPage)
		return res
	#----------------------------------------------------------------------
	def setFullPage(self,arg__1):
		"""
		setFullPage(arg__1)
			arg__1=QtCore.bool

		If fp is true, enables support for painting over the entire page; otherwise restricts painting to the printable area reported by the device.
		By default, full page printing is disabled
		In this case, the origin of the PySide.QtGui.QPrinter s coordinate system coincides with the top-left corner of the printable area.
		If full page printing is enabled, the origin of the PySide.QtGui.QPrinter s coordinate system coincides with the top-left corner of the paper itself
		In this case, the device metrics will report the exact same dimensions as indicated by QPrinter.PaperSize
		It may not be possible to print on the entire physical page because of the printers margins, so the application must account for the margins itself.
		"""
		res = super(QPrinter,self).setFullPage(arg__1)
		return res
	#----------------------------------------------------------------------
	def setNumCopies(self,arg__1):
		"""
		setNumCopies(arg__1)
			arg__1=QtCore.int

		Sets the number of copies to be printed to numCopies .
		The printer driver reads this setting and prints the specified number of copies.
		Use PySide.QtGui.QPrinter.setCopyCount() instead.
		"""
		res = super(QPrinter,self).setNumCopies(arg__1)
		return res
	#----------------------------------------------------------------------
	def setOrientation(self,arg__1):
		"""
		setOrientation(arg__1)
			arg__1=QtGui.QPrinter.Orientation

		Sets the print orientation to orientation .
		The orientation can be either QPrinter.Portrait or QPrinter.Landscape .
		The printer driver reads this setting and prints using the specified orientation.
		On Windows, this option can be changed while printing and will take effect from the next call to PySide.QtGui.QPrinter.newPage() .
		On Mac OS X, changing the orientation during a print job has no effect.
		"""
		res = super(QPrinter,self).setOrientation(arg__1)
		return res
	#----------------------------------------------------------------------
	def setOutputFileName(self,arg__1):
		"""
		setOutputFileName(arg__1)
			arg__1=unicode

		Sets the name of the output file to fileName .
		Setting a null or empty name (0 or ) disables printing to a file
		Setting a non-empty name enables printing to a file.
		This can change the value of PySide.QtGui.QPrinter.outputFormat()
		If the file name has the suffix .ps then PostScript is automatically selected as output format
		If the file name has the .pdf suffix PDF is generated
		If the file name has a suffix other than .ps and .pdf, the output format used is the one set with PySide.QtGui.QPrinter.setOutputFormat() .
		PySide.QtGui.QPrinter uses Qts cross-platform PostScript or PDF print engines respectively
		If you can produce this format natively, for example Mac OS X can generate PDFs from its print engine, set the output format back to NativeFormat .
		"""
		res = super(QPrinter,self).setOutputFileName(arg__1)
		return res
	#----------------------------------------------------------------------
	def setOutputFormat(self,format):
		"""
		setOutputFormat(format)
			format=QtGui.QPrinter.OutputFormat

		Sets the output format for this printer to format .
		"""
		res = super(QPrinter,self).setOutputFormat(format)
		return res
	#----------------------------------------------------------------------
	def setPageMargins(self,left,top,right,bottom,unit):
		"""
		setPageMargins(left,top,right,bottom,unit)
			left=QtCore.qreal
			top=QtCore.qreal
			right=QtCore.qreal
			bottom=QtCore.qreal
			unit=QtGui.QPrinter.Unit

		This function sets the left , top , right and bottom page margins for this printer
		The unit of the margins are specified with the unit parameter.
		"""
		res = super(QPrinter,self).setPageMargins(left,top,right,bottom,unit)
		return res
	#----------------------------------------------------------------------
	def setPageOrder(self,arg__1):
		"""
		setPageOrder(arg__1)
			arg__1=QtGui.QPrinter.PageOrder

		Sets the page order to pageOrder .
		The page order can be QPrinter.FirstPageFirst or QPrinter.LastPageFirst
		The application is responsible for reading the page order and printing accordingly.
		This function is mostly useful for setting a default value that the user can override in the print dialog.
		This function is only supported under X11.
		"""
		res = super(QPrinter,self).setPageOrder(arg__1)
		return res
	#----------------------------------------------------------------------
	def setPageSize(self,arg__1):
		"""
		setPageSize(arg__1)
			arg__1=QtGui.QPrinter.PageSize

		Sets the printer page size based on newPageSize .
		Use PySide.QtGui.QPrinter.setPaperSize() instead.
		"""
		res = super(QPrinter,self).setPageSize(arg__1)
		return res
	#----------------------------------------------------------------------
	def setPaperSize(self,*args,**kwargs):
		"""
		setPaperSize(arg__1)
			arg__1=QtGui.QPrinter.PageSize

		setPaperSize(paperSize,unit)
			paperSize=QtCore.QSizeF
			unit=QtGui.QPrinter.Unit


		"""
		res = super(QPrinter,self).setPaperSize(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setPaperSource(self,arg__1):
		"""
		setPaperSource(arg__1)
			arg__1=QtGui.QPrinter.PaperSource

		Sets the paper source setting to source .
		Windows only: This option can be changed while printing and will take effect from the next call to PySide.QtGui.QPrinter.newPage()
		"""
		res = super(QPrinter,self).setPaperSource(arg__1)
		return res
	#----------------------------------------------------------------------
	def setPrintProgram(self,arg__1):
		"""
		setPrintProgram(arg__1)
			arg__1=unicode

		Sets the name of the program that should do the print job to printProg .
		On X11, this function sets the program to call with the PostScript output
		On other platforms, it has no effect.
		"""
		res = super(QPrinter,self).setPrintProgram(arg__1)
		return res
	#----------------------------------------------------------------------
	def setPrintRange(self,range):
		"""
		setPrintRange(range)
			range=QtGui.QPrinter.PrintRange

		Sets the print range option in to be range .
		"""
		res = super(QPrinter,self).setPrintRange(range)
		return res
	#----------------------------------------------------------------------
	def setPrinterName(self,arg__1):
		"""
		setPrinterName(arg__1)
			arg__1=unicode

		Sets the printer name to name .
		"""
		res = super(QPrinter,self).setPrinterName(arg__1)
		return res
	#----------------------------------------------------------------------
	def setResolution(self,arg__1):
		"""
		setResolution(arg__1)
			arg__1=QtCore.int

		Requests that the printer prints at dpi or as near to dpi as possible.
		This setting affects the coordinate system as returned by, for example QPainter.viewport() .
		This function must be called before QPainter.begin() to have an effect on all platforms.
		"""
		res = super(QPrinter,self).setResolution(arg__1)
		return res

from PySide import QtGui, QtCore

class QWizard(QtGui.QWizard):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QWizard,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def currentId(self):
		"""
		This property holds the ID of the current page.
		This property cannot be set directly
		To change the current page, call PySide.QtGui.QWizard.next() , PySide.QtGui.QWizard.back() , or PySide.QtGui.QWizard.restart() .
		By default, this property has a value of -1, indicating that no page is currently shown.
		"""
		res = super(QWizard,self).currentId()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def currentPage(self):
		"""
		Returns a pointer to the current page, or 0 if there is no current page (e.g., before the wizard is shown).
		This is equivalent to calling page( PySide.QtGui.QWizard.currentId() ).
		"""
		res = super(QWizard,self).currentPage()
		isinstance(res,QtGui.QWizardPage)
		return res
	#----------------------------------------------------------------------
	def helpRequested(self):
		"""

		"""
		res = super(QWizard,self).helpRequested()
		return res
	#----------------------------------------------------------------------
	def nextId(self):
		"""
		This virtual function is called by PySide.QtGui.QWizard to find out which page to show when the user clicks the Next button.
		The return value is the ID of the next page, or -1 if no page follows.
		The default implementation calls QWizardPage.nextId() on the PySide.QtGui.QWizard.currentPage() .
		By reimplementing this function, you can specify a dynamic page order.
		"""
		res = super(QWizard,self).nextId()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def options(self):
		"""
		This property holds the various options that affect the look and feel of the wizard.
		By default, the following options are set (depending on the platform):
		"""
		res = super(QWizard,self).options()
		isinstance(res,QtGui.QWizard.WizardOptions)
		return res
	#----------------------------------------------------------------------
	def pageIds(self):
		"""
		Returns the list of page IDs.
		"""
		res = super(QWizard,self).pageIds()
		return res
	#----------------------------------------------------------------------
	def sideWidget(self):
		"""
		Returns the widget on the left side of the wizard or 0.
		By default, no side widget is present.
		"""
		res = super(QWizard,self).sideWidget()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def startId(self):
		"""
		This property holds the ID of the first page.
		If this property isnt explicitly set, this property defaults to the lowest page ID in this wizard, or -1 if no page has been inserted yet.
		"""
		res = super(QWizard,self).startId()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def subTitleFormat(self):
		"""
		This property holds the text format used by page subtitles.
		The default format is Qt.AutoText .
		"""
		res = super(QWizard,self).subTitleFormat()
		isinstance(res,QtCore.Qt.TextFormat)
		return res
	#----------------------------------------------------------------------
	def titleFormat(self):
		"""
		This property holds the text format used by page titles.
		The default format is Qt.AutoText .
		"""
		res = super(QWizard,self).titleFormat()
		isinstance(res,QtCore.Qt.TextFormat)
		return res
	#----------------------------------------------------------------------
	def validateCurrentPage(self):
		"""
		This virtual function is called by PySide.QtGui.QWizard when the user clicks Next or Finish to perform some last-minute validation
		If it returns true, the next page is shown (or the wizard finishes); otherwise, the current page stays up.
		The default implementation calls QWizardPage.validatePage() on the PySide.QtGui.QWizard.currentPage() .
		When possible, it is usually better style to disable the Next or Finish button (by specifying mandatory fields or by reimplementing QWizardPage.isComplete() ) than to reimplement PySide.QtGui.QWizard.validateCurrentPage() .
		"""
		res = super(QWizard,self).validateCurrentPage()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def visitedPages(self):
		"""
		Returns the list of IDs of visited pages, in the order in which the pages were visited.
		Pressing Back marks the current page as unvisited again.
		"""
		res = super(QWizard,self).visitedPages()
		return res
	#----------------------------------------------------------------------
	def wizardStyle(self):
		"""
		This property holds the look and feel of the wizard.
		By default, PySide.QtGui.QWizard uses the AeroStyle on a Windows Vista system with alpha compositing enabled, regardless of the current widget style
		If this is not the case, the default wizard style depends on the current widget style as follows: MacStyle is the default if the current widget style is QMacStyle , ModernStyle is the default if the current widget style is PySide.QtGui.QWindowsStyle , and ClassicStyle is the default in all other cases.
		"""
		res = super(QWizard,self).wizardStyle()
		isinstance(res,QtGui.QWizard.WizardStyle)
		return res
	#----------------------------------------------------------------------
	def addPage(self,page):
		"""
		addPage(page)
			page=QtGui.QWizardPage

		Adds the given page to the wizard, and returns the pages ID.
		The ID is guaranteed to be larger than any other ID in the PySide.QtGui.QWizard so far.
		"""
		res = super(QWizard,self).addPage(page)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def button(self,which):
		"""
		button(which)
			which=QtGui.QWizard.WizardButton

		Returns the button corresponding to role which .
		"""
		res = super(QWizard,self).button(which)
		isinstance(res,QtGui.QAbstractButton)
		return res
	#----------------------------------------------------------------------
	def buttonText(self,which):
		"""
		buttonText(which)
			which=QtGui.QWizard.WizardButton

		Returns the text on button which .
		If a text has ben set using PySide.QtGui.QWizard.setButtonText() , this text is returned.
		By default, the text on buttons depends on the PySide.QtGui.QWizard.wizardStyle()
		For example, on Mac OS X, the Next button is called Continue .
		"""
		res = super(QWizard,self).buttonText(which)
		return res
	#----------------------------------------------------------------------
	def cleanupPage(self,id):
		"""
		cleanupPage(id)
			id=QtCore.int

		This virtual function is called by PySide.QtGui.QWizard to clean up page id just before the user leaves it by clicking Back (unless the QWizard.IndependentPages option is set).
		The default implementation calls QWizardPage.cleanupPage() on page(id ).
		"""
		res = super(QWizard,self).cleanupPage(id)
		return res
	#----------------------------------------------------------------------
	def field(self,name):
		"""
		field(name)
			name=unicode

		Returns the value of the field called name .
		This function can be used to access fields on any page of the wizard.
		"""
		res = super(QWizard,self).field(name)
		return res
	#----------------------------------------------------------------------
	def hasVisitedPage(self,id):
		"""
		hasVisitedPage(id)
			id=QtCore.int

		Returns true if the page history contains page id ; otherwise, returns false.
		Pressing Back marks the current page as unvisited again.
		"""
		res = super(QWizard,self).hasVisitedPage(id)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def initializePage(self,id):
		"""
		initializePage(id)
			id=QtCore.int

		This virtual function is called by PySide.QtGui.QWizard to prepare page id just before it is shown either as a result of QWizard.restart() being called, or as a result of the user clicking Next
		(However, if the QWizard.IndependentPages option is set, this function is only called the first time the page is shown.)
		By reimplementing this function, you can ensure that the pages fields are properly initialized based on fields from previous pages.
		The default implementation calls QWizardPage.initializePage() on page(id ).
		"""
		res = super(QWizard,self).initializePage(id)
		return res
	#----------------------------------------------------------------------
	def page(self,id):
		"""
		page(id)
			id=QtCore.int

		Returns the page with the given id , or 0 if there is no such page.
		"""
		res = super(QWizard,self).page(id)
		isinstance(res,QtGui.QWizardPage)
		return res
	#----------------------------------------------------------------------
	def pixmap(self,which):
		"""
		pixmap(which)
			which=QtGui.QWizard.WizardPixmap

		Returns the pixmap set for role which .
		By default, the only pixmap that is set is the BackgroundPixmap on Mac OS X.
		"""
		res = super(QWizard,self).pixmap(which)
		isinstance(res,QtGui.QPixmap)
		return res
	#----------------------------------------------------------------------
	def removePage(self,id):
		"""
		removePage(id)
			id=QtCore.int

		Removes the page with the given id
		PySide.QtGui.QWizard.cleanupPage() will be called if necessary.
		"""
		res = super(QWizard,self).removePage(id)
		return res
	#----------------------------------------------------------------------
	def setButton(self,which,button):
		"""
		setButton(which,button)
			which=QtGui.QWizard.WizardButton
			button=QtGui.QAbstractButton

		Sets the button corresponding to role which to button .
		To add extra buttons to the wizard (e.g., a Print button), one way is to call PySide.QtGui.QWizard.setButton() with CustomButton1 to CustomButton3 , and make the buttons visible using the HaveCustomButton1 to HaveCustomButton3 options.
		"""
		res = super(QWizard,self).setButton(which,button)
		return res
	#----------------------------------------------------------------------
	def setButtonLayout(self,layout):
		"""
		setButtonLayout(layout)
			layout=unKnown


		"""
		res = super(QWizard,self).setButtonLayout(layout)
		return res
	#----------------------------------------------------------------------
	def setButtonText(self,which,text):
		"""
		setButtonText(which,text)
			which=QtGui.QWizard.WizardButton
			text=unicode

		Sets the text on button which to be text .
		By default, the text on buttons depends on the PySide.QtGui.QWizard.wizardStyle()
		For example, on Mac OS X, the Next button is called Continue .
		To add extra buttons to the wizard (e.g., a Print button), one way is to call PySide.QtGui.QWizard.setButtonText() with CustomButton1 , CustomButton2 , or CustomButton3 to set their text, and make the buttons visible using the HaveCustomButton1 , HaveCustomButton2 , and/or HaveCustomButton3 options.
		Button texts may also be set on a per-page basis using QWizardPage.setButtonText() .
		"""
		res = super(QWizard,self).setButtonText(which,text)
		return res
	#----------------------------------------------------------------------
	def setDefaultProperty(self,className,property,changedSignal):
		"""
		setDefaultProperty(className,property,changedSignal)
			className=str
			property=str
			changedSignal=str

		Sets the default property for className to be property , and the associated change signal to be changedSignal .
		The default property is used when an instance of className (or of one of its subclasses) is passed to QWizardPage.registerField() and no property is specified.
		PySide.QtGui.QWizard knows the most common Qt widgets
		For these (or their subclasses), you dont need to specify a property or a changedSignal
		The table below lists these widgets:
		"""
		res = super(QWizard,self).setDefaultProperty(className,property,changedSignal)
		return res
	#----------------------------------------------------------------------
	def setField(self,name,value):
		"""
		setField(name,value)
			name=unicode
			value=object

		Sets the value of the field called name to value .
		This function can be used to set fields on any page of the wizard.
		"""
		res = super(QWizard,self).setField(name,value)
		return res
	#----------------------------------------------------------------------
	def setOption(self,option,on=None):
		"""
		setOption(option,on=None)
			option=QtGui.QWizard.WizardOption
			on=QtCore.bool

		Sets the given option to be enabled if on is true; otherwise, clears the given option .
		"""
		res = super(QWizard,self).setOption(option,on)
		return res
	#----------------------------------------------------------------------
	def setOptions(self,options):
		"""
		setOptions(options)
			options=QtGui.QWizard.WizardOptions

		This property holds the various options that affect the look and feel of the wizard.
		By default, the following options are set (depending on the platform):
		"""
		res = super(QWizard,self).setOptions(options)
		return res
	#----------------------------------------------------------------------
	def setPage(self,id,page):
		"""
		setPage(id,page)
			id=QtCore.int
			page=QtGui.QWizardPage

		Adds the given page to the wizard with the given id .
		"""
		res = super(QWizard,self).setPage(id,page)
		return res
	#----------------------------------------------------------------------
	def setPixmap(self,which,pixmap):
		"""
		setPixmap(which,pixmap)
			which=QtGui.QWizard.WizardPixmap
			pixmap=QtGui.QPixmap

		Sets the pixmap for role which to pixmap .
		The pixmaps are used by PySide.QtGui.QWizard when displaying a page
		Which pixmaps are actually used depend on the wizard style .
		Pixmaps can also be set for a specific page using QWizardPage.setPixmap() .
		"""
		res = super(QWizard,self).setPixmap(which,pixmap)
		return res
	#----------------------------------------------------------------------
	def setSideWidget(self,widget):
		"""
		setSideWidget(widget)
			widget=QtGui.QWidget

		Sets the given widget to be shown on the left side of the wizard
		For styles which use the WatermarkPixmap ( ClassicStyle and ModernStyle ) the side widget is displayed on top of the watermark, for other styles or when the watermark is not provided the side widget is displayed on the left side of the wizard.
		Passing 0 shows no side widget.
		When the widget is not 0 the wizard reparents it.
		Any previous side widget is hidden.
		You may call PySide.QtGui.QWizard.setSideWidget() with the same widget at different times.
		All widgets set here will be deleted by the wizard when it is destroyed unless you separately reparent the widget after setting some other side widget (or 0).
		By default, no side widget is present.
		"""
		res = super(QWizard,self).setSideWidget(widget)
		return res
	#----------------------------------------------------------------------
	def setStartId(self,id):
		"""
		setStartId(id)
			id=QtCore.int

		This property holds the ID of the first page.
		If this property isnt explicitly set, this property defaults to the lowest page ID in this wizard, or -1 if no page has been inserted yet.
		"""
		res = super(QWizard,self).setStartId(id)
		return res
	#----------------------------------------------------------------------
	def setSubTitleFormat(self,format):
		"""
		setSubTitleFormat(format)
			format=QtCore.Qt.TextFormat

		This property holds the text format used by page subtitles.
		The default format is Qt.AutoText .
		"""
		res = super(QWizard,self).setSubTitleFormat(format)
		return res
	#----------------------------------------------------------------------
	def setTitleFormat(self,format):
		"""
		setTitleFormat(format)
			format=QtCore.Qt.TextFormat

		This property holds the text format used by page titles.
		The default format is Qt.AutoText .
		"""
		res = super(QWizard,self).setTitleFormat(format)
		return res
	#----------------------------------------------------------------------
	def setWizardStyle(self,style):
		"""
		setWizardStyle(style)
			style=QtGui.QWizard.WizardStyle

		This property holds the look and feel of the wizard.
		By default, PySide.QtGui.QWizard uses the AeroStyle on a Windows Vista system with alpha compositing enabled, regardless of the current widget style
		If this is not the case, the default wizard style depends on the current widget style as follows: MacStyle is the default if the current widget style is QMacStyle , ModernStyle is the default if the current widget style is PySide.QtGui.QWindowsStyle , and ClassicStyle is the default in all other cases.
		"""
		res = super(QWizard,self).setWizardStyle(style)
		return res
	#----------------------------------------------------------------------
	def testOption(self,option):
		"""
		testOption(option)
			option=QtGui.QWizard.WizardOption

		Returns true if the given option is enabled; otherwise, returns false.
		"""
		res = super(QWizard,self).testOption(option)
		isinstance(res,bool)
		return res

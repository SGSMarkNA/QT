from PySide import QtGui, QtCore

class QWizardPage(QtGui.QWizardPage):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QWizardPage,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def cleanupPage(self):
		"""
		This virtual function is called by QWizard.cleanupPage() when the user leaves the page by clicking Back (unless the QWizard.IndependentPages option is set).
		The default implementation resets the pages fields to their original values (the values they had before PySide.QtGui.QWizardPage.initializePage() was called).
		"""
		res = super(QWizardPage,self).cleanupPage()
		return res
	#----------------------------------------------------------------------
	def completeChanged(self):
		"""

		"""
		res = super(QWizardPage,self).completeChanged()
		return res
	#----------------------------------------------------------------------
	def initializePage(self):
		"""
		This virtual function is called by QWizard.initializePage() to prepare the page just before it is shown either as a result of QWizard.restart() being called, or as a result of the user clicking Next
		(However, if the QWizard.IndependentPages option is set, this function is only called the first time the page is shown.)
		By reimplementing this function, you can ensure that the pages fields are properly initialized based on fields from previous pages
		For example:
		The default implementation does nothing.
		"""
		res = super(QWizardPage,self).initializePage()
		return res
	#----------------------------------------------------------------------
	def isCommitPage(self):
		"""
		Returns true if this page is a commit page; otherwise returns false.
		"""
		res = super(QWizardPage,self).isCommitPage()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isComplete(self):
		"""
		This virtual function is called by PySide.QtGui.QWizard to determine whether the Next or Finish button should be enabled or disabled.
		The default implementation returns true if all mandatory fields are filled; otherwise, it returns false.
		If you reimplement this function, make sure to emit PySide.QtGui.QWizardPage.completeChanged() , from the rest of your implementation, whenever the value of PySide.QtGui.QWizardPage.isComplete() changes
		This ensures that PySide.QtGui.QWizard updates the enabled or disabled state of its buttons
		An example of the reimplementation is available here.
		"""
		res = super(QWizardPage,self).isComplete()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isFinalPage(self):
		"""
		This function is called by PySide.QtGui.QWizard to determine whether the Finish button should be shown for this page or not.
		By default, it returns true if there is no next page (i.e., PySide.QtGui.QWizardPage.nextId() returns -1); otherwise, it returns false.
		By explicitly calling setFinalPage(true), you can let the user perform an early finish.
		"""
		res = super(QWizardPage,self).isFinalPage()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def nextId(self):
		"""
		This virtual function is called by QWizard.nextId() to find out which page to show when the user clicks the Next button.
		The return value is the ID of the next page, or -1 if no page follows.
		By default, this function returns the lowest ID greater than the ID of the current page, or -1 if there is no such ID.
		By reimplementing this function, you can specify a dynamic page order
		For example:
		"""
		res = super(QWizardPage,self).nextId()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def subTitle(self):
		"""
		This property holds the subtitle of the page.
		The subtitle is shown by the PySide.QtGui.QWizard , between the title and the actual page
		Subtitles are optional
		In ClassicStyle and ModernStyle , using subtitles is necessary to make the header appear
		In MacStyle , the subtitle is shown as a text label just above the actual page.
		The subtitle may be plain text or HTML, depending on the value of the QWizard.subTitleFormat property.
		By default, this property contains an empty string.
		"""
		res = super(QWizardPage,self).subTitle()
		return res
	#----------------------------------------------------------------------
	def title(self):
		"""
		This property holds the title of the page.
		The title is shown by the PySide.QtGui.QWizard , above the actual page
		All pages should have a title.
		The title may be plain text or HTML, depending on the value of the QWizard.titleFormat property.
		By default, this property contains an empty string.
		"""
		res = super(QWizardPage,self).title()
		return res
	#----------------------------------------------------------------------
	def validatePage(self):
		"""
		This virtual function is called by QWizard.validateCurrentPage() when the user clicks Next or Finish to perform some last-minute validation
		If it returns true, the next page is shown (or the wizard finishes); otherwise, the current page stays up.
		The default implementation returns true.
		When possible, it is usually better style to disable the Next or Finish button (by specifying mandatory fields or reimplementing PySide.QtGui.QWizardPage.isComplete() ) than to reimplement PySide.QtGui.QWizardPage.validatePage() .
		"""
		res = super(QWizardPage,self).validatePage()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def wizard(self):
		"""
		Returns the wizard associated with this page, or 0 if this page hasnt been inserted into a PySide.QtGui.QWizard yet.
		"""
		res = super(QWizardPage,self).wizard()
		isinstance(res,QtGui.QWizard)
		return res
	#----------------------------------------------------------------------
	def buttonText(self,which):
		"""
		buttonText(which)
			which=QtGui.QWizard.WizardButton


		"""
		res = super(QWizardPage,self).buttonText(which)
		return res
	#----------------------------------------------------------------------
	def field(self,name):
		"""
		field(name)
			name=unicode

		Returns the value of the field called name .
		This function can be used to access fields on any page of the wizard
		It is equivalent to calling PySide.QtGui.QWizardPage.wizard() ->``name`` :meth:` <PySide.QtGui.QWizard.field>` ).
		Example:
		"""
		res = super(QWizardPage,self).field(name)
		return res
	#----------------------------------------------------------------------
	def pixmap(self,which):
		"""
		pixmap(which)
			which=QtGui.QWizard.WizardPixmap


		"""
		res = super(QWizardPage,self).pixmap(which)
		isinstance(res,QtGui.QPixmap)
		return res
	#----------------------------------------------------------------------
	def registerField(self,name,widget,property=None,changedSignal=None):
		"""
		registerField(name,widget,property=None,changedSignal=None)
			name=unicode
			widget=QtGui.QWidget
			property=str
			changedSignal=str

		Creates a field called name associated with the given property of the given widget
		From then on, that property becomes accessible using PySide.QtGui.QWizardPage.field() and PySide.QtGui.QWizardPage.setField() .
		Fields are global to the entire wizard and make it easy for any single page to access information stored by another page, without having to put all the logic in PySide.QtGui.QWizard or having the pages know explicitly about each other.
		If name ends with an asterisk (* ), the field is a mandatory field
		When a page has mandatory fields, the Next and/or Finish buttons are enabled only when all mandatory fields are filled
		This requires a changedSignal to be specified, to tell PySide.QtGui.QWizard to recheck the value stored by the mandatory field.
		PySide.QtGui.QWizard knows the most common Qt widgets
		For these (or their subclasses), you dont need to specify a property or a changedSignal
		The table below lists these widgets:
		You can use QWizard.setDefaultProperty() to add entries to this table or to override existing entries.
		To consider a field filled, PySide.QtGui.QWizard simply checks that their current value doesnt equal their original value (the value they had before PySide.QtGui.QWizardPage.initializePage() was called)
		For PySide.QtGui.QLineEdit , it also checks that PySide.QtGui.QLineEdit.hasAcceptableInput() returns true, to honor any validator or mask.
		PySide.QtGui.QWizard s mandatory field mechanism is provided for convenience
		It can be bypassed by reimplementing QWizardPage.isComplete() .
		"""
		res = super(QWizardPage,self).registerField(name,widget,property,changedSignal)
		return res
	#----------------------------------------------------------------------
	def setButtonText(self,which,text):
		"""
		setButtonText(which,text)
			which=QtGui.QWizard.WizardButton
			text=unicode


		"""
		res = super(QWizardPage,self).setButtonText(which,text)
		return res
	#----------------------------------------------------------------------
	def setCommitPage(self,commitPage):
		"""
		setCommitPage(commitPage)
			commitPage=QtCore.bool

		Sets this page to be a commit page if commitPage is true; otherwise, sets it to be a normal page.
		A commit page is a page that represents an action which cannot be undone by clicking Back or Cancel .
		A Commit button replaces the Next button on a commit page
		Clicking this button simply calls QWizard.next() just like clicking Next does.
		A page entered directly from a commit page has its Back button disabled.
		"""
		res = super(QWizardPage,self).setCommitPage(commitPage)
		return res
	#----------------------------------------------------------------------
	def setField(self,name,value):
		"""
		setField(name,value)
			name=unicode
			value=object

		Sets the value of the field called name to value .
		This function can be used to set fields on any page of the wizard
		It is equivalent to calling PySide.QtGui.QWizardPage.wizard() ->``name`` :meth:` <PySide.QtGui.QWizard.setField>` , value ).
		"""
		res = super(QWizardPage,self).setField(name,value)
		return res
	#----------------------------------------------------------------------
	def setFinalPage(self,finalPage):
		"""
		setFinalPage(finalPage)
			finalPage=QtCore.bool

		Explicitly sets this page to be final if finalPage is true.
		After calling setFinalPage(true), PySide.QtGui.QWizardPage.isFinalPage() returns true and the Finish button is visible (and enabled if PySide.QtGui.QWizardPage.isComplete() returns true).
		After calling setFinalPage(false), PySide.QtGui.QWizardPage.isFinalPage() returns true if PySide.QtGui.QWizardPage.nextId() returns -1; otherwise, it returns false.
		"""
		res = super(QWizardPage,self).setFinalPage(finalPage)
		return res
	#----------------------------------------------------------------------
	def setPixmap(self,which,pixmap):
		"""
		setPixmap(which,pixmap)
			which=QtGui.QWizard.WizardPixmap
			pixmap=QtGui.QPixmap


		"""
		res = super(QWizardPage,self).setPixmap(which,pixmap)
		return res
	#----------------------------------------------------------------------
	def setSubTitle(self,subTitle):
		"""
		setSubTitle(subTitle)
			subTitle=unicode

		This property holds the subtitle of the page.
		The subtitle is shown by the PySide.QtGui.QWizard , between the title and the actual page
		Subtitles are optional
		In ClassicStyle and ModernStyle , using subtitles is necessary to make the header appear
		In MacStyle , the subtitle is shown as a text label just above the actual page.
		The subtitle may be plain text or HTML, depending on the value of the QWizard.subTitleFormat property.
		By default, this property contains an empty string.
		"""
		res = super(QWizardPage,self).setSubTitle(subTitle)
		return res
	#----------------------------------------------------------------------
	def setTitle(self,title):
		"""
		setTitle(title)
			title=unicode

		This property holds the title of the page.
		The title is shown by the PySide.QtGui.QWizard , above the actual page
		All pages should have a title.
		The title may be plain text or HTML, depending on the value of the QWizard.titleFormat property.
		By default, this property contains an empty string.
		"""
		res = super(QWizardPage,self).setTitle(title)
		return res

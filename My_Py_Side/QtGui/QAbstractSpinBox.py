from PySide import QtGui, QtCore

class QAbstractSpinBox(QtGui.QAbstractSpinBox):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QAbstractSpinBox,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def alignment(self):
		"""
		This property holds the alignment of the spin box.
		Possible Values are Qt.AlignLeft , Qt.AlignRight , and Qt.AlignHCenter .
		By default, the alignment is Qt.AlignLeft
		Attempting to set the alignment to an illegal flag combination does nothing.
		"""
		res = super(QAbstractSpinBox,self).alignment()
		isinstance(res,QtCore.Qt.Alignment)
		return res
	#----------------------------------------------------------------------
	def buttonSymbols(self):
		"""
		This property holds the current button symbol mode.
		The possible values can be either UpDownArrows or PlusMinus
		The default is UpDownArrows .
		Note that some styles might render PlusMinus and UpDownArrows identically.
		"""
		res = super(QAbstractSpinBox,self).buttonSymbols()
		isinstance(res,QtGui.QAbstractSpinBox.ButtonSymbols)
		return res
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Clears the lineedit of all text but prefix and suffix.
		"""
		res = super(QAbstractSpinBox,self).clear()
		return res
	#----------------------------------------------------------------------
	def correctionMode(self):
		"""
		This property holds the mode to correct an Intermediate value if editing finishes.
		The default mode is QAbstractSpinBox.CorrectToPreviousValue .
		"""
		res = super(QAbstractSpinBox,self).correctionMode()
		isinstance(res,QtGui.QAbstractSpinBox.CorrectionMode)
		return res
	#----------------------------------------------------------------------
	def editingFinished(self):
		"""

		"""
		res = super(QAbstractSpinBox,self).editingFinished()
		return res
	#----------------------------------------------------------------------
	def hasAcceptableInput(self):
		"""
		This property holds whether the input satisfies the current validation.
		"""
		res = super(QAbstractSpinBox,self).hasAcceptableInput()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def hasFrame(self):
		"""
		This property holds whether the spin box draws itself with a frame.
		If enabled (the default) the spin box draws itself inside a frame, otherwise the spin box draws itself without any frame.
		"""
		res = super(QAbstractSpinBox,self).hasFrame()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def interpretText(self):
		"""
		This function interprets the text of the spin box
		If the value has changed since last interpretation it will emit signals.
		"""
		res = super(QAbstractSpinBox,self).interpretText()
		return res
	#----------------------------------------------------------------------
	def isAccelerated(self):
		"""
		This property holds whether the spin box will accelerate the frequency of the steps when pressing the step Up/Down buttons..
		If enabled the spin box will increase/decrease the value faster the longer you hold the button down.
		"""
		res = super(QAbstractSpinBox,self).isAccelerated()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isReadOnly(self):
		"""
		This property holds whether the spin box is read only..
		In read-only mode, the user can still copy the text to the clipboard, or drag and drop the text; but cannot edit it.
		The PySide.QtGui.QLineEdit in the PySide.QtGui.QAbstractSpinBox does not show a cursor in read-only mode.
		"""
		res = super(QAbstractSpinBox,self).isReadOnly()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def keyboardTracking(self):
		"""
		This property holds whether keyboard tracking is enabled for the spinbox..
		If keyboard tracking is enabled (the default), the spinbox emits the valueChanged() signal while the new value is being entered from the keyboard.
		E.g
		when the user enters the value 600 by typing 6, 0, and 0, the spinbox emits 3 signals with the values 6, 60, and 600 respectively.
		If keyboard tracking is disabled, the spinbox doesnt emit the valueChanged() signal while typing
		It emits the signal later, when the return key is pressed, when keyboard focus is lost, or when other spinbox functionality is used, e.g
		pressing an arrow key.
		"""
		res = super(QAbstractSpinBox,self).keyboardTracking()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def lineEdit(self):
		"""
		This function returns a pointer to the line edit of the spin box.
		"""
		res = super(QAbstractSpinBox,self).lineEdit()
		isinstance(res,QtGui.QLineEdit)
		return res
	#----------------------------------------------------------------------
	def specialValueText(self):
		"""
		This property holds the special-value text.
		If set, the spin box will display this text instead of a numeric value whenever the current value is equal to minimum()
		Typical use is to indicate that this choice has a special (default) meaning.
		For example, if your spin box allows the user to choose a scale factor (or zoom level) for displaying an image, and your application is able to automatically choose one that will enable the image to fit completely within the display window, you can set up the spin box like this:
		The user will then be able to choose a scale from 1% to 1000% or select Auto to leave it up to the application to choose
		Your code must then interpret the spin box value of 0 as a request from the user to scale the image to fit inside the window.
		All values are displayed with the prefix and suffix (if set), except for the special value, which only shows the special value text
		This special text is passed in the QSpinBox.valueChanged() signal that passes a PySide.QtCore.QString .
		To turn off the special-value text display, call this function with an empty string
		The default is no special-value text, i.e
		the numeric value is shown as usual.
		If no special-value text is set, PySide.QtGui.QAbstractSpinBox.specialValueText() returns an empty string.
		"""
		res = super(QAbstractSpinBox,self).specialValueText()
		return res
	#----------------------------------------------------------------------
	def stepEnabled(self):
		"""
		Virtual function that determines whether stepping up and down is legal at any given time.
		The up arrow will be painted as disabled unless ( PySide.QtGui.QAbstractSpinBox.stepEnabled() & StepUpEnabled ) != 0.
		The default implementation will return ( StepUpEnabled | StepDownEnabled ) if wrapping is turned on
		Else it will return StepDownEnabled if value is > minimum() ored with StepUpEnabled if value < maximum().
		If you subclass PySide.QtGui.QAbstractSpinBox you will need to reimplement this function.
		"""
		res = super(QAbstractSpinBox,self).stepEnabled()
		isinstance(res,QtGui.QAbstractSpinBox.StepEnabled)
		return res
	#----------------------------------------------------------------------
	def text(self):
		"""
		This property holds the spin boxs text, including any prefix and suffix.
		There is no default text.
		"""
		res = super(QAbstractSpinBox,self).text()
		return res
	#----------------------------------------------------------------------
	def wrapping(self):
		"""
		This property holds whether the spin box is circular..
		If wrapping is true stepping up from maximum() value will take you to the minimum() value and vica versa
		Wrapping only make sense if you have minimum() and maximum() values set.
		"""
		res = super(QAbstractSpinBox,self).wrapping()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def fixup(self,input):
		"""
		fixup(input)
			input=unicode

		This virtual function is called by the PySide.QtGui.QAbstractSpinBox if the input is not validated to QValidator.Acceptable when Return is pressed or PySide.QtGui.QAbstractSpinBox.interpretText() is called
		It will try to change the text so it is valid
		Reimplemented in the various subclasses.
		"""
		res = super(QAbstractSpinBox,self).fixup(input)
		return res
	#----------------------------------------------------------------------
	def initStyleOption(self,option):
		"""
		initStyleOption(option)
			option=QtGui.QStyleOptionSpinBox

		Initialize option with the values from this PySide.QtGui.QSpinBox
		This method is useful for subclasses when they need a PySide.QtGui.QStyleOptionSpinBox , but dont want to fill in all the information themselves.
		"""
		res = super(QAbstractSpinBox,self).initStyleOption(option)
		return res
	#----------------------------------------------------------------------
	def setAccelerated(self,on):
		"""
		setAccelerated(on)
			on=QtCore.bool

		This property holds whether the spin box will accelerate the frequency of the steps when pressing the step Up/Down buttons..
		If enabled the spin box will increase/decrease the value faster the longer you hold the button down.
		"""
		res = super(QAbstractSpinBox,self).setAccelerated(on)
		return res
	#----------------------------------------------------------------------
	def setAlignment(self,flag):
		"""
		setAlignment(flag)
			flag=QtCore.Qt.Alignment

		This property holds the alignment of the spin box.
		Possible Values are Qt.AlignLeft , Qt.AlignRight , and Qt.AlignHCenter .
		By default, the alignment is Qt.AlignLeft
		Attempting to set the alignment to an illegal flag combination does nothing.
		"""
		res = super(QAbstractSpinBox,self).setAlignment(flag)
		return res
	#----------------------------------------------------------------------
	def setButtonSymbols(self,bs):
		"""
		setButtonSymbols(bs)
			bs=QtGui.QAbstractSpinBox.ButtonSymbols

		This property holds the current button symbol mode.
		The possible values can be either UpDownArrows or PlusMinus
		The default is UpDownArrows .
		Note that some styles might render PlusMinus and UpDownArrows identically.
		"""
		res = super(QAbstractSpinBox,self).setButtonSymbols(bs)
		return res
	#----------------------------------------------------------------------
	def setCorrectionMode(self,cm):
		"""
		setCorrectionMode(cm)
			cm=QtGui.QAbstractSpinBox.CorrectionMode

		This property holds the mode to correct an Intermediate value if editing finishes.
		The default mode is QAbstractSpinBox.CorrectToPreviousValue .
		"""
		res = super(QAbstractSpinBox,self).setCorrectionMode(cm)
		return res
	#----------------------------------------------------------------------
	def setFrame(self,arg__1):
		"""
		setFrame(arg__1)
			arg__1=QtCore.bool

		This property holds whether the spin box draws itself with a frame.
		If enabled (the default) the spin box draws itself inside a frame, otherwise the spin box draws itself without any frame.
		"""
		res = super(QAbstractSpinBox,self).setFrame(arg__1)
		return res
	#----------------------------------------------------------------------
	def setKeyboardTracking(self,kt):
		"""
		setKeyboardTracking(kt)
			kt=QtCore.bool

		This property holds whether keyboard tracking is enabled for the spinbox..
		If keyboard tracking is enabled (the default), the spinbox emits the valueChanged() signal while the new value is being entered from the keyboard.
		E.g
		when the user enters the value 600 by typing 6, 0, and 0, the spinbox emits 3 signals with the values 6, 60, and 600 respectively.
		If keyboard tracking is disabled, the spinbox doesnt emit the valueChanged() signal while typing
		It emits the signal later, when the return key is pressed, when keyboard focus is lost, or when other spinbox functionality is used, e.g
		pressing an arrow key.
		"""
		res = super(QAbstractSpinBox,self).setKeyboardTracking(kt)
		return res
	#----------------------------------------------------------------------
	def setLineEdit(self,edit):
		"""
		setLineEdit(edit)
			edit=QtGui.QLineEdit

		Sets the line edit of the spinbox to be lineEdit instead of the current line edit widget
		lineEdit can not be 0.
		PySide.QtGui.QAbstractSpinBox takes ownership of the new lineEdit
		If QLineEdit.validator() for the lineEdit returns 0, the internal validator of the spinbox will be set on the line edit.
		"""
		res = super(QAbstractSpinBox,self).setLineEdit(edit)
		return res
	#----------------------------------------------------------------------
	def setReadOnly(self,r):
		"""
		setReadOnly(r)
			r=QtCore.bool

		This property holds whether the spin box is read only..
		In read-only mode, the user can still copy the text to the clipboard, or drag and drop the text; but cannot edit it.
		The PySide.QtGui.QLineEdit in the PySide.QtGui.QAbstractSpinBox does not show a cursor in read-only mode.
		"""
		res = super(QAbstractSpinBox,self).setReadOnly(r)
		return res
	#----------------------------------------------------------------------
	def setSpecialValueText(self,txt):
		"""
		setSpecialValueText(txt)
			txt=unicode

		This property holds the special-value text.
		If set, the spin box will display this text instead of a numeric value whenever the current value is equal to minimum()
		Typical use is to indicate that this choice has a special (default) meaning.
		For example, if your spin box allows the user to choose a scale factor (or zoom level) for displaying an image, and your application is able to automatically choose one that will enable the image to fit completely within the display window, you can set up the spin box like this:
		The user will then be able to choose a scale from 1% to 1000% or select Auto to leave it up to the application to choose
		Your code must then interpret the spin box value of 0 as a request from the user to scale the image to fit inside the window.
		All values are displayed with the prefix and suffix (if set), except for the special value, which only shows the special value text
		This special text is passed in the QSpinBox.valueChanged() signal that passes a PySide.QtCore.QString .
		To turn off the special-value text display, call this function with an empty string
		The default is no special-value text, i.e
		the numeric value is shown as usual.
		If no special-value text is set, PySide.QtGui.QAbstractSpinBox.specialValueText() returns an empty string.
		"""
		res = super(QAbstractSpinBox,self).setSpecialValueText(txt)
		return res
	#----------------------------------------------------------------------
	def setWrapping(self,w):
		"""
		setWrapping(w)
			w=QtCore.bool

		This property holds whether the spin box is circular..
		If wrapping is true stepping up from maximum() value will take you to the minimum() value and vica versa
		Wrapping only make sense if you have minimum() and maximum() values set.
		"""
		res = super(QAbstractSpinBox,self).setWrapping(w)
		return res
	#----------------------------------------------------------------------
	def stepBy(self,steps):
		"""
		stepBy(steps)
			steps=QtCore.int

		Virtual function that is called whenever the user triggers a step
		The steps parameter indicates how many steps were taken, e.g
		Pressing Qt.Key_Down will trigger a call to stepBy(-1), whereas pressing Qt.Key_Prior will trigger a call to stepBy(10).
		If you subclass PySide.QtGui.QAbstractSpinBox you must reimplement this function
		Note that this function is called even if the resulting value will be outside the bounds of minimum and maximum
		Its this functions job to handle these situations.
		"""
		res = super(QAbstractSpinBox,self).stepBy(steps)
		return res
	#----------------------------------------------------------------------
	def validate(self,input,pos):
		"""
		validate(input,pos)
			input=unicode
			pos=QtCore.int

		This virtual function is called by the PySide.QtGui.QAbstractSpinBox to determine whether input is valid
		The pos parameter indicates the position in the string
		Reimplemented in the various subclasses.
		"""
		res = super(QAbstractSpinBox,self).validate(input,pos)
		return res

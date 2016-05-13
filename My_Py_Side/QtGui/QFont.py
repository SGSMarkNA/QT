from PySide import QtGui, QtCore

class QFont(QtGui.QFont):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QFont,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def bold(self):
		"""
		Returns true if PySide.QtGui.QFont.weight() is a value greater than QFont.Normal ; otherwise returns false.
		"""
		res = super(QFont,self).bold()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def capitalization(self):
		"""
		Returns the current capitalization type of the font.
		"""
		res = super(QFont,self).capitalization()
		isinstance(res,QtGui.QFont.Capitalization)
		return res
	#----------------------------------------------------------------------
	def defaultFamily(self):
		"""
		Returns the family name that corresponds to the current style hint.
		"""
		res = super(QFont,self).defaultFamily()
		return res
	#----------------------------------------------------------------------
	def exactMatch(self):
		"""
		Returns true if a window system font exactly matching the settings of this font is available.
		"""
		res = super(QFont,self).exactMatch()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def family(self):
		"""
		Returns the requested font family name, i.e
		the name set in the constructor or the last setFont() call.
		"""
		res = super(QFont,self).family()
		return res
	#----------------------------------------------------------------------
	def fixedPitch(self):
		"""
		Returns true if fixed pitch has been set; otherwise returns false.
		"""
		res = super(QFont,self).fixedPitch()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def handle(self):
		"""
		Returns the window system handle to the font, for low-level access
		Using this function is not portable.
		"""
		res = super(QFont,self).handle()
		isinstance(res,QtCore.Qt::HANDLE)
		return res
	#----------------------------------------------------------------------
	def italic(self):
		"""
		Returns true if the PySide.QtGui.QFont.style() of the font is not QFont.StyleNormal
		"""
		res = super(QFont,self).italic()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def kerning(self):
		"""
		Returns true if kerning should be used when drawing text with this font.
		"""
		res = super(QFont,self).kerning()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def key(self):
		"""
		Returns the fonts key, a textual representation of a font
		It is typically used as the key for a cache or dictionary of fonts.
		"""
		res = super(QFont,self).key()
		return res
	#----------------------------------------------------------------------
	def lastResortFamily(self):
		"""
		Returns the last resort font family name.
		The current implementation tries a wide variety of common fonts, returning the first one it finds
		Is is possible that no family is found in which case an empty string is returned.
		"""
		res = super(QFont,self).lastResortFamily()
		return res
	#----------------------------------------------------------------------
	def lastResortFont(self):
		"""
		Returns a last resort font name for the font matching algorithm
		This is used if the last resort family is not available
		It will always return a name, if necessary returning something like fixed or system.
		The current implementation tries a wide variety of common fonts, returning the first one it finds
		The implementation may change at any time, but this function will always return a string containing something.
		It is theoretically possible that there really isnt a PySide.QtGui.QFont.lastResortFont() in which case Qt will abort with an error message
		We have not been able to identify a case where this happens
		Please report it as a bug if it does, preferably with a list of the fonts you have installed.
		"""
		res = super(QFont,self).lastResortFont()
		return res
	#----------------------------------------------------------------------
	def letterSpacing(self):
		"""
		Returns the letter spacing for the font.
		"""
		res = super(QFont,self).letterSpacing()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def letterSpacingType(self):
		"""
		Returns the spacing type used for letter spacing.
		"""
		res = super(QFont,self).letterSpacingType()
		isinstance(res,QtGui.QFont.SpacingType)
		return res
	#----------------------------------------------------------------------
	def overline(self):
		"""
		Returns true if overline has been set; otherwise returns false.
		"""
		res = super(QFont,self).overline()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def pixelSize(self):
		"""
		Returns the pixel size of the font if it was set with PySide.QtGui.QFont.setPixelSize()
		Returns -1 if the size was set with PySide.QtGui.QFont.setPointSize() or PySide.QtGui.QFont.setPointSizeF() .
		"""
		res = super(QFont,self).pixelSize()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def pointSize(self):
		"""
		Returns the point size of the font
		Returns -1 if the font size was specified in pixels.
		"""
		res = super(QFont,self).pointSize()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def pointSizeF(self):
		"""
		Returns the point size of the font
		Returns -1 if the font size was specified in pixels.
		"""
		res = super(QFont,self).pointSizeF()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def rawMode(self):
		"""
		Returns true if raw mode is used for font name matching; otherwise returns false.
		"""
		res = super(QFont,self).rawMode()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def rawName(self):
		"""
		Returns the name of the font within the underlying window system.
		On X11, this function will return an empty string if Qt is built with FontConfig support; otherwise the XLFD (X Logical Font Description) is returned.
		Using the return value of this function is usually notportable .
		"""
		res = super(QFont,self).rawName()
		return res
	#----------------------------------------------------------------------
	def resolve(self):
		"""

		"""
		res = super(QFont,self).resolve()
		isinstance(res,QtCore.uint)
		return res
	#----------------------------------------------------------------------
	def stretch(self):
		"""
		Returns the stretch factor for the font.
		"""
		res = super(QFont,self).stretch()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def strikeOut(self):
		"""
		Returns true if strikeout has been set; otherwise returns false.
		"""
		res = super(QFont,self).strikeOut()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def style(self):
		"""
		Returns the style of the font.
		"""
		res = super(QFont,self).style()
		isinstance(res,QtGui.QFont.Style)
		return res
	#----------------------------------------------------------------------
	def styleHint(self):
		"""
		Returns the QFont.StyleHint .
		The style hint affects the font matching algorithm
		See QFont.StyleHint for the list of available hints.
		"""
		res = super(QFont,self).styleHint()
		isinstance(res,QtGui.QFont.StyleHint)
		return res
	#----------------------------------------------------------------------
	def styleStrategy(self):
		"""
		Returns the QFont.StyleStrategy .
		The style strategy affects the font matching algorithm
		See QFont.StyleStrategy for the list of available strategies.
		"""
		res = super(QFont,self).styleStrategy()
		isinstance(res,QtGui.QFont.StyleStrategy)
		return res
	#----------------------------------------------------------------------
	def toString(self):
		"""
		Returns a description of the font
		The description is a comma-separated list of the attributes, perfectly suited for use in PySide.QtCore.QSettings .
		"""
		res = super(QFont,self).toString()
		return res
	#----------------------------------------------------------------------
	def underline(self):
		"""
		Returns true if underline has been set; otherwise returns false.
		"""
		res = super(QFont,self).underline()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def weight(self):
		"""
		Returns the weight of the font which is one of the enumerated values from QFont.Weight .
		"""
		res = super(QFont,self).weight()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def wordSpacing(self):
		"""
		Returns the word spacing for the font.
		"""
		res = super(QFont,self).wordSpacing()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def x11Screen(self):
		"""

		"""
		res = super(QFont,self).x11Screen()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def fromString(self,arg__1):
		"""
		fromString(arg__1)
			arg__1=unicode

		Sets this font to match the description descrip
		The description is a comma-separated list of the font attributes, as returned by PySide.QtGui.QFont.toString() .
		"""
		res = super(QFont,self).fromString(arg__1)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isCopyOf(self,arg__1):
		"""
		isCopyOf(arg__1)
			arg__1=QtGui.QFont

		Returns true if this font and f are copies of each other, i.e
		one of them was created as a copy of the other and neither has been modified since
		This is much stricter than equality.
		"""
		res = super(QFont,self).isCopyOf(arg__1)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,arg__1):
		"""
		__ne__(arg__1)
			arg__1=QtGui.QFont

		Returns true if this font is different from f ; otherwise returns false.
		Two QFonts are considered to be different if their font attributes are different
		If PySide.QtGui.QFont.rawMode() is enabled for both fonts, only the family fields are compared.
		"""
		res = super(QFont,self).__ne__(arg__1)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __lt__(self,arg__1):
		"""
		__lt__(arg__1)
			arg__1=QtGui.QFont

		Provides an arbitrary comparison of this font and font f
		All that is guaranteed is that the operator returns false if both fonts are equal and that (f1 < f2) == !(f2 < f1) if the fonts are not equal.
		This function is useful in some circumstances, for example if you want to use PySide.QtGui.QFont objects as keys in a QMap .
		"""
		res = super(QFont,self).__lt__(arg__1)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,arg__1):
		"""
		__eq__(arg__1)
			arg__1=QtGui.QFont

		Returns true if this font is equal to f ; otherwise returns false.
		Two QFonts are considered equal if their font attributes are equal
		If PySide.QtGui.QFont.rawMode() is enabled for both fonts, only the family fields are compared.
		"""
		res = super(QFont,self).__eq__(arg__1)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def resolve(self,*args,**kwargs):
		"""
		resolve(mask)
			mask=QtCore.uint

		resolve(arg__1)
			arg__1=QtGui.QFont


		"""
		res = super(QFont,self).resolve(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setBold(self,arg__1):
		"""
		setBold(arg__1)
			arg__1=QtCore.bool

		If enable is true sets the fonts weight to QFont.Bold ; otherwise sets the weight to QFont.Normal .
		For finer boldness control use PySide.QtGui.QFont.setWeight() .
		"""
		res = super(QFont,self).setBold(arg__1)
		return res
	#----------------------------------------------------------------------
	def setCapitalization(self,arg__1):
		"""
		setCapitalization(arg__1)
			arg__1=QtGui.QFont.Capitalization

		Sets the capitalization of the text in this font to caps .
		A fonts capitalization makes the text appear in the selected capitalization mode.
		"""
		res = super(QFont,self).setCapitalization(arg__1)
		return res
	#----------------------------------------------------------------------
	def setFamily(self,arg__1):
		"""
		setFamily(arg__1)
			arg__1=unicode

		Sets the family name of the font
		The name is case insensitive and may include a foundry name.
		The family name may optionally also include a foundry name, e.g
		Helvetica [Cronyx]
		If the family is available from more than one foundry and the foundry isnt specified, an arbitrary foundry is chosen
		If the family isnt available a family will be set using the font matching algorithm.
		"""
		res = super(QFont,self).setFamily(arg__1)
		return res
	#----------------------------------------------------------------------
	def setFixedPitch(self,arg__1):
		"""
		setFixedPitch(arg__1)
			arg__1=QtCore.bool

		If enable is true, sets fixed pitch on; otherwise sets fixed pitch off.
		"""
		res = super(QFont,self).setFixedPitch(arg__1)
		return res
	#----------------------------------------------------------------------
	def setItalic(self,b):
		"""
		setItalic(b)
			b=QtCore.bool

		Sets the PySide.QtGui.QFont.style() of the font to QFont.StyleItalic if enable is true; otherwise the style is set to QFont.StyleNormal .
		"""
		res = super(QFont,self).setItalic(b)
		return res
	#----------------------------------------------------------------------
	def setKerning(self,arg__1):
		"""
		setKerning(arg__1)
			arg__1=QtCore.bool

		Enables kerning for this font if enable is true; otherwise disables it
		By default, kerning is enabled.
		When kerning is enabled, glyph metrics do not add up anymore, even for Latin text
		In other words, the assumption that width(a) + width(b) is equal to width(ab) is not neccesairly true.
		"""
		res = super(QFont,self).setKerning(arg__1)
		return res
	#----------------------------------------------------------------------
	def setLetterSpacing(self,type,spacing):
		"""
		setLetterSpacing(type,spacing)
			type=QtGui.QFont.SpacingType
			spacing=QtCore.qreal

		Sets the letter spacing for the font to spacing and the type of spacing to type .
		Letter spacing changes the default spacing between individual letters in the font
		The spacing between the letters can be made smaller as well as larger.
		"""
		res = super(QFont,self).setLetterSpacing(type,spacing)
		return res
	#----------------------------------------------------------------------
	def setOverline(self,arg__1):
		"""
		setOverline(arg__1)
			arg__1=QtCore.bool

		If enable is true, sets overline on; otherwise sets overline off.
		"""
		res = super(QFont,self).setOverline(arg__1)
		return res
	#----------------------------------------------------------------------
	def setPixelSize(self,arg__1):
		"""
		setPixelSize(arg__1)
			arg__1=QtCore.int

		Sets the font size to pixelSize pixels.
		Using this function makes the font device dependent
		Use PySide.QtGui.QFont.setPointSize() or PySide.QtGui.QFont.setPointSizeF() to set the size of the font in a device independent manner.
		"""
		res = super(QFont,self).setPixelSize(arg__1)
		return res
	#----------------------------------------------------------------------
	def setPointSize(self,arg__1):
		"""
		setPointSize(arg__1)
			arg__1=QtCore.int

		Sets the point size to pointSize
		The point size must be greater than zero.
		"""
		res = super(QFont,self).setPointSize(arg__1)
		return res
	#----------------------------------------------------------------------
	def setPointSizeF(self,arg__1):
		"""
		setPointSizeF(arg__1)
			arg__1=QtCore.qreal

		Sets the point size to pointSize
		The point size must be greater than zero
		The requested precision may not be achieved on all platforms.
		"""
		res = super(QFont,self).setPointSizeF(arg__1)
		return res
	#----------------------------------------------------------------------
	def setRawMode(self,arg__1):
		"""
		setRawMode(arg__1)
			arg__1=QtCore.bool

		If enable is true, turns raw mode on; otherwise turns raw mode off
		This function only has an effect under X11.
		If raw mode is enabled, Qt will search for an X font with a complete font name matching the family name, ignoring all other values set for the PySide.QtGui.QFont
		If the font name matches several fonts, Qt will use the first font returned by X
		PySide.QtGui.QFontInfo cannot be used to fetch information about a PySide.QtGui.QFont using raw mode (it will return the values set in the PySide.QtGui.QFont for all parameters, including the family name).
		"""
		res = super(QFont,self).setRawMode(arg__1)
		return res
	#----------------------------------------------------------------------
	def setRawName(self,arg__1):
		"""
		setRawName(arg__1)
			arg__1=unicode

		Sets a font by its system specific name
		The function is particularly useful under X, where system font settings (for example X resources) are usually available in XLFD (X Logical Font Description) form only
		You can pass an XLFD as name to this function.
		A font set with PySide.QtGui.QFont.setRawName() is still a full-featured PySide.QtGui.QFont
		It can be queried (for example with PySide.QtGui.QFont.italic() ) or modified (for example with PySide.QtGui.QFont.setItalic() ) and is therefore also suitable for rendering rich text.
		If Qts internal font database cannot resolve the raw name, the font becomes a raw font with name as its family.
		Note that the present implementation does not handle wildcards in XLFDs well, and that font aliases (file fonts.alias in the font directory on X11) are not supported.
		"""
		res = super(QFont,self).setRawName(arg__1)
		return res
	#----------------------------------------------------------------------
	def setStretch(self,arg__1):
		"""
		setStretch(arg__1)
			arg__1=QtCore.int

		Sets the stretch factor for the font.
		The stretch factor changes the width of all characters in the font by factor percent
		For example, setting factor to 150 results in all characters in the font being 1.5 times (ie
		150%) wider
		The default stretch factor is 100
		The minimum stretch factor is 1, and the maximum stretch factor is 4000.
		The stretch factor is only applied to outline fonts
		The stretch factor is ignored for bitmap fonts.
		NOTE: PySide.QtGui.QFont cannot stretch XLFD fonts
		When loading XLFD fonts on X11, the stretch factor is matched against a predefined set of values for the SETWIDTH_NAME field of the XLFD.
		"""
		res = super(QFont,self).setStretch(arg__1)
		return res
	#----------------------------------------------------------------------
	def setStrikeOut(self,arg__1):
		"""
		setStrikeOut(arg__1)
			arg__1=QtCore.bool

		If enable is true, sets strikeout on; otherwise sets strikeout off.
		"""
		res = super(QFont,self).setStrikeOut(arg__1)
		return res
	#----------------------------------------------------------------------
	def setStyle(self,style):
		"""
		setStyle(style)
			style=QtGui.QFont.Style

		Sets the style of the font to style .
		"""
		res = super(QFont,self).setStyle(style)
		return res
	#----------------------------------------------------------------------
	def setStyleHint(self,arg__1,strategy=None):
		"""
		setStyleHint(arg__1,strategy=None)
			arg__1=QtGui.QFont.StyleHint
			strategy=QtGui.QFont.StyleStrategy

		Sets the style hint and strategy to hint and strategy , respectively.
		If these arent set explicitly the style hint will default to AnyStyle and the style strategy to PreferDefault .
		Qt does not support style hints on X11 since this information is not provided by the window system.
		"""
		res = super(QFont,self).setStyleHint(arg__1,strategy)
		return res
	#----------------------------------------------------------------------
	def setStyleStrategy(self,s):
		"""
		setStyleStrategy(s)
			s=QtGui.QFont.StyleStrategy

		Sets the style strategy for the font to s .
		"""
		res = super(QFont,self).setStyleStrategy(s)
		return res
	#----------------------------------------------------------------------
	def setUnderline(self,arg__1):
		"""
		setUnderline(arg__1)
			arg__1=QtCore.bool

		If enable is true, sets underline on; otherwise sets underline off.
		"""
		res = super(QFont,self).setUnderline(arg__1)
		return res
	#----------------------------------------------------------------------
	def setWeight(self,arg__1):
		"""
		setWeight(arg__1)
			arg__1=QtCore.int

		Sets the weight the font to weight , which should be a value from the QFont.Weight enumeration.
		"""
		res = super(QFont,self).setWeight(arg__1)
		return res
	#----------------------------------------------------------------------
	def setWordSpacing(self,spacing):
		"""
		setWordSpacing(spacing)
			spacing=QtCore.qreal

		Sets the word spacing for the font to spacing .
		Word spacing changes the default spacing between individual words
		A positive value increases the word spacing by a corresponding amount of pixels, while a negative value decreases the inter-word spacing accordingly.
		Word spacing will not apply to writing systems, where indiviaul words are not separated by white space.
		"""
		res = super(QFont,self).setWordSpacing(spacing)
		return res
	#----------------------------------------------------------------------
	def x11SetScreen(self,screen=None):
		"""
		x11SetScreen(screen=None)
			screen=QtCore.int


		"""
		res = super(QFont,self).x11SetScreen(screen)
		return res

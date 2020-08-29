from PySide import QtGui, QtCore

class QFontDatabase(QtGui.QFontDatabase):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QFontDatabase,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def writingSystems(self):
		"""
		Returns a sorted list of the available writing systems
		This is list generated from information about all installed fonts on the system.
		"""
		res = super(QFontDatabase,self).writingSystems()
		return res
	#----------------------------------------------------------------------
	def bold(self,family,style):
		"""
		bold(family,style)
			family=unicode
			style=unicode

		Returns true if the font that has family family and style style is bold; otherwise returns false.
		"""
		res = super(QFontDatabase,self).bold(family,style)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def families(self,writingSystem=None):
		"""
		families(writingSystem=None)
			writingSystem=QtGui.QFontDatabase.WritingSystem

		Returns a sorted list of the available font families which support the writingSystem .
		If a family exists in several foundries, the returned name for that font is in the form family [foundry]
		Examples: Times [Adobe], Times [Cronyx], Palatino.
		"""
		res = super(QFontDatabase,self).families(writingSystem)
		return res
	#----------------------------------------------------------------------
	def font(self,family,style,pointSize):
		"""
		font(family,style,pointSize)
			family=unicode
			style=unicode
			pointSize=QtCore.int

		Returns a PySide.QtGui.QFont object that has family family , style style and point size pointSize
		If no matching font could be created, a PySide.QtGui.QFont object that uses the applications default font is returned.
		"""
		res = super(QFontDatabase,self).font(family,style,pointSize)
		isinstance(res,QtGui.QFont)
		return res
	#----------------------------------------------------------------------
	def isBitmapScalable(self,family,style=None):
		"""
		isBitmapScalable(family,style=None)
			family=unicode
			style=unicode

		Returns true if the font that has family family and style style is a scalable bitmap font; otherwise returns false
		Scaling a bitmap font usually produces an unattractive hardly readable result, because the pixels of the font are scaled
		If you need to scale a bitmap font it is better to scale it to one of the fixed sizes returned by PySide.QtGui.QFontDatabase.smoothSizes() .
		"""
		res = super(QFontDatabase,self).isBitmapScalable(family,style)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isFixedPitch(self,family,style=None):
		"""
		isFixedPitch(family,style=None)
			family=unicode
			style=unicode

		Returns true if the font that has family family and style style is fixed pitch; otherwise returns false.
		"""
		res = super(QFontDatabase,self).isFixedPitch(family,style)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isScalable(self,family,style=None):
		"""
		isScalable(family,style=None)
			family=unicode
			style=unicode

		Returns true if the font that has family family and style style is scalable; otherwise returns false.
		"""
		res = super(QFontDatabase,self).isScalable(family,style)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isSmoothlyScalable(self,family,style=None):
		"""
		isSmoothlyScalable(family,style=None)
			family=unicode
			style=unicode

		Returns true if the font that has family family and style style is smoothly scalable; otherwise returns false
		If this function returns true, its safe to scale this font to any size, and the result will always look attractive.
		"""
		res = super(QFontDatabase,self).isSmoothlyScalable(family,style)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def italic(self,family,style):
		"""
		italic(family,style)
			family=unicode
			style=unicode

		Returns true if the font that has family family and style style is italic; otherwise returns false.
		"""
		res = super(QFontDatabase,self).italic(family,style)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def pointSizes(self,family,style=None):
		"""
		pointSizes(family,style=None)
			family=unicode
			style=unicode

		Returns a list of the point sizes available for the font that has family family and style style
		The list may be empty.
		"""
		res = super(QFontDatabase,self).pointSizes(family,style)
		return res
	#----------------------------------------------------------------------
	def smoothSizes(self,family,style):
		"""
		smoothSizes(family,style)
			family=unicode
			style=unicode

		Returns the point sizes of a font that has family family and style style that will look attractive
		The list may be empty
		For non-scalable fonts and bitmap scalable fonts, this function is equivalent to PySide.QtGui.QFontDatabase.pointSizes() .
		"""
		res = super(QFontDatabase,self).smoothSizes(family,style)
		return res
	#----------------------------------------------------------------------
	def styleString(self,*args,**kwargs):
		"""
		styleString(font)
			font=QtGui.QFont

		styleString(fontInfo)
			fontInfo=QtGui.QFontInfo

		Returns a string that describes the style of the font
		For example, Bold Italic, Bold, Italic or Normal
		An empty string may be returned.
		"""
		res = super(QFontDatabase,self).styleString(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def styles(self,family):
		"""
		styles(family)
			family=unicode

		Returns a list of the styles available for the font family family
		Some example styles: Light, Light Italic, Bold, Oblique, Demi
		The list may be empty.
		"""
		res = super(QFontDatabase,self).styles(family)
		return res
	#----------------------------------------------------------------------
	def weight(self,family,style):
		"""
		weight(family,style)
			family=unicode
			style=unicode

		Returns the weight of the font that has family family and style style
		If there is no such family and style combination, returns -1.
		"""
		res = super(QFontDatabase,self).weight(family,style)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def writingSystems(self,family):
		"""
		writingSystems(family)
			family=unicode

		Returns a sorted list of the writing systems supported by a given font family .
		"""
		res = super(QFontDatabase,self).writingSystems(family)
		return res

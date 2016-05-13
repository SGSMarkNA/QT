from PySide import QtGui, QtCore

class QFontInfo(QtGui.QFontInfo):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QFontInfo,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def bold(self):
		"""
		Returns true if PySide.QtGui.QFontInfo.weight() would return a value greater than QFont.Normal ; otherwise returns false.
		"""
		res = super(QFontInfo,self).bold()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def exactMatch(self):
		"""
		Returns true if the matched window system font is exactly the same as the one specified by the font; otherwise returns false.
		"""
		res = super(QFontInfo,self).exactMatch()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def family(self):
		"""
		Returns the family name of the matched window system font.
		"""
		res = super(QFontInfo,self).family()
		return res
	#----------------------------------------------------------------------
	def fixedPitch(self):
		"""
		Returns the fixed pitch value of the matched window system font.
		"""
		res = super(QFontInfo,self).fixedPitch()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def italic(self):
		"""
		Returns the italic value of the matched window system font.
		"""
		res = super(QFontInfo,self).italic()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def overline(self):
		"""
		Returns the overline value of the matched window system font.
		Here we read the overline flag directly from the PySide.QtGui.QFont
		This is OK for X11 and for Windows because we always get what we want.
		"""
		res = super(QFontInfo,self).overline()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def pixelSize(self):
		"""
		Returns the pixel size of the matched window system font.
		"""
		res = super(QFontInfo,self).pixelSize()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def pointSize(self):
		"""
		Returns the point size of the matched window system font.
		"""
		res = super(QFontInfo,self).pointSize()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def pointSizeF(self):
		"""
		Returns the point size of the matched window system font.
		"""
		res = super(QFontInfo,self).pointSizeF()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def rawMode(self):
		"""
		Returns true if the font is a raw mode font; otherwise returns false.
		If it is a raw mode font, all other functions in PySide.QtGui.QFontInfo will return the same values set in the PySide.QtGui.QFont , regardless of the font actually used.
		"""
		res = super(QFontInfo,self).rawMode()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def strikeOut(self):
		"""
		Returns the strikeout value of the matched window system font.
		This is OK for X11 and for Windows because we always get what we want.
		"""
		res = super(QFontInfo,self).strikeOut()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def style(self):
		"""
		Returns the style value of the matched window system font.
		"""
		res = super(QFontInfo,self).style()
		isinstance(res,QtGui.QFont.Style)
		return res
	#----------------------------------------------------------------------
	def styleHint(self):
		"""
		Returns the style of the matched window system font.
		Currently only returns the style hint set in PySide.QtGui.QFont .
		"""
		res = super(QFontInfo,self).styleHint()
		isinstance(res,QtGui.QFont.StyleHint)
		return res
	#----------------------------------------------------------------------
	def underline(self):
		"""
		Returns the underline value of the matched window system font.
		Here we read the underline flag directly from the PySide.QtGui.QFont
		This is OK for X11 and for Windows because we always get what we want.
		"""
		res = super(QFontInfo,self).underline()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def weight(self):
		"""
		Returns the weight of the matched window system font.
		"""
		res = super(QFontInfo,self).weight()
		isinstance(res,QtCore.int)
		return res

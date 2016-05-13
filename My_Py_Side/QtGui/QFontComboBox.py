from PySide import QtGui, QtCore

class QFontComboBox(QtGui.QFontComboBox):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QFontComboBox,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def currentFont(self):
		"""
		This property holds the currently selected font.
		"""
		res = super(QFontComboBox,self).currentFont()
		isinstance(res,QtGui.QFont)
		return res
	#----------------------------------------------------------------------
	def fontFilters(self):
		"""
		This property holds the filter for the combobox.
		By default, all fonts are listed.
		"""
		res = super(QFontComboBox,self).fontFilters()
		isinstance(res,QtGui.QFontComboBox.FontFilters)
		return res
	#----------------------------------------------------------------------
	def writingSystem(self):
		"""
		This property holds the writing system that serves as a filter for the combobox.
		If script is QFontDatabase.Any (the default), all fonts are listed.
		"""
		res = super(QFontComboBox,self).writingSystem()
		isinstance(res,QtGui.QFontDatabase.WritingSystem)
		return res
	#----------------------------------------------------------------------
	def setFontFilters(self,filters):
		"""
		setFontFilters(filters)
			filters=QtGui.QFontComboBox.FontFilters

		This property holds the filter for the combobox.
		By default, all fonts are listed.
		"""
		res = super(QFontComboBox,self).setFontFilters(filters)
		return res
	#----------------------------------------------------------------------
	def setWritingSystem(self,arg__1):
		"""
		setWritingSystem(arg__1)
			arg__1=QtGui.QFontDatabase.WritingSystem

		This property holds the writing system that serves as a filter for the combobox.
		If script is QFontDatabase.Any (the default), all fonts are listed.
		"""
		res = super(QFontComboBox,self).setWritingSystem(arg__1)
		return res

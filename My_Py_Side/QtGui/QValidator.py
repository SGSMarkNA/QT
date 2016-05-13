from PySide import QtGui, QtCore

class QValidator(QtGui.QValidator):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QValidator,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def locale(self):
		"""
		Returns the locale for the validator
		The locale is by default initialized to the same as QLocale().
		"""
		res = super(QValidator,self).locale()
		isinstance(res,QtCore.QLocale)
		return res
	#----------------------------------------------------------------------
	def fixup(self,arg__1):
		"""
		fixup(arg__1)
			arg__1=unicode

		This function attempts to change input to be valid according to this validators rules
		It need not result in a valid string: callers of this function must re-test afterwards; the default does nothing.
		Reimplementations of this function can change input even if they do not produce a valid string
		For example, an ISBN validator might want to delete every character except digits and -, even if the result is still not a valid ISBN; a surname validator might want to remove whitespace from the start and end of the string, even if the resulting string is not in the list of accepted surnames.
		"""
		res = super(QValidator,self).fixup(arg__1)
		return res
	#----------------------------------------------------------------------
	def setLocale(self,locale):
		"""
		setLocale(locale)
			locale=QtCore.QLocale

		Sets the locale that will be used for the validator
		Unless setLocale has been called, the validator will use the default locale set with QLocale.setDefault()
		If a default locale has not been set, it is the operating systems locale.
		"""
		res = super(QValidator,self).setLocale(locale)
		return res
	#----------------------------------------------------------------------
	def validate(self,arg__1,arg__2):
		"""
		validate(arg__1,arg__2)
			arg__1=unicode
			arg__2=QtCore.int

		This virtual function returns Invalid if input is invalid according to this validators rules, Intermediate if it is likely that a little more editing will make the input acceptable (e.g
		the user types 4 into a widget which accepts integers between 10 and 99), and Acceptable if the input is valid.
		The function can change both input and pos (the cursor position) if required.
		"""
		res = super(QValidator,self).validate(arg__1,arg__2)
		return res

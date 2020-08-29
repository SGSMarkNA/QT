from PySide import QtGui, QtCore

class QTranslator(QtCore.QTranslator):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTranslator,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def isEmpty(self):
		"""
		Returns true if this translator is empty, otherwise returns false
		This function works with stripped and unstripped translation files.
		"""
		res = super(QTranslator,self).isEmpty()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def load(self,*args,**kwargs):
		"""
		load(data)
			data=QtCore.uchar

		load(filename,directory=None,search_delimiters=None,suffix=None)
			filename=unicode
			directory=unicode
			search_delimiters=unicode
			suffix=unicode

		This function overloads PySide.QtCore.QTranslator.load() .
		Loads the QM file data data of length len into the translator.
		The data is not copied
		The caller must be able to guarantee that data will not be deleted or modified.
		"""
		res = super(QTranslator,self).load(*args,**kwargs)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def translate(self,*args,**kwargs):
		"""
		translate(context,sourceText,disambiguation=None)
			context=str
			sourceText=str
			disambiguation=str

		translate(context,sourceText,disambiguation,n)
			context=str
			sourceText=str
			disambiguation=str
			n=QtCore.int

		Returns the translation for the key (context , sourceText , disambiguation )
		If none is found, also tries (context , sourceText , )
		If that still fails, returns an empty string.
		If you need to programatically insert translations in to a PySide.QtCore.QTranslator , this function can be reimplemented.
		"""
		res = super(QTranslator,self).translate(*args,**kwargs)
		return res

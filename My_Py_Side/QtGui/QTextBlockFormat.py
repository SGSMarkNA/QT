from PySide import QtGui, QtCore

class QTextBlockFormat(QtGui.QTextBlockFormat):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextBlockFormat,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def alignment(self):
		"""
		Returns the paragraphs alignment.
		"""
		res = super(QTextBlockFormat,self).alignment()
		isinstance(res,QtCore.Qt.Alignment)
		return res
	#----------------------------------------------------------------------
	def bottomMargin(self):
		"""
		Returns the paragraphs bottom margin.
		"""
		res = super(QTextBlockFormat,self).bottomMargin()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def indent(self):
		"""
		Returns the paragraphs indent.
		"""
		res = super(QTextBlockFormat,self).indent()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def leftMargin(self):
		"""
		Returns the paragraphs left margin.
		"""
		res = super(QTextBlockFormat,self).leftMargin()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def nonBreakableLines(self):
		"""
		Returns true if the lines in the paragraph are non-breakable; otherwise returns false.
		"""
		res = super(QTextBlockFormat,self).nonBreakableLines()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def pageBreakPolicy(self):
		"""
		Returns the currently set page break policy for the paragraph
		The default is QTextFormat.PageBreak_Auto .
		"""
		res = super(QTextBlockFormat,self).pageBreakPolicy()
		isinstance(res,QtGui.QTextFormat.PageBreakFlags)
		return res
	#----------------------------------------------------------------------
	def rightMargin(self):
		"""
		Returns the paragraphs right margin.
		"""
		res = super(QTextBlockFormat,self).rightMargin()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def tabPositions(self):
		"""
		Returns a list of tab positions defined for the text block.
		"""
		res = super(QTextBlockFormat,self).tabPositions()
		return res
	#----------------------------------------------------------------------
	def textIndent(self):
		"""
		Returns the paragraphs text indent.
		"""
		res = super(QTextBlockFormat,self).textIndent()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def topMargin(self):
		"""
		Returns the paragraphs top margin.
		"""
		res = super(QTextBlockFormat,self).topMargin()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def setAlignment(self,alignment):
		"""
		setAlignment(alignment)
			alignment=QtCore.Qt.Alignment


		"""
		res = super(QTextBlockFormat,self).setAlignment(alignment)
		return res
	#----------------------------------------------------------------------
	def setBottomMargin(self,margin):
		"""
		setBottomMargin(margin)
			margin=QtCore.qreal

		Sets the paragraphs bottom margin .
		"""
		res = super(QTextBlockFormat,self).setBottomMargin(margin)
		return res
	#----------------------------------------------------------------------
	def setIndent(self,indent):
		"""
		setIndent(indent)
			indent=QtCore.int

		Sets the paragraphs indentation
		Margins are set independently of indentation with PySide.QtGui.QTextBlockFormat.setLeftMargin() and PySide.QtGui.QTextBlockFormat.setTextIndent()
		The indentation is an integer that is multiplied with the document-wide standard indent, resulting in the actual indent of the paragraph.
		"""
		res = super(QTextBlockFormat,self).setIndent(indent)
		return res
	#----------------------------------------------------------------------
	def setLeftMargin(self,margin):
		"""
		setLeftMargin(margin)
			margin=QtCore.qreal

		Sets the paragraphs left margin
		Indentation can be applied separately with PySide.QtGui.QTextBlockFormat.setIndent() .
		"""
		res = super(QTextBlockFormat,self).setLeftMargin(margin)
		return res
	#----------------------------------------------------------------------
	def setNonBreakableLines(self,b):
		"""
		setNonBreakableLines(b)
			b=QtCore.bool

		If b is true, the lines in the paragraph are treated as non-breakable; otherwise they are breakable.
		"""
		res = super(QTextBlockFormat,self).setNonBreakableLines(b)
		return res
	#----------------------------------------------------------------------
	def setPageBreakPolicy(self,flags):
		"""
		setPageBreakPolicy(flags)
			flags=QtGui.QTextFormat.PageBreakFlags


		"""
		res = super(QTextBlockFormat,self).setPageBreakPolicy(flags)
		return res
	#----------------------------------------------------------------------
	def setRightMargin(self,margin):
		"""
		setRightMargin(margin)
			margin=QtCore.qreal

		Sets the paragraphs right margin .
		"""
		res = super(QTextBlockFormat,self).setRightMargin(margin)
		return res
	#----------------------------------------------------------------------
	def setTabPositions(self,tabs):
		"""
		setTabPositions(tabs)
			tabs=unKnown


		"""
		res = super(QTextBlockFormat,self).setTabPositions(tabs)
		return res
	#----------------------------------------------------------------------
	def setTextIndent(self,aindent):
		"""
		setTextIndent(aindent)
			aindent=QtCore.qreal

		Sets the indent for the first line in the block
		This allows the first line of a paragraph to be indented differently to the other lines, enhancing the readability of the text.
		"""
		res = super(QTextBlockFormat,self).setTextIndent(aindent)
		return res
	#----------------------------------------------------------------------
	def setTopMargin(self,margin):
		"""
		setTopMargin(margin)
			margin=QtCore.qreal

		Sets the paragraphs top margin .
		"""
		res = super(QTextBlockFormat,self).setTopMargin(margin)
		return res

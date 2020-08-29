from PySide import QtGui, QtCore

class QStylePainter(QtGui.QStylePainter):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QStylePainter,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def style(self):
		"""
		Return the current style used by the PySide.QtGui.QStylePainter .
		"""
		res = super(QStylePainter,self).style()
		isinstance(res,QtGui.QStyle)
		return res
	#----------------------------------------------------------------------
	def begin(self,*args,**kwargs):
		"""
		begin(pd,w)
			pd=QtGui.QPaintDevice
			w=QtGui.QWidget

		begin(w)
			w=QtGui.QWidget

		This is an overloaded function.
		Begin painting operations on paint device pd as if it was widget .
		This is automatically called by the constructor that takes a PySide.QtGui.QPaintDevice and a PySide.QtGui.QWidget .
		"""
		res = super(QStylePainter,self).begin(*args,**kwargs)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def drawComplexControl(self,cc,opt):
		"""
		drawComplexControl(cc,opt)
			cc=QtGui.QStyle.ComplexControl
			opt=QtGui.QStyleOptionComplex


		"""
		res = super(QStylePainter,self).drawComplexControl(cc,opt)
		return res
	#----------------------------------------------------------------------
	def drawControl(self,ce,opt):
		"""
		drawControl(ce,opt)
			ce=QtGui.QStyle.ControlElement
			opt=QtGui.QStyleOption


		"""
		res = super(QStylePainter,self).drawControl(ce,opt)
		return res
	#----------------------------------------------------------------------
	def drawItemPixmap(self,r,flags,pixmap):
		"""
		drawItemPixmap(r,flags,pixmap)
			r=QtCore.QRect
			flags=QtCore.int
			pixmap=QtGui.QPixmap

		Draws the pixmap in rectangle rect
		The pixmap is aligned according to flags .
		"""
		res = super(QStylePainter,self).drawItemPixmap(r,flags,pixmap)
		return res
	#----------------------------------------------------------------------
	def drawItemText(self,r,flags,pal,enabled,text,textRole=None):
		"""
		drawItemText(r,flags,pal,enabled,text,textRole=None)
			r=QtCore.QRect
			flags=QtCore.int
			pal=QtGui.QPalette
			enabled=QtCore.bool
			text=unicode
			textRole=QtGui.QPalette.ColorRole


		"""
		res = super(QStylePainter,self).drawItemText(r,flags,pal,enabled,text,textRole)
		return res
	#----------------------------------------------------------------------
	def drawPrimitive(self,pe,opt):
		"""
		drawPrimitive(pe,opt)
			pe=QtGui.QStyle.PrimitiveElement
			opt=QtGui.QStyleOption


		"""
		res = super(QStylePainter,self).drawPrimitive(pe,opt)
		return res

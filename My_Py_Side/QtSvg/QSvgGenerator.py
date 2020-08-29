from PySide import QtGui, QtCore

class QSvgGenerator(QtSvg.QSvgGenerator):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSvgGenerator,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def description(self):
		"""
		This property holds the description of the generated SVG drawing.
		"""
		res = super(QSvgGenerator,self).description()
		return res
	#----------------------------------------------------------------------
	def fileName(self):
		"""
		This property holds the target filename for the generated SVG drawing.
		"""
		res = super(QSvgGenerator,self).fileName()
		return res
	#----------------------------------------------------------------------
	def outputDevice(self):
		"""
		This property holds the output device for the generated SVG drawing.
		If both output device and file name are specified, the output device will have precedence.
		"""
		res = super(QSvgGenerator,self).outputDevice()
		isinstance(res,QtCore.QIODevice)
		return res
	#----------------------------------------------------------------------
	def resolution(self):
		"""
		This property holds the resolution of the generated output.
		The resolution is specified in dots per inch, and is used to calculate the physical size of an SVG drawing.
		"""
		res = super(QSvgGenerator,self).resolution()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""
		This property holds the size of the generated SVG drawing.
		By default this property is set to QSize(-1, -1) , which indicates that the generator should not output the width and height attributes of the <svg> element.
		"""
		res = super(QSvgGenerator,self).size()
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def title(self):
		"""
		This property holds the title of the generated SVG drawing.
		"""
		res = super(QSvgGenerator,self).title()
		return res
	#----------------------------------------------------------------------
	def viewBox(self):
		"""
		Returns PySide.QtSvg.QSvgGenerator.viewBoxF()
		toRect() .
		"""
		res = super(QSvgGenerator,self).viewBox()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def viewBoxF(self):
		"""
		This property holds the PySide.QtSvg.QSvgGenerator.viewBox() of the generated SVG drawing.
		By default this property is set to QRect(0, 0, -1, -1) , which indicates that the generator should not output the PySide.QtSvg.QSvgGenerator.viewBox() attribute of the <svg> element.
		"""
		res = super(QSvgGenerator,self).viewBoxF()
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def setDescription(self,description):
		"""
		setDescription(description)
			description=unicode

		This property holds the description of the generated SVG drawing.
		"""
		res = super(QSvgGenerator,self).setDescription(description)
		return res
	#----------------------------------------------------------------------
	def setFileName(self,fileName):
		"""
		setFileName(fileName)
			fileName=unicode

		This property holds the target filename for the generated SVG drawing.
		"""
		res = super(QSvgGenerator,self).setFileName(fileName)
		return res
	#----------------------------------------------------------------------
	def setOutputDevice(self,outputDevice):
		"""
		setOutputDevice(outputDevice)
			outputDevice=QtCore.QIODevice

		This property holds the output device for the generated SVG drawing.
		If both output device and file name are specified, the output device will have precedence.
		"""
		res = super(QSvgGenerator,self).setOutputDevice(outputDevice)
		return res
	#----------------------------------------------------------------------
	def setResolution(self,dpi):
		"""
		setResolution(dpi)
			dpi=QtCore.int

		This property holds the resolution of the generated output.
		The resolution is specified in dots per inch, and is used to calculate the physical size of an SVG drawing.
		"""
		res = super(QSvgGenerator,self).setResolution(dpi)
		return res
	#----------------------------------------------------------------------
	def setSize(self,size):
		"""
		setSize(size)
			size=QtCore.QSize

		This property holds the size of the generated SVG drawing.
		By default this property is set to QSize(-1, -1) , which indicates that the generator should not output the width and height attributes of the <svg> element.
		"""
		res = super(QSvgGenerator,self).setSize(size)
		return res
	#----------------------------------------------------------------------
	def setTitle(self,title):
		"""
		setTitle(title)
			title=unicode

		This property holds the title of the generated SVG drawing.
		"""
		res = super(QSvgGenerator,self).setTitle(title)
		return res
	#----------------------------------------------------------------------
	def setViewBox(self,*args,**kwargs):
		"""
		setViewBox(viewBox)
			viewBox=QtCore.QRectF

		setViewBox(viewBox)
			viewBox=QtCore.QRect

		This property holds the PySide.QtSvg.QSvgGenerator.viewBox() of the generated SVG drawing.
		By default this property is set to QRect(0, 0, -1, -1) , which indicates that the generator should not output the PySide.QtSvg.QSvgGenerator.viewBox() attribute of the <svg> element.
		"""
		res = super(QSvgGenerator,self).setViewBox(*args,**kwargs)
		return res

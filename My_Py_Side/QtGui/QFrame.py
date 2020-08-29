from PySide import QtGui, QtCore
from QWidget import QWidget
class QFrame(QtGui.QFrame, QWidget):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QFrame,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def frameRect(self):
		"""
		This property holds the frames rectangle.
		The frames rectangle is the rectangle the frame is drawn in
		By default, this is the entire widget
		Setting the rectangle does does not cause a widget update
		The frame rectangle is automatically adjusted when the widget changes size.
		If you set the rectangle to a null rectangle (for example, PySide.QtCore.QRect (0, 0, 0, 0)), then the resulting frame rectangle is equivalent to the widget rectangle .
		"""
		res = super(QFrame,self).frameRect()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def frameShadow(self):
		"""
		This property holds the frame shadow value from the frame style.
		"""
		res = super(QFrame,self).frameShadow()
		isinstance(res,QtGui.QFrame.Shadow)
		return res
	#----------------------------------------------------------------------
	def frameShape(self):
		"""
		This property holds the frame shape value from the frame style.
		"""
		res = super(QFrame,self).frameShape()
		isinstance(res,QtGui.QFrame.Shape)
		return res
	#----------------------------------------------------------------------
	def frameStyle(self):
		"""
		Returns the frame style.
		The default value is QFrame.Plain .
		"""
		res = super(QFrame,self).frameStyle()

		return res
	#----------------------------------------------------------------------
	def frameWidth(self):
		"""
		This property holds the width of the frame that is drawn..
		Note that the frame width depends on the frame style , not only the line width and the mid-line width
		For example, the style specified by NoFrame always has a frame width of 0, whereas the style Panel has a frame width equivalent to the line width.
		"""
		res = super(QFrame,self).frameWidth()

		return res
	#----------------------------------------------------------------------
	def lineWidth(self):
		"""
		This property holds the line width.
		Note that the total line width for frames used as separators ( HLine and VLine ) is specified by PySide.QtGui.QFrame.frameWidth() .
		The default value is 1.
		"""
		res = super(QFrame,self).lineWidth()

		return res
	#----------------------------------------------------------------------
	def midLineWidth(self):
		"""
		This property holds the width of the mid-line.
		The default value is 0.
		"""
		res = super(QFrame,self).midLineWidth()

		return res
	#----------------------------------------------------------------------
	def drawFrame(self,arg__1):
		"""
		drawFrame(arg__1)
			arg__1=QtGui.QPainter

		Mostly for the sake of Q3Frame
		"""
		res = super(QFrame,self).drawFrame(arg__1)
		return res
	#----------------------------------------------------------------------
	def setFrameRect(self,arg__1):
		"""
		setFrameRect(arg__1)
			arg__1=QtCore.QRect

		This property holds the frames rectangle.
		The frames rectangle is the rectangle the frame is drawn in
		By default, this is the entire widget
		Setting the rectangle does does not cause a widget update
		The frame rectangle is automatically adjusted when the widget changes size.
		If you set the rectangle to a null rectangle (for example, PySide.QtCore.QRect (0, 0, 0, 0)), then the resulting frame rectangle is equivalent to the widget rectangle .
		"""
		res = super(QFrame,self).setFrameRect(arg__1)
		return res
	#----------------------------------------------------------------------
	def setFrameShadow(self,arg__1):
		"""
		setFrameShadow(arg__1)
			arg__1=QtGui.QFrame.Shadow

		This property holds the frame shadow value from the frame style.
		"""
		res = super(QFrame,self).setFrameShadow(arg__1)
		return res
	#----------------------------------------------------------------------
	def setFrameShape(self,arg__1):
		"""
		setFrameShape(arg__1)
			arg__1=QtGui.QFrame.Shape

		This property holds the frame shape value from the frame style.
		"""
		res = super(QFrame,self).setFrameShape(arg__1)
		return res
	#----------------------------------------------------------------------
	def setFrameStyle(self,arg__1):
		"""
		setFrameStyle(arg__1)
			arg__1=QtCore.int

		Sets the frame style to style .
		The style is the bitwise OR between a frame shape and a frame shadow style
		See the picture of the frames in the main class documentation.
		The frame shapes are given in QFrame.Shape and the shadow styles in QFrame.Shadow .
		If a mid-line width greater than 0 is specified, an additional line is drawn for Raised or Sunken Box , HLine , and VLine frames
		The mid-color of the current color group is used for drawing middle lines.
		"""
		res = super(QFrame,self).setFrameStyle(arg__1)
		return res
	#----------------------------------------------------------------------
	def setLineWidth(self,arg__1):
		"""
		setLineWidth(arg__1)
			arg__1=QtCore.int

		This property holds the line width.
		Note that the total line width for frames used as separators ( HLine and VLine ) is specified by PySide.QtGui.QFrame.frameWidth() .
		The default value is 1.
		"""
		res = super(QFrame,self).setLineWidth(arg__1)
		return res
	#----------------------------------------------------------------------
	def setMidLineWidth(self,arg__1):
		"""
		setMidLineWidth(arg__1)
			arg__1=QtCore.int

		This property holds the width of the mid-line.
		The default value is 0.
		"""
		res = super(QFrame,self).setMidLineWidth(arg__1)
		return res

	FrameRect   = property(frameRect, setFrameRect)
	FrameShadow = property(frameShadow, setFrameShadow)
	FrameShape  = property(frameShape, setFrameShape)
	FrameStyle  = property(frameStyle, setFrameStyle)
	FrameWidth  = property(frameWidth)
	LineWidth   = property(lineWidth, setLineWidth)


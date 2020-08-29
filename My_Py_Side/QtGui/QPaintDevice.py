from PySide import QtGui, QtCore

class QPaintDevice(QtGui.QPaintDevice):
	''''''
	#def __init__(self,*args,**kwargs):
		#''''''
		#super(QPaintDevice,self).__init__(*args,**kwargs)
	##----------------------------------------------------------------------
	#def colorCount(self):
		#"""
		#Returns the number of different colors available for the paint device
		#Since this value is an int, it will not be sufficient to represent the number of colors on 32 bit displays, in this case INT_MAX is returned instead.
		#"""
		#res = super(QPaintDevice,self).colorCount()

		#return res
	##----------------------------------------------------------------------
	#def depth(self):
		#"""
		#Returns the bit depth (number of bit planes) of the paint device.
		#"""
		#res = super(QPaintDevice,self).depth()

		#return res
	##----------------------------------------------------------------------
	#def height(self):
		#"""
		#Returns the height of the paint device in default coordinate system units (e.g
		#pixels for PySide.QtGui.QPixmap and PySide.QtGui.QWidget ).
		#"""
		#res = super(QPaintDevice,self).height()

		#return res
	##----------------------------------------------------------------------
	#def heightMM(self):
		#"""
		#Returns the height of the paint device in millimeters
		#Due to platform limitations it may not be possible to use this function to determine the actual physical size of a widget on the screen.
		#"""
		#res = super(QPaintDevice,self).heightMM()

		#return res
	##----------------------------------------------------------------------
	#def logicalDpiX(self):
		#"""
		#Returns the horizontal resolution of the device in dots per inch, which is used when computing font sizes
		#For X11, this is usually the same as could be computed from PySide.QtGui.QPaintDevice.widthMM() .
		#Note that if the PySide.QtGui.QPaintDevice.logicalDpiX() doesnt equal the PySide.QtGui.QPaintDevice.physicalDpiX() , the corresponding PySide.QtGui.QPaintEngine must handle the resolution mapping.
		#"""
		#res = super(QPaintDevice,self).logicalDpiX()

		#return res
	##----------------------------------------------------------------------
	#def logicalDpiY(self):
		#"""
		#Returns the vertical resolution of the device in dots per inch, which is used when computing font sizes
		#For X11, this is usually the same as could be computed from PySide.QtGui.QPaintDevice.heightMM() .
		#Note that if the PySide.QtGui.QPaintDevice.logicalDpiY() doesnt equal the PySide.QtGui.QPaintDevice.physicalDpiY() , the corresponding PySide.QtGui.QPaintEngine must handle the resolution mapping.
		#"""
		#res = super(QPaintDevice,self).logicalDpiY()

		#return res
	##----------------------------------------------------------------------
	#def numColors(self):
		#"""
		#Use PySide.QtGui.QPaintDevice.colorCount() instead.
		#Returns the number of different colors available for the paint device
		#Since this value is an int, it will not be sufficient to represent the number of colors on 32 bit displays, in this case INT_MAX is returned instead.
		#"""
		#res = super(QPaintDevice,self).numColors()

		#return res
	##----------------------------------------------------------------------
	#def paintEngine(self):
		#"""
		#Returns a pointer to the paint engine used for drawing on the device.
		#"""
		#res = super(QPaintDevice,self).paintEngine()
		#isinstance(res,QtGui.QPaintEngine)
		#return res
	##----------------------------------------------------------------------
	#def paintingActive(self):
		#"""
		#Returns true if the device is currently being painted on, i.e
		#someone has called QPainter.begin() but not yet called QPainter.end() for this device; otherwise returns false.
		#"""
		#res = super(QPaintDevice,self).paintingActive()
		#isinstance(res,bool)
		#return res
	##----------------------------------------------------------------------
	#def physicalDpiX(self):
		#"""
		#Returns the horizontal resolution of the device in dots per inch
		#For example, when printing, this resolution refers to the physical printers resolution
		#The logical DPI on the other hand, refers to the resolution used by the actual paint engine.
		#Note that if the PySide.QtGui.QPaintDevice.physicalDpiX() doesnt equal the PySide.QtGui.QPaintDevice.logicalDpiX() , the corresponding PySide.QtGui.QPaintEngine must handle the resolution mapping.
		#"""
		#res = super(QPaintDevice,self).physicalDpiX()

		#return res
	##----------------------------------------------------------------------
	#def physicalDpiY(self):
		#"""
		#Returns the horizontal resolution of the device in dots per inch
		#For example, when printing, this resolution refers to the physical printers resolution
		#The logical DPI on the other hand, refers to the resolution used by the actual paint engine.
		#Note that if the PySide.QtGui.QPaintDevice.physicalDpiY() doesnt equal the PySide.QtGui.QPaintDevice.logicalDpiY() , the corresponding PySide.QtGui.QPaintEngine must handle the resolution mapping.
		#"""
		#res = super(QPaintDevice,self).physicalDpiY()

		#return res
	##----------------------------------------------------------------------
	#def width(self):
		#"""
		#Returns the width of the paint device in default coordinate system units (e.g
		#pixels for PySide.QtGui.QPixmap and PySide.QtGui.QWidget ).
		#"""
		#res = super(QPaintDevice,self).width()

		#return res
	##----------------------------------------------------------------------
	#def widthMM(self):
		#"""
		#Returns the width of the paint device in millimeters
		#Due to platform limitations it may not be possible to use this function to determine the actual physical size of a widget on the screen.
		#"""
		#res = super(QPaintDevice,self).widthMM()

		#return res
	##----------------------------------------------------------------------
	#def metric(self,metric):
		#"""
		#metric(metric)
			#metric=QtGui.QPaintDevice.PaintDeviceMetric

		#Returns the metric information for the given paint device metric .
		#"""
		#res = super(QPaintDevice,self).metric(metric)

		#return res

	#ColorCount     = property(colorCount)
	#Depth          = property(depth)
	#DevType        = property(devType)
	#Height         = property(height)
	#HeightMM       = property(heightMM)
	#LogicalDpiX    = property(logicalDpiX)
	#LogicalDpiY    = property(logicalDpiY)
	#NumColors      = property(numColors)
	#PaintEngine    = property(paintEngine)
	#PaintingActive = property(paintingActive)
	#PhysicalDpiX   = property(physicalDpiX)
	#PhysicalDpiY   = property(physicalDpiY)
	#Width          = property(width)
	#WidthMM        = property(widthMM)
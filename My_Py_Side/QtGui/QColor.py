from PySide import QtGui, QtCore

class QColor(QtGui.QColor):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QColor,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __reduce__(self):
		"""

		"""
		res = super(QColor,self).__reduce__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __repr__(self):
		"""

		"""
		res = super(QColor,self).__repr__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __str__(self):
		"""

		"""
		res = super(QColor,self).__str__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def alpha(self):
		"""
		Returns the alpha color component of this color.
		"""
		res = super(QColor,self).alpha()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def alphaF(self):
		"""
		Returns the alpha color component of this color.
		"""
		res = super(QColor,self).alphaF()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def black(self):
		"""
		Returns the black color component of this color.
		"""
		res = super(QColor,self).black()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def blackF(self):
		"""
		Returns the black color component of this color.
		"""
		res = super(QColor,self).blackF()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def blue(self):
		"""
		Returns the blue color component of this color.
		"""
		res = super(QColor,self).blue()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def blueF(self):
		"""
		Returns the blue color component of this color.
		"""
		res = super(QColor,self).blueF()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def cyan(self):
		"""
		Returns the cyan color component of this color.
		"""
		res = super(QColor,self).cyan()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def cyanF(self):
		"""
		Returns the cyan color component of this color.
		"""
		res = super(QColor,self).cyanF()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def getCmyk(self):
		"""
		Sets the contents pointed to by c , m , y , k , and a , to the cyan, magenta, yellow, black, and alpha-channel (transparency) components of the colors CMYK value.
		These components can be retrieved individually using the PySide.QtGui.QColor.cyan() , PySide.QtGui.QColor.magenta() , PySide.QtGui.QColor.yellow() , PySide.QtGui.QColor.black() and PySide.QtGui.QColor.alpha() functions.
		"""
		res = super(QColor,self).getCmyk()
		return res
	#----------------------------------------------------------------------
	def getCmykF(self):
		"""
		Sets the contents pointed to by c , m , y , k , and a , to the cyan, magenta, yellow, black, and alpha-channel (transparency) components of the colors CMYK value.
		These components can be retrieved individually using the PySide.QtGui.QColor.cyanF() , PySide.QtGui.QColor.magentaF() , PySide.QtGui.QColor.yellowF() , PySide.QtGui.QColor.blackF() and PySide.QtGui.QColor.alphaF() functions.
		"""
		res = super(QColor,self).getCmykF()
		return res
	#----------------------------------------------------------------------
	def getHsl(self):
		"""
		Sets the contents pointed to by h , s , l , and a , to the hue, saturation, lightness, and alpha-channel (transparency) components of the colors HSL value.
		These components can be retrieved individually using the hueHsl(), saturationHsl(), PySide.QtGui.QColor.lightness() and PySide.QtGui.QColor.alpha() functions.
		"""
		res = super(QColor,self).getHsl()
		return res
	#----------------------------------------------------------------------
	def getHslF(self):
		"""
		Sets the contents pointed to by h , s , l , and a , to the hue, saturation, lightness, and alpha-channel (transparency) components of the colors HSL value.
		These components can be retrieved individually using the hueHslF(), saturationHslF(), PySide.QtGui.QColor.lightnessF() and PySide.QtGui.QColor.alphaF() functions.
		"""
		res = super(QColor,self).getHslF()
		return res
	#----------------------------------------------------------------------
	def getHsv(self):
		"""
		Sets the contents pointed to by h , s , v , and a , to the hue, saturation, value, and alpha-channel (transparency) components of the colors HSV value.
		These components can be retrieved individually using the PySide.QtGui.QColor.hue() , PySide.QtGui.QColor.saturation() , PySide.QtGui.QColor.value() and PySide.QtGui.QColor.alpha() functions.
		"""
		res = super(QColor,self).getHsv()
		return res
	#----------------------------------------------------------------------
	def getHsvF(self):
		"""
		Sets the contents pointed to by h , s , v , and a , to the hue, saturation, value, and alpha-channel (transparency) components of the colors HSV value.
		These components can be retrieved individually using the PySide.QtGui.QColor.hueF() , PySide.QtGui.QColor.saturationF() , PySide.QtGui.QColor.valueF() and PySide.QtGui.QColor.alphaF() functions.
		"""
		res = super(QColor,self).getHsvF()
		return res
	#----------------------------------------------------------------------
	def getRgb(self):
		"""
		Sets the contents pointed to by r , g , b , and a , to the red, green, blue, and alpha-channel (transparency) components of the colors RGB value.
		These components can be retrieved individually using the PySide.QtGui.QColor.red() , PySide.QtGui.QColor.green() , PySide.QtGui.QColor.blue() and PySide.QtGui.QColor.alpha() functions.
		"""
		res = super(QColor,self).getRgb()
		return res
	#----------------------------------------------------------------------
	def getRgbF(self):
		"""
		Sets the contents pointed to by r , g , b , and a , to the red, green, blue, and alpha-channel (transparency) components of the colors RGB value.
		These components can be retrieved individually using the PySide.QtGui.QColor.redF() , PySide.QtGui.QColor.greenF() , PySide.QtGui.QColor.blueF() and PySide.QtGui.QColor.alphaF() functions.
		"""
		res = super(QColor,self).getRgbF()
		return res
	#----------------------------------------------------------------------
	def green(self):
		"""
		Returns the green color component of this color.
		"""
		res = super(QColor,self).green()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def greenF(self):
		"""
		Returns the green color component of this color.
		"""
		res = super(QColor,self).greenF()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def hslHue(self):
		"""
		Returns the hue color component of this color.
		"""
		res = super(QColor,self).hslHue()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def hslHueF(self):
		"""
		Returns the hue color component of this color.
		"""
		res = super(QColor,self).hslHueF()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def hslSaturation(self):
		"""
		Returns the saturation color component of this color.
		"""
		res = super(QColor,self).hslSaturation()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def hslSaturationF(self):
		"""
		Returns the saturation color component of this color.
		"""
		res = super(QColor,self).hslSaturationF()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def hsvHue(self):
		"""
		Returns the hue color component of this color.
		"""
		res = super(QColor,self).hsvHue()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def hsvHueF(self):
		"""
		Returns the hue color component of this color.
		"""
		res = super(QColor,self).hsvHueF()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def hsvSaturation(self):
		"""
		Returns the saturation color component of this color.
		"""
		res = super(QColor,self).hsvSaturation()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def hsvSaturationF(self):
		"""
		Returns the saturation color component of this color.
		"""
		res = super(QColor,self).hsvSaturationF()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def hue(self):
		"""
		Returns the hue color component of this color.
		The color is implicitly converted to HSV.
		"""
		res = super(QColor,self).hue()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def hueF(self):
		"""
		Returns the hue color component of this color.
		The color is implicitly converted to HSV.
		"""
		res = super(QColor,self).hueF()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def invalidate(self):
		"""

		"""
		res = super(QColor,self).invalidate()
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if the color is valid; otherwise returns false.
		"""
		res = super(QColor,self).isValid()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def lightness(self):
		"""
		Returns the lightness color component of this color.
		"""
		res = super(QColor,self).lightness()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def lightnessF(self):
		"""
		Returns the lightness color component of this color.
		"""
		res = super(QColor,self).lightnessF()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def magenta(self):
		"""
		Returns the magenta color component of this color.
		"""
		res = super(QColor,self).magenta()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def magentaF(self):
		"""
		Returns the magenta color component of this color.
		"""
		res = super(QColor,self).magentaF()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def name(self):
		"""
		Returns the name of the color in the format #RRGGBB; i.e
		a # character followed by three two-digit hexadecimal numbers.
		"""
		res = super(QColor,self).name()
		return res
	#----------------------------------------------------------------------
	def red(self):
		"""
		Returns the red color component of this color.
		"""
		res = super(QColor,self).red()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def redF(self):
		"""
		Returns the red color component of this color.
		"""
		res = super(QColor,self).redF()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def rgb(self):
		"""
		Returns the RGB value of the color
		The alpha value is opaque.
		"""
		res = super(QColor,self).rgb()
		return res
	#----------------------------------------------------------------------
	def rgba(self):
		"""
		Returns the RGB value of the color, including its alpha.
		For an invalid color, the alpha value of the returned color is unspecified.
		"""
		res = super(QColor,self).rgba()
		return res
	#----------------------------------------------------------------------
	def saturation(self):
		"""
		Returns the saturation color component of this color.
		The color is implicitly converted to HSV.
		"""
		res = super(QColor,self).saturation()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def saturationF(self):
		"""
		Returns the saturation color component of this color.
		The color is implicitly converted to HSV.
		"""
		res = super(QColor,self).saturationF()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def spec(self):
		"""
		Returns how the color was specified.
		"""
		res = super(QColor,self).spec()
		isinstance(res,QtGui.QColor.Spec)
		return res
	#----------------------------------------------------------------------
	def toCmyk(self):
		"""
		Creates and returns a CMYK PySide.QtGui.QColor based on this color.
		"""
		res = super(QColor,self).toCmyk()
		isinstance(res,QtGui.QColor)
		return res
	#----------------------------------------------------------------------
	def toHsl(self):
		"""
		Creates and returns an HSL PySide.QtGui.QColor based on this color.
		"""
		res = super(QColor,self).toHsl()
		isinstance(res,QtGui.QColor)
		return res
	#----------------------------------------------------------------------
	def toHsv(self):
		"""
		Creates and returns an HSV PySide.QtGui.QColor based on this color.
		"""
		res = super(QColor,self).toHsv()
		isinstance(res,QtGui.QColor)
		return res
	#----------------------------------------------------------------------
	def toRgb(self):
		"""
		Create and returns an RGB PySide.QtGui.QColor based on this color.
		"""
		res = super(QColor,self).toRgb()
		isinstance(res,QtGui.QColor)
		return res
	#----------------------------------------------------------------------
	def toTuple(self):
		"""

		"""
		res = super(QColor,self).toTuple()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def value(self):
		"""
		Returns the value color component of this color.
		"""
		res = super(QColor,self).value()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def valueF(self):
		"""
		Returns the value color component of this color.
		"""
		res = super(QColor,self).valueF()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def yellow(self):
		"""
		Returns the yellow color component of this color.
		"""
		res = super(QColor,self).yellow()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def yellowF(self):
		"""
		Returns the yellow color component of this color.
		"""
		res = super(QColor,self).yellowF()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def __setstate__(self,arg__1):
		"""
		__setstate__(arg__1)
			arg__1=Object


		"""
		res = super(QColor,self).__setstate__(arg__1)
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def convertTo(self,colorSpec):
		"""
		convertTo(colorSpec)
			colorSpec=QtGui.QColor.Spec

		Creates a copy of this color in the format specified by colorSpec .
		"""
		res = super(QColor,self).convertTo(colorSpec)
		isinstance(res,QtGui.QColor)
		return res
	#----------------------------------------------------------------------
	def darker(self,f=None):
		"""
		darker(f=None)
			f=QtCore.int

		Returns a darker (or lighter) color, but does not change this object.
		If the factor is greater than 100, this functions returns a darker color
		Setting factor to 300 returns a color that has one-third the brightness
		If the factor is less than 100, the return color is lighter, but we recommend using the PySide.QtGui.QColor.lighter() function for this purpose
		If the factor is 0 or negative, the return value is unspecified.
		The function converts the current RGB color to HSV, divides the value (V) component by factor and converts the color back to RGB.
		"""
		res = super(QColor,self).darker(f)
		isinstance(res,QtGui.QColor)
		return res
	#----------------------------------------------------------------------
	def lighter(self,f=None):
		"""
		lighter(f=None)
			f=QtCore.int

		Returns a lighter (or darker) color, but does not change this object.
		If the factor is greater than 100, this functions returns a lighter color
		Setting factor to 150 returns a color that is 50% brighter
		If the factor is less than 100, the return color is darker, but we recommend using the PySide.QtGui.QColor.darker() function for this purpose
		If the factor is 0 or negative, the return value is unspecified.
		The function converts the current RGB color to HSV, multiplies the value (V) component by factor and converts the color back to RGB.
		"""
		res = super(QColor,self).lighter(f)
		isinstance(res,QtGui.QColor)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,c):
		"""
		__ne__(c)
			c=QtGui.QColor

		Returns true if this color has a different RGB and alpha values from color ; otherwise returns false.
		"""
		res = super(QColor,self).__ne__(c)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,c):
		"""
		__eq__(c)
			c=QtGui.QColor

		Returns true if this color has the same RGB and alpha values as color ; otherwise returns false.
		"""
		res = super(QColor,self).__eq__(c)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setAlpha(self,alpha):
		"""
		setAlpha(alpha)
			alpha=QtCore.int

		Sets the alpha of this color to alpha
		Integer alpha is specified in the range 0-255.
		"""
		res = super(QColor,self).setAlpha(alpha)
		return res
	#----------------------------------------------------------------------
	def setAlphaF(self,alpha):
		"""
		setAlphaF(alpha)
			alpha=QtCore.qreal

		Sets the alpha of this color to alpha
		qreal alpha is specified in the range 0.0-1.0.
		"""
		res = super(QColor,self).setAlphaF(alpha)
		return res
	#----------------------------------------------------------------------
	def setBlue(self,blue):
		"""
		setBlue(blue)
			blue=QtCore.int

		Sets the blue color component of this color to blue
		Integer components are specified in the range 0-255.
		"""
		res = super(QColor,self).setBlue(blue)
		return res
	#----------------------------------------------------------------------
	def setBlueF(self,blue):
		"""
		setBlueF(blue)
			blue=QtCore.qreal

		Sets the blue color component of this color to blue
		Float components are specified in the range 0.0-1.0.
		"""
		res = super(QColor,self).setBlueF(blue)
		return res
	#----------------------------------------------------------------------
	def setCmyk(self,c,m,y,k,a=None):
		"""
		setCmyk(c,m,y,k,a=None)
			c=QtCore.int
			m=QtCore.int
			y=QtCore.int
			k=QtCore.int
			a=QtCore.int

		Sets the color to CMYK values, c (cyan), m (magenta), y (yellow), k (black), and a (alpha-channel, i.e
		transparency).
		All the values must be in the range 0-255.
		"""
		res = super(QColor,self).setCmyk(c,m,y,k,a)
		return res
	#----------------------------------------------------------------------
	def setCmykF(self,c,m,y,k,a=None):
		"""
		setCmykF(c,m,y,k,a=None)
			c=QtCore.qreal
			m=QtCore.qreal
			y=QtCore.qreal
			k=QtCore.qreal
			a=QtCore.qreal

		This is an overloaded function.
		Sets the color to CMYK values, c (cyan), m (magenta), y (yellow), k (black), and a (alpha-channel, i.e
		transparency).
		All the values must be in the range 0.0-1.0.
		"""
		res = super(QColor,self).setCmykF(c,m,y,k,a)
		return res
	#----------------------------------------------------------------------
	def setColorFromString(self,name):
		"""
		setColorFromString(name)
			name=unicode


		"""
		res = super(QColor,self).setColorFromString(name)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setGreen(self,green):
		"""
		setGreen(green)
			green=QtCore.int

		Sets the green color component of this color to green
		Integer components are specified in the range 0-255.
		"""
		res = super(QColor,self).setGreen(green)
		return res
	#----------------------------------------------------------------------
	def setGreenF(self,green):
		"""
		setGreenF(green)
			green=QtCore.qreal

		Sets the green color component of this color to green
		Float components are specified in the range 0.0-1.0.
		"""
		res = super(QColor,self).setGreenF(green)
		return res
	#----------------------------------------------------------------------
	def setHsl(self,h,s,l,a=None):
		"""
		setHsl(h,s,l,a=None)
			h=QtCore.int
			s=QtCore.int
			l=QtCore.int
			a=QtCore.int

		Sets a HSL color value; h is the hue, s is the saturation, l is the lightness and a is the alpha component of the HSL color.
		The saturation, value and alpha-channel values must be in the range 0-255, and the hue value must be greater than -1.
		"""
		res = super(QColor,self).setHsl(h,s,l,a)
		return res
	#----------------------------------------------------------------------
	def setHslF(self,h,s,l,a=None):
		"""
		setHslF(h,s,l,a=None)
			h=QtCore.qreal
			s=QtCore.qreal
			l=QtCore.qreal
			a=QtCore.qreal

		Sets a HSL color lightness; h is the hue, s is the saturation, l is the lightness and a is the alpha component of the HSL color.
		All the values must be in the range 0.0-1.0.
		"""
		res = super(QColor,self).setHslF(h,s,l,a)
		return res
	#----------------------------------------------------------------------
	def setHsv(self,h,s,v,a=None):
		"""
		setHsv(h,s,v,a=None)
			h=QtCore.int
			s=QtCore.int
			v=QtCore.int
			a=QtCore.int

		Sets a HSV color value; h is the hue, s is the saturation, v is the value and a is the alpha component of the HSV color.
		The saturation, value and alpha-channel values must be in the range 0-255, and the hue value must be greater than -1.
		"""
		res = super(QColor,self).setHsv(h,s,v,a)
		return res
	#----------------------------------------------------------------------
	def setHsvF(self,h,s,v,a=None):
		"""
		setHsvF(h,s,v,a=None)
			h=QtCore.qreal
			s=QtCore.qreal
			v=QtCore.qreal
			a=QtCore.qreal

		Sets a HSV color value; h is the hue, s is the saturation, v is the value and a is the alpha component of the HSV color.
		All the values must be in the range 0.0-1.0.
		"""
		res = super(QColor,self).setHsvF(h,s,v,a)
		return res
	#----------------------------------------------------------------------
	def setNamedColor(self,name):
		"""
		setNamedColor(name)
			name=unicode

		Sets the RGB value of this PySide.QtGui.QColor to name , which may be in one of these formats:
		The color is invalid if name cannot be parsed.
		"""
		res = super(QColor,self).setNamedColor(name)
		return res
	#----------------------------------------------------------------------
	def setRed(self,red):
		"""
		setRed(red)
			red=QtCore.int

		Sets the red color component of this color to red
		Integer components are specified in the range 0-255.
		"""
		res = super(QColor,self).setRed(red)
		return res
	#----------------------------------------------------------------------
	def setRedF(self,red):
		"""
		setRedF(red)
			red=QtCore.qreal

		Sets the red color component of this color to red
		Float components are specified in the range 0.0-1.0.
		"""
		res = super(QColor,self).setRedF(red)
		return res
	#----------------------------------------------------------------------
	def setRgb(self,*args,**kwargs):
		"""
		setRgb(rgb)
			rgb=long

		setRgb(r,g,b,a=None)
			r=QtCore.int
			g=QtCore.int
			b=QtCore.int
			a=QtCore.int


		"""
		res = super(QColor,self).setRgb(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setRgbF(self,r,g,b,a=None):
		"""
		setRgbF(r,g,b,a=None)
			r=QtCore.qreal
			g=QtCore.qreal
			b=QtCore.qreal
			a=QtCore.qreal

		Sets the color channels of this color to r (red), g (green), b (blue) and a (alpha, transparency).
		All values must be in the range 0.0-1.0.
		"""
		res = super(QColor,self).setRgbF(r,g,b,a)
		return res
	#----------------------------------------------------------------------
	def setRgba(self,rgba):
		"""
		setRgba(rgba)
			rgba=long


		"""
		res = super(QColor,self).setRgba(rgba)
		return res

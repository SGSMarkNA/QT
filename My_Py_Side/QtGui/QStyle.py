from PySide import QtGui, QtCore

class QStyle(QtGui.QStyle):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QStyle,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def proxy(self):
		"""
		This function returns the current proxy for this style
		By default most styles will return themselves
		However when a proxy style is in use, it will allow the style to call back into its proxy.
		"""
		res = super(QStyle,self).proxy()
		isinstance(res,QtGui.QStyle)
		return res
	#----------------------------------------------------------------------
	def standardPalette(self):
		"""
		Returns the styles standard palette.
		Note that on systems that support system colors, the styles standard palette is not used
		In particular, the Windows XP, Vista, and Mac styles do not use the standard palette, but make use of native theme engines
		With these styles, you should not set the palette with QApplication::setStandardPalette().
		"""
		res = super(QStyle,self).standardPalette()
		isinstance(res,QtGui.QPalette)
		return res
	#----------------------------------------------------------------------
	def combinedLayoutSpacing(self,controls1,controls2,orientation,option=None,widget=None):
		"""
		combinedLayoutSpacing(controls1,controls2,orientation,option=None,widget=None)
			controls1=QtGui.QSizePolicy.ControlTypes
			controls2=QtGui.QSizePolicy.ControlTypes
			orientation=QtCore.Qt.Orientation
			option=QtGui.QStyleOption
			widget=QtGui.QWidget


		"""
		res = super(QStyle,self).combinedLayoutSpacing(controls1,controls2,orientation,option,widget)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def drawComplexControl(self,cc,opt,p,widget=None):
		"""
		drawComplexControl(cc,opt,p,widget=None)
			cc=QtGui.QStyle.ComplexControl
			opt=QtGui.QStyleOptionComplex
			p=QtGui.QPainter
			widget=QtGui.QWidget

		Draws the given control using the provided painter with the style options specified by option .
		The widget argument is optional and can be used as aid in drawing the control.
		The option parameter is a pointer to a PySide.QtGui.QStyleOptionComplex object that can be cast to the correct subclass using the qstyleoption_cast() function
		Note that the rect member of the specified option must be in logical coordinates
		Reimplementations of this function should use PySide.QtGui.QStyle.visualRect() to change the logical coordinates into screen coordinates before calling the PySide.QtGui.QStyle.drawPrimitive() or PySide.QtGui.QStyle.drawControl() function.
		The table below is listing the complex control elements and their associated style option subclass
		The style options contain all the parameters required to draw the controls, including QStyleOption.state which holds the style flags that are used when drawing
		The table also describes which flags that are set when casting the given option to the appropriate subclass.
		"""
		res = super(QStyle,self).drawComplexControl(cc,opt,p,widget)
		return res
	#----------------------------------------------------------------------
	def drawControl(self,element,opt,p,widget=None):
		"""
		drawControl(element,opt,p,widget=None)
			element=QtGui.QStyle.ControlElement
			opt=QtGui.QStyleOption
			p=QtGui.QPainter
			widget=QtGui.QWidget

		Draws the given element with the provided painter with the style options specified by option .
		The widget argument is optional and can be used as aid in drawing the control
		The option parameter is a pointer to a PySide.QtGui.QStyleOption object that can be cast to the correct subclass using the qstyleoption_cast() function.
		The table below is listing the control elements and their associated style option subclass
		The style options contain all the parameters required to draw the controls, including QStyleOption.state which holds the style flags that are used when drawing
		The table also describes which flags that are set when casting the given option to the appropriate subclass.
		Note that if a control element is not listed here, it is because it uses a plain PySide.QtGui.QStyleOption object.
		"""
		res = super(QStyle,self).drawControl(element,opt,p,widget)
		return res
	#----------------------------------------------------------------------
	def drawItemPixmap(self,painter,rect,alignment,pixmap):
		"""
		drawItemPixmap(painter,rect,alignment,pixmap)
			painter=QtGui.QPainter
			rect=QtCore.QRect
			alignment=QtCore.int
			pixmap=QtGui.QPixmap

		Draws the given pixmap in the specified rectangle , according to the specified alignment , using the provided painter .
		"""
		res = super(QStyle,self).drawItemPixmap(painter,rect,alignment,pixmap)
		return res
	#----------------------------------------------------------------------
	def drawItemText(self,painter,rect,flags,pal,enabled,text,textRole=None):
		"""
		drawItemText(painter,rect,flags,pal,enabled,text,textRole=None)
			painter=QtGui.QPainter
			rect=QtCore.QRect
			flags=QtCore.int
			pal=QtGui.QPalette
			enabled=QtCore.bool
			text=unicode
			textRole=QtGui.QPalette.ColorRole


		"""
		res = super(QStyle,self).drawItemText(painter,rect,flags,pal,enabled,text,textRole)
		return res
	#----------------------------------------------------------------------
	def drawPrimitive(self,pe,opt,p,widget=None):
		"""
		drawPrimitive(pe,opt,p,widget=None)
			pe=QtGui.QStyle.PrimitiveElement
			opt=QtGui.QStyleOption
			p=QtGui.QPainter
			widget=QtGui.QWidget

		Draws the given primitive element with the provided painter using the style options specified by option .
		The widget argument is optional and may contain a widget that may aid in drawing the primitive element.
		The table below is listing the primitive elements and their associated style option subclasses
		The style options contain all the parameters required to draw the elements, including QStyleOption.state which holds the style flags that are used when drawing
		The table also describes which flags that are set when casting the given option to the appropriate subclass.
		Note that if a primitive element is not listed here, it is because it uses a plain PySide.QtGui.QStyleOption object.
		"""
		res = super(QStyle,self).drawPrimitive(pe,opt,p,widget)
		return res
	#----------------------------------------------------------------------
	def generatedIconPixmap(self,iconMode,pixmap,opt):
		"""
		generatedIconPixmap(iconMode,pixmap,opt)
			iconMode=QtGui.QIcon.Mode
			pixmap=QtGui.QPixmap
			opt=QtGui.QStyleOption


		"""
		res = super(QStyle,self).generatedIconPixmap(iconMode,pixmap,opt)
		isinstance(res,QtGui.QPixmap)
		return res
	#----------------------------------------------------------------------
	def hitTestComplexControl(self,cc,opt,pt,widget=None):
		"""
		hitTestComplexControl(cc,opt,pt,widget=None)
			cc=QtGui.QStyle.ComplexControl
			opt=QtGui.QStyleOptionComplex
			pt=QtCore.QPoint
			widget=QtGui.QWidget

		Returns the sub control at the given position in the given complex control (with the style options specified by option ).
		Note that the position is expressed in screen coordinates.
		The option argument is a pointer to a PySide.QtGui.QStyleOptionComplex object (or one of its subclasses)
		The object can be cast to the appropriate type using the qstyleoption_cast() function
		See PySide.QtGui.QStyle.drawComplexControl() for details
		The widget argument is optional and can contain additional information for the function.
		"""
		res = super(QStyle,self).hitTestComplexControl(cc,opt,pt,widget)
		isinstance(res,QtGui.QStyle.SubControl)
		return res
	#----------------------------------------------------------------------
	def itemPixmapRect(self,r,flags,pixmap):
		"""
		itemPixmapRect(r,flags,pixmap)
			r=QtCore.QRect
			flags=QtCore.int
			pixmap=QtGui.QPixmap

		Returns the area within the given rectangle in which to draw the specified pixmap according to the defined alignment .
		"""
		res = super(QStyle,self).itemPixmapRect(r,flags,pixmap)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def itemTextRect(self,fm,r,flags,enabled,text):
		"""
		itemTextRect(fm,r,flags,enabled,text)
			fm=QtGui.QFontMetrics
			r=QtCore.QRect
			flags=QtCore.int
			enabled=QtCore.bool
			text=unicode

		Returns the area within the given rectangle in which to draw the provided text according to the specified font metrics and alignment
		The enabled parameter indicates whether or not the associated item is enabled.
		If the given rectangle is larger than the area needed to render the text , the rectangle that is returned will be offset within rectangle according to the specified alignment
		For example, if alignment is Qt.AlignCenter , the returned rectangle will be centered within rectangle
		If the given rectangle is smaller than the area needed, the returned rectangle will be the smallest rectangle large enough to render the text .
		"""
		res = super(QStyle,self).itemTextRect(fm,r,flags,enabled,text)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def layoutSpacing(self,control1,control2,orientation,option=None,widget=None):
		"""
		layoutSpacing(control1,control2,orientation,option=None,widget=None)
			control1=QtGui.QSizePolicy.ControlType
			control2=QtGui.QSizePolicy.ControlType
			orientation=QtCore.Qt.Orientation
			option=QtGui.QStyleOption
			widget=QtGui.QWidget


		"""
		res = super(QStyle,self).layoutSpacing(control1,control2,orientation,option,widget)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def pixelMetric(self,metric,option=None,widget=None):
		"""
		pixelMetric(metric,option=None,widget=None)
			metric=QtGui.QStyle.PixelMetric
			option=QtGui.QStyleOption
			widget=QtGui.QWidget

		Returns the value of the given pixel metric .
		The specified option and widget can be used for calculating the metric
		In general, the widget argument is not used
		The option can be cast to the appropriate type using the qstyleoption_cast() function
		Note that the option may be zero even for PixelMetrics that can make use of it
		See the table below for the appropriate option casts:
		Some pixel metrics are called from widgets and some are only called internally by the style
		If the metric is not called by a widget, it is the discretion of the style author to make use of it
		For some styles, this may not be appropriate.
		"""
		res = super(QStyle,self).pixelMetric(metric,option,widget)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def polish(self,*args,**kwargs):
		"""
		polish(arg__1)
			arg__1=QtGui.QPalette

		polish(arg__1)
			arg__1=QtGui.QWidget

		polish(arg__1)
			arg__1=QtGui.QApplication

		This is an overloaded function.
		Changes the palette according to style specific requirements for color palettes (if any).
		"""
		res = super(QStyle,self).polish(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setProxy(self,style):
		"""
		setProxy(style)
			style=QtGui.QStyle


		"""
		res = super(QStyle,self).setProxy(style)
		return res
	#----------------------------------------------------------------------
	def sizeFromContents(self,ct,opt,contentsSize,w=None):
		"""
		sizeFromContents(ct,opt,contentsSize,w=None)
			ct=QtGui.QStyle.ContentsType
			opt=QtGui.QStyleOption
			contentsSize=QtCore.QSize
			w=QtGui.QWidget

		Returns the size of the element described by the specified option and type , based on the provided contentsSize .
		The option argument is a pointer to a PySide.QtGui.QStyleOption or one of its subclasses
		The option can be cast to the appropriate type using the qstyleoption_cast() function
		The widget is an optional argument and can contain extra information used for calculating the size.
		See the table below for the appropriate option casts:
		"""
		res = super(QStyle,self).sizeFromContents(ct,opt,contentsSize,w)
		isinstance(res,QtCore.QSize)
		return res
	#----------------------------------------------------------------------
	def standardIcon(self,standardIcon,option=None,widget=None):
		"""
		standardIcon(standardIcon,option=None,widget=None)
			standardIcon=QtGui.QStyle.StandardPixmap
			option=QtGui.QStyleOption
			widget=QtGui.QWidget

		Returns an icon for the given standardIcon .
		The standardIcon is a standard pixmap which can follow some existing GUI style or guideline
		The option argument can be used to pass extra information required when defining the appropriate icon
		The widget argument is optional and can also be used to aid the determination of the icon.
		"""
		res = super(QStyle,self).standardIcon(standardIcon,option,widget)
		isinstance(res,QtGui.QIcon)
		return res
	#----------------------------------------------------------------------
	def standardPixmap(self,standardPixmap,opt=None,widget=None):
		"""
		standardPixmap(standardPixmap,opt=None,widget=None)
			standardPixmap=QtGui.QStyle.StandardPixmap
			opt=QtGui.QStyleOption
			widget=QtGui.QWidget

		Returns a pixmap for the given standardPixmap .
		A standard pixmap is a pixmap that can follow some existing GUI style or guideline
		The option argument can be used to pass extra information required when defining the appropriate pixmap
		The widget argument is optional and can also be used to aid the determination of the pixmap.
		Developers calling PySide.QtGui.QStyle.standardPixmap() should instead call PySide.QtGui.QStyle.standardIcon() Developers who re-implemented PySide.QtGui.QStyle.standardPixmap() should instead re-implement the slot PySide.QtGui.QStyle.standardIconImplementation() .
		"""
		res = super(QStyle,self).standardPixmap(standardPixmap,opt,widget)
		isinstance(res,QtGui.QPixmap)
		return res
	#----------------------------------------------------------------------
	def styleHint(self,stylehint,opt=None,widget=None,returnData=None):
		"""
		styleHint(stylehint,opt=None,widget=None,returnData=None)
			stylehint=QtGui.QStyle.StyleHint
			opt=QtGui.QStyleOption
			widget=QtGui.QWidget
			returnData=QtGui.QStyleHintReturn

		Returns an integer representing the specified style hint for the given widget described by the provided style option .
		returnData is used when the querying widget needs more detailed data than the integer that PySide.QtGui.QStyle.styleHint() returns
		See the PySide.QtGui.QStyleHintReturn class description for details.
		"""
		res = super(QStyle,self).styleHint(stylehint,opt,widget,returnData)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def subControlRect(self,cc,opt,sc,widget=None):
		"""
		subControlRect(cc,opt,sc,widget=None)
			cc=QtGui.QStyle.ComplexControl
			opt=QtGui.QStyleOptionComplex
			sc=QtGui.QStyle.SubControl
			widget=QtGui.QWidget

		Returns the rectangle containing the specified subControl of the given complex control (with the style specified by option )
		The rectangle is defined in screen coordinates.
		The option argument is a pointer to PySide.QtGui.QStyleOptionComplex or one of its subclasses, and can be cast to the appropriate type using the qstyleoption_cast() function
		See PySide.QtGui.QStyle.drawComplexControl() for details
		The widget is optional and can contain additional information for the function.
		"""
		res = super(QStyle,self).subControlRect(cc,opt,sc,widget)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def subElementRect(self,subElement,option,widget=None):
		"""
		subElementRect(subElement,option,widget=None)
			subElement=QtGui.QStyle.SubElement
			option=QtGui.QStyleOption
			widget=QtGui.QWidget

		Returns the sub-area for the given element as described in the provided style option
		The returned rectangle is defined in screen coordinates.
		The widget argument is optional and can be used to aid determining the area
		The PySide.QtGui.QStyleOption object can be cast to the appropriate type using the qstyleoption_cast() function
		See the table below for the appropriate option casts:
		"""
		res = super(QStyle,self).subElementRect(subElement,option,widget)
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def unpolish(self,*args,**kwargs):
		"""
		unpolish(arg__1)
			arg__1=QtGui.QWidget

		unpolish(arg__1)
			arg__1=QtGui.QApplication

		Uninitialize the given widget s appearance.
		This function is the counterpart to PySide.QtGui.QStyle.polish()
		It is called for every polished widget whenever the style is dynamically changed; the former style has to unpolish its settings before the new style can polish them again.
		Note that PySide.QtGui.QStyle.unpolish() will only be called if the widget is destroyed
		This can cause problems in some cases, e.g, if you remove a widget from the UI, cache it, and then reinsert it after the style has changed; some of Qts classes cache their widgets.
		"""
		res = super(QStyle,self).unpolish(*args,**kwargs)
		return res

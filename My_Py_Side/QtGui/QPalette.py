from PySide import QtGui, QtCore

class QPalette(QtGui.QPalette):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QPalette,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def alternateBase(self):
		"""
		Returns the alternate base brush of the current color group.
		"""
		res = super(QPalette,self).alternateBase()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def base(self):
		"""
		Returns the base brush of the current color group.
		"""
		res = super(QPalette,self).base()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def brightText(self):
		"""
		Returns the bright text foreground brush of the current color group.
		"""
		res = super(QPalette,self).brightText()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def button(self):
		"""
		Returns the button brush of the current color group.
		"""
		res = super(QPalette,self).button()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def buttonText(self):
		"""
		Returns the button text foreground brush of the current color group.
		"""
		res = super(QPalette,self).buttonText()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def cacheKey(self):
		"""
		Returns a number that identifies the contents of this PySide.QtGui.QPalette object
		Distinct PySide.QtGui.QPalette objects can have the same key if they refer to the same contents.
		The PySide.QtGui.QPalette.cacheKey() will change when the palette is altered.
		"""
		res = super(QPalette,self).cacheKey()
		isinstance(res,QtCore.qint64)
		return res
	#----------------------------------------------------------------------
	def currentColorGroup(self):
		"""
		Returns the palettes current color group.
		"""
		res = super(QPalette,self).currentColorGroup()
		isinstance(res,QtGui.QPalette.ColorGroup)
		return res
	#----------------------------------------------------------------------
	def dark(self):
		"""
		Returns the dark brush of the current color group.
		"""
		res = super(QPalette,self).dark()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def highlight(self):
		"""
		Returns the highlight brush of the current color group.
		"""
		res = super(QPalette,self).highlight()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def highlightedText(self):
		"""
		Returns the highlighted text brush of the current color group.
		"""
		res = super(QPalette,self).highlightedText()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def init(self):
		"""

		"""
		res = super(QPalette,self).init()
		return res
	#----------------------------------------------------------------------
	def light(self):
		"""
		Returns the light brush of the current color group.
		"""
		res = super(QPalette,self).light()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def link(self):
		"""
		Returns the unvisited link text brush of the current color group.
		"""
		res = super(QPalette,self).link()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def linkVisited(self):
		"""
		Returns the visited link text brush of the current color group.
		"""
		res = super(QPalette,self).linkVisited()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def mid(self):
		"""
		Returns the mid brush of the current color group.
		"""
		res = super(QPalette,self).mid()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def midlight(self):
		"""
		Returns the midlight brush of the current color group.
		"""
		res = super(QPalette,self).midlight()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def resolve(self):
		"""

		"""
		res = super(QPalette,self).resolve()
		isinstance(res,QtCore.uint)
		return res
	#----------------------------------------------------------------------
	def shadow(self):
		"""
		Returns the shadow brush of the current color group.
		"""
		res = super(QPalette,self).shadow()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def text(self):
		"""
		Returns the text foreground brush of the current color group.
		"""
		res = super(QPalette,self).text()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def toolTipBase(self):
		"""
		Returns the tool tip base brush of the current color group
		This brush is used by PySide.QtGui.QToolTip and PySide.QtGui.QWhatsThis .
		"""
		res = super(QPalette,self).toolTipBase()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def toolTipText(self):
		"""
		Returns the tool tip text brush of the current color group
		This brush is used by PySide.QtGui.QToolTip and PySide.QtGui.QWhatsThis .
		"""
		res = super(QPalette,self).toolTipText()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def window(self):
		"""
		Returns the window (general background) brush of the current color group.
		"""
		res = super(QPalette,self).window()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def windowText(self):
		"""
		Returns the window text (general foreground) brush of the current color group.
		"""
		res = super(QPalette,self).windowText()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def brush(self,*args,**kwargs):
		"""
		brush(cg,cr)
			cg=QtGui.QPalette.ColorGroup
			cr=QtGui.QPalette.ColorRole

		brush(cr)
			cr=QtGui.QPalette.ColorRole

		Returns the brush in the specified color group , used for the given color role .
		"""
		res = super(QPalette,self).brush(*args,**kwargs)
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def color(self,*args,**kwargs):
		"""
		color(cr)
			cr=QtGui.QPalette.ColorRole

		color(cg,cr)
			cg=QtGui.QPalette.ColorGroup
			cr=QtGui.QPalette.ColorRole

		This is an overloaded function.
		Returns the color that has been set for the given color role in the current QPalette.ColorGroup .
		"""
		res = super(QPalette,self).color(*args,**kwargs)
		isinstance(res,QtGui.QColor)
		return res
	#----------------------------------------------------------------------
	def isBrushSet(self,cg,cr):
		"""
		isBrushSet(cg,cr)
			cg=QtGui.QPalette.ColorGroup
			cr=QtGui.QPalette.ColorRole

		Returns true if the QPalette.ColorGroup cg and QPalette.ColorRole cr has been set previously on this palette; otherwise returns false.
		"""
		res = super(QPalette,self).isBrushSet(cg,cr)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isCopyOf(self,p):
		"""
		isCopyOf(p)
			p=QtGui.QPalette

		Returns true if this palette and p are copies of each other, i.e
		one of them was created as a copy of the other and neither was subsequently modified; otherwise returns false
		This is much stricter than equality.
		"""
		res = super(QPalette,self).isCopyOf(p)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isEqual(self,cr1,cr2):
		"""
		isEqual(cr1,cr2)
			cr1=QtGui.QPalette.ColorGroup
			cr2=QtGui.QPalette.ColorGroup

		Returns true (usually quickly) if color group cg1 is equal to cg2 ; otherwise returns false.
		"""
		res = super(QPalette,self).isEqual(cr1,cr2)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,p):
		"""
		__ne__(p)
			p=QtGui.QPalette

		Returns true (slowly) if this palette is different from p ; otherwise returns false (usually quickly).
		"""
		res = super(QPalette,self).__ne__(p)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,p):
		"""
		__eq__(p)
			p=QtGui.QPalette

		Returns true (usually quickly) if this palette is equal to p ; otherwise returns false (slowly).
		"""
		res = super(QPalette,self).__eq__(p)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def resolve(self,*args,**kwargs):
		"""
		resolve(mask)
			mask=QtCore.uint

		resolve(arg__1)
			arg__1=QtGui.QPalette


		"""
		res = super(QPalette,self).resolve(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setBrush(self,*args,**kwargs):
		"""
		setBrush(cr,brush)
			cr=QtGui.QPalette.ColorRole
			brush=QtGui.QBrush

		setBrush(cg,cr,brush)
			cg=QtGui.QPalette.ColorGroup
			cr=QtGui.QPalette.ColorRole
			brush=QtGui.QBrush

		Sets the brush for the given color role to the specified brush for all groups in the palette.
		"""
		res = super(QPalette,self).setBrush(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setColor(self,*args,**kwargs):
		"""
		setColor(cr,color)
			cr=QtGui.QPalette.ColorRole
			color=QtGui.QColor

		setColor(cg,cr,color)
			cg=QtGui.QPalette.ColorGroup
			cr=QtGui.QPalette.ColorRole
			color=QtGui.QColor

		This is an overloaded function.
		Sets the color used for the given color role , in all color groups, to the specified solid color .
		"""
		res = super(QPalette,self).setColor(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setColorGroup(self,*args,**kwargs):
		"""
		setColorGroup(cr,windowText,button,light,dark,mid,text,bright_text,base,alternate_base,window,midlight,button_text,shadow,highlight,highlighted_text,link,link_visited,toolTipBase,toolTipText)
			cr=QtGui.QPalette.ColorGroup
			windowText=QtGui.QBrush
			button=QtGui.QBrush
			light=QtGui.QBrush
			dark=QtGui.QBrush
			mid=QtGui.QBrush
			text=QtGui.QBrush
			bright_text=QtGui.QBrush
			base=QtGui.QBrush
			alternate_base=QtGui.QBrush
			window=QtGui.QBrush
			midlight=QtGui.QBrush
			button_text=QtGui.QBrush
			shadow=QtGui.QBrush
			highlight=QtGui.QBrush
			highlighted_text=QtGui.QBrush
			link=QtGui.QBrush
			link_visited=QtGui.QBrush
			toolTipBase=QtGui.QBrush
			toolTipText=QtGui.QBrush

		setColorGroup(cr,windowText,button,light,dark,mid,text,bright_text,base,alternate_base,window,midlight,button_text,shadow,highlight,highlighted_text,link,link_visited)
			cr=QtGui.QPalette.ColorGroup
			windowText=QtGui.QBrush
			button=QtGui.QBrush
			light=QtGui.QBrush
			dark=QtGui.QBrush
			mid=QtGui.QBrush
			text=QtGui.QBrush
			bright_text=QtGui.QBrush
			base=QtGui.QBrush
			alternate_base=QtGui.QBrush
			window=QtGui.QBrush
			midlight=QtGui.QBrush
			button_text=QtGui.QBrush
			shadow=QtGui.QBrush
			highlight=QtGui.QBrush
			highlighted_text=QtGui.QBrush
			link=QtGui.QBrush
			link_visited=QtGui.QBrush

		setColorGroup(cr,windowText,button,light,dark,mid,text,bright_text,base,window)
			cr=QtGui.QPalette.ColorGroup
			windowText=QtGui.QBrush
			button=QtGui.QBrush
			light=QtGui.QBrush
			dark=QtGui.QBrush
			mid=QtGui.QBrush
			text=QtGui.QBrush
			bright_text=QtGui.QBrush
			base=QtGui.QBrush
			window=QtGui.QBrush


		"""
		res = super(QPalette,self).setColorGroup(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setCurrentColorGroup(self,cg):
		"""
		setCurrentColorGroup(cg)
			cg=QtGui.QPalette.ColorGroup

		Set the palettes current color group to cg .
		"""
		res = super(QPalette,self).setCurrentColorGroup(cg)
		return res

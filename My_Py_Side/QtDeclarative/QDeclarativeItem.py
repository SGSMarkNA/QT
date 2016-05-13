from PySide import QtGui, QtCore

class QDeclarativeItem(QtDeclarative.QDeclarativeItem):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDeclarativeItem,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def baselineOffset(self):
		"""

		"""
		res = super(QDeclarativeItem,self).baselineOffset()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def childrenRect(self):
		"""

		"""
		res = super(QDeclarativeItem,self).childrenRect()
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def clip(self):
		"""

		"""
		res = super(QDeclarativeItem,self).clip()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def forceActiveFocus(self):
		"""

		"""
		res = super(QDeclarativeItem,self).forceActiveFocus()
		return res
	#----------------------------------------------------------------------
	def hasActiveFocus(self):
		"""

		"""
		res = super(QDeclarativeItem,self).hasActiveFocus()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def height(self):
		"""
		Return the height of the item
		"""
		res = super(QDeclarativeItem,self).height()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def heightValid(self):
		"""
		Returns whether the height property has been set explicitly.
		"""
		res = super(QDeclarativeItem,self).heightValid()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def implicitHeight(self):
		"""
		Returns the height of the item that is implied by other properties that determine the content.
		"""
		res = super(QDeclarativeItem,self).implicitHeight()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def implicitWidth(self):
		"""
		Returns the width of the item that is implied by other properties that determine the content.
		"""
		res = super(QDeclarativeItem,self).implicitWidth()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def isComponentComplete(self):
		"""
		Returns true if construction of the QML component is complete; otherwise returns false.
		It is often desirable to delay some processing until the component is completed.
		"""
		res = super(QDeclarativeItem,self).isComponentComplete()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def keepMouseGrab(self):
		"""
		Returns a value indicating whether mouse input should remain with this item exclusively.
		"""
		res = super(QDeclarativeItem,self).keepMouseGrab()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def resetHeight(self):
		"""
		Reset the height of the item
		"""
		res = super(QDeclarativeItem,self).resetHeight()
		return res
	#----------------------------------------------------------------------
	def resetWidth(self):
		"""
		Reset the width of the item
		"""
		res = super(QDeclarativeItem,self).resetWidth()
		return res
	#----------------------------------------------------------------------
	def smooth(self):
		"""
		Returns true if the item should be drawn with antialiasing and smooth pixmap filtering, false otherwise.
		The default is false.
		"""
		res = super(QDeclarativeItem,self).smooth()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def transformOrigin(self):
		"""
		Returns the current transform origin.
		"""
		res = super(QDeclarativeItem,self).transformOrigin()
		isinstance(res,QtDeclarative.QDeclarativeItem.TransformOrigin)
		return res
	#----------------------------------------------------------------------
	def width(self):
		"""
		Return the width of the item
		"""
		res = super(QDeclarativeItem,self).width()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def widthValid(self):
		"""
		Returns whether the width property has been set explicitly.
		"""
		res = super(QDeclarativeItem,self).widthValid()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def childAt(self,x,y):
		"""
		childAt(x,y)
			x=QtCore.qreal
			y=QtCore.qreal


		"""
		res = super(QDeclarativeItem,self).childAt(x,y)
		isinstance(res,QtDeclarative.QDeclarativeItem)
		return res
	#----------------------------------------------------------------------
	def geometryChanged(self,newGeometry,oldGeometry):
		"""
		geometryChanged(newGeometry,oldGeometry)
			newGeometry=QtCore.QRectF
			oldGeometry=QtCore.QRectF

		This function is called to handle this items changes in geometry from oldGeometry to newGeometry
		If the two geometries are the same, it doesnt do anything.
		"""
		res = super(QDeclarativeItem,self).geometryChanged(newGeometry,oldGeometry)
		return res
	#----------------------------------------------------------------------
	def inputMethodPreHandler(self,arg__1):
		"""
		inputMethodPreHandler(arg__1)
			arg__1=QtGui.QInputMethodEvent


		"""
		res = super(QDeclarativeItem,self).inputMethodPreHandler(arg__1)
		return res
	#----------------------------------------------------------------------
	def keyPressPreHandler(self,arg__1):
		"""
		keyPressPreHandler(arg__1)
			arg__1=QtGui.QKeyEvent


		"""
		res = super(QDeclarativeItem,self).keyPressPreHandler(arg__1)
		return res
	#----------------------------------------------------------------------
	def keyReleasePreHandler(self,arg__1):
		"""
		keyReleasePreHandler(arg__1)
			arg__1=QtGui.QKeyEvent


		"""
		res = super(QDeclarativeItem,self).keyReleasePreHandler(arg__1)
		return res
	#----------------------------------------------------------------------
	def mapFromItem(self,item,x,y):
		"""
		mapFromItem(item,x,y)
			item=QtScript.QScriptValue
			x=QtCore.qreal
			y=QtCore.qreal


		"""
		res = super(QDeclarativeItem,self).mapFromItem(item,x,y)
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def mapToItem(self,item,x,y):
		"""
		mapToItem(item,x,y)
			item=QtScript.QScriptValue
			x=QtCore.qreal
			y=QtCore.qreal


		"""
		res = super(QDeclarativeItem,self).mapToItem(item,x,y)
		isinstance(res,QtScript.QScriptValue)
		return res
	#----------------------------------------------------------------------
	def setBaselineOffset(self,arg__1):
		"""
		setBaselineOffset(arg__1)
			arg__1=QtCore.qreal


		"""
		res = super(QDeclarativeItem,self).setBaselineOffset(arg__1)
		return res
	#----------------------------------------------------------------------
	def setClip(self,arg__1):
		"""
		setClip(arg__1)
			arg__1=QtCore.bool


		"""
		res = super(QDeclarativeItem,self).setClip(arg__1)
		return res
	#----------------------------------------------------------------------
	def setFocus(self,arg__1):
		"""
		setFocus(arg__1)
			arg__1=QtCore.bool


		"""
		res = super(QDeclarativeItem,self).setFocus(arg__1)
		return res
	#----------------------------------------------------------------------
	def setHeight(self,arg__1):
		"""
		setHeight(arg__1)
			arg__1=QtCore.qreal

		Set the height of the item
		"""
		res = super(QDeclarativeItem,self).setHeight(arg__1)
		return res
	#----------------------------------------------------------------------
	def setImplicitHeight(self,arg__1):
		"""
		setImplicitHeight(arg__1)
			arg__1=QtCore.qreal

		Sets the implied height of the item to h
		This is the height implied by other properties that determine the content.
		"""
		res = super(QDeclarativeItem,self).setImplicitHeight(arg__1)
		return res
	#----------------------------------------------------------------------
	def setImplicitWidth(self,arg__1):
		"""
		setImplicitWidth(arg__1)
			arg__1=QtCore.qreal

		Sets the implied width of the item to w
		This is the width implied by other properties that determine the content.
		"""
		res = super(QDeclarativeItem,self).setImplicitWidth(arg__1)
		return res
	#----------------------------------------------------------------------
	def setKeepMouseGrab(self,arg__1):
		"""
		setKeepMouseGrab(arg__1)
			arg__1=QtCore.bool

		The flag indicating whether the mouse should remain with this item is set to keep .
		This is useful for items that wish to grab and keep mouse interaction following a predefined gesture
		For example, an item that is interested in horizontal mouse movement may set keepMouseGrab to true once a threshold has been exceeded
		Once keepMouseGrab has been set to true, filtering items will not react to mouse events.
		If the item does not indicate that it wishes to retain mouse grab, a filtering item may steal the grab
		For example, Flickable may attempt to steal a mouse grab if it detects that the user has begun to move the viewport.
		"""
		res = super(QDeclarativeItem,self).setKeepMouseGrab(arg__1)
		return res
	#----------------------------------------------------------------------
	def setParentItem(self,parent):
		"""
		setParentItem(parent)
			parent=QtDeclarative.QDeclarativeItem


		"""
		res = super(QDeclarativeItem,self).setParentItem(parent)
		return res
	#----------------------------------------------------------------------
	def setSize(self,size):
		"""
		setSize(size)
			size=QtCore.QSizeF


		"""
		res = super(QDeclarativeItem,self).setSize(size)
		return res
	#----------------------------------------------------------------------
	def setSmooth(self,arg__1):
		"""
		setSmooth(arg__1)
			arg__1=QtCore.bool

		Sets whether the item should be drawn with antialiasing and smooth pixmap filtering to smooth .
		"""
		res = super(QDeclarativeItem,self).setSmooth(arg__1)
		return res
	#----------------------------------------------------------------------
	def setTransformOrigin(self,arg__1):
		"""
		setTransformOrigin(arg__1)
			arg__1=QtDeclarative.QDeclarativeItem.TransformOrigin

		Set the transform origin .
		"""
		res = super(QDeclarativeItem,self).setTransformOrigin(arg__1)
		return res
	#----------------------------------------------------------------------
	def setWidth(self,arg__1):
		"""
		setWidth(arg__1)
			arg__1=QtCore.qreal

		Set the width of the item
		"""
		res = super(QDeclarativeItem,self).setWidth(arg__1)
		return res

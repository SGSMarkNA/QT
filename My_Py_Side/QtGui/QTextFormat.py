from PySide import QtGui, QtCore

class QTextFormat(QtGui.QTextFormat):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextFormat,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def background(self):
		"""
		Returns the brush used to paint the documents background.
		"""
		res = super(QTextFormat,self).background()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def clearBackground(self):
		"""
		Clears the brush used to paint the documents background
		The default brush will be used.
		"""
		res = super(QTextFormat,self).clearBackground()
		return res
	#----------------------------------------------------------------------
	def clearForeground(self):
		"""
		Clears the brush used to paint the documents foreground
		The default brush will be used.
		"""
		res = super(QTextFormat,self).clearForeground()
		return res
	#----------------------------------------------------------------------
	def foreground(self):
		"""
		Returns the brush used to render foreground details, such as text, frame outlines, and table borders.
		"""
		res = super(QTextFormat,self).foreground()
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def isBlockFormat(self):
		"""
		Returns true if this text format is a BlockFormat ; otherwise returns false.
		"""
		res = super(QTextFormat,self).isBlockFormat()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isCharFormat(self):
		"""
		Returns true if this text format is a CharFormat ; otherwise returns false.
		"""
		res = super(QTextFormat,self).isCharFormat()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isFrameFormat(self):
		"""
		Returns true if this text format is a FrameFormat ; otherwise returns false.
		"""
		res = super(QTextFormat,self).isFrameFormat()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isImageFormat(self):
		"""
		Returns true if this text format is an image format; otherwise returns false.
		"""
		res = super(QTextFormat,self).isImageFormat()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isListFormat(self):
		"""
		Returns true if this text format is a ListFormat ; otherwise returns false.
		"""
		res = super(QTextFormat,self).isListFormat()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isTableCellFormat(self):
		"""
		Returns true if this text format is a TableCellFormat ; otherwise returns false.
		"""
		res = super(QTextFormat,self).isTableCellFormat()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isTableFormat(self):
		"""
		Returns true if this text format is a TableFormat ; otherwise returns false.
		"""
		res = super(QTextFormat,self).isTableFormat()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if the format is valid (i.e
		is not InvalidFormat ); otherwise returns false.
		"""
		res = super(QTextFormat,self).isValid()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def layoutDirection(self):
		"""
		Returns the documents layout direction.
		"""
		res = super(QTextFormat,self).layoutDirection()
		isinstance(res,QtCore.Qt.LayoutDirection)
		return res
	#----------------------------------------------------------------------
	def objectIndex(self):
		"""
		Returns the index of the format object, or -1 if the format object is invalid.
		"""
		res = super(QTextFormat,self).objectIndex()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def objectType(self):
		"""
		Returns the text formats object type.
		"""
		res = super(QTextFormat,self).objectType()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def properties(self):
		"""
		Returns a map with all properties of this text format.
		"""
		res = super(QTextFormat,self).properties()
		return res
	#----------------------------------------------------------------------
	def propertyCount(self):
		"""
		Returns the number of properties stored in the format.
		"""
		res = super(QTextFormat,self).propertyCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def toBlockFormat(self):
		"""
		Returns this format as a block format.
		"""
		res = super(QTextFormat,self).toBlockFormat()
		isinstance(res,QtGui.QTextBlockFormat)
		return res
	#----------------------------------------------------------------------
	def toCharFormat(self):
		"""
		Returns this format as a character format.
		"""
		res = super(QTextFormat,self).toCharFormat()
		isinstance(res,QtGui.QTextCharFormat)
		return res
	#----------------------------------------------------------------------
	def toFrameFormat(self):
		"""
		Returns this format as a frame format.
		"""
		res = super(QTextFormat,self).toFrameFormat()
		isinstance(res,QtGui.QTextFrameFormat)
		return res
	#----------------------------------------------------------------------
	def toImageFormat(self):
		"""
		Returns this format as an image format.
		"""
		res = super(QTextFormat,self).toImageFormat()
		isinstance(res,QtGui.QTextImageFormat)
		return res
	#----------------------------------------------------------------------
	def toListFormat(self):
		"""
		Returns this format as a list format.
		"""
		res = super(QTextFormat,self).toListFormat()
		isinstance(res,QtGui.QTextListFormat)
		return res
	#----------------------------------------------------------------------
	def toTableCellFormat(self):
		"""
		Returns this format as a table cell format.
		"""
		res = super(QTextFormat,self).toTableCellFormat()
		isinstance(res,QtGui.QTextTableCellFormat)
		return res
	#----------------------------------------------------------------------
	def toTableFormat(self):
		"""
		Returns this format as a table format.
		"""
		res = super(QTextFormat,self).toTableFormat()
		isinstance(res,QtGui.QTextTableFormat)
		return res
	#----------------------------------------------------------------------
	def type(self):
		"""
		Returns the type of this format.
		"""
		res = super(QTextFormat,self).type()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def boolProperty(self,propertyId):
		"""
		boolProperty(propertyId)
			propertyId=QtCore.int

		Returns the value of the property specified by propertyId
		If the property isnt of QTextFormat::Bool type, false is returned instead.
		"""
		res = super(QTextFormat,self).boolProperty(propertyId)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def brushProperty(self,propertyId):
		"""
		brushProperty(propertyId)
			propertyId=QtCore.int

		Returns the value of the property given by propertyId ; if the property isnt of QVariant.Brush type, Qt.NoBrush is returned instead.
		"""
		res = super(QTextFormat,self).brushProperty(propertyId)
		isinstance(res,QtGui.QBrush)
		return res
	#----------------------------------------------------------------------
	def clearProperty(self,propertyId):
		"""
		clearProperty(propertyId)
			propertyId=QtCore.int

		Clears the value of the property given by propertyId
		"""
		res = super(QTextFormat,self).clearProperty(propertyId)
		return res
	#----------------------------------------------------------------------
	def colorProperty(self,propertyId):
		"""
		colorProperty(propertyId)
			propertyId=QtCore.int

		Returns the value of the property given by propertyId ; if the property isnt of QVariant.Color type, an invalid color is returned instead.
		"""
		res = super(QTextFormat,self).colorProperty(propertyId)
		isinstance(res,QtGui.QColor)
		return res
	#----------------------------------------------------------------------
	def doubleProperty(self,propertyId):
		"""
		doubleProperty(propertyId)
			propertyId=QtCore.int

		Returns the value of the property specified by propertyId
		If the property isnt of QVariant.Double or QMetaType.Float type, 0 is returned instead.
		"""
		res = super(QTextFormat,self).doubleProperty(propertyId)
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def hasProperty(self,propertyId):
		"""
		hasProperty(propertyId)
			propertyId=QtCore.int

		Returns true if the text format has a property with the given propertyId ; otherwise returns false.
		"""
		res = super(QTextFormat,self).hasProperty(propertyId)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def intProperty(self,propertyId):
		"""
		intProperty(propertyId)
			propertyId=QtCore.int

		Returns the value of the property specified by propertyId
		If the property is not of QTextFormat::Integer type, 0 is returned instead.
		"""
		res = super(QTextFormat,self).intProperty(propertyId)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def lengthProperty(self,propertyId):
		"""
		lengthProperty(propertyId)
			propertyId=QtCore.int

		Returns the value of the property given by propertyId .
		"""
		res = super(QTextFormat,self).lengthProperty(propertyId)
		isinstance(res,QtGui.QTextLength)
		return res
	#----------------------------------------------------------------------
	def lengthVectorProperty(self,propertyId):
		"""
		lengthVectorProperty(propertyId)
			propertyId=QtCore.int

		Returns the value of the property given by propertyId
		If the property isnt of QTextFormat::LengthVector type, an empty length vector is returned instead.
		"""
		res = super(QTextFormat,self).lengthVectorProperty(propertyId)
		return res
	#----------------------------------------------------------------------
	def merge(self,other):
		"""
		merge(other)
			other=QtGui.QTextFormat

		Merges the other format with this format; where there are conflicts the other format takes precedence.
		"""
		res = super(QTextFormat,self).merge(other)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,rhs):
		"""
		__ne__(rhs)
			rhs=QtGui.QTextFormat

		Returns true if this text format is different from the other text format.
		"""
		res = super(QTextFormat,self).__ne__(rhs)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,rhs):
		"""
		__eq__(rhs)
			rhs=QtGui.QTextFormat

		Returns true if this text format is the same as the other text format.
		"""
		res = super(QTextFormat,self).__eq__(rhs)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def penProperty(self,propertyId):
		"""
		penProperty(propertyId)
			propertyId=QtCore.int

		Returns the value of the property given by propertyId ; if the property isnt of QVariant.Pen type, Qt.NoPen is returned instead.
		"""
		res = super(QTextFormat,self).penProperty(propertyId)
		isinstance(res,QtGui.QPen)
		return res
	#----------------------------------------------------------------------
	def property(self,propertyId):
		"""
		property(propertyId)
			propertyId=QtCore.int

		Returns the property specified by the given propertyId .
		"""
		res = super(QTextFormat,self).property(propertyId)
		return res
	#----------------------------------------------------------------------
	def setBackground(self,brush):
		"""
		setBackground(brush)
			brush=QtGui.QBrush

		Sets the brush use to paint the documents background to the brush specified.
		"""
		res = super(QTextFormat,self).setBackground(brush)
		return res
	#----------------------------------------------------------------------
	def setForeground(self,brush):
		"""
		setForeground(brush)
			brush=QtGui.QBrush

		Sets the foreground brush to the specified brush
		The foreground brush is mostly used to render text.
		"""
		res = super(QTextFormat,self).setForeground(brush)
		return res
	#----------------------------------------------------------------------
	def setLayoutDirection(self,direction):
		"""
		setLayoutDirection(direction)
			direction=QtCore.Qt.LayoutDirection


		"""
		res = super(QTextFormat,self).setLayoutDirection(direction)
		return res
	#----------------------------------------------------------------------
	def setObjectIndex(self,object):
		"""
		setObjectIndex(object)
			object=QtCore.int

		Sets the format objects object index .
		"""
		res = super(QTextFormat,self).setObjectIndex(object)
		return res
	#----------------------------------------------------------------------
	def setObjectType(self,type):
		"""
		setObjectType(type)
			type=QtCore.int

		Sets the text formats object type to type .
		"""
		res = super(QTextFormat,self).setObjectType(type)
		return res
	#----------------------------------------------------------------------
	def setProperty(self,*args,**kwargs):
		"""
		setProperty(propertyId,value)
			propertyId=QtCore.int
			value=object

		setProperty(propertyId,lengths)
			propertyId=QtCore.int
			lengths=unKnown

		Sets the property specified by the propertyId to the given value .
		"""
		res = super(QTextFormat,self).setProperty(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def stringProperty(self,propertyId):
		"""
		stringProperty(propertyId)
			propertyId=QtCore.int

		Returns the value of the property given by propertyId ; if the property isnt of QVariant.String type, an empty string is returned instead.
		"""
		res = super(QTextFormat,self).stringProperty(propertyId)
		return res

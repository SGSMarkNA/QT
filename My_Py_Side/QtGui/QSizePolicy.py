from PySide import QtGui, QtCore

class QSizePolicy(QtGui.QSizePolicy):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSizePolicy,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def controlType(self):
		"""
		Returns the control type associated with the widget for which this size policy applies.
		"""
		res = super(QSizePolicy,self).controlType()
		isinstance(res,QtGui.QSizePolicy.ControlType)
		return res
	#----------------------------------------------------------------------
	def expandingDirections(self):
		"""
		Returns whether a widget can make use of more space than the QWidget.sizeHint() function indicates.
		A value of Qt.Horizontal or Qt.Vertical means that the widget can grow horizontally or vertically (i.e., the horizontal or vertical policy is Expanding or MinimumExpanding ), whereas Qt.Horizontal | Qt.Vertical means that it can grow in both dimensions.
		"""
		res = super(QSizePolicy,self).expandingDirections()
		isinstance(res,QtCore.Qt.Orientations)
		return res
	#----------------------------------------------------------------------
	def hasHeightForWidth(self):
		"""
		Returns true if the widgets preferred height depends on its width; otherwise returns false.
		"""
		res = super(QSizePolicy,self).hasHeightForWidth()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def horizontalPolicy(self):
		"""
		Returns the horizontal component of the size policy.
		"""
		res = super(QSizePolicy,self).horizontalPolicy()
		isinstance(res,QtGui.QSizePolicy.Policy)
		return res
	#----------------------------------------------------------------------
	def horizontalStretch(self):
		"""
		Returns the horizontal stretch factor of the size policy.
		"""
		res = super(QSizePolicy,self).horizontalStretch()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def transpose(self):
		"""
		Swaps the horizontal and vertical policies and stretches.
		"""
		res = super(QSizePolicy,self).transpose()
		return res
	#----------------------------------------------------------------------
	def verticalPolicy(self):
		"""
		Returns the vertical component of the size policy.
		"""
		res = super(QSizePolicy,self).verticalPolicy()
		isinstance(res,QtGui.QSizePolicy.Policy)
		return res
	#----------------------------------------------------------------------
	def verticalStretch(self):
		"""
		Returns the vertical stretch factor of the size policy.
		"""
		res = super(QSizePolicy,self).verticalStretch()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,s):
		"""
		__ne__(s)
			s=QtGui.QSizePolicy

		Returns true if this policy is different from other ; otherwise returns false.
		"""
		res = super(QSizePolicy,self).__ne__(s)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,s):
		"""
		__eq__(s)
			s=QtGui.QSizePolicy

		Returns true if this policy is equal to other ; otherwise returns false.
		"""
		res = super(QSizePolicy,self).__eq__(s)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setControlType(self,type):
		"""
		setControlType(type)
			type=QtGui.QSizePolicy.ControlType

		Sets the control type associated with the widget for which this size policy applies to type .
		The control type specifies the type of the widget for which this size policy applies
		It is used by some styles, notably QMacStyle , to insert proper spacing between widgets
		For example, the Mac OS X Aqua guidelines specify that push buttons should be separated by 12 pixels, whereas vertically stacked radio buttons only require 6 pixels.
		"""
		res = super(QSizePolicy,self).setControlType(type)
		return res
	#----------------------------------------------------------------------
	def setHeightForWidth(self,b):
		"""
		setHeightForWidth(b)
			b=QtCore.bool

		Sets the flag determining whether the widgets preferred height depends on its width, to dependent .
		"""
		res = super(QSizePolicy,self).setHeightForWidth(b)
		return res
	#----------------------------------------------------------------------
	def setHorizontalPolicy(self,d):
		"""
		setHorizontalPolicy(d)
			d=QtGui.QSizePolicy.Policy

		Sets the horizontal component to the given policy .
		"""
		res = super(QSizePolicy,self).setHorizontalPolicy(d)
		return res
	#----------------------------------------------------------------------
	def setHorizontalStretch(self,stretchFactor):
		"""
		setHorizontalStretch(stretchFactor)
			stretchFactor=QtCore.uchar

		Sets the horizontal stretch factor of the size policy to the given stretchFactor .
		"""
		res = super(QSizePolicy,self).setHorizontalStretch(stretchFactor)
		return res
	#----------------------------------------------------------------------
	def setVerticalPolicy(self,d):
		"""
		setVerticalPolicy(d)
			d=QtGui.QSizePolicy.Policy

		Sets the vertical component to the given policy .
		"""
		res = super(QSizePolicy,self).setVerticalPolicy(d)
		return res
	#----------------------------------------------------------------------
	def setVerticalStretch(self,stretchFactor):
		"""
		setVerticalStretch(stretchFactor)
			stretchFactor=QtCore.uchar

		Sets the vertical stretch factor of the size policy to the given stretchFactor .
		"""
		res = super(QSizePolicy,self).setVerticalStretch(stretchFactor)
		return res

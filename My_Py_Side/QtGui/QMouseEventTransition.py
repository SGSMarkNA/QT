from PySide import QtGui, QtCore

class QMouseEventTransition(QtGui.QMouseEventTransition):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QMouseEventTransition,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def button(self):
		"""
		This property holds the button that this mouse event transition is associated with.
		"""
		res = super(QMouseEventTransition,self).button()
		isinstance(res,QtCore.Qt.MouseButton)
		return res
	#----------------------------------------------------------------------
	def hitTestPath(self):
		"""
		Returns the hit test path for this mouse event transition.
		"""
		res = super(QMouseEventTransition,self).hitTestPath()
		isinstance(res,QtGui.QPainterPath)
		return res
	#----------------------------------------------------------------------
	def modifierMask(self):
		"""
		This property holds the keyboard modifier mask that this mouse event transition checks for.
		"""
		res = super(QMouseEventTransition,self).modifierMask()
		isinstance(res,QtCore.Qt.KeyboardModifiers)
		return res
	#----------------------------------------------------------------------
	def setButton(self,button):
		"""
		setButton(button)
			button=QtCore.Qt.MouseButton

		This property holds the button that this mouse event transition is associated with.
		"""
		res = super(QMouseEventTransition,self).setButton(button)
		return res
	#----------------------------------------------------------------------
	def setHitTestPath(self,path):
		"""
		setHitTestPath(path)
			path=QtGui.QPainterPath

		Sets the hit test path for this mouse event transition to path
		If a valid path has been set, the transition will only trigger if the mouse event position ( QMouseEvent.pos() ) is inside the path.
		"""
		res = super(QMouseEventTransition,self).setHitTestPath(path)
		return res
	#----------------------------------------------------------------------
	def setModifierMask(self,modifiers):
		"""
		setModifierMask(modifiers)
			modifiers=QtCore.Qt.KeyboardModifiers

		This property holds the keyboard modifier mask that this mouse event transition checks for.
		"""
		res = super(QMouseEventTransition,self).setModifierMask(modifiers)
		return res

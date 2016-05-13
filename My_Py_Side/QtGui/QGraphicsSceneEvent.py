from PySide import QtGui, QtCore

class QGraphicsSceneEvent(QtGui.QGraphicsSceneEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsSceneEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def widget(self):
		"""
		Returns the widget where the event originated, or 0 if the event originates from another application.
		"""
		res = super(QGraphicsSceneEvent,self).widget()
		isinstance(res,QtGui.QWidget)
		return res

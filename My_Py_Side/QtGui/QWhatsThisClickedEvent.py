from PySide import QtGui, QtCore

class QWhatsThisClickedEvent(QtGui.QWhatsThisClickedEvent):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QWhatsThisClickedEvent,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def href(self):
		"""
		Returns the URL that was clicked by the user in the Whats This? text.
		"""
		res = super(QWhatsThisClickedEvent,self).href()
		return res

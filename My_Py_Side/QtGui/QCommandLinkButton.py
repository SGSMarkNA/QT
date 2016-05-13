from PySide import QtGui, QtCore

class QCommandLinkButton(QtGui.QCommandLinkButton):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QCommandLinkButton,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def description(self):
		"""
		This property holds A descriptive label to complement the button text.
		Setting this property will set a descriptive text on the button, complementing the text label
		This will usually be displayed in a smaller font than the primary text.
		"""
		res = super(QCommandLinkButton,self).description()
		return res
	#----------------------------------------------------------------------
	def setDescription(self,description):
		"""
		setDescription(description)
			description=unicode

		This property holds A descriptive label to complement the button text.
		Setting this property will set a descriptive text on the button, complementing the text label
		This will usually be displayed in a smaller font than the primary text.
		"""
		res = super(QCommandLinkButton,self).setDescription(description)
		return res

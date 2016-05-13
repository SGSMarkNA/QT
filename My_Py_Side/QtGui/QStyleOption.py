from PySide import QtGui, QtCore

class QStyleOption(QtGui.QStyleOption):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QStyleOption,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def initFrom(self,w):
		"""
		initFrom(w)
			w=QtGui.QWidget

		Initializes the state , direction , rect , palette , and fontMetrics member variables based on the specified widget .
		This is a convenience function; the member variables can also be initialized manually.
		"""
		res = super(QStyleOption,self).initFrom(w)
		return res

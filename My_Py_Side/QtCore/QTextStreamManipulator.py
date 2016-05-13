from PySide import QtGui, QtCore

class QTextStreamManipulator(QtCore.QTextStreamManipulator):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QTextStreamManipulator,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def exec_(self,s):
		"""
		exec_(s)
			s=QtCore.QTextStream


		"""
		res = super(QTextStreamManipulator,self).exec_(s)
		return res

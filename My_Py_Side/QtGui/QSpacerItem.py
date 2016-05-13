from PySide import QtGui, QtCore

class QSpacerItem(QtGui.QSpacerItem):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSpacerItem,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def changeSize(self,w,h,hData=None,vData=None):
		"""
		changeSize(w,h,hData=None,vData=None)
			w=QtCore.int
			h=QtCore.int
			hData=QtGui.QSizePolicy.Policy
			vData=QtGui.QSizePolicy.Policy


		"""
		res = super(QSpacerItem,self).changeSize(w,h,hData,vData)
		return res

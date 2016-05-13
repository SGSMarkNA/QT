from PySide import QtGui, QtCore

class QDrag(QtGui.QDrag):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QDrag,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def hotSpot(self):
		"""
		Returns the position of the hot spot relative to the top-left corner of the cursor.
		"""
		res = super(QDrag,self).hotSpot()
		isinstance(res,QtCore.QPoint)
		return res
	#----------------------------------------------------------------------
	def mimeData(self):
		"""
		Returns the MIME data that is encapsulated by the drag object.
		"""
		res = super(QDrag,self).mimeData()
		isinstance(res,QtCore.QMimeData)
		return res
	#----------------------------------------------------------------------
	def pixmap(self):
		"""
		Returns the pixmap used to represent the data in a drag and drop operation.
		"""
		res = super(QDrag,self).pixmap()
		isinstance(res,QtGui.QPixmap)
		return res
	#----------------------------------------------------------------------
	def source(self):
		"""
		Returns the source of the drag object
		This is the widget where the drag and drop operation originated.
		"""
		res = super(QDrag,self).source()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def target(self):
		"""
		Returns the target of the drag and drop operation
		This is the widget where the drag object was dropped.
		"""
		res = super(QDrag,self).target()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def exec_(self,*args,**kwargs):
		"""
		exec_(supportedActions=None)
			supportedActions=QtCore.Qt.DropActions

		exec_(supportedActions,defaultAction)
			supportedActions=QtCore.Qt.DropActions
			defaultAction=QtCore.Qt.DropAction


		"""
		res = super(QDrag,self).exec_(*args,**kwargs)
		isinstance(res,QtCore.Qt.DropAction)
		return res
	#----------------------------------------------------------------------
	def setDragCursor(self,cursor,action):
		"""
		setDragCursor(cursor,action)
			cursor=QtGui.QPixmap
			action=QtCore.Qt.DropAction


		"""
		res = super(QDrag,self).setDragCursor(cursor,action)
		return res
	#----------------------------------------------------------------------
	def setHotSpot(self,hotspot):
		"""
		setHotSpot(hotspot)
			hotspot=QtCore.QPoint

		Sets the position of the hot spot relative to the top-left corner of the pixmap used to the point specified by hotspot .
		"""
		res = super(QDrag,self).setHotSpot(hotspot)
		return res
	#----------------------------------------------------------------------
	def setMimeData(self,data):
		"""
		setMimeData(data)
			data=QtCore.QMimeData

		Sets the data to be sent to the given MIME data
		Ownership of the data is transferred to the PySide.QtGui.QDrag object.
		"""
		res = super(QDrag,self).setMimeData(data)
		return res
	#----------------------------------------------------------------------
	def setPixmap(self,arg__1):
		"""
		setPixmap(arg__1)
			arg__1=QtGui.QPixmap

		Sets pixmap as the pixmap used to represent the data in a drag and drop operation
		You can only set a pixmap before the drag is started.
		"""
		res = super(QDrag,self).setPixmap(arg__1)
		return res
	#----------------------------------------------------------------------
	def start(self,supportedActions=None):
		"""
		start(supportedActions=None)
			supportedActions=QtCore.Qt.DropActions


		"""
		res = super(QDrag,self).start(supportedActions)
		isinstance(res,QtCore.Qt.DropAction)
		return res

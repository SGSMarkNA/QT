from PySide import QtGui, QtCore

class QSplashScreen(QtGui.QSplashScreen):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSplashScreen,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def pixmap(self):
		"""
		Returns the pixmap that is used in the splash screen
		The image does not have any of the text drawn by PySide.QtGui.QSplashScreen.showMessage() calls.
		"""
		res = super(QSplashScreen,self).pixmap()
		isinstance(res,QtGui.QPixmap)
		return res
	#----------------------------------------------------------------------
	def drawContents(self,painter):
		"""
		drawContents(painter)
			painter=QtGui.QPainter

		Draw the contents of the splash screen using painter painter
		The default implementation draws the message passed by PySide.QtGui.QSplashScreen.showMessage()
		Reimplement this function if you want to do your own drawing on the splash screen.
		"""
		res = super(QSplashScreen,self).drawContents(painter)
		return res
	#----------------------------------------------------------------------
	def finish(self,w):
		"""
		finish(w)
			w=QtGui.QWidget

		Makes the splash screen wait until the widget mainWin is displayed before calling PySide.QtGui.QWidget.close() on itself.
		"""
		res = super(QSplashScreen,self).finish(w)
		return res
	#----------------------------------------------------------------------
	def setPixmap(self,pixmap):
		"""
		setPixmap(pixmap)
			pixmap=QtGui.QPixmap

		Sets the pixmap that will be used as the splash screens image to pixmap .
		"""
		res = super(QSplashScreen,self).setPixmap(pixmap)
		return res

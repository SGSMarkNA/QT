from PySide import QtGui, QtCore

class QSystemTrayIcon(QtGui.QSystemTrayIcon):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QSystemTrayIcon,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def contextMenu(self):
		"""
		Returns the current context menu for the system tray entry.
		"""
		res = super(QSystemTrayIcon,self).contextMenu()
		isinstance(res,QtGui.QMenu)
		return res
	#----------------------------------------------------------------------
	def geometry(self):
		"""
		Returns the geometry of the system tray icon in screen coordinates.
		"""
		res = super(QSystemTrayIcon,self).geometry()
		isinstance(res,QtCore.QRect)
		return res
	#----------------------------------------------------------------------
	def icon(self):
		"""
		This property holds the system tray icon.
		On Windows, the system tray icon size is 16x16; on X11, the preferred size is 22x22
		The icon will be scaled to the appropriate size as necessary.
		"""
		res = super(QSystemTrayIcon,self).icon()
		isinstance(res,QtGui.QIcon)
		return res
	#----------------------------------------------------------------------
	def isVisible(self):
		"""
		This property holds whether the system tray entry is visible.
		Setting this property to true or calling PySide.QtGui.QSystemTrayIcon.show() makes the system tray icon visible; setting this property to false or calling PySide.QtGui.QSystemTrayIcon.hide() hides it.
		"""
		res = super(QSystemTrayIcon,self).isVisible()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def messageClicked(self):
		"""

		"""
		res = super(QSystemTrayIcon,self).messageClicked()
		return res
	#----------------------------------------------------------------------
	def toolTip(self):
		"""
		This property holds the tooltip for the system tray entry.
		On some systems, the tooltips length is limited
		The tooltip will be truncated if necessary.
		"""
		res = super(QSystemTrayIcon,self).toolTip()
		return res
	#----------------------------------------------------------------------
	def setContextMenu(self,menu):
		"""
		setContextMenu(menu)
			menu=QtGui.QMenu

		Sets the specified menu to be the context menu for the system tray icon.
		The menu will pop up when the user requests the context menu for the system tray icon by clicking the mouse button.
		On Mac OS X, this is currenly converted to a NSMenu, so the aboutToHide() signal is not emitted.
		"""
		res = super(QSystemTrayIcon,self).setContextMenu(menu)
		return res
	#----------------------------------------------------------------------
	def setIcon(self,icon):
		"""
		setIcon(icon)
			icon=QtGui.QIcon

		This property holds the system tray icon.
		On Windows, the system tray icon size is 16x16; on X11, the preferred size is 22x22
		The icon will be scaled to the appropriate size as necessary.
		"""
		res = super(QSystemTrayIcon,self).setIcon(icon)
		return res
	#----------------------------------------------------------------------
	def setToolTip(self,tip):
		"""
		setToolTip(tip)
			tip=unicode

		This property holds the tooltip for the system tray entry.
		On some systems, the tooltips length is limited
		The tooltip will be truncated if necessary.
		"""
		res = super(QSystemTrayIcon,self).setToolTip(tip)
		return res
	#----------------------------------------------------------------------
	def showMessage(self,title,msg,icon=None,msecs=None):
		"""
		showMessage(title,msg,icon=None,msecs=None)
			title=unicode
			msg=unicode
			icon=QtGui.QSystemTrayIcon.MessageIcon
			msecs=QtCore.int

		Shows a balloon message for the entry with the given title , message and icon for the time specified in millisecondsTimeoutHint
		title and message must be plain text strings.
		Message can be clicked by the user; the PySide.QtGui.QSystemTrayIcon.messageClicked() signal will emitted when this occurs.
		Note that display of messages are dependent on the system configuration and user preferences, and that messages may not appear at all
		Hence, it should not be relied upon as the sole means for providing critical information.
		On Windows, the millisecondsTimeoutHint is usually ignored by the system when the application has focus.
		On Mac OS X, the Growl notification system must be installed for this function to display messages.
		"""
		res = super(QSystemTrayIcon,self).showMessage(title,msg,icon,msecs)
		return res

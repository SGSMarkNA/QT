from PySide import QtGui, QtCore

class QGraphicsLayoutItem(QtGui.QGraphicsLayoutItem):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGraphicsLayoutItem,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def contentsRect(self):
		"""
		Returns the contents rect in local coordinates.
		The contents rect defines the subrectangle used by an associated layout when arranging subitems
		This function is a convenience function that adjusts the items PySide.QtGui.QGraphicsLayoutItem.geometry() by its contents margins
		Note that PySide.QtGui.QGraphicsLayoutItem.getContentsMargins() is a virtual function that you can reimplement to return the items contents margins.
		"""
		res = super(QGraphicsLayoutItem,self).contentsRect()
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def geometry(self):
		"""
		Returns the items geometry (e.g., position and size) as a PySide.QtCore.QRectF
		This function is equivalent to PySide.QtCore.QRectF (pos(), size() ).
		"""
		res = super(QGraphicsLayoutItem,self).geometry()
		isinstance(res,QtCore.QRectF)
		return res
	#----------------------------------------------------------------------
	def getContentsMargins(self):
		"""
		This virtual function provides the left , top , right and bottom contents margins for this PySide.QtGui.QGraphicsLayoutItem
		The default implementation assumes all contents margins are 0
		The parameters point to values stored in qreals
		If any of the pointers is 0, that value will not be updated.
		"""
		res = super(QGraphicsLayoutItem,self).getContentsMargins()
		return res
	#----------------------------------------------------------------------
	def graphicsItem(self):
		"""
		Returns the PySide.QtGui.QGraphicsItem that this layout item represents
		For PySide.QtGui.QGraphicsWidget it will return itself
		For custom items it can return an aggregated value.
		"""
		res = super(QGraphicsLayoutItem,self).graphicsItem()
		isinstance(res,QtGui.QGraphicsItem)
		return res
	#----------------------------------------------------------------------
	def isLayout(self):
		"""
		Returns true if this PySide.QtGui.QGraphicsLayoutItem is a layout (e.g., is inherited by an object that arranges other PySide.QtGui.QGraphicsLayoutItem objects); otherwise returns false.
		"""
		res = super(QGraphicsLayoutItem,self).isLayout()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def maximumHeight(self):
		"""
		Returns the maximum height.
		"""
		res = super(QGraphicsLayoutItem,self).maximumHeight()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def maximumSize(self):
		"""
		Returns the maximum size.
		"""
		res = super(QGraphicsLayoutItem,self).maximumSize()
		isinstance(res,QtCore.QSizeF)
		return res
	#----------------------------------------------------------------------
	def maximumWidth(self):
		"""
		Returns the maximum width.
		"""
		res = super(QGraphicsLayoutItem,self).maximumWidth()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def minimumHeight(self):
		"""
		Returns the minimum height.
		"""
		res = super(QGraphicsLayoutItem,self).minimumHeight()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def minimumSize(self):
		"""
		Returns the minimum size.
		"""
		res = super(QGraphicsLayoutItem,self).minimumSize()
		isinstance(res,QtCore.QSizeF)
		return res
	#----------------------------------------------------------------------
	def minimumWidth(self):
		"""
		Returns the minimum width.
		"""
		res = super(QGraphicsLayoutItem,self).minimumWidth()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def ownedByLayout(self):
		"""
		Returns whether a layout should delete this item in its destructor
		If its true, then the layout will delete it
		If its false, then it is assumed that another object has the ownership of it, and the layout wont delete this item.
		If the item inherits both PySide.QtGui.QGraphicsItem and PySide.QtGui.QGraphicsLayoutItem (such as PySide.QtGui.QGraphicsWidget does) the item is really part of two ownership hierarchies
		This property informs what the layout should do with its child items when it is destructed
		In the case of PySide.QtGui.QGraphicsWidget , it is preferred that when the layout is deleted it wont delete its children (since they are also part of the graphics item hierarchy).
		By default this value is initialized to false in PySide.QtGui.QGraphicsLayoutItem , but it is overridden by PySide.QtGui.QGraphicsLayout to return true
		This is because PySide.QtGui.QGraphicsLayout is not normally part of the PySide.QtGui.QGraphicsItem hierarchy, so the parent layout should delete it
		Subclasses might override this default behaviour by calling setOwnedByLayout(true).
		"""
		res = super(QGraphicsLayoutItem,self).ownedByLayout()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def parentLayoutItem(self):
		"""
		Returns the parent of this PySide.QtGui.QGraphicsLayoutItem , or 0 if there is no parent, or if the parent does not inherit from PySide.QtGui.QGraphicsLayoutItem ( PySide.QtGui.QGraphicsLayoutItem is often used through multiple inheritance with PySide.QtCore.QObject -derived classes).
		"""
		res = super(QGraphicsLayoutItem,self).parentLayoutItem()
		isinstance(res,QtGui.QGraphicsLayoutItem)
		return res
	#----------------------------------------------------------------------
	def preferredHeight(self):
		"""
		Returns the preferred height.
		"""
		res = super(QGraphicsLayoutItem,self).preferredHeight()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def preferredSize(self):
		"""
		Returns the preferred size.
		"""
		res = super(QGraphicsLayoutItem,self).preferredSize()
		isinstance(res,QtCore.QSizeF)
		return res
	#----------------------------------------------------------------------
	def preferredWidth(self):
		"""
		Returns the preferred width.
		"""
		res = super(QGraphicsLayoutItem,self).preferredWidth()
		isinstance(res,QtCore.qreal)
		return res
	#----------------------------------------------------------------------
	def sizePolicy(self):
		"""
		Returns the current size policy.
		"""
		res = super(QGraphicsLayoutItem,self).sizePolicy()
		isinstance(res,QtGui.QSizePolicy)
		return res
	#----------------------------------------------------------------------
	def updateGeometry(self):
		"""
		This virtual function discards any cached size hint information
		You should always call this function if you change the return value of the PySide.QtGui.QGraphicsLayoutItem.sizeHint() function
		Subclasses must always call the base implementation when reimplementing this function.
		"""
		res = super(QGraphicsLayoutItem,self).updateGeometry()
		return res
	#----------------------------------------------------------------------
	def effectiveSizeHint(self,which,constraint=None):
		"""
		effectiveSizeHint(which,constraint=None)
			which=QtCore.Qt.SizeHint
			constraint=QtCore.QSizeF


		"""
		res = super(QGraphicsLayoutItem,self).effectiveSizeHint(which,constraint)
		isinstance(res,QtCore.QSizeF)
		return res
	#----------------------------------------------------------------------
	def effectiveSizeHints(self,constraint):
		"""
		effectiveSizeHints(constraint)
			constraint=QtCore.QSizeF


		"""
		res = super(QGraphicsLayoutItem,self).effectiveSizeHints(constraint)
		isinstance(res,QtCore.QSizeF)
		return res
	#----------------------------------------------------------------------
	def setGeometry(self,rect):
		"""
		setGeometry(rect)
			rect=QtCore.QRectF

		This virtual function sets the geometry of the PySide.QtGui.QGraphicsLayoutItem to rect , which is in parent coordinates (e.g., the top-left corner of rect is equivalent to the items position in parent coordinates).
		You must reimplement this function in a subclass of PySide.QtGui.QGraphicsLayoutItem to receive geometry updates
		The layout will call this function when it does a rearrangement.
		If rect is outside of the bounds of minimumSize and maximumSize, it will be adjusted to its closest size so that it is within the legal bounds.
		"""
		res = super(QGraphicsLayoutItem,self).setGeometry(rect)
		return res
	#----------------------------------------------------------------------
	def setGraphicsItem(self,item):
		"""
		setGraphicsItem(item)
			item=QtGui.QGraphicsItem

		If the PySide.QtGui.QGraphicsLayoutItem represents a PySide.QtGui.QGraphicsItem , and it wants to take advantage of the automatic reparenting capabilities of PySide.QtGui.QGraphicsLayout it should set this value
		Note that if you delete item and not delete the layout item, you are responsible of calling setGraphicsItem(0) in order to avoid having a dangling pointer.
		"""
		res = super(QGraphicsLayoutItem,self).setGraphicsItem(item)
		return res
	#----------------------------------------------------------------------
	def setMaximumHeight(self,height):
		"""
		setMaximumHeight(height)
			height=QtCore.qreal

		Sets the maximum height to height .
		"""
		res = super(QGraphicsLayoutItem,self).setMaximumHeight(height)
		return res
	#----------------------------------------------------------------------
	def setMaximumSize(self,*args,**kwargs):
		"""
		setMaximumSize(w,h)
			w=QtCore.qreal
			h=QtCore.qreal

		setMaximumSize(size)
			size=QtCore.QSizeF

		This convenience function is equivalent to calling setMaximumSize( PySide.QtCore.QSizeF (w , h )).
		"""
		res = super(QGraphicsLayoutItem,self).setMaximumSize(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setMaximumWidth(self,width):
		"""
		setMaximumWidth(width)
			width=QtCore.qreal

		Sets the maximum width to width .
		"""
		res = super(QGraphicsLayoutItem,self).setMaximumWidth(width)
		return res
	#----------------------------------------------------------------------
	def setMinimumHeight(self,height):
		"""
		setMinimumHeight(height)
			height=QtCore.qreal

		Sets the minimum height to height .
		"""
		res = super(QGraphicsLayoutItem,self).setMinimumHeight(height)
		return res
	#----------------------------------------------------------------------
	def setMinimumSize(self,*args,**kwargs):
		"""
		setMinimumSize(size)
			size=QtCore.QSizeF

		setMinimumSize(w,h)
			w=QtCore.qreal
			h=QtCore.qreal

		Sets the minimum size to size
		This property overrides PySide.QtGui.QGraphicsLayoutItem.sizeHint() for Qt.MinimumSize and ensures that PySide.QtGui.QGraphicsLayoutItem.effectiveSizeHint() will never return a size smaller than size
		In order to unset the minimum size, use an invalid size.
		"""
		res = super(QGraphicsLayoutItem,self).setMinimumSize(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setMinimumWidth(self,width):
		"""
		setMinimumWidth(width)
			width=QtCore.qreal

		Sets the minimum width to width .
		"""
		res = super(QGraphicsLayoutItem,self).setMinimumWidth(width)
		return res
	#----------------------------------------------------------------------
	def setOwnedByLayout(self,ownedByLayout):
		"""
		setOwnedByLayout(ownedByLayout)
			ownedByLayout=QtCore.bool

		Sets whether a layout should delete this item in its destructor or not
		ownership must be true to in order for the layout to delete it.
		"""
		res = super(QGraphicsLayoutItem,self).setOwnedByLayout(ownedByLayout)
		return res
	#----------------------------------------------------------------------
	def setParentLayoutItem(self,parent):
		"""
		setParentLayoutItem(parent)
			parent=QtGui.QGraphicsLayoutItem

		Sets the parent of this PySide.QtGui.QGraphicsLayoutItem to parent .
		"""
		res = super(QGraphicsLayoutItem,self).setParentLayoutItem(parent)
		return res
	#----------------------------------------------------------------------
	def setPreferredHeight(self,height):
		"""
		setPreferredHeight(height)
			height=QtCore.qreal

		Sets the preferred height to height .
		"""
		res = super(QGraphicsLayoutItem,self).setPreferredHeight(height)
		return res
	#----------------------------------------------------------------------
	def setPreferredSize(self,*args,**kwargs):
		"""
		setPreferredSize(w,h)
			w=QtCore.qreal
			h=QtCore.qreal

		setPreferredSize(size)
			size=QtCore.QSizeF

		This convenience function is equivalent to calling setPreferredSize( PySide.QtCore.QSizeF (w , h )).
		"""
		res = super(QGraphicsLayoutItem,self).setPreferredSize(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setPreferredWidth(self,width):
		"""
		setPreferredWidth(width)
			width=QtCore.qreal

		Sets the preferred width to width .
		"""
		res = super(QGraphicsLayoutItem,self).setPreferredWidth(width)
		return res
	#----------------------------------------------------------------------
	def setSizePolicy(self,*args,**kwargs):
		"""
		setSizePolicy(policy)
			policy=QtGui.QSizePolicy

		setSizePolicy(hPolicy,vPolicy,controlType=None)
			hPolicy=QtGui.QSizePolicy.Policy
			vPolicy=QtGui.QSizePolicy.Policy
			controlType=QtGui.QSizePolicy.ControlType

		Sets the size policy to policy
		The size policy describes how the item should grow horizontally and vertically when arranged in a layout.
		PySide.QtGui.QGraphicsLayoutItem s default size policy is ( QSizePolicy.Fixed , QSizePolicy.Fixed , QSizePolicy.DefaultType ), but it is common for subclasses to change the default
		For example, PySide.QtGui.QGraphicsWidget defaults to ( QSizePolicy.Preferred , QSizePolicy.Preferred , QSizePolicy.DefaultType ).
		"""
		res = super(QGraphicsLayoutItem,self).setSizePolicy(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def sizeHint(self,which,constraint=None):
		"""
		sizeHint(which,constraint=None)
			which=QtCore.Qt.SizeHint
			constraint=QtCore.QSizeF


		"""
		res = super(QGraphicsLayoutItem,self).sizeHint(which,constraint)
		isinstance(res,QtCore.QSizeF)
		return res

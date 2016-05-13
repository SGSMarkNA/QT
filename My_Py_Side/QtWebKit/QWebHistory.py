from PySide import QtGui, QtCore

class QWebHistory(QtWebKit.QWebHistory):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QWebHistory,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def back(self):
		"""
		Set the current item to be the previous item in the history and goes to the corresponding page; i.e., goes back one history item.
		"""
		res = super(QWebHistory,self).back()
		return res
	#----------------------------------------------------------------------
	def backItem(self):
		"""
		Returns the item before the current item in the history.
		"""
		res = super(QWebHistory,self).backItem()
		isinstance(res,QtWebKit.QWebHistoryItem)
		return res
	#----------------------------------------------------------------------
	def canGoBack(self):
		"""
		Returns true if there is an item preceding the current item in the history; otherwise returns false.
		"""
		res = super(QWebHistory,self).canGoBack()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def canGoForward(self):
		"""
		Returns true if we have an item to go forward to; otherwise returns false.
		"""
		res = super(QWebHistory,self).canGoForward()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Clears the history.
		"""
		res = super(QWebHistory,self).clear()
		return res
	#----------------------------------------------------------------------
	def count(self):
		"""
		Returns the total number of items in the history.
		"""
		res = super(QWebHistory,self).count()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def currentItem(self):
		"""
		Returns the current item in the history.
		"""
		res = super(QWebHistory,self).currentItem()
		isinstance(res,QtWebKit.QWebHistoryItem)
		return res
	#----------------------------------------------------------------------
	def currentItemIndex(self):
		"""
		Returns the index of the current item in history.
		"""
		res = super(QWebHistory,self).currentItemIndex()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def forward(self):
		"""
		Sets the current item to be the next item in the history and goes to the corresponding page; i.e., goes forward one history item.
		"""
		res = super(QWebHistory,self).forward()
		return res
	#----------------------------------------------------------------------
	def forwardItem(self):
		"""
		Returns the item after the current item in the history.
		"""
		res = super(QWebHistory,self).forwardItem()
		isinstance(res,QtWebKit.QWebHistoryItem)
		return res
	#----------------------------------------------------------------------
	def items(self):
		"""
		Returns a list of all items currently in the history.
		"""
		res = super(QWebHistory,self).items()
		return res
	#----------------------------------------------------------------------
	def maximumItemCount(self):
		"""
		Returns the maximum number of items in the history.
		"""
		res = super(QWebHistory,self).maximumItemCount()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def backItems(self,maxItems):
		"""
		backItems(maxItems)
			maxItems=QtCore.int

		Returns the list of items in the backwards history list
		At most maxItems entries are returned.
		"""
		res = super(QWebHistory,self).backItems(maxItems)
		return res
	#----------------------------------------------------------------------
	def forwardItems(self,maxItems):
		"""
		forwardItems(maxItems)
			maxItems=QtCore.int

		Returns the list of items in the forward history list
		At most maxItems entries are returned.
		"""
		res = super(QWebHistory,self).forwardItems(maxItems)
		return res
	#----------------------------------------------------------------------
	def goToItem(self,item):
		"""
		goToItem(item)
			item=QtWebKit.QWebHistoryItem

		Sets the current item to be the specified item in the history and goes to the page.
		"""
		res = super(QWebHistory,self).goToItem(item)
		return res
	#----------------------------------------------------------------------
	def itemAt(self,i):
		"""
		itemAt(i)
			i=QtCore.int

		Returns the item at index i in the history.
		"""
		res = super(QWebHistory,self).itemAt(i)
		isinstance(res,QtWebKit.QWebHistoryItem)
		return res
	#----------------------------------------------------------------------
	def setMaximumItemCount(self,count):
		"""
		setMaximumItemCount(count)
			count=QtCore.int

		Sets the maximum number of items in the history to count .
		"""
		res = super(QWebHistory,self).setMaximumItemCount(count)
		return res

from PySide import QtGui, QtCore

class QItemSelection(QtGui.QItemSelection):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QItemSelection,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def back(self):
		"""

		"""
		res = super(QItemSelection,self).back()
		isinstance(res,QtGui.QItemSelectionRange)
		return res
	#----------------------------------------------------------------------
	def clear(self):
		"""

		"""
		res = super(QItemSelection,self).clear()
		return res
	#----------------------------------------------------------------------
	def count(self):
		"""

		"""
		res = super(QItemSelection,self).count()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def detachShared(self):
		"""

		"""
		res = super(QItemSelection,self).detachShared()
		return res
	#----------------------------------------------------------------------
	def detach_helper(self):
		"""

		"""
		res = super(QItemSelection,self).detach_helper()
		return res
	#----------------------------------------------------------------------
	def empty(self):
		"""

		"""
		res = super(QItemSelection,self).empty()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def first(self):
		"""

		"""
		res = super(QItemSelection,self).first()
		isinstance(res,QtGui.QItemSelectionRange)
		return res
	#----------------------------------------------------------------------
	def front(self):
		"""

		"""
		res = super(QItemSelection,self).front()
		isinstance(res,QtGui.QItemSelectionRange)
		return res
	#----------------------------------------------------------------------
	def indexes(self):
		"""
		Returns a list of model indexes that correspond to the selected items.
		"""
		res = super(QItemSelection,self).indexes()
		return res
	#----------------------------------------------------------------------
	def isEmpty(self):
		"""

		"""
		res = super(QItemSelection,self).isEmpty()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def last(self):
		"""

		"""
		res = super(QItemSelection,self).last()
		isinstance(res,QtGui.QItemSelectionRange)
		return res
	#----------------------------------------------------------------------
	def length(self):
		"""

		"""
		res = super(QItemSelection,self).length()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def PySide.QtGui.QItemSelection.operator[](i)(self):
		"""

		"""
		res = super(QItemSelection,self).PySide.QtGui.QItemSelection.operator[](i)()
		isinstance(res,QtGui.QItemSelectionRange)
		return res
	#----------------------------------------------------------------------
	def pop_back(self):
		"""

		"""
		res = super(QItemSelection,self).pop_back()
		return res
	#----------------------------------------------------------------------
	def pop_front(self):
		"""

		"""
		res = super(QItemSelection,self).pop_front()
		return res
	#----------------------------------------------------------------------
	def removeFirst(self):
		"""

		"""
		res = super(QItemSelection,self).removeFirst()
		return res
	#----------------------------------------------------------------------
	def removeLast(self):
		"""

		"""
		res = super(QItemSelection,self).removeLast()
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""

		"""
		res = super(QItemSelection,self).size()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def takeFirst(self):
		"""

		"""
		res = super(QItemSelection,self).takeFirst()
		isinstance(res,QtGui.QItemSelectionRange)
		return res
	#----------------------------------------------------------------------
	def takeLast(self):
		"""

		"""
		res = super(QItemSelection,self).takeLast()
		isinstance(res,QtGui.QItemSelectionRange)
		return res
	#----------------------------------------------------------------------
	def toSet(self):
		"""

		"""
		res = super(QItemSelection,self).toSet()
		return res
	#----------------------------------------------------------------------
	def toVector(self):
		"""

		"""
		res = super(QItemSelection,self).toVector()
		return res
	#----------------------------------------------------------------------
	def append(self,*args,**kwargs):
		"""
		append(t)
			t=unKnown

		append(t)
			t=QtGui.QItemSelectionRange


		"""
		res = super(QItemSelection,self).append(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def at(self,i):
		"""
		at(i)
			i=QtCore.int


		"""
		res = super(QItemSelection,self).at(i)
		isinstance(res,QtGui.QItemSelectionRange)
		return res
	#----------------------------------------------------------------------
	def contains(self,index):
		"""
		contains(index)
			index=QtCore.QModelIndex

		Returns true if the selection contains the given index ; otherwise returns false.
		"""
		res = super(QItemSelection,self).contains(index)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def count(self,t):
		"""
		count(t)
			t=QtGui.QItemSelectionRange


		"""
		res = super(QItemSelection,self).count(t)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def detach_helper(self,alloc):
		"""
		detach_helper(alloc)
			alloc=QtCore.int


		"""
		res = super(QItemSelection,self).detach_helper(alloc)
		return res
	#----------------------------------------------------------------------
	def endsWith(self,t):
		"""
		endsWith(t)
			t=QtGui.QItemSelectionRange


		"""
		res = super(QItemSelection,self).endsWith(t)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def indexOf(self,t,from=None):
		"""
		indexOf(t,from=None)
			t=QtGui.QItemSelectionRange
			from=QtCore.int


		"""
		res = super(QItemSelection,self).indexOf(t,from)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def insert(self,i,t):
		"""
		insert(i,t)
			i=QtCore.int
			t=QtGui.QItemSelectionRange


		"""
		res = super(QItemSelection,self).insert(i,t)
		return res
	#----------------------------------------------------------------------
	def isSharedWith(self,other):
		"""
		isSharedWith(other)
			other=unKnown


		"""
		res = super(QItemSelection,self).isSharedWith(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def lastIndexOf(self,t,from=None):
		"""
		lastIndexOf(t,from=None)
			t=QtGui.QItemSelectionRange
			from=QtCore.int


		"""
		res = super(QItemSelection,self).lastIndexOf(t,from)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def merge(self,other,command):
		"""
		merge(other,command)
			other=QtGui.QItemSelection
			command=QtGui.QItemSelectionModel.SelectionFlags


		"""
		res = super(QItemSelection,self).merge(other,command)
		return res
	#----------------------------------------------------------------------
	def mid(self,pos,length=None):
		"""
		mid(pos,length=None)
			pos=QtCore.int
			length=QtCore.int


		"""
		res = super(QItemSelection,self).mid(pos,length)
		return res
	#----------------------------------------------------------------------
	def move(self,from,to):
		"""
		move(from,to)
			from=QtCore.int
			to=QtCore.int


		"""
		res = super(QItemSelection,self).move(from,to)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,l):
		"""
		__ne__(l)
			l=unKnown


		"""
		res = super(QItemSelection,self).__ne__(l)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __add__(self,l):
		"""
		__add__(l)
			l=unKnown


		"""
		res = super(QItemSelection,self).__add__(l)
		return res
	#----------------------------------------------------------------------
	def __iadd__(self,*args,**kwargs):
		"""
		__iadd__(l)
			l=unKnown

		__iadd__(t)
			t=QtGui.QItemSelectionRange


		"""
		res = super(QItemSelection,self).__iadd__(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def __lshift__(self,*args,**kwargs):
		"""
		__lshift__(l)
			l=unKnown

		__lshift__(t)
			t=QtGui.QItemSelectionRange


		"""
		res = super(QItemSelection,self).__lshift__(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,l):
		"""
		__eq__(l)
			l=unKnown


		"""
		res = super(QItemSelection,self).__eq__(l)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def prepend(self,t):
		"""
		prepend(t)
			t=QtGui.QItemSelectionRange


		"""
		res = super(QItemSelection,self).prepend(t)
		return res
	#----------------------------------------------------------------------
	def push_back(self,t):
		"""
		push_back(t)
			t=QtGui.QItemSelectionRange


		"""
		res = super(QItemSelection,self).push_back(t)
		return res
	#----------------------------------------------------------------------
	def push_front(self,t):
		"""
		push_front(t)
			t=QtGui.QItemSelectionRange


		"""
		res = super(QItemSelection,self).push_front(t)
		return res
	#----------------------------------------------------------------------
	def removeAll(self,t):
		"""
		removeAll(t)
			t=QtGui.QItemSelectionRange


		"""
		res = super(QItemSelection,self).removeAll(t)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def removeAt(self,i):
		"""
		removeAt(i)
			i=QtCore.int


		"""
		res = super(QItemSelection,self).removeAt(i)
		return res
	#----------------------------------------------------------------------
	def removeOne(self,t):
		"""
		removeOne(t)
			t=QtGui.QItemSelectionRange


		"""
		res = super(QItemSelection,self).removeOne(t)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def replace(self,i,t):
		"""
		replace(i,t)
			i=QtCore.int
			t=QtGui.QItemSelectionRange


		"""
		res = super(QItemSelection,self).replace(i,t)
		return res
	#----------------------------------------------------------------------
	def reserve(self,size):
		"""
		reserve(size)
			size=QtCore.int


		"""
		res = super(QItemSelection,self).reserve(size)
		return res
	#----------------------------------------------------------------------
	def select(self,topLeft,bottomRight):
		"""
		select(topLeft,bottomRight)
			topLeft=QtCore.QModelIndex
			bottomRight=QtCore.QModelIndex

		Adds the items in the range that extends from the top-left model item, specified by the topLeft index, to the bottom-right item, specified by bottomRight to the list.
		"""
		res = super(QItemSelection,self).select(topLeft,bottomRight)
		return res
	#----------------------------------------------------------------------
	def setSharable(self,sharable):
		"""
		setSharable(sharable)
			sharable=QtCore.bool


		"""
		res = super(QItemSelection,self).setSharable(sharable)
		return res
	#----------------------------------------------------------------------
	def startsWith(self,t):
		"""
		startsWith(t)
			t=QtGui.QItemSelectionRange


		"""
		res = super(QItemSelection,self).startsWith(t)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def swap(self,i,j):
		"""
		swap(i,j)
			i=QtCore.int
			j=QtCore.int


		"""
		res = super(QItemSelection,self).swap(i,j)
		return res
	#----------------------------------------------------------------------
	def takeAt(self,i):
		"""
		takeAt(i)
			i=QtCore.int


		"""
		res = super(QItemSelection,self).takeAt(i)
		isinstance(res,QtGui.QItemSelectionRange)
		return res
	#----------------------------------------------------------------------
	def value(self,*args,**kwargs):
		"""
		value(i)
			i=QtCore.int

		value(i,defaultValue)
			i=QtCore.int
			defaultValue=QtGui.QItemSelectionRange


		"""
		res = super(QItemSelection,self).value(*args,**kwargs)
		isinstance(res,QtGui.QItemSelectionRange)
		return res

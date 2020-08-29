from PySide import QtGui, QtCore

class QWebElementCollection(QtWebKit.QWebElementCollection):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QWebElementCollection,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __getitem__(self):
		"""

		"""
		res = super(QWebElementCollection,self).__getitem__()
		return res
	#----------------------------------------------------------------------
	def __len__(self):
		"""

		"""
		res = super(QWebElementCollection,self).__len__()
		return res
	#----------------------------------------------------------------------
	def count(self):
		"""
		Returns the number of elements in the collection.
		"""
		res = super(QWebElementCollection,self).count()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def first(self):
		"""
		Returns the first element in the collection.
		"""
		res = super(QWebElementCollection,self).first()
		isinstance(res,QtWebKit.QWebElement)
		return res
	#----------------------------------------------------------------------
	def last(self):
		"""
		Returns the last element in the collection.
		"""
		res = super(QWebElementCollection,self).last()
		isinstance(res,QtWebKit.QWebElement)
		return res
	#----------------------------------------------------------------------
	def PySide.QtWebKit.QWebElementCollection.operator[](i)(self):
		"""
		Returns the element at the specified position in the collection.
		"""
		res = super(QWebElementCollection,self).PySide.QtWebKit.QWebElementCollection.operator[](i)()
		isinstance(res,QtWebKit.QWebElement)
		return res
	#----------------------------------------------------------------------
	def toList(self):
		"""
		Returns a QList object with the elements contained in this collection.
		"""
		res = super(QWebElementCollection,self).toList()
		return res
	#----------------------------------------------------------------------
	def append(self,collection):
		"""
		append(collection)
			collection=QtWebKit.QWebElementCollection

		Extends the collection by appending all items of other .
		The resulting collection may include duplicate elements.
		"""
		res = super(QWebElementCollection,self).append(collection)
		return res
	#----------------------------------------------------------------------
	def at(self,i):
		"""
		at(i)
			i=QtCore.int

		Returns the element at index position i in the collection.
		"""
		res = super(QWebElementCollection,self).at(i)
		isinstance(res,QtWebKit.QWebElement)
		return res
	#----------------------------------------------------------------------
	def __add__(self,other):
		"""
		__add__(other)
			other=QtWebKit.QWebElementCollection

		Returns a collection that contains all the elements of this collection followed by all the elements in the other collection
		Duplicates may occur in the result.
		"""
		res = super(QWebElementCollection,self).__add__(other)
		isinstance(res,QtWebKit.QWebElementCollection)
		return res
	#----------------------------------------------------------------------
	def __iadd__(self,other):
		"""
		__iadd__(other)
			other=QtWebKit.QWebElementCollection

		Appends the items of the other list to this list and returns a reference to this list.
		"""
		res = super(QWebElementCollection,self).__iadd__(other)
		isinstance(res,QtWebKit.QWebElementCollection)
		return res

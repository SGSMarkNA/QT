from PySide import QtGui, QtCore

class QXmlStreamAttributes(QtCore.QXmlStreamAttributes):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QXmlStreamAttributes,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def alignOfTypedData(self):
		"""

		"""
		res = super(QXmlStreamAttributes,self).alignOfTypedData()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def capacity(self):
		"""

		"""
		res = super(QXmlStreamAttributes,self).capacity()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def clear(self):
		"""

		"""
		res = super(QXmlStreamAttributes,self).clear()
		return res
	#----------------------------------------------------------------------
	def constData(self):
		"""

		"""
		res = super(QXmlStreamAttributes,self).constData()
		isinstance(res,QtCore.QXmlStreamAttribute)
		return res
	#----------------------------------------------------------------------
	def count(self):
		"""

		"""
		res = super(QXmlStreamAttributes,self).count()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def data(self):
		"""

		"""
		res = super(QXmlStreamAttributes,self).data()
		isinstance(res,QtCore.QXmlStreamAttribute)
		return res
	#----------------------------------------------------------------------
	def detach_helper(self):
		"""

		"""
		res = super(QXmlStreamAttributes,self).detach_helper()
		return res
	#----------------------------------------------------------------------
	def empty(self):
		"""

		"""
		res = super(QXmlStreamAttributes,self).empty()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def first(self):
		"""

		"""
		res = super(QXmlStreamAttributes,self).first()
		isinstance(res,QtCore.QXmlStreamAttribute)
		return res
	#----------------------------------------------------------------------
	def front(self):
		"""

		"""
		res = super(QXmlStreamAttributes,self).front()
		isinstance(res,QtCore.QXmlStreamAttribute)
		return res
	#----------------------------------------------------------------------
	def isEmpty(self):
		"""

		"""
		res = super(QXmlStreamAttributes,self).isEmpty()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def last(self):
		"""

		"""
		res = super(QXmlStreamAttributes,self).last()
		isinstance(res,QtCore.QXmlStreamAttribute)
		return res
	#----------------------------------------------------------------------
	def PySide.QtCore.QXmlStreamAttributes.operator[](i)(self):
		"""

		"""
		res = super(QXmlStreamAttributes,self).PySide.QtCore.QXmlStreamAttributes.operator[](i)()
		isinstance(res,QtCore.QXmlStreamAttribute)
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""

		"""
		res = super(QXmlStreamAttributes,self).size()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def sizeOfTypedData(self):
		"""

		"""
		res = super(QXmlStreamAttributes,self).sizeOfTypedData()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def squeeze(self):
		"""

		"""
		res = super(QXmlStreamAttributes,self).squeeze()
		return res
	#----------------------------------------------------------------------
	def append(self,*args,**kwargs):
		"""
		append(attribute)
			attribute=QtCore.QXmlStreamAttribute

		append(qualifiedName,value)
			qualifiedName=unicode
			value=unicode

		append(namespaceUri,name,value)
			namespaceUri=unicode
			name=unicode
			value=unicode

		Appends the given attribute to the end of the vector.
		"""
		res = super(QXmlStreamAttributes,self).append(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def at(self,i):
		"""
		at(i)
			i=QtCore.int


		"""
		res = super(QXmlStreamAttributes,self).at(i)
		isinstance(res,QtCore.QXmlStreamAttribute)
		return res
	#----------------------------------------------------------------------
	def contains(self,t):
		"""
		contains(t)
			t=QtCore.QXmlStreamAttribute


		"""
		res = super(QXmlStreamAttributes,self).contains(t)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def count(self,t):
		"""
		count(t)
			t=QtCore.QXmlStreamAttribute


		"""
		res = super(QXmlStreamAttributes,self).count(t)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def endsWith(self,t):
		"""
		endsWith(t)
			t=QtCore.QXmlStreamAttribute


		"""
		res = super(QXmlStreamAttributes,self).endsWith(t)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def erase(self,abegin,aend):
		"""
		erase(abegin,aend)
			abegin=QtCore.QXmlStreamAttribute
			aend=QtCore.QXmlStreamAttribute


		"""
		res = super(QXmlStreamAttributes,self).erase(abegin,aend)
		isinstance(res,QtCore.QXmlStreamAttribute)
		return res
	#----------------------------------------------------------------------
	def fill(self,t,size=None):
		"""
		fill(t,size=None)
			t=QtCore.QXmlStreamAttribute
			size=QtCore.int


		"""
		res = super(QXmlStreamAttributes,self).fill(t,size)
		return res
	#----------------------------------------------------------------------
	def hasAttribute(self,*args,**kwargs):
		"""
		hasAttribute(qualifiedName)
			qualifiedName=unicode

		hasAttribute(namespaceUri,name)
			namespaceUri=unicode
			name=unicode

		Returns true if this PySide.QtCore.QXmlStreamAttributes has an attribute whose qualified name is qualifiedName ; otherwise returns false.
		Note that this is not namespace aware
		For instance, if this PySide.QtCore.QXmlStreamAttributes contains an attribute whose lexical name is xlink:href this doesnt tell that an attribute named href in the XLink namespace is present, since the xlink prefix can be bound to any namespace
		Use the overload that takes a namespace URI and a local name as parameter, for namespace aware code.
		"""
		res = super(QXmlStreamAttributes,self).hasAttribute(*args,**kwargs)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def indexOf(self,t,from=None):
		"""
		indexOf(t,from=None)
			t=QtCore.QXmlStreamAttribute
			from=QtCore.int


		"""
		res = super(QXmlStreamAttributes,self).indexOf(t,from)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def insert(self,*args,**kwargs):
		"""
		insert(i,t)
			i=QtCore.int
			t=QtCore.QXmlStreamAttribute

		insert(i,n,t)
			i=QtCore.int
			n=QtCore.int
			t=QtCore.QXmlStreamAttribute

		insert(before,n,t)
			before=QtCore.QXmlStreamAttribute
			n=QtCore.int
			t=QtCore.QXmlStreamAttribute


		"""
		res = super(QXmlStreamAttributes,self).insert(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def isSharedWith(self,other):
		"""
		isSharedWith(other)
			other=unKnown


		"""
		res = super(QXmlStreamAttributes,self).isSharedWith(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def lastIndexOf(self,t,from=None):
		"""
		lastIndexOf(t,from=None)
			t=QtCore.QXmlStreamAttribute
			from=QtCore.int


		"""
		res = super(QXmlStreamAttributes,self).lastIndexOf(t,from)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def mid(self,pos,length=None):
		"""
		mid(pos,length=None)
			pos=QtCore.int
			length=QtCore.int


		"""
		res = super(QXmlStreamAttributes,self).mid(pos,length)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,v):
		"""
		__ne__(v)
			v=unKnown


		"""
		res = super(QXmlStreamAttributes,self).__ne__(v)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __add__(self,l):
		"""
		__add__(l)
			l=unKnown


		"""
		res = super(QXmlStreamAttributes,self).__add__(l)
		return res
	#----------------------------------------------------------------------
	def __iadd__(self,*args,**kwargs):
		"""
		__iadd__(l)
			l=unKnown

		__iadd__(t)
			t=QtCore.QXmlStreamAttribute

		__iadd__(l)
			l=unKnown


		"""
		res = super(QXmlStreamAttributes,self).__iadd__(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def __lshift__(self,*args,**kwargs):
		"""
		__lshift__(t)
			t=QtCore.QXmlStreamAttribute

		__lshift__(l)
			l=unKnown


		"""
		res = super(QXmlStreamAttributes,self).__lshift__(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,v):
		"""
		__eq__(v)
			v=unKnown


		"""
		res = super(QXmlStreamAttributes,self).__eq__(v)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def prepend(self,t):
		"""
		prepend(t)
			t=QtCore.QXmlStreamAttribute


		"""
		res = super(QXmlStreamAttributes,self).prepend(t)
		return res
	#----------------------------------------------------------------------
	def realloc(self,size,alloc):
		"""
		realloc(size,alloc)
			size=QtCore.int
			alloc=QtCore.int


		"""
		res = super(QXmlStreamAttributes,self).realloc(size,alloc)
		return res
	#----------------------------------------------------------------------
	def remove(self,*args,**kwargs):
		"""
		remove(i,n)
			i=QtCore.int
			n=QtCore.int

		remove(i)
			i=QtCore.int


		"""
		res = super(QXmlStreamAttributes,self).remove(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def replace(self,i,t):
		"""
		replace(i,t)
			i=QtCore.int
			t=QtCore.QXmlStreamAttribute


		"""
		res = super(QXmlStreamAttributes,self).replace(i,t)
		return res
	#----------------------------------------------------------------------
	def reserve(self,size):
		"""
		reserve(size)
			size=QtCore.int


		"""
		res = super(QXmlStreamAttributes,self).reserve(size)
		return res
	#----------------------------------------------------------------------
	def resize(self,size):
		"""
		resize(size)
			size=QtCore.int


		"""
		res = super(QXmlStreamAttributes,self).resize(size)
		return res
	#----------------------------------------------------------------------
	def setSharable(self,sharable):
		"""
		setSharable(sharable)
			sharable=QtCore.bool


		"""
		res = super(QXmlStreamAttributes,self).setSharable(sharable)
		return res
	#----------------------------------------------------------------------
	def startsWith(self,t):
		"""
		startsWith(t)
			t=QtCore.QXmlStreamAttribute


		"""
		res = super(QXmlStreamAttributes,self).startsWith(t)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def value(self,*args,**kwargs):
		"""
		value(namespaceUri,name)
			namespaceUri=unicode
			name=unicode

		value(qualifiedName)
			qualifiedName=unicode

		Returns the value of the attribute name in the namespace described with namespaceUri , or an empty string reference if the attribute is not defined
		The namespaceUri can be empty.
		"""
		res = super(QXmlStreamAttributes,self).value(*args,**kwargs)
		isinstance(res,QtCore.QStringRef)
		return res

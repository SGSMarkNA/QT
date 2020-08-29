from PySide import QtGui, QtCore

class QBitArray(QtCore.QBitArray):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QBitArray,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __getitem__(self):
		"""

		"""
		res = super(QBitArray,self).__getitem__()
		return res
	#----------------------------------------------------------------------
	def __len__(self):
		"""

		"""
		res = super(QBitArray,self).__len__()
		return res
	#----------------------------------------------------------------------
	def __setitem__(self):
		"""

		"""
		res = super(QBitArray,self).__setitem__()
		return res
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Clears the contents of the bit array and makes it empty.
		"""
		res = super(QBitArray,self).clear()
		return res
	#----------------------------------------------------------------------
	def count(self):
		"""
		Same as PySide.QtCore.QBitArray.size() .
		"""
		res = super(QBitArray,self).count()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def isEmpty(self):
		"""
		Returns true if this bit array has size 0; otherwise returns false.
		"""
		res = super(QBitArray,self).isEmpty()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if this bit array is null; otherwise returns false.
		Example:
		Qt makes a distinction between null bit arrays and empty bit arrays for historical reasons
		For most applications, what matters is whether or not a bit array contains any data, and this can be determined using PySide.QtCore.QBitArray.isEmpty() .
		"""
		res = super(QBitArray,self).isNull()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""
		Returns the number of bits stored in the bit array.
		"""
		res = super(QBitArray,self).size()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def at(self,i):
		"""
		at(i)
			i=QtCore.int

		Returns the value of the bit at index position i .
		i must be a valid index position in the bit array (i.e., 0 <= i < PySide.QtCore.QBitArray.size() ).
		"""
		res = super(QBitArray,self).at(i)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def clearBit(self,i):
		"""
		clearBit(i)
			i=QtCore.int

		Sets the bit at index position i to 0.
		i must be a valid index position in the bit array (i.e., 0 <= i < PySide.QtCore.QBitArray.size() ).
		"""
		res = super(QBitArray,self).clearBit(i)
		return res
	#----------------------------------------------------------------------
	def count(self,on):
		"""
		count(on)
			on=QtCore.bool

		If on is true, this function returns the number of 1-bits stored in the bit array; otherwise the number of 0-bits is returned.
		"""
		res = super(QBitArray,self).count(on)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def fill(self,*args,**kwargs):
		"""
		fill(val,first,last)
			val=QtCore.bool
			first=QtCore.int
			last=QtCore.int

		fill(val,size=None)
			val=QtCore.bool
			size=QtCore.int

		This is an overloaded function.
		Sets bits at index positions begin up to and excluding end to value .
		begin and end must be a valid index position in the bit array (i.e., 0 <= begin <= PySide.QtCore.QBitArray.size() and 0 <= end <= PySide.QtCore.QBitArray.size() ).
		"""
		res = super(QBitArray,self).fill(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,a):
		"""
		__ne__(a)
			a=QtCore.QBitArray

		Returns true if other is not equal to this bit array; otherwise returns false.
		"""
		res = super(QBitArray,self).__ne__(a)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __and__(self,arg__2):
		"""
		__and__(arg__2)
			arg__2=QtCore.QBitArray


		"""
		res = super(QBitArray,self).__and__(arg__2)
		isinstance(res,QtCore.QBitArray)
		return res
	#----------------------------------------------------------------------
	def __iand__(self,arg__1):
		"""
		__iand__(arg__1)
			arg__1=QtCore.QBitArray

		Performs the AND operation between all bits in this bit array and other
		Assigns the result to this bit array, and returns a reference to it.
		The result has the length of the longest of the two bit arrays, with any missing bits (if one array is shorter than the other) taken to be 0.
		Example:
		"""
		res = super(QBitArray,self).__iand__(arg__1)
		isinstance(res,QtCore.QBitArray)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,a):
		"""
		__eq__(a)
			a=QtCore.QBitArray

		Returns true if other is equal to this bit array; otherwise returns false.
		"""
		res = super(QBitArray,self).__eq__(a)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __xor__(self,arg__2):
		"""
		__xor__(arg__2)
			arg__2=QtCore.QBitArray


		"""
		res = super(QBitArray,self).__xor__(arg__2)
		isinstance(res,QtCore.QBitArray)
		return res
	#----------------------------------------------------------------------
	def __ixor__(self,arg__1):
		"""
		__ixor__(arg__1)
			arg__1=QtCore.QBitArray

		Performs the XOR operation between all bits in this bit array and other
		Assigns the result to this bit array, and returns a reference to it.
		The result has the length of the longest of the two bit arrays, with any missing bits (if one array is shorter than the other) taken to be 0.
		Example:
		"""
		res = super(QBitArray,self).__ixor__(arg__1)
		isinstance(res,QtCore.QBitArray)
		return res
	#----------------------------------------------------------------------
	def __or__(self,arg__2):
		"""
		__or__(arg__2)
			arg__2=QtCore.QBitArray


		"""
		res = super(QBitArray,self).__or__(arg__2)
		isinstance(res,QtCore.QBitArray)
		return res
	#----------------------------------------------------------------------
	def __ior__(self,arg__1):
		"""
		__ior__(arg__1)
			arg__1=QtCore.QBitArray

		Performs the OR operation between all bits in this bit array and other
		Assigns the result to this bit array, and returns a reference to it.
		The result has the length of the longest of the two bit arrays, with any missing bits (if one array is shorter than the other) taken to be 0.
		Example:
		"""
		res = super(QBitArray,self).__ior__(arg__1)
		isinstance(res,QtCore.QBitArray)
		return res
	#----------------------------------------------------------------------
	def resize(self,size):
		"""
		resize(size)
			size=QtCore.int

		Resizes the bit array to size bits.
		If size is greater than the current size, the bit array is extended to make it size bits with the extra bits added to the end
		The new bits are initialized to false (0).
		If size is less than the current size, bits are removed from the end.
		"""
		res = super(QBitArray,self).resize(size)
		return res
	#----------------------------------------------------------------------
	def setBit(self,*args,**kwargs):
		"""
		setBit(i)
			i=QtCore.int

		setBit(i,val)
			i=QtCore.int
			val=QtCore.bool

		Sets the bit at index position i to 1.
		i must be a valid index position in the bit array (i.e., 0 <= i < PySide.QtCore.QBitArray.size() ).
		"""
		res = super(QBitArray,self).setBit(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def testBit(self,i):
		"""
		testBit(i)
			i=QtCore.int

		Returns true if the bit at index position i is 1; otherwise returns false.
		i must be a valid index position in the bit array (i.e., 0 <= i < PySide.QtCore.QBitArray.size() ).
		"""
		res = super(QBitArray,self).testBit(i)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def toggleBit(self,i):
		"""
		toggleBit(i)
			i=QtCore.int

		Inverts the value of the bit at index position i , returning the previous value of that bit as either true (if it was set) or false (if it was unset).
		If the previous value was 0, the new value will be 1
		If the previous value was 1, the new value will be 0.
		i must be a valid index position in the bit array (i.e., 0 <= i < PySide.QtCore.QBitArray.size() ).
		"""
		res = super(QBitArray,self).toggleBit(i)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def truncate(self,pos):
		"""
		truncate(pos)
			pos=QtCore.int

		Truncates the bit array at index position pos .
		If pos is beyond the end of the array, nothing happens.
		"""
		res = super(QBitArray,self).truncate(pos)
		return res

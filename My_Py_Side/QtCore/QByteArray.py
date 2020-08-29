from PySide import QtGui, QtCore

class QByteArray(QtCore.QByteArray):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QByteArray,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __getitem__(self):
		"""

		"""
		res = super(QByteArray,self).__getitem__()
		return res
	#----------------------------------------------------------------------
	def __getslice__(self):
		"""

		"""
		res = super(QByteArray,self).__getslice__()
		return res
	#----------------------------------------------------------------------
	def __len__(self):
		"""

		"""
		res = super(QByteArray,self).__len__()
		return res
	#----------------------------------------------------------------------
	def __reduce__(self):
		"""

		"""
		res = super(QByteArray,self).__reduce__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __repr__(self):
		"""

		"""
		res = super(QByteArray,self).__repr__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __setitem__(self):
		"""

		"""
		res = super(QByteArray,self).__setitem__()
		return res
	#----------------------------------------------------------------------
	def __str__(self):
		"""

		"""
		res = super(QByteArray,self).__str__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def capacity(self):
		"""
		Returns the maximum number of bytes that can be stored in the byte array without forcing a reallocation.
		The sole purpose of this function is to provide a means of fine tuning PySide.QtCore.QByteArray s memory usage
		In general, you will rarely ever need to call this function
		If you want to know how many bytes are in the byte array, call PySide.QtCore.QByteArray.size() .
		"""
		res = super(QByteArray,self).capacity()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Clears the contents of the byte array and makes it empty.
		"""
		res = super(QByteArray,self).clear()
		return res
	#----------------------------------------------------------------------
	def count(self):
		"""
		This is an overloaded function.
		Same as PySide.QtCore.QByteArray.size() .
		"""
		res = super(QByteArray,self).count()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def data(self):
		"""
		This is an overloaded function.
		"""
		res = super(QByteArray,self).data()
		return res
	#----------------------------------------------------------------------
	def isEmpty(self):
		"""
		Returns true if the byte array has size 0; otherwise returns false.
		Example:
		"""
		res = super(QByteArray,self).isEmpty()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isNull(self):
		"""
		Returns true if this byte array is null; otherwise returns false.
		Example:
		Qt makes a distinction between null byte arrays and empty byte arrays for historical reasons
		For most applications, what matters is whether or not a byte array contains any data, and this can be determined using PySide.QtCore.QByteArray.isEmpty() .
		"""
		res = super(QByteArray,self).isNull()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def length(self):
		"""
		Same as PySide.QtCore.QByteArray.size() .
		"""
		res = super(QByteArray,self).length()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def nulTerminated(self):
		"""

		"""
		res = super(QByteArray,self).nulTerminated()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def simplified(self):
		"""
		Returns a byte array that has whitespace removed from the start and the end, and which has each sequence of internal whitespace replaced with a single space.
		Whitespace means any character for which the standard C++ isspace() function returns true
		This includes the ASCII characters t, n, v, f, r, and  .
		Example:
		"""
		res = super(QByteArray,self).simplified()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def size(self):
		"""
		Returns the number of bytes in this byte array.
		The last byte in the byte array is at position PySide.QtCore.QByteArray.size() - 1
		In addition, PySide.QtCore.QByteArray ensures that the byte at position PySide.QtCore.QByteArray.size() is always 0, so that you can use the return value of PySide.QtCore.QByteArray.data() and PySide.QtCore.QByteArray.constData() as arguments to functions that expect 0-terminated strings.
		Example:
		"""
		res = super(QByteArray,self).size()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def squeeze(self):
		"""
		Releases any memory not required to store the arrays data.
		The sole purpose of this function is to provide a means of fine tuning PySide.QtCore.QByteArray s memory usage
		In general, you will rarely ever need to call this function.
		"""
		res = super(QByteArray,self).squeeze()
		return res
	#----------------------------------------------------------------------
	def toBase64(self):
		"""
		Returns a copy of the byte array, encoded as Base64.
		The algorithm used to encode Base64-encoded data is defined in RFC 2045 .
		"""
		res = super(QByteArray,self).toBase64()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def toDouble(self):
		"""
		Returns the byte array converted to a double value.
		Returns 0.0 if the conversion fails.
		If ok is not 0: if a conversion error occurs, *``ok`` is set to false; otherwise *``ok`` is set to true.
		"""
		res = super(QByteArray,self).toDouble()
		isinstance(res,QtCore.double)
		return res
	#----------------------------------------------------------------------
	def toFloat(self):
		"""
		Returns the byte array converted to a float value.
		Returns 0.0 if the conversion fails.
		If ok is not 0: if a conversion error occurs, *``ok`` is set to false; otherwise *``ok`` is set to true.
		"""
		res = super(QByteArray,self).toFloat()
		isinstance(res,QtCore.float)
		return res
	#----------------------------------------------------------------------
	def toHex(self):
		"""
		Returns a hex encoded copy of the byte array
		The hex encoding uses the numbers 0-9 and the letters a-f.
		"""
		res = super(QByteArray,self).toHex()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def toLower(self):
		"""
		Returns a lowercase copy of the byte array
		The bytearray is interpreted as a Latin-1 encoded string.
		Example:
		"""
		res = super(QByteArray,self).toLower()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def toUpper(self):
		"""
		Returns an uppercase copy of the byte array
		The bytearray is interpreted as a Latin-1 encoded string.
		Example:
		"""
		res = super(QByteArray,self).toUpper()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def trimmed(self):
		"""
		Returns a byte array that has whitespace removed from the start and the end.
		Whitespace means any character for which the standard C++ isspace() function returns true
		This includes the ASCII characters t, n, v, f, r, and  .
		Example:
		Unlike PySide.QtCore.QByteArray.simplified() , PySide.QtCore.QByteArray.trimmed() leaves internal whitespace alone.
		"""
		res = super(QByteArray,self).trimmed()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def append(self,*args,**kwargs):
		"""
		append(c)
			c=QtCore.char

		append(a)
			a=QtCore.QByteArray

		This is an overloaded function.
		Appends the character ch to this byte array.
		"""
		res = super(QByteArray,self).append(*args,**kwargs)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def at(self,i):
		"""
		at(i)
			i=QtCore.int

		Returns the character at index position i in the byte array.
		i must be a valid index position in the byte array (i.e., 0 <= i < PySide.QtCore.QByteArray.size() ).
		"""
		res = super(QByteArray,self).at(i)
		isinstance(res,QtCore.char)
		return res
	#----------------------------------------------------------------------
	def chop(self,n):
		"""
		chop(n)
			n=QtCore.int

		Removes n bytes from the end of the byte array.
		If n is greater than PySide.QtCore.QByteArray.size() , the result is an empty byte array.
		Example:
		"""
		res = super(QByteArray,self).chop(n)
		return res
	#----------------------------------------------------------------------
	def contains(self,*args,**kwargs):
		"""
		contains(a)
			a=QtCore.QByteArray

		contains(c)
			c=QtCore.char

		Returns true if the byte array contains an occurrence of the byte array ba ; otherwise returns false.
		"""
		res = super(QByteArray,self).contains(*args,**kwargs)
		isinstance(res,QtCore.QBool)
		return res
	#----------------------------------------------------------------------
	def count(self,*args,**kwargs):
		"""
		count(a)
			a=QtCore.QByteArray

		count(c)
			c=QtCore.char

		Returns the number of (potentially overlapping) occurrences of byte array ba in this byte array.
		"""
		res = super(QByteArray,self).count(*args,**kwargs)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def endsWith(self,*args,**kwargs):
		"""
		endsWith(a)
			a=QtCore.QByteArray

		endsWith(c)
			c=QtCore.char

		Returns true if this byte array ends with byte array ba ; otherwise returns false.
		Example:
		"""
		res = super(QByteArray,self).endsWith(*args,**kwargs)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def expand(self,i):
		"""
		expand(i)
			i=QtCore.int


		"""
		res = super(QByteArray,self).expand(i)
		return res
	#----------------------------------------------------------------------
	def fill(self,c,size=None):
		"""
		fill(c,size=None)
			c=QtCore.char
			size=QtCore.int

		Sets every byte in the byte array to character ch
		If size is different from -1 (the default), the byte array is resized to size size beforehand.
		Example:
		"""
		res = super(QByteArray,self).fill(c,size)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def indexOf(self,a,from=None):
		"""
		indexOf(a,from=None)
			a=QtCore.QByteArray
			from=QtCore.int

		Returns the index position of the first occurrence of the byte array ba in this byte array, searching forward from index position from
		Returns -1 if ba could not be found.
		Example:
		"""
		res = super(QByteArray,self).indexOf(a,from)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def insert(self,i,a):
		"""
		insert(i,a)
			i=QtCore.int
			a=QtCore.QByteArray

		Inserts the byte array ba at index position i and returns a reference to this byte array.
		Example:
		"""
		res = super(QByteArray,self).insert(i,a)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def isSharedWith(self,other):
		"""
		isSharedWith(other)
			other=QtCore.QByteArray


		"""
		res = super(QByteArray,self).isSharedWith(other)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def lastIndexOf(self,a,from=None):
		"""
		lastIndexOf(a,from=None)
			a=QtCore.QByteArray
			from=QtCore.int

		Returns the index position of the last occurrence of the byte array ba in this byte array, searching backward from index position from
		If from is -1 (the default), the search starts at the last byte
		Returns -1 if ba could not be found.
		Example:
		"""
		res = super(QByteArray,self).lastIndexOf(a,from)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def left(self,len):
		"""
		left(len)
			len=QtCore.int

		Returns a byte array that contains the leftmost len bytes of this byte array.
		The entire byte array is returned if len is greater than PySide.QtCore.QByteArray.size() .
		Example:
		"""
		res = super(QByteArray,self).left(len)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def leftJustified(self,width,fill=None,truncate=None):
		"""
		leftJustified(width,fill=None,truncate=None)
			width=QtCore.int
			fill=QtCore.char
			truncate=QtCore.bool

		Returns a byte array of size width that contains this byte array padded by the fill character.
		If truncate is false and the PySide.QtCore.QByteArray.size() of the byte array is more than width , then the returned byte array is a copy of this byte array.
		If truncate is true and the PySide.QtCore.QByteArray.size() of the byte array is more than width , then any bytes in a copy of the byte array after position width are removed, and the copy is returned.
		Example:
		"""
		res = super(QByteArray,self).leftJustified(width,fill,truncate)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def mid(self,index,len=None):
		"""
		mid(index,len=None)
			index=QtCore.int
			len=QtCore.int

		Returns a byte array containing len bytes from this byte array, starting at position pos .
		If len is -1 (the default), or pos + len >= PySide.QtCore.QByteArray.size() , returns a byte array containing all bytes starting at position pos until the end of the byte array.
		Example:
		"""
		res = super(QByteArray,self).mid(index,len)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,a2):
		"""
		__ne__(a2)
			a2=QtCore.QByteArray


		"""
		res = super(QByteArray,self).__ne__(a2)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __add__(self,*args,**kwargs):
		"""
		__add__(a2)
			a2=QtCore.QByteArray

		__add__(arg__1)
			arg__1=Unicode

		__add__(a2)
			a2=QtCore.char

		__add__(arg__1)
			arg__1=tring

		__add__(arg__1)
			arg__1=Unicode

		__add__(a1)
			a1=QtCore.char


		"""
		res = super(QByteArray,self).__add__(*args,**kwargs)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def __iadd__(self,*args,**kwargs):
		"""
		__iadd__(a)
			a=QtCore.QByteArray

		__iadd__(c)
			c=QtCore.char

		Appends the byte array ba onto the end of this byte array and returns a reference to this byte array.
		Example:
		Note: PySide.QtCore.QByteArray is an implicitly shared class
		Consequently, if this is an empty PySide.QtCore.QByteArray , then this will just share the data held in ba
		In this case, no copying of data is done, taking constant time
		If a shared instance is modified, it will be copied (copy-on-write), taking linear time .
		If this is not an empty PySide.QtCore.QByteArray , a deep copy of the data is performed, taking linear time .
		This operation typically does not suffer from allocation overhead, because PySide.QtCore.QByteArray preallocates extra space at the end of the data so that it may grow without reallocating for each append operation.
		"""
		res = super(QByteArray,self).__iadd__(*args,**kwargs)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def __lt__(self,*args,**kwargs):
		"""
		__lt__(a2)
			a2=str

		__lt__(a2)
			a2=QtCore.QByteArray


		"""
		res = super(QByteArray,self).__lt__(*args,**kwargs)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __le__(self,a2):
		"""
		__le__(a2)
			a2=QtCore.QByteArray


		"""
		res = super(QByteArray,self).__le__(a2)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,a2):
		"""
		__eq__(a2)
			a2=QtCore.QByteArray


		"""
		res = super(QByteArray,self).__eq__(a2)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __gt__(self,a2):
		"""
		__gt__(a2)
			a2=QtCore.QByteArray


		"""
		res = super(QByteArray,self).__gt__(a2)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def __ge__(self,a2):
		"""
		__ge__(a2)
			a2=QtCore.QByteArray


		"""
		res = super(QByteArray,self).__ge__(a2)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def prepend(self,*args,**kwargs):
		"""
		prepend(a)
			a=QtCore.QByteArray

		prepend(c)
			c=QtCore.char

		Prepends the byte array ba to this byte array and returns a reference to this byte array.
		Example:
		This is the same as insert(0, ba ).
		Note: PySide.QtCore.QByteArray is an implicitly shared class
		Consequently, if this is an empty PySide.QtCore.QByteArray , then this will just share the data held in ba
		In this case, no copying of data is done, taking constant time
		If a shared instance is modified, it will be copied (copy-on-write), taking linear time .
		If this is not an empty PySide.QtCore.QByteArray , a deep copy of the data is performed, taking linear time .
		"""
		res = super(QByteArray,self).prepend(*args,**kwargs)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def realloc(self,alloc):
		"""
		realloc(alloc)
			alloc=QtCore.int


		"""
		res = super(QByteArray,self).realloc(alloc)
		return res
	#----------------------------------------------------------------------
	def remove(self,index,len):
		"""
		remove(index,len)
			index=QtCore.int
			len=QtCore.int

		Removes len bytes from the array, starting at index position pos , and returns a reference to the array.
		If pos is out of range, nothing happens
		If pos is valid, but pos + len is larger than the size of the array, the array is truncated at position pos .
		Example:
		"""
		res = super(QByteArray,self).remove(index,len)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def repeated(self,times):
		"""
		repeated(times)
			times=QtCore.int

		Returns a copy of this byte array repeated the specified number of times .
		If times is less than 1, an empty byte array is returned.
		Example:
		"""
		res = super(QByteArray,self).repeated(times)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def replace(self,*args,**kwargs):
		"""
		replace(index,len,s)
			index=QtCore.int
			len=QtCore.int
			s=QtCore.QByteArray

		replace(before,after)
			before=unicode
			after=QtCore.QByteArray

		replace(before,after)
			before=QtCore.char
			after=QtCore.char

		replace(before,after)
			before=QtCore.char
			after=QtCore.QByteArray

		replace(before,after)
			before=QtCore.QByteArray
			after=QtCore.QByteArray

		Replaces len bytes from index position pos with the byte array after , and returns a reference to this byte array.
		Example:
		"""
		res = super(QByteArray,self).replace(*args,**kwargs)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def reserve(self,size):
		"""
		reserve(size)
			size=QtCore.int

		Attempts to allocate memory for at least size bytes
		If you know in advance how large the byte array will be, you can call this function, and if you call PySide.QtCore.QByteArray.resize() often you are likely to get better performance
		If size is an underestimate, the worst that will happen is that the PySide.QtCore.QByteArray will be a bit slower.
		The sole purpose of this function is to provide a means of fine tuning PySide.QtCore.QByteArray s memory usage
		In general, you will rarely ever need to call this function
		If you want to change the size of the byte array, call PySide.QtCore.QByteArray.resize() .
		"""
		res = super(QByteArray,self).reserve(size)
		return res
	#----------------------------------------------------------------------
	def resize(self,size):
		"""
		resize(size)
			size=QtCore.int

		Sets the size of the byte array to size bytes.
		If size is greater than the current size, the byte array is extended to make it size bytes with the extra bytes added to the end
		The new bytes are uninitialized.
		If size is less than the current size, bytes are removed from the end.
		"""
		res = super(QByteArray,self).resize(size)
		return res
	#----------------------------------------------------------------------
	def right(self,len):
		"""
		right(len)
			len=QtCore.int

		Returns a byte array that contains the rightmost len bytes of this byte array.
		The entire byte array is returned if len is greater than PySide.QtCore.QByteArray.size() .
		Example:
		"""
		res = super(QByteArray,self).right(len)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def rightJustified(self,width,fill=None,truncate=None):
		"""
		rightJustified(width,fill=None,truncate=None)
			width=QtCore.int
			fill=QtCore.char
			truncate=QtCore.bool

		Returns a byte array of size width that contains the fill character followed by this byte array.
		If truncate is false and the size of the byte array is more than width , then the returned byte array is a copy of this byte array.
		If truncate is true and the size of the byte array is more than width , then the resulting byte array is truncated at position width .
		Example:
		"""
		res = super(QByteArray,self).rightJustified(width,fill,truncate)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def setNum(self,*args,**kwargs):
		"""
		setNum(arg__1,f=None,prec=None)
			arg__1=QtCore.double
			f=QtCore.char
			prec=QtCore.int

		setNum(arg__1,base=None)
			arg__1=QtCore.qlonglong
			base=QtCore.int

		setNum(arg__1,base=None)
			arg__1=QtCore.int
			base=QtCore.int

		This is an overloaded function.
		Sets the byte array to the printed value of n , formatted in format f with precision prec , and returns a reference to the byte array.
		The format f can be any of the following:
		With e, E, and f, prec is the number of digits after the decimal point
		With g and G, prec is the maximum number of significant digits (trailing zeroes are omitted).
		"""
		res = super(QByteArray,self).setNum(*args,**kwargs)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def setRawData(self,a,n):
		"""
		setRawData(a,n)
			a=str
			n=QtCore.uint

		Resets the PySide.QtCore.QByteArray to use the first size bytes of the data array
		The bytes are not copied
		The PySide.QtCore.QByteArray will contain the data pointer
		The caller guarantees that data will not be deleted or modified as long as this PySide.QtCore.QByteArray and any copies of it exist that have not been modified.
		This function can be used instead of PySide.QtCore.QByteArray.fromRawData() to re-use existings PySide.QtCore.QByteArray objects to save memory re-allocations.
		"""
		res = super(QByteArray,self).setRawData(a,n)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def split(self,sep):
		"""
		split(sep)
			sep=QtCore.char

		Splits the byte array into subarrays wherever sep occurs, and returns the list of those arrays
		If sep does not match anywhere in the byte array, PySide.QtCore.QByteArray.split() returns a single-element list containing this byte array.
		"""
		res = super(QByteArray,self).split(sep)
		return res
	#----------------------------------------------------------------------
	def startsWith(self,*args,**kwargs):
		"""
		startsWith(a)
			a=QtCore.QByteArray

		startsWith(c)
			c=QtCore.char

		Returns true if this byte array starts with byte array ba ; otherwise returns false.
		Example:
		"""
		res = super(QByteArray,self).startsWith(*args,**kwargs)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def toInt(self,base=None):
		"""
		toInt(base=None)
			base=QtCore.int

		Returns the byte array converted to an int using base base , which is 10 by default and must be between 2 and 36, or 0.
		If base is 0, the base is determined automatically using the following rules: If the byte array begins with 0x, it is assumed to be hexadecimal; if it begins with 0, it is assumed to be octal; otherwise it is assumed to be decimal.
		Returns 0 if the conversion fails.
		If ok is not 0: if a conversion error occurs, *``ok`` is set to false; otherwise *``ok`` is set to true.
		"""
		res = super(QByteArray,self).toInt(base)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def toLong(self,base=None):
		"""
		toLong(base=None)
			base=QtCore.int

		Returns the byte array converted to a long int using base base , which is 10 by default and must be between 2 and 36, or 0.
		If base is 0, the base is determined automatically using the following rules: If the byte array begins with 0x, it is assumed to be hexadecimal; if it begins with 0, it is assumed to be octal; otherwise it is assumed to be decimal.
		Returns 0 if the conversion fails.
		If ok is not 0: if a conversion error occurs, *``ok`` is set to false; otherwise *``ok`` is set to true.
		"""
		res = super(QByteArray,self).toLong(base)
		isinstance(res,QtCore.long)
		return res
	#----------------------------------------------------------------------
	def toLongLong(self,base=None):
		"""
		toLongLong(base=None)
			base=QtCore.int

		Returns the byte array converted to a long long using base base , which is 10 by default and must be between 2 and 36, or 0.
		If base is 0, the base is determined automatically using the following rules: If the byte array begins with 0x, it is assumed to be hexadecimal; if it begins with 0, it is assumed to be octal; otherwise it is assumed to be decimal.
		Returns 0 if the conversion fails.
		If ok is not 0: if a conversion error occurs, *``ok`` is set to false; otherwise *``ok`` is set to true.
		"""
		res = super(QByteArray,self).toLongLong(base)
		isinstance(res,QtCore.qlonglong)
		return res
	#----------------------------------------------------------------------
	def toPercentEncoding(self,exclude=None,include=None,percent=None):
		"""
		toPercentEncoding(exclude=None,include=None,percent=None)
			exclude=QtCore.QByteArray
			include=QtCore.QByteArray
			percent=QtCore.char

		Returns a URI/URL-style percent-encoded copy of this byte array
		The percent parameter allows you to override the default % character for another.
		By default, this function will encode all characters that are not one of the following:
		ALPHA (a to z and A to Z) / DIGIT (0 to 9) / - /
		/  _  / ~
		To prevent characters from being encoded pass them to exclude
		To force characters to be encoded pass them to include
		The percent character is always encoded.
		Example:
		The hex encoding uses the numbers 0-9 and the uppercase letters A-F.
		"""
		res = super(QByteArray,self).toPercentEncoding(exclude,include,percent)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def toShort(self,base=None):
		"""
		toShort(base=None)
			base=QtCore.int

		Returns the byte array converted to a short using base base , which is 10 by default and must be between 2 and 36, or 0.
		If base is 0, the base is determined automatically using the following rules: If the byte array begins with 0x, it is assumed to be hexadecimal; if it begins with 0, it is assumed to be octal; otherwise it is assumed to be decimal.
		Returns 0 if the conversion fails.
		If ok is not 0: if a conversion error occurs, *``ok`` is set to false; otherwise *``ok`` is set to true.
		"""
		res = super(QByteArray,self).toShort(base)
		isinstance(res,QtCore.short)
		return res
	#----------------------------------------------------------------------
	def toUInt(self,base=None):
		"""
		toUInt(base=None)
			base=QtCore.int

		Returns the byte array converted to an unsigned int using base base , which is 10 by default and must be between 2 and 36, or 0.
		If base is 0, the base is determined automatically using the following rules: If the byte array begins with 0x, it is assumed to be hexadecimal; if it begins with 0, it is assumed to be octal; otherwise it is assumed to be decimal.
		Returns 0 if the conversion fails.
		If ok is not 0: if a conversion error occurs, *``ok`` is set to false; otherwise *``ok`` is set to true.
		"""
		res = super(QByteArray,self).toUInt(base)
		isinstance(res,QtCore.uint)
		return res
	#----------------------------------------------------------------------
	def toULong(self,base=None):
		"""
		toULong(base=None)
			base=QtCore.int

		Returns the byte array converted to an unsigned long int using base base , which is 10 by default and must be between 2 and 36, or 0.
		If base is 0, the base is determined automatically using the following rules: If the byte array begins with 0x, it is assumed to be hexadecimal; if it begins with 0, it is assumed to be octal; otherwise it is assumed to be decimal.
		Returns 0 if the conversion fails.
		If ok is not 0: if a conversion error occurs, *``ok`` is set to false; otherwise *``ok`` is set to true.
		"""
		res = super(QByteArray,self).toULong(base)
		isinstance(res,QtCore.ulong)
		return res
	#----------------------------------------------------------------------
	def toULongLong(self,base=None):
		"""
		toULongLong(base=None)
			base=QtCore.int

		Returns the byte array converted to an unsigned long long using base base , which is 10 by default and must be between 2 and 36, or 0.
		If base is 0, the base is determined automatically using the following rules: If the byte array begins with 0x, it is assumed to be hexadecimal; if it begins with 0, it is assumed to be octal; otherwise it is assumed to be decimal.
		Returns 0 if the conversion fails.
		If ok is not 0: if a conversion error occurs, *``ok`` is set to false; otherwise *``ok`` is set to true.
		"""
		res = super(QByteArray,self).toULongLong(base)
		isinstance(res,QtCore.qulonglong)
		return res
	#----------------------------------------------------------------------
	def toUShort(self,base=None):
		"""
		toUShort(base=None)
			base=QtCore.int

		Returns the byte array converted to an unsigned short using base base , which is 10 by default and must be between 2 and 36, or 0.
		If base is 0, the base is determined automatically using the following rules: If the byte array begins with 0x, it is assumed to be hexadecimal; if it begins with 0, it is assumed to be octal; otherwise it is assumed to be decimal.
		Returns 0 if the conversion fails.
		If ok is not 0: if a conversion error occurs, *``ok`` is set to false; otherwise *``ok`` is set to true.
		"""
		res = super(QByteArray,self).toUShort(base)
		isinstance(res,QtCore.ushort)
		return res
	#----------------------------------------------------------------------
	def truncate(self,pos):
		"""
		truncate(pos)
			pos=QtCore.int

		Truncates the byte array at index position pos .
		If pos is beyond the end of the array, nothing happens.
		Example:
		"""
		res = super(QByteArray,self).truncate(pos)
		return res

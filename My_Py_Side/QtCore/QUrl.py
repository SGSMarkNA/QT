from PySide import QtGui, QtCore

class QUrl(QtCore.QUrl):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QUrl,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __reduce__(self):
		"""

		"""
		res = super(QUrl,self).__reduce__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __repr__(self):
		"""

		"""
		res = super(QUrl,self).__repr__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def authority(self):
		"""
		Returns the authority of the URL if it is defined; otherwise an empty string is returned.
		"""
		res = super(QUrl,self).authority()
		return res
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Resets the content of the PySide.QtCore.QUrl
		After calling this function, the PySide.QtCore.QUrl is equal to one that has been constructed with the default empty constructor.
		"""
		res = super(QUrl,self).clear()
		return res
	#----------------------------------------------------------------------
	def encodedFragment(self):
		"""
		Returns the fragment of the URL if it is defined; otherwise an empty string is returned
		The returned value will have its non-ASCII and other control characters percent-encoded, as in PySide.QtCore.QUrl.toEncoded() .
		"""
		res = super(QUrl,self).encodedFragment()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def encodedHost(self):
		"""
		Returns the host part of the URL if it is defined; otherwise an empty string is returned.
		Note: PySide.QtCore.QUrl.encodedHost() does not return percent-encoded hostnames
		Instead, the ACE-encoded (bare ASCII in Punycode encoding) form will be returned for any non-ASCII hostname.
		This function is equivalent to calling QUrl.toAce() on the return value of PySide.QtCore.QUrl.host() .
		"""
		res = super(QUrl,self).encodedHost()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def encodedPassword(self):
		"""
		Returns the password of the URL if it is defined; otherwise an empty string is returned
		The returned value will have its non-ASCII and other control characters percent-encoded, as in PySide.QtCore.QUrl.toEncoded() .
		"""
		res = super(QUrl,self).encodedPassword()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def encodedPath(self):
		"""
		Returns the path of the URL if it is defined; otherwise an empty string is returned
		The returned value will have its non-ASCII and other control characters percent-encoded, as in PySide.QtCore.QUrl.toEncoded() .
		"""
		res = super(QUrl,self).encodedPath()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def encodedQuery(self):
		"""
		Returns the query string of the URL in percent encoded form.
		"""
		res = super(QUrl,self).encodedQuery()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def encodedQueryItems(self):
		"""
		Returns the query string of the URL, as a map of encoded keys and values.
		"""
		res = super(QUrl,self).encodedQueryItems()
		return res
	#----------------------------------------------------------------------
	def encodedUserName(self):
		"""
		Returns the user name of the URL if it is defined; otherwise an empty string is returned
		The returned value will have its non-ASCII and other control characters percent-encoded, as in PySide.QtCore.QUrl.toEncoded() .
		"""
		res = super(QUrl,self).encodedUserName()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def errorString(self):
		"""
		Returns a text string that explains why an URL is invalid in the case being; otherwise returns an empty string.
		"""
		res = super(QUrl,self).errorString()
		return res
	#----------------------------------------------------------------------
	def fragment(self):
		"""
		Returns the fragment of the URL.
		"""
		res = super(QUrl,self).fragment()
		return res
	#----------------------------------------------------------------------
	def hasFragment(self):
		"""
		Returns true if this URL contains a fragment (i.e., if # was seen on it).
		"""
		res = super(QUrl,self).hasFragment()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def hasQuery(self):
		"""
		Returns true if this URL contains a Query (i.e., if ? was seen on it).
		"""
		res = super(QUrl,self).hasQuery()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def host(self):
		"""
		Returns the host of the URL if it is defined; otherwise an empty string is returned.
		"""
		res = super(QUrl,self).host()
		return res
	#----------------------------------------------------------------------
	def isEmpty(self):
		"""
		Returns true if the URL has no data; otherwise returns false.
		"""
		res = super(QUrl,self).isEmpty()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isRelative(self):
		"""
		Returns true if the URL is relative; otherwise returns false
		A URL is relative if its scheme is undefined; this function is therefore equivalent to calling PySide.QtCore.QUrl.scheme()
		PySide.QtCore.QUrl.isEmpty() .
		"""
		res = super(QUrl,self).isRelative()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if the URL is valid; otherwise returns false.
		The URL is run through a conformance test
		Every part of the URL must conform to the standard encoding rules of the URI standard for the URL to be reported as valid.
		"""
		res = super(QUrl,self).isValid()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def password(self):
		"""
		Returns the password of the URL if it is defined; otherwise an empty string is returned.
		"""
		res = super(QUrl,self).password()
		return res
	#----------------------------------------------------------------------
	def path(self):
		"""
		Returns the path of the URL.
		"""
		res = super(QUrl,self).path()
		return res
	#----------------------------------------------------------------------
	def port(self):
		"""
		Returns the port of the URL, or -1 if the port is unspecified.
		"""
		res = super(QUrl,self).port()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def queryItems(self):
		"""
		Returns the query string of the URL, as a map of keys and values.
		"""
		res = super(QUrl,self).queryItems()
		return res
	#----------------------------------------------------------------------
	def queryPairDelimiter(self):
		"""
		Returns the character used to delimit between key-value pairs in the query string of the URL.
		"""
		res = super(QUrl,self).queryPairDelimiter()
		isinstance(res,QtCore.char)
		return res
	#----------------------------------------------------------------------
	def queryValueDelimiter(self):
		"""
		Returns the character used to delimit between keys and values in the query string of the URL.
		"""
		res = super(QUrl,self).queryValueDelimiter()
		isinstance(res,QtCore.char)
		return res
	#----------------------------------------------------------------------
	def scheme(self):
		"""
		Returns the scheme of the URL
		If an empty string is returned, this means the scheme is undefined and the URL is then relative.
		"""
		res = super(QUrl,self).scheme()
		return res
	#----------------------------------------------------------------------
	def toLocalFile(self):
		"""
		Returns the path of this URL formatted as a local file path.
		"""
		res = super(QUrl,self).toLocalFile()
		return res
	#----------------------------------------------------------------------
	def userInfo(self):
		"""
		Returns the user info of the URL, or an empty string if the user info is undefined.
		"""
		res = super(QUrl,self).userInfo()
		return res
	#----------------------------------------------------------------------
	def userName(self):
		"""
		Returns the user name of the URL if it is defined; otherwise an empty string is returned.
		"""
		res = super(QUrl,self).userName()
		return res
	#----------------------------------------------------------------------
	def addEncodedQueryItem(self,key,value):
		"""
		addEncodedQueryItem(key,value)
			key=QtCore.QByteArray
			value=QtCore.QByteArray

		Inserts the pair key = value into the query string of the URL.
		Note: this function does not verify that either key or value are properly encoded
		It is the callers responsibility to ensure that the query delimiters are properly encoded, if any.
		"""
		res = super(QUrl,self).addEncodedQueryItem(key,value)
		return res
	#----------------------------------------------------------------------
	def addQueryItem(self,key,value):
		"""
		addQueryItem(key,value)
			key=unicode
			value=unicode

		Inserts the pair key = value into the query string of the URL.
		The key/value pair is encoded before it is added to the query
		The pair is converted into separate strings internally
		The key and value is first encoded into UTF-8 and then delimited by the character returned by valueDelimiter()
		Each key/value pair is delimited by the character returned by pairDelimiter().
		"""
		res = super(QUrl,self).addQueryItem(key,value)
		return res
	#----------------------------------------------------------------------
	def allEncodedQueryItemValues(self,key):
		"""
		allEncodedQueryItemValues(key)
			key=QtCore.QByteArray

		Returns the a list of query string values whose key is equal to key from the URL.
		Note: if the encoded key does not match the encoded version of the query, this function will not work
		That is, if the encoded query of this URL is search=Qt%20Rules, calling this function with key = %73earch will return an empty list.
		"""
		res = super(QUrl,self).allEncodedQueryItemValues(key)
		return res
	#----------------------------------------------------------------------
	def allQueryItemValues(self,key):
		"""
		allQueryItemValues(key)
			key=unicode

		Returns the a list of query string values whose key is equal to key from the URL.
		"""
		res = super(QUrl,self).allQueryItemValues(key)
		return res
	#----------------------------------------------------------------------
	def encodedQueryItemValue(self,key):
		"""
		encodedQueryItemValue(key)
			key=QtCore.QByteArray

		Returns the first query string value whose key is equal to key from the URL.
		Note: if the encoded key does not match the encoded version of the query, this function will not work
		That is, if the encoded query of this URL is search=Qt%20Rules, calling this function with key = %73earch will return an empty string.
		"""
		res = super(QUrl,self).encodedQueryItemValue(key)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def hasEncodedQueryItem(self,key):
		"""
		hasEncodedQueryItem(key)
			key=QtCore.QByteArray

		Returns true if there is a query string pair whose key is equal to key from the URL.
		Note: if the encoded key does not match the encoded version of the query, this function will return false
		That is, if the encoded query of this URL is search=Qt%20Rules, calling this function with key = %73earch will return false.
		"""
		res = super(QUrl,self).hasEncodedQueryItem(key)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def hasQueryItem(self,key):
		"""
		hasQueryItem(key)
			key=unicode

		Returns true if there is a query string pair whose key is equal to key from the URL.
		"""
		res = super(QUrl,self).hasQueryItem(key)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isParentOf(self,url):
		"""
		isParentOf(url)
			url=QtCore.QUrl

		Returns true if this URL is a parent of childUrl
		childUrl is a child of this URL if the two URLs share the same scheme and authority, and this URLs path is a parent of the path of childUrl .
		"""
		res = super(QUrl,self).isParentOf(url)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,url):
		"""
		__ne__(url)
			url=QtCore.QUrl

		Returns true if this URL and the given url are not equal; otherwise returns false.
		"""
		res = super(QUrl,self).__ne__(url)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __lt__(self,url):
		"""
		__lt__(url)
			url=QtCore.QUrl

		Returns true if this URL is less than the given url
		This provides a means of ordering URLs.
		"""
		res = super(QUrl,self).__lt__(url)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,url):
		"""
		__eq__(url)
			url=QtCore.QUrl

		Returns true if this URL and the given url are equal; otherwise returns false.
		"""
		res = super(QUrl,self).__eq__(url)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def port(self,defaultPort):
		"""
		port(defaultPort)
			defaultPort=QtCore.int

		This is an overloaded function.
		Returns the port of the URL, or defaultPort if the port is unspecified.
		Example:
		"""
		res = super(QUrl,self).port(defaultPort)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def queryItemValue(self,key):
		"""
		queryItemValue(key)
			key=unicode

		Returns the first query string value whose key is equal to key from the URL.
		"""
		res = super(QUrl,self).queryItemValue(key)
		return res
	#----------------------------------------------------------------------
	def removeAllEncodedQueryItems(self,key):
		"""
		removeAllEncodedQueryItems(key)
			key=QtCore.QByteArray

		Removes all the query string pairs whose key is equal to key from the URL.
		Note: if the encoded key does not match the encoded version of the query, this function will not work
		That is, if the encoded query of this URL is search=Qt%20Rules, calling this function with key = %73earch will do nothing.
		"""
		res = super(QUrl,self).removeAllEncodedQueryItems(key)
		return res
	#----------------------------------------------------------------------
	def removeAllQueryItems(self,key):
		"""
		removeAllQueryItems(key)
			key=unicode

		Removes all the query string pairs whose key is equal to key from the URL.
		"""
		res = super(QUrl,self).removeAllQueryItems(key)
		return res
	#----------------------------------------------------------------------
	def removeEncodedQueryItem(self,key):
		"""
		removeEncodedQueryItem(key)
			key=QtCore.QByteArray

		Removes the first query string pair whose key is equal to key from the URL.
		Note: if the encoded key does not match the encoded version of the query, this function will not work
		That is, if the encoded query of this URL is search=Qt%20Rules, calling this function with key = %73earch will do nothing.
		"""
		res = super(QUrl,self).removeEncodedQueryItem(key)
		return res
	#----------------------------------------------------------------------
	def removeQueryItem(self,key):
		"""
		removeQueryItem(key)
			key=unicode

		Removes the first query string pair whose key is equal to key from the URL.
		"""
		res = super(QUrl,self).removeQueryItem(key)
		return res
	#----------------------------------------------------------------------
	def resolved(self,relative):
		"""
		resolved(relative)
			relative=QtCore.QUrl

		Returns the result of the merge of this URL with relative
		This URL is used as a base to convert relative to an absolute URL.
		If relative is not a relative URL, this function will return relative directly
		Otherwise, the paths of the two URLs are merged, and the new URL returned has the scheme and authority of the base URL, but with the merged path, as in the following example:
		Calling PySide.QtCore.QUrl.resolved() with .
		returns a PySide.QtCore.QUrl whose directory is one level higher than the original
		Similarly, calling PySide.QtCore.QUrl.resolved() with ../.
		removes two levels from the path
		If relative is /, the path becomes /.
		"""
		res = super(QUrl,self).resolved(relative)
		isinstance(res,QtCore.QUrl)
		return res
	#----------------------------------------------------------------------
	def setAuthority(self,authority):
		"""
		setAuthority(authority)
			authority=unicode

		Sets the authority of the URL to authority .
		The authority of a URL is the combination of user info, a host name and a port
		All of these elements are optional; an empty authority is therefore valid.
		The user info and host are separated by a @, and the host and port are separated by a :
		If the user info is empty, the @ must be omitted; although a stray : is permitted if the port is empty.
		The following example shows a valid authority string:
		"""
		res = super(QUrl,self).setAuthority(authority)
		return res
	#----------------------------------------------------------------------
	def setEncodedFragment(self,fragment):
		"""
		setEncodedFragment(fragment)
			fragment=QtCore.QByteArray

		Sets the URLs fragment to the percent-encoded fragment
		The fragment is the last part of the URL, represented by a # followed by a string of characters
		It is typically used in HTTP for referring to a certain link or point on a page:
		The fragment is sometimes also referred to as the URL reference.
		Passing an argument of QByteArray() (a null PySide.QtCore.QByteArray ) will unset the fragment
		Passing an argument of PySide.QtCore.QByteArray () (an empty but not null PySide.QtCore.QByteArray ) will set the fragment to an empty string (as if the original URL had a lone #).
		"""
		res = super(QUrl,self).setEncodedFragment(fragment)
		return res
	#----------------------------------------------------------------------
	def setEncodedHost(self,host):
		"""
		setEncodedHost(host)
			host=QtCore.QByteArray

		Sets the URLs host to the ACE- or percent-encoded host
		The host is part of the user info element in the authority of the URL, as described in PySide.QtCore.QUrl.setAuthority() .
		"""
		res = super(QUrl,self).setEncodedHost(host)
		return res
	#----------------------------------------------------------------------
	def setEncodedPassword(self,password):
		"""
		setEncodedPassword(password)
			password=QtCore.QByteArray

		Sets the URLs password to the percent-encoded password
		The password is part of the user info element in the authority of the URL, as described in PySide.QtCore.QUrl.setUserInfo() .
		Note: this function does not verify that password is properly encoded
		It is the callers responsibility to ensure that the any delimiters (such as colons or slashes) are properly encoded.
		"""
		res = super(QUrl,self).setEncodedPassword(password)
		return res
	#----------------------------------------------------------------------
	def setEncodedPath(self,path):
		"""
		setEncodedPath(path)
			path=QtCore.QByteArray

		Sets the URLs path to the percent-encoded path
		The path is the part of the URL that comes after the authority but before the query string.
		For non-hierarchical schemes, the path will be everything following the scheme declaration, as in the following example:
		Note: this function does not verify that path is properly encoded
		It is the callers responsibility to ensure that the any delimiters (such as ? and #) are properly encoded.
		"""
		res = super(QUrl,self).setEncodedPath(path)
		return res
	#----------------------------------------------------------------------
	def setEncodedQuery(self,query):
		"""
		setEncodedQuery(query)
			query=QtCore.QByteArray

		Sets the query string of the URL to query
		The string is inserted as-is, and no further encoding is performed when calling PySide.QtCore.QUrl.toEncoded() .
		This function is useful if you need to pass a query string that does not fit into the key-value pattern, or that uses a different scheme for encoding special characters than what is suggested by PySide.QtCore.QUrl .
		Passing a value of QByteArray() to query (a null PySide.QtCore.QByteArray ) unsets the query completely
		However, passing a value of PySide.QtCore.QByteArray () will set the query to an empty value, as if the original URL had a lone ?.
		"""
		res = super(QUrl,self).setEncodedQuery(query)
		return res
	#----------------------------------------------------------------------
	def setEncodedQueryItems(self,query):
		"""
		setEncodedQueryItems(query)
			query=unKnown


		"""
		res = super(QUrl,self).setEncodedQueryItems(query)
		return res
	#----------------------------------------------------------------------
	def setEncodedUrl(self,*args,**kwargs):
		"""
		setEncodedUrl(url)
			url=QtCore.QByteArray

		setEncodedUrl(url,mode)
			url=QtCore.QByteArray
			mode=QtCore.QUrl.ParsingMode

		Constructs a URL by parsing the contents of encodedUrl .
		encodedUrl is assumed to be a URL string in percent encoded form, containing only ASCII characters.
		Use PySide.QtCore.QUrl.isValid() to determine if a valid URL was constructed.
		"""
		res = super(QUrl,self).setEncodedUrl(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setEncodedUserName(self,userName):
		"""
		setEncodedUserName(userName)
			userName=QtCore.QByteArray

		Sets the URLs user name to the percent-encoded userName
		The userName is part of the user info element in the authority of the URL, as described in PySide.QtCore.QUrl.setUserInfo() .
		Note: this function does not verify that userName is properly encoded
		It is the callers responsibility to ensure that the any delimiters (such as colons or slashes) are properly encoded.
		"""
		res = super(QUrl,self).setEncodedUserName(userName)
		return res
	#----------------------------------------------------------------------
	def setFragment(self,fragment):
		"""
		setFragment(fragment)
			fragment=unicode

		Sets the fragment of the URL to fragment
		The fragment is the last part of the URL, represented by a # followed by a string of characters
		It is typically used in HTTP for referring to a certain link or point on a page:
		The fragment is sometimes also referred to as the URL reference.
		Passing an argument of QString() (a null PySide.QtCore.QString ) will unset the fragment
		Passing an argument of PySide.QtCore.QString () (an empty but not null PySide.QtCore.QString ) will set the fragment to an empty string (as if the original URL had a lone #).
		"""
		res = super(QUrl,self).setFragment(fragment)
		return res
	#----------------------------------------------------------------------
	def setHost(self,host):
		"""
		setHost(host)
			host=unicode

		Sets the host of the URL to host
		The host is part of the authority.
		"""
		res = super(QUrl,self).setHost(host)
		return res
	#----------------------------------------------------------------------
	def setPassword(self,password):
		"""
		setPassword(password)
			password=unicode

		Sets the URLs password to password
		The password is part of the user info element in the authority of the URL, as described in PySide.QtCore.QUrl.setUserInfo() .
		"""
		res = super(QUrl,self).setPassword(password)
		return res
	#----------------------------------------------------------------------
	def setPath(self,path):
		"""
		setPath(path)
			path=unicode

		Sets the path of the URL to path
		The path is the part of the URL that comes after the authority but before the query string.
		For non-hierarchical schemes, the path will be everything following the scheme declaration, as in the following example:
		"""
		res = super(QUrl,self).setPath(path)
		return res
	#----------------------------------------------------------------------
	def setPort(self,port):
		"""
		setPort(port)
			port=QtCore.int

		Sets the port of the URL to port
		The port is part of the authority of the URL, as described in PySide.QtCore.QUrl.setAuthority() .
		port must be between 0 and 65535 inclusive
		Setting the port to -1 indicates that the port is unspecified.
		"""
		res = super(QUrl,self).setPort(port)
		return res
	#----------------------------------------------------------------------
	def setQueryDelimiters(self,valueDelimiter,pairDelimiter):
		"""
		setQueryDelimiters(valueDelimiter,pairDelimiter)
			valueDelimiter=QtCore.char
			pairDelimiter=QtCore.char

		Sets the characters used for delimiting between keys and values, and between key-value pairs in the URLs query string
		The default value delimiter is = and the default pair delimiter is &.
		valueDelimiter will be used for separating keys from values, and pairDelimiter will be used to separate key-value pairs
		Any occurrences of these delimiting characters in the encoded representation of the keys and values of the query string are percent encoded.
		If valueDelimiter is set to - and pairDelimiter is /, the above query string would instead be represented like this:
		Calling this function does not change the delimiters of the current query string
		It only affects PySide.QtCore.QUrl.queryItems() , PySide.QtCore.QUrl.setQueryItems() and addQueryItems().
		"""
		res = super(QUrl,self).setQueryDelimiters(valueDelimiter,pairDelimiter)
		return res
	#----------------------------------------------------------------------
	def setQueryItems(self,query):
		"""
		setQueryItems(query)
			query=unKnown


		"""
		res = super(QUrl,self).setQueryItems(query)
		return res
	#----------------------------------------------------------------------
	def setScheme(self,scheme):
		"""
		setScheme(scheme)
			scheme=unicode

		Sets the scheme of the URL to scheme
		As a scheme can only contain ASCII characters, no conversion or encoding is done on the input.
		The scheme describes the type (or protocol) of the URL
		Its represented by one or more ASCII characters at the start the URL, and is followed by a :
		The following example shows a URL where the scheme is ftp:
		The scheme can also be empty, in which case the URL is interpreted as relative.
		"""
		res = super(QUrl,self).setScheme(scheme)
		return res
	#----------------------------------------------------------------------
	def setUrl(self,*args,**kwargs):
		"""
		setUrl(url,mode)
			url=unicode
			mode=QtCore.QUrl.ParsingMode

		setUrl(url)
			url=unicode

		This is an overloaded function.
		Parses url using the parsing mode parsingMode .
		"""
		res = super(QUrl,self).setUrl(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setUserInfo(self,userInfo):
		"""
		setUserInfo(userInfo)
			userInfo=unicode

		Sets the user info of the URL to userInfo
		The user info is an optional part of the authority of the URL, as described in PySide.QtCore.QUrl.setAuthority() .
		The user info consists of a user name and optionally a password, separated by a :
		If the password is empty, the colon must be omitted
		The following example shows a valid user info string:
		"""
		res = super(QUrl,self).setUserInfo(userInfo)
		return res
	#----------------------------------------------------------------------
	def setUserName(self,userName):
		"""
		setUserName(userName)
			userName=unicode

		Sets the URLs user name to userName
		The userName is part of the user info element in the authority of the URL, as described in PySide.QtCore.QUrl.setUserInfo() .
		"""
		res = super(QUrl,self).setUserName(userName)
		return res
	#----------------------------------------------------------------------
	def toEncoded(self,options=None):
		"""
		toEncoded(options=None)
			options=QtCore.QUrl.FormattingOptions


		"""
		res = super(QUrl,self).toEncoded(options)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def toString(self,options=None):
		"""
		toString(options=None)
			options=QtCore.QUrl.FormattingOptions


		"""
		res = super(QUrl,self).toString(options)
		return res

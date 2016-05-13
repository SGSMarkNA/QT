from PySide import QtGui, QtCore

class QRegExp(QtCore.QRegExp):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QRegExp,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def __reduce__(self):
		"""

		"""
		res = super(QRegExp,self).__reduce__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def __repr__(self):
		"""

		"""
		res = super(QRegExp,self).__repr__()
		isinstance(res,Object)
		return res
	#----------------------------------------------------------------------
	def captureCount(self):
		"""
		Returns the number of captures contained in the regular expression.
		"""
		res = super(QRegExp,self).captureCount()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def capturedTexts(self):
		"""
		Returns a list of the captured text strings.
		The first string in the list is the entire matched string
		Each subsequent list element contains a string that matched a (capturing) subexpression of the regexp.
		For example:
		The above example also captures elements that may be present but which we have no interest in
		This problem can be solved by using non-capturing parentheses:
		Note that if you want to iterate over the list, you should iterate over a copy, e.g.
		Some regexps can match an indeterminate number of times
		For example if the input string is Offsets: 12 14 99 231 7 and the regexp, rx , is (d+)+ , we would hope to get a list of all the numbers matched
		However, after calling rx.indexIn(str) , PySide.QtCore.QRegExp.capturedTexts() will return the list (12, 12), i.e
		the entire match was 12 and the first subexpression matched was 12
		The correct approach is to use PySide.QtCore.QRegExp.cap() in a loop .
		The order of elements in the string list is as follows
		The first element is the entire matching string
		Each subsequent element corresponds to the next capturing open left parentheses
		Thus PySide.QtCore.QRegExp.capturedTexts() [1] is the text of the first capturing parentheses, PySide.QtCore.QRegExp.capturedTexts() [2] is the text of the second and so on (corresponding to $1, $2, etc., in some other regexp languages).
		"""
		res = super(QRegExp,self).capturedTexts()
		return res
	#----------------------------------------------------------------------
	def caseSensitivity(self):
		"""
		Returns Qt.CaseSensitive if the regexp is matched case sensitively; otherwise returns Qt.CaseInsensitive .
		"""
		res = super(QRegExp,self).caseSensitivity()
		isinstance(res,QtCore.Qt.CaseSensitivity)
		return res
	#----------------------------------------------------------------------
	def errorString(self):
		"""
		Returns a text string that explains why a regexp pattern is invalid the case being; otherwise returns no error occurred.
		"""
		res = super(QRegExp,self).errorString()
		return res
	#----------------------------------------------------------------------
	def isEmpty(self):
		"""
		Returns true if the pattern string is empty; otherwise returns false.
		If you call PySide.QtCore.QRegExp.exactMatch() with an empty pattern on an empty string it will return true; otherwise it returns false since it operates over the whole string
		If you call PySide.QtCore.QRegExp.indexIn() with an empty pattern on any string it will return the start offset (0 by default) because the empty pattern matches the emptiness at the start of the string
		In this case the length of the match returned by PySide.QtCore.QRegExp.matchedLength() will be 0.
		See QString.isEmpty() .
		"""
		res = super(QRegExp,self).isEmpty()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isMinimal(self):
		"""
		Returns true if minimal (non-greedy) matching is enabled; otherwise returns false.
		"""
		res = super(QRegExp,self).isMinimal()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def isValid(self):
		"""
		Returns true if the regular expression is valid; otherwise returns false
		An invalid regular expression never matches.
		The pattern [a-z is an example of an invalid pattern, since it lacks a closing square bracket.
		Note that the validity of a regexp may also depend on the setting of the wildcard flag, for example *.html is a valid wildcard regexp but an invalid full regexp.
		"""
		res = super(QRegExp,self).isValid()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def matchedLength(self):
		"""
		Returns the length of the last matched string, or -1 if there was no match.
		"""
		res = super(QRegExp,self).matchedLength()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def numCaptures(self):
		"""
		Returns the number of captures contained in the regular expression.
		"""
		res = super(QRegExp,self).numCaptures()
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def pattern(self):
		"""
		Returns the pattern string of the regular expression
		The pattern has either regular expression syntax or wildcard syntax, depending on PySide.QtCore.QRegExp.patternSyntax() .
		"""
		res = super(QRegExp,self).pattern()
		return res
	#----------------------------------------------------------------------
	def patternSyntax(self):
		"""
		Returns the syntax used by the regular expression
		The default is QRegExp.RegExp .
		"""
		res = super(QRegExp,self).patternSyntax()
		isinstance(res,QtCore.QRegExp.PatternSyntax)
		return res
	#----------------------------------------------------------------------
	def cap(self,nth=None):
		"""
		cap(nth=None)
			nth=QtCore.int

		Returns the text captured by the nth subexpression
		The entire match has index 0 and the parenthesized subexpressions have indexes starting from 1 (excluding non-capturing parentheses).
		The order of elements matched by PySide.QtCore.QRegExp.cap() is as follows
		The first element, cap(0), is the entire matching string
		Each subsequent element corresponds to the next capturing open left parentheses
		Thus cap(1) is the text of the first capturing parentheses, cap(2) is the text of the second, and so on.
		"""
		res = super(QRegExp,self).cap(nth)
		return res
	#----------------------------------------------------------------------
	def exactMatch(self,str):
		"""
		exactMatch(str)
			str=unicode

		Returns true if str is matched exactly by this regular expression; otherwise returns false
		You can determine how much of the string was matched by calling PySide.QtCore.QRegExp.matchedLength() .
		For a given regexp string R, exactMatch(R) is the equivalent of indexIn(^R$) since PySide.QtCore.QRegExp.exactMatch() effectively encloses the regexp in the start of string and end of string anchors, except that it sets PySide.QtCore.QRegExp.matchedLength() differently.
		For example, if the regular expression is blue , then PySide.QtCore.QRegExp.exactMatch() returns true only for input blue
		For inputs bluebell , blutak and lightblue , PySide.QtCore.QRegExp.exactMatch() returns false and PySide.QtCore.QRegExp.matchedLength() will return 4, 3 and 0 respectively.
		Although const, this function sets PySide.QtCore.QRegExp.matchedLength() , PySide.QtCore.QRegExp.capturedTexts() , and PySide.QtCore.QRegExp.pos() .
		"""
		res = super(QRegExp,self).exactMatch(str)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def indexIn(self,str,offset=None,caretMode=None):
		"""
		indexIn(str,offset=None,caretMode=None)
			str=unicode
			offset=QtCore.int
			caretMode=QtCore.QRegExp.CaretMode

		Attempts to find a match in str from position offset (0 by default)
		If offset is -1, the search starts at the last character; if -2, at the next to last character; etc.
		Returns the position of the first match, or -1 if there was no match.
		The caretMode parameter can be used to instruct whether ^ should match at index 0 or at offset .
		You might prefer to use QString.indexOf() , QString.contains() , or even QStringList.filter()
		To replace matches use QString.replace() .
		Example:
		Although const, this function sets PySide.QtCore.QRegExp.matchedLength() , PySide.QtCore.QRegExp.capturedTexts() and PySide.QtCore.QRegExp.pos() .
		If the PySide.QtCore.QRegExp is a wildcard expression (see PySide.QtCore.QRegExp.setPatternSyntax() ) and want to test a string against the whole wildcard expression, use PySide.QtCore.QRegExp.exactMatch() instead of this function.
		"""
		res = super(QRegExp,self).indexIn(str,offset,caretMode)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def lastIndexIn(self,str,offset=None,caretMode=None):
		"""
		lastIndexIn(str,offset=None,caretMode=None)
			str=unicode
			offset=QtCore.int
			caretMode=QtCore.QRegExp.CaretMode

		Attempts to find a match backwards in str from position offset
		If offset is -1 (the default), the search starts at the last character; if -2, at the next to last character; etc.
		Returns the position of the first match, or -1 if there was no match.
		The caretMode parameter can be used to instruct whether ^ should match at index 0 or at offset .
		Although const, this function sets PySide.QtCore.QRegExp.matchedLength() , PySide.QtCore.QRegExp.capturedTexts() and PySide.QtCore.QRegExp.pos() .
		"""
		res = super(QRegExp,self).lastIndexIn(str,offset,caretMode)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def __ne__(self,rx):
		"""
		__ne__(rx)
			rx=QtCore.QRegExp

		Returns true if this regular expression is not equal to rx ; otherwise returns false.
		"""
		res = super(QRegExp,self).__ne__(rx)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def __eq__(self,rx):
		"""
		__eq__(rx)
			rx=QtCore.QRegExp

		Returns true if this regular expression is equal to rx ; otherwise returns false.
		Two PySide.QtCore.QRegExp objects are equal if they have the same pattern strings and the same settings for case sensitivity, wildcard and minimal matching.
		"""
		res = super(QRegExp,self).__eq__(rx)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def pos(self,nth=None):
		"""
		pos(nth=None)
			nth=QtCore.int

		Returns the position of the nth captured text in the searched string
		If nth is 0 (the default), PySide.QtCore.QRegExp.pos() returns the position of the whole match.
		Example:
		For zero-length matches, PySide.QtCore.QRegExp.pos() always returns -1
		(For example, if cap(4) would return an empty string, pos(4) returns -1.) This is a feature of the implementation.
		"""
		res = super(QRegExp,self).pos(nth)
		isinstance(res,QtCore.int)
		return res
	#----------------------------------------------------------------------
	def replace(self,sourceString,after):
		"""
		replace(sourceString,after)
			sourceString=unicode
			after=unicode

		Replaces every occurrence of the regular expression in sourceString with after.
                Returns a new Python string with the modified contents
		For example:
		For regular expressions containing capturing parentheses, occurrences of 1, 2, ..., in after
                are replaced with rx.cap(1), cap(2), ...
		"""
		res = super(QRegExp,self).replace(sourceString,after)
		return res
	#----------------------------------------------------------------------
	def setCaseSensitivity(self,cs):
		"""
		setCaseSensitivity(cs)
			cs=QtCore.Qt.CaseSensitivity


		"""
		res = super(QRegExp,self).setCaseSensitivity(cs)
		return res
	#----------------------------------------------------------------------
	def setMinimal(self,minimal):
		"""
		setMinimal(minimal)
			minimal=QtCore.bool

		Enables or disables minimal matching
		If minimal is false, matching is greedy (maximal) which is the default.
		For example, suppose we have the input string We must be <b>bold</b>, very <b>bold</b>! and the pattern <b>.*</b>
		With the default greedy (maximal) matching, the match is We must be <b>bold</b>, very <b>bold</b> !
		But with minimal (non-greedy) matching, the first match is: We must be <b>bold</b> , very <b>bold</b>! and the second match is We must be <b>bold</b>, very <b>bold</b> !
		In practice we might use the pattern <b>[^<]*</b> instead, although this will still fail for nested tags.
		"""
		res = super(QRegExp,self).setMinimal(minimal)
		return res
	#----------------------------------------------------------------------
	def setPattern(self,pattern):
		"""
		setPattern(pattern)
			pattern=unicode

		Sets the pattern string to pattern
		The case sensitivity, wildcard, and minimal matching options are not changed.
		"""
		res = super(QRegExp,self).setPattern(pattern)
		return res
	#----------------------------------------------------------------------
	def setPatternSyntax(self,syntax):
		"""
		setPatternSyntax(syntax)
			syntax=QtCore.QRegExp.PatternSyntax

		Sets the syntax mode for the regular expression
		The default is QRegExp.RegExp .
		Setting syntax to QRegExp.Wildcard enables simple shell-like wildcard matching
		For example, r*.txt matches the string readme.txt in wildcard mode, but does not match readme .
		Setting syntax to QRegExp.FixedString means that the pattern is interpreted as a plain string
		Special characters (e.g., backslash) dont need to be escaped then.
		"""
		res = super(QRegExp,self).setPatternSyntax(syntax)
		return res

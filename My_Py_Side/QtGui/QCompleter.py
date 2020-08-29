from PySide import QtGui, QtCore

class QCompleter(QtGui.QCompleter):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QCompleter,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def caseSensitivity(self):
		"""
		This property holds the case sensitivity of the matching.
		The default is Qt.CaseSensitive .
		"""
		res = super(QCompleter,self).caseSensitivity()
		isinstance(res,QtCore.Qt.CaseSensitivity)
		return res
	#----------------------------------------------------------------------
	def completionColumn(self):
		"""
		This property holds the column in the model in which completions are searched for..
		If the PySide.QtGui.QCompleter.popup() is a PySide.QtGui.QListView , it is automatically setup to display this column.
		By default, the match column is 0.
		"""
		res = super(QCompleter,self).completionColumn()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def completionCount(self):
		"""
		Returns the number of completions for the current prefix
		For an unsorted model with a large number of items this can be expensive
		Use PySide.QtGui.QCompleter.setCurrentRow() and PySide.QtGui.QCompleter.currentCompletion() to iterate through all the completions.
		"""
		res = super(QCompleter,self).completionCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def completionMode(self):
		"""
		This property holds how the completions are provided to the user.
		The default value is QCompleter.PopupCompletion .
		"""
		res = super(QCompleter,self).completionMode()
		isinstance(res,QtGui.QCompleter.CompletionMode)
		return res
	#----------------------------------------------------------------------
	def completionModel(self):
		"""
		Returns the completion model
		The completion model is a read-only list model that contains all the possible matches for the current completion prefix
		The completion model is auto-updated to reflect the current completions.
		"""
		res = super(QCompleter,self).completionModel()
		isinstance(res,QtCore.QAbstractItemModel)
		return res
	#----------------------------------------------------------------------
	def completionPrefix(self):
		"""
		This property holds the completion prefix used to provide completions..
		The PySide.QtGui.QCompleter.completionModel() is updated to reflect the list of possible matches for prefix .
		"""
		res = super(QCompleter,self).completionPrefix()
		return res
	#----------------------------------------------------------------------
	def completionRole(self):
		"""
		This property holds the item role to be used to query the contents of items for matching..
		The default role is Qt.EditRole .
		"""
		res = super(QCompleter,self).completionRole()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def currentCompletion(self):
		"""
		Returns the current completion string
		This includes the PySide.QtGui.QCompleter.completionPrefix()
		When used alongside PySide.QtGui.QCompleter.setCurrentRow() , it can be used to iterate through all the matches.
		"""
		res = super(QCompleter,self).currentCompletion()
		return res
	#----------------------------------------------------------------------
	def currentIndex(self):
		"""
		Returns the model index of the current completion in the PySide.QtGui.QCompleter.completionModel() .
		"""
		res = super(QCompleter,self).currentIndex()
		isinstance(res,QtCore.QModelIndex)
		return res
	#----------------------------------------------------------------------
	def currentRow(self):
		"""
		Returns the current row.
		"""
		res = super(QCompleter,self).currentRow()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def maxVisibleItems(self):
		"""
		This property holds the maximum allowed size on screen of the completer, measured in items.
		By default, this property has a value of 7.
		"""
		res = super(QCompleter,self).maxVisibleItems()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def model(self):
		"""
		Returns the model that provides completion strings.
		"""
		res = super(QCompleter,self).model()
		isinstance(res,QtCore.QAbstractItemModel)
		return res
	#----------------------------------------------------------------------
	def modelSorting(self):
		"""
		This property holds the way the model is sorted.
		By default, no assumptions are made about the order of the items in the model that provides the completions.
		If the models data for the PySide.QtGui.QCompleter.completionColumn() and PySide.QtGui.QCompleter.completionRole() is sorted in ascending order, you can set this property to CaseSensitivelySortedModel or CaseInsensitivelySortedModel
		On large models, this can lead to significant performance improvements because the completer object can then use a binary search algorithm instead of linear search algorithm.
		The sort order (i.e ascending or descending order) of the model is determined dynamically by inspecting the contents of the model.
		"""
		res = super(QCompleter,self).modelSorting()
		isinstance(res,QtGui.QCompleter.ModelSorting)
		return res
	#----------------------------------------------------------------------
	def popup(self):
		"""
		Returns the popup used to display completions.
		"""
		res = super(QCompleter,self).popup()
		isinstance(res,QtGui.QAbstractItemView)
		return res
	#----------------------------------------------------------------------
	def widget(self):
		"""
		Returns the widget for which the completer object is providing completions.
		"""
		res = super(QCompleter,self).widget()
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def wrapAround(self):
		"""
		This property holds the completions wrap around when navigating through items.
		The default is true.
		"""
		res = super(QCompleter,self).wrapAround()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def pathFromIndex(self,index):
		"""
		pathFromIndex(index)
			index=QtCore.QModelIndex

		Returns the path for the given index
		The completer object uses this to obtain the completion text from the underlying model.
		The default implementation returns the edit role of the item for list models
		It returns the absolute file path if the model is a PySide.QtGui.QFileSystemModel .
		"""
		res = super(QCompleter,self).pathFromIndex(index)
		return res
	#----------------------------------------------------------------------
	def setCaseSensitivity(self,caseSensitivity):
		"""
		setCaseSensitivity(caseSensitivity)
			caseSensitivity=QtCore.Qt.CaseSensitivity

		This property holds the case sensitivity of the matching.
		The default is Qt.CaseSensitive .
		"""
		res = super(QCompleter,self).setCaseSensitivity(caseSensitivity)
		return res
	#----------------------------------------------------------------------
	def setCompletionColumn(self,column):
		"""
		setCompletionColumn(column)
			column=QtCore.int

		This property holds the column in the model in which completions are searched for..
		If the PySide.QtGui.QCompleter.popup() is a PySide.QtGui.QListView , it is automatically setup to display this column.
		By default, the match column is 0.
		"""
		res = super(QCompleter,self).setCompletionColumn(column)
		return res
	#----------------------------------------------------------------------
	def setCompletionMode(self,mode):
		"""
		setCompletionMode(mode)
			mode=QtGui.QCompleter.CompletionMode

		This property holds how the completions are provided to the user.
		The default value is QCompleter.PopupCompletion .
		"""
		res = super(QCompleter,self).setCompletionMode(mode)
		return res
	#----------------------------------------------------------------------
	def setCompletionRole(self,role):
		"""
		setCompletionRole(role)
			role=QtCore.int

		This property holds the item role to be used to query the contents of items for matching..
		The default role is Qt.EditRole .
		"""
		res = super(QCompleter,self).setCompletionRole(role)
		return res
	#----------------------------------------------------------------------
	def setCurrentRow(self,row):
		"""
		setCurrentRow(row)
			row=QtCore.int

		Sets the current row to the row specified
		Returns true if successful; otherwise returns false.
		This function may be used along with PySide.QtGui.QCompleter.currentCompletion() to iterate through all the possible completions.
		"""
		res = super(QCompleter,self).setCurrentRow(row)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def setMaxVisibleItems(self,maxItems):
		"""
		setMaxVisibleItems(maxItems)
			maxItems=QtCore.int

		This property holds the maximum allowed size on screen of the completer, measured in items.
		By default, this property has a value of 7.
		"""
		res = super(QCompleter,self).setMaxVisibleItems(maxItems)
		return res
	#----------------------------------------------------------------------
	def setModel(self,c):
		"""
		setModel(c)
			c=QtCore.QAbstractItemModel

		Sets the model which provides completions to model
		The model can be list model or a tree model
		If a model has been already previously set and it has the PySide.QtGui.QCompleter as its parent, it is deleted.
		For convenience, if model is a PySide.QtGui.QFileSystemModel , PySide.QtGui.QCompleter switches its PySide.QtGui.QCompleter.caseSensitivity() to Qt.CaseInsensitive on Windows and Qt.CaseSensitive on other platforms.
		"""
		res = super(QCompleter,self).setModel(c)
		return res
	#----------------------------------------------------------------------
	def setModelSorting(self,sorting):
		"""
		setModelSorting(sorting)
			sorting=QtGui.QCompleter.ModelSorting

		This property holds the way the model is sorted.
		By default, no assumptions are made about the order of the items in the model that provides the completions.
		If the models data for the PySide.QtGui.QCompleter.completionColumn() and PySide.QtGui.QCompleter.completionRole() is sorted in ascending order, you can set this property to CaseSensitivelySortedModel or CaseInsensitivelySortedModel
		On large models, this can lead to significant performance improvements because the completer object can then use a binary search algorithm instead of linear search algorithm.
		The sort order (i.e ascending or descending order) of the model is determined dynamically by inspecting the contents of the model.
		"""
		res = super(QCompleter,self).setModelSorting(sorting)
		return res
	#----------------------------------------------------------------------
	def setPopup(self,popup):
		"""
		setPopup(popup)
			popup=QtGui.QAbstractItemView

		Sets the popup used to display completions to popup
		PySide.QtGui.QCompleter takes ownership of the view.
		A PySide.QtGui.QListView is automatically created when the PySide.QtGui.QCompleter.completionMode() is set to QCompleter.PopupCompletion or QCompleter.UnfilteredPopupCompletion
		The default popup displays the PySide.QtGui.QCompleter.completionColumn() .
		Ensure that this function is called before the view settings are modified
		This is required since views properties may require that a model has been set on the view (for example, hiding columns in the view requires a model to be set on the view).
		"""
		res = super(QCompleter,self).setPopup(popup)
		return res
	#----------------------------------------------------------------------
	def setWidget(self,widget):
		"""
		setWidget(widget)
			widget=QtGui.QWidget

		Sets the widget for which completion are provided for to widget
		This function is automatically called when a PySide.QtGui.QCompleter is set on a PySide.QtGui.QLineEdit using QLineEdit.setCompleter() or on a PySide.QtGui.QComboBox using QComboBox.setCompleter()
		The widget needs to be set explicitly when providing completions for custom widgets.
		"""
		res = super(QCompleter,self).setWidget(widget)
		return res
	#----------------------------------------------------------------------
	def splitPath(self,path):
		"""
		splitPath(path)
			path=unicode

		Splits the given path into strings that are used to match at each level in the PySide.QtGui.QCompleter.model() .
		The default implementation of PySide.QtGui.QCompleter.splitPath() splits a file system path based on QDir.separator() when the sourceModel() is a PySide.QtGui.QFileSystemModel .
		When used with list models, the first item in the returned list is used for matching.
		"""
		res = super(QCompleter,self).splitPath(path)
		return res

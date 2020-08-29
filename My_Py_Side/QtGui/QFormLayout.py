from PySide import QtGui, QtCore

class QFormLayout(QtGui.QFormLayout):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QFormLayout,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def fieldGrowthPolicy(self):
		"""
		This property holds the way in which the forms fields grow.
		The default value depends on the widget or application style
		For QMacStyle , the default is FieldsStayAtSizeHint ; for PySide.QtGui.QCommonStyle derived styles (like Plastique and Windows), the default is ExpandingFieldsGrow ; for Qt Extended styles, the default is AllNonFixedFieldsGrow .
		If none of the fields can grow and the form is resized, extra space is distributed according to the current form alignment .
		"""
		res = super(QFormLayout,self).fieldGrowthPolicy()
		isinstance(res,QtGui.QFormLayout.FieldGrowthPolicy)
		return res
	#----------------------------------------------------------------------
	def formAlignment(self):
		"""
		This property holds the alignment of the form layouts contents within the layouts geometry.
		The default value depends on the widget or application style
		For QMacStyle , the default is Qt.AlignHCenter | Qt.AlignTop ; for the other styles, the default is Qt.AlignLeft | Qt.AlignTop .
		"""
		res = super(QFormLayout,self).formAlignment()
		isinstance(res,QtCore.Qt.Alignment)
		return res
	#----------------------------------------------------------------------
	def horizontalSpacing(self):
		"""
		This property holds the spacing between widgets that are laid out side by side.
		By default, if no value is explicitly set, the layouts horizontal spacing is inherited from the parent layout, or from the style settings for the parent widget.
		"""
		res = super(QFormLayout,self).horizontalSpacing()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def labelAlignment(self):
		"""
		This property holds the horizontal alignment of the labels.
		The default value depends on the widget or application style
		For PySide.QtGui.QCommonStyle derived styles, except for PySide.QtGui.QPlastiqueStyle , the default is Qt.AlignLeft ; for the other styles, the default is Qt.AlignRight .
		"""
		res = super(QFormLayout,self).labelAlignment()
		isinstance(res,QtCore.Qt.Alignment)
		return res
	#----------------------------------------------------------------------
	def resetFieldGrowthPolicy(self):
		"""

		"""
		res = super(QFormLayout,self).resetFieldGrowthPolicy()
		return res
	#----------------------------------------------------------------------
	def resetFormAlignment(self):
		"""

		"""
		res = super(QFormLayout,self).resetFormAlignment()
		return res
	#----------------------------------------------------------------------
	def resetLabelAlignment(self):
		"""

		"""
		res = super(QFormLayout,self).resetLabelAlignment()
		return res
	#----------------------------------------------------------------------
	def resetRowWrapPolicy(self):
		"""

		"""
		res = super(QFormLayout,self).resetRowWrapPolicy()
		return res
	#----------------------------------------------------------------------
	def rowCount(self):
		"""
		Returns the number of rows in the form.
		"""
		res = super(QFormLayout,self).rowCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def rowWrapPolicy(self):
		"""
		This property holds the way in which the forms rows wrap.
		The default value depends on the widget or application style
		For Qt Extended styles and QS60Style , the default is WrapLongRows ; for the other styles, the default is DontWrapRows .
		If you want to display each label above its associated field (instead of next to it), set this property to WrapAllRows .
		"""
		res = super(QFormLayout,self).rowWrapPolicy()
		isinstance(res,QtGui.QFormLayout.RowWrapPolicy)
		return res
	#----------------------------------------------------------------------
	def verticalSpacing(self):
		"""
		This property holds the spacing between widgets that are laid out vertically.
		By default, if no value is explicitly set, the layouts vertical spacing is inherited from the parent layout, or from the style settings for the parent widget.
		"""
		res = super(QFormLayout,self).verticalSpacing()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def addRow(self,*args,**kwargs):
		"""
		addRow(labelText,field)
			labelText=unicode
			field=QtGui.QLayout

		addRow(widget)
			widget=QtGui.QWidget

		addRow(layout)
			layout=QtGui.QLayout

		addRow(label,field)
			label=QtGui.QWidget
			field=QtGui.QLayout

		addRow(labelText,field)
			labelText=unicode
			field=QtGui.QWidget

		addRow(label,field)
			label=QtGui.QWidget
			field=QtGui.QWidget

		This is an overloaded function.
		This overload automatically creates a PySide.QtGui.QLabel behind the scenes with labelText as its text.
		"""
		res = super(QFormLayout,self).addRow(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def getItemPosition(self,index):
		"""
		getItemPosition(index)
			index=QtCore.int

		Retrieves the row and role (column) of the item at the specified index
		If index is out of bounds, *``rowPtr`` is set to -1; otherwise the row is stored in *``rowPtr`` and the role is stored in *``rolePtr`` .
		"""
		res = super(QFormLayout,self).getItemPosition(index)
		return res
	#----------------------------------------------------------------------
	def getLayoutPosition(self,layout):
		"""
		getLayoutPosition(layout)
			layout=QtGui.QLayout

		Retrieves the row and role (column) of the specified child layout
		If layout is not in the form layout, *``rowPtr`` is set to -1; otherwise the row is stored in *``rowPtr`` and the role is stored in *``rolePtr`` .
		"""
		res = super(QFormLayout,self).getLayoutPosition(layout)
		return res
	#----------------------------------------------------------------------
	def getWidgetPosition(self,widget):
		"""
		getWidgetPosition(widget)
			widget=QtGui.QWidget

		Retrieves the row and role (column) of the specified widget in the layout
		If widget is not in the layout, *``rowPtr`` is set to -1; otherwise the row is stored in *``rowPtr`` and the role is stored in *``rolePtr`` .
		"""
		res = super(QFormLayout,self).getWidgetPosition(widget)
		return res
	#----------------------------------------------------------------------
	def insertRow(self,*args,**kwargs):
		"""
		insertRow(row,labelText,field)
			row=QtCore.int
			labelText=unicode
			field=QtGui.QWidget

		insertRow(row,labelText,field)
			row=QtCore.int
			labelText=unicode
			field=QtGui.QLayout

		insertRow(row,widget)
			row=QtCore.int
			widget=QtGui.QWidget

		insertRow(row,layout)
			row=QtCore.int
			layout=QtGui.QLayout

		insertRow(row,label,field)
			row=QtCore.int
			label=QtGui.QWidget
			field=QtGui.QWidget

		insertRow(row,label,field)
			row=QtCore.int
			label=QtGui.QWidget
			field=QtGui.QLayout

		This is an overloaded function.
		This overload automatically creates a PySide.QtGui.QLabel behind the scenes with labelText as its text
		The field is set as the new PySide.QtGui.QLabel s buddy .
		"""
		res = super(QFormLayout,self).insertRow(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def itemAt(self,row,role):
		"""
		itemAt(row,role)
			row=QtCore.int
			role=QtGui.QFormLayout.ItemRole

		Returns the layout item in the given row with the specified role (column)
		Returns 0 if there is no such item.
		"""
		res = super(QFormLayout,self).itemAt(row,role)
		isinstance(res,QtGui.QLayoutItem)
		return res
	#----------------------------------------------------------------------
	def labelForField(self,*args,**kwargs):
		"""
		labelForField(field)
			field=QtGui.QWidget

		labelForField(field)
			field=QtGui.QLayout

		Returns the label associated with the given field .
		"""
		res = super(QFormLayout,self).labelForField(*args,**kwargs)
		isinstance(res,QtGui.QWidget)
		return res
	#----------------------------------------------------------------------
	def setFieldGrowthPolicy(self,policy):
		"""
		setFieldGrowthPolicy(policy)
			policy=QtGui.QFormLayout.FieldGrowthPolicy

		This property holds the way in which the forms fields grow.
		The default value depends on the widget or application style
		For QMacStyle , the default is FieldsStayAtSizeHint ; for PySide.QtGui.QCommonStyle derived styles (like Plastique and Windows), the default is ExpandingFieldsGrow ; for Qt Extended styles, the default is AllNonFixedFieldsGrow .
		If none of the fields can grow and the form is resized, extra space is distributed according to the current form alignment .
		"""
		res = super(QFormLayout,self).setFieldGrowthPolicy(policy)
		return res
	#----------------------------------------------------------------------
	def setFormAlignment(self,alignment):
		"""
		setFormAlignment(alignment)
			alignment=QtCore.Qt.Alignment

		This property holds the alignment of the form layouts contents within the layouts geometry.
		The default value depends on the widget or application style
		For QMacStyle , the default is Qt.AlignHCenter | Qt.AlignTop ; for the other styles, the default is Qt.AlignLeft | Qt.AlignTop .
		"""
		res = super(QFormLayout,self).setFormAlignment(alignment)
		return res
	#----------------------------------------------------------------------
	def setHorizontalSpacing(self,spacing):
		"""
		setHorizontalSpacing(spacing)
			spacing=QtCore.int

		This property holds the spacing between widgets that are laid out side by side.
		By default, if no value is explicitly set, the layouts horizontal spacing is inherited from the parent layout, or from the style settings for the parent widget.
		"""
		res = super(QFormLayout,self).setHorizontalSpacing(spacing)
		return res
	#----------------------------------------------------------------------
	def setItem(self,row,role,item):
		"""
		setItem(row,role,item)
			row=QtCore.int
			role=QtGui.QFormLayout.ItemRole
			item=QtGui.QLayoutItem

		Sets the item in the given row for the given role to item , extending the layout with empty rows if necessary.
		If the cell is already occupied, the item is not inserted and an error message is sent to the console
		The item spans both columns.
		"""
		res = super(QFormLayout,self).setItem(row,role,item)
		return res
	#----------------------------------------------------------------------
	def setLabelAlignment(self,alignment):
		"""
		setLabelAlignment(alignment)
			alignment=QtCore.Qt.Alignment

		This property holds the horizontal alignment of the labels.
		The default value depends on the widget or application style
		For PySide.QtGui.QCommonStyle derived styles, except for PySide.QtGui.QPlastiqueStyle , the default is Qt.AlignLeft ; for the other styles, the default is Qt.AlignRight .
		"""
		res = super(QFormLayout,self).setLabelAlignment(alignment)
		return res
	#----------------------------------------------------------------------
	def setLayout(self,row,role,layout):
		"""
		setLayout(row,role,layout)
			row=QtCore.int
			role=QtGui.QFormLayout.ItemRole
			layout=QtGui.QLayout

		Sets the sub-layout in the given row for the given role to layout , extending the form layout with empty rows if necessary.
		If the cell is already occupied, the layout is not inserted and an error message is sent to the console.
		"""
		res = super(QFormLayout,self).setLayout(row,role,layout)
		return res
	#----------------------------------------------------------------------
	def setRowWrapPolicy(self,policy):
		"""
		setRowWrapPolicy(policy)
			policy=QtGui.QFormLayout.RowWrapPolicy

		This property holds the way in which the forms rows wrap.
		The default value depends on the widget or application style
		For Qt Extended styles and QS60Style , the default is WrapLongRows ; for the other styles, the default is DontWrapRows .
		If you want to display each label above its associated field (instead of next to it), set this property to WrapAllRows .
		"""
		res = super(QFormLayout,self).setRowWrapPolicy(policy)
		return res
	#----------------------------------------------------------------------
	def setVerticalSpacing(self,spacing):
		"""
		setVerticalSpacing(spacing)
			spacing=QtCore.int

		This property holds the spacing between widgets that are laid out vertically.
		By default, if no value is explicitly set, the layouts vertical spacing is inherited from the parent layout, or from the style settings for the parent widget.
		"""
		res = super(QFormLayout,self).setVerticalSpacing(spacing)
		return res
	#----------------------------------------------------------------------
	def setWidget(self,row,role,widget):
		"""
		setWidget(row,role,widget)
			row=QtCore.int
			role=QtGui.QFormLayout.ItemRole
			widget=QtGui.QWidget

		Sets the widget in the given row for the given role to widget , extending the layout with empty rows if necessary.
		If the cell is already occupied, the widget is not inserted and an error message is sent to the console.
		"""
		res = super(QFormLayout,self).setWidget(row,role,widget)
		return res

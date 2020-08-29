import QT
import Qt_Roles_And_Enums
QtCore            = QT.QtCore
QtGui             = QT.QtGui
Qt                = QT.Qt
user_type_counter = QT.user_type_counter
Item_Data_Roles   = Qt_Roles_And_Enums.Standered_Item_Data_Roles
AbstractItemView  = Qt_Roles_And_Enums.AbstractItemView
Constants         = Qt_Roles_And_Enums.Constants

class QMimeData(QtCore.QMimeData):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super_data = kwargs.pop("super_data", None)
		super(QMimeData,self).__init__(*args,**kwargs)
		if super_data:
			[self.setData(formate_key, super_data.data(formate_key)) for formate_key in  super_data.formats()]
	#----------------------------------------------------------------------
	def clear(self):
		"""
		Removes all the MIME type and data entries in the object.
		"""
		res = super(QMimeData,self).clear()
		return res
	#----------------------------------------------------------------------
	def colorData(self):
		"""
		Returns a color if the data stored in the object represents a color (MIME type application/x-color ); otherwise returns a null variant.
		A PySide.QtCore.QVariant is used because PySide.QtCore.QMimeData belongs to the QtCore library, whereas PySide.QtGui.QColor belongs to QtGui
		To convert the PySide.QtCore.QVariant to a PySide.QtGui.QColor , simply use qvariant_cast()
		For example:
		"""
		res = super(QMimeData,self).colorData()
		return res
	#----------------------------------------------------------------------
	def formats(self):
		"""
		Returns a list of formats supported by the object
		This is a list of MIME types for which the object can return suitable data
		The formats in the list are in a priority order.
		For the most common types of data, you can call the higher-level functions PySide.QtCore.QMimeData.hasText() , PySide.QtCore.QMimeData.hasHtml() , PySide.QtCore.QMimeData.hasUrls() , PySide.QtCore.QMimeData.hasImage() , and PySide.QtCore.QMimeData.hasColor() instead.
		"""
		res = super(QMimeData,self).formats()
		return res
	#----------------------------------------------------------------------
	def hasColor(self):
		"""
		Returns true if the object can return a color (MIME type application/x-color ); otherwise returns false.
		"""
		res = super(QMimeData,self).hasColor()
		
		return res
	#----------------------------------------------------------------------
	def hasHtml(self):
		"""
		Returns true if the object can return HTML (MIME type text/html ); otherwise returns false.
		"""
		res = super(QMimeData,self).hasHtml()
		
		return res
	#----------------------------------------------------------------------
	def hasImage(self):
		"""
		Returns true if the object can return an image; otherwise returns false.
		"""
		res = super(QMimeData,self).hasImage()
		
		return res
	#----------------------------------------------------------------------
	def hasText(self):
		"""
		Returns true if the object can return plain text (MIME type text/plain ); otherwise returns false.
		"""
		res = super(QMimeData,self).hasText()
		
		return res
	#----------------------------------------------------------------------
	def hasUrls(self):
		"""
		Returns true if the object can return a list of urls; otherwise returns false.
		URLs correspond to the MIME type text/uri-list .
		"""
		res = super(QMimeData,self).hasUrls()
		
		return res
	#----------------------------------------------------------------------
	def html(self):
		"""
		Returns a string if the data stored in the object is HTML (MIME type text/html ); otherwise returns an empty string.
		"""
		res = super(QMimeData,self).html()
		return res
	#----------------------------------------------------------------------
	def imageData(self):
		"""
		Returns a PySide.QtCore.QVariant storing a PySide.QtGui.QImage if the object can return an image; otherwise returns a null variant.
		A PySide.QtCore.QVariant is used because PySide.QtCore.QMimeData belongs to the QtCore library, whereas PySide.QtGui.QImage belongs to QtGui
		To convert the PySide.QtCore.QVariant to a PySide.QtGui.QImage , simply use qvariant_cast()
		For example:
		"""
		res = super(QMimeData,self).imageData()
		return res
	#----------------------------------------------------------------------
	def text(self):
		"""
		Returns a plain text (MIME type text/plain ) representation of the data.
		"""
		res = super(QMimeData,self).text()
		return res
	#----------------------------------------------------------------------
	def urls(self):
		"""
		Returns a list of URLs contained within the MIME data object.
		URLs correspond to the MIME type text/uri-list .
		"""
		res = super(QMimeData,self).urls()
		return res
	#----------------------------------------------------------------------
	def data(self,mimetype):
		"""
		data(mimetype)
			mimetype=unicode

		Returns the data stored in the object in the format described by the MIME type specified by mimeType .
		"""
		res = super(QMimeData,self).data(mimetype)
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def hasFormat(self,mimetype):
		"""
		hasFormat(mimetype)
			mimetype=unicode

		Returns true if the object can return data for the MIME type specified by mimeType ; otherwise returns false.
		For the most common types of data, you can call the higher-level functions PySide.QtCore.QMimeData.hasText() , PySide.QtCore.QMimeData.hasHtml() , PySide.QtCore.QMimeData.hasUrls() , PySide.QtCore.QMimeData.hasImage() , and PySide.QtCore.QMimeData.hasColor() instead.
		"""
		res = super(QMimeData,self).hasFormat(mimetype)
		
		return res
	#----------------------------------------------------------------------
	def removeFormat(self,mimetype):
		"""
		removeFormat(mimetype)
			mimetype=unicode

		Removes the data entry for mimeType in the object.
		"""
		res = super(QMimeData,self).removeFormat(mimetype)
		return res
	#----------------------------------------------------------------------
	def retrieveData(self,mimetype,preferredType):
		"""
		retrieveData(mimetype,preferredType)
			mimetype=unicode
			preferredType=QtCore.QVariant::Type


		"""
		res = super(QMimeData,self).retrieveData(mimetype,preferredType)
		return res
	#----------------------------------------------------------------------
	def setColorData(self,color):
		"""
		setColorData(color)
			color=object

		Sets the color data in the object to the given color .
		Colors correspond to the MIME type application/x-color .
		"""
		res = super(QMimeData,self).setColorData(color)
		return res
	##----------------------------------------------------------------------
	#def setData(self,mimetype,data):
		#"""
		#setData(mimetype,data)
			#mimetype=unicode
			#data=QtCore.QByteArray

		#Sets the data associated with the MIME type given by mimeType to the specified data .
		#For the most common types of data, you can call the higher-level functions PySide.QtCore.QMimeData.setText() , PySide.QtCore.QMimeData.setHtml() , PySide.QtCore.QMimeData.setUrls() , PySide.QtCore.QMimeData.setImageData() , and PySide.QtCore.QMimeData.setColorData() instead.
		#Note that if you want to use a custom data type in an item view drag and drop operation, you must register it as a Qt meta type , using the Q_DECLARE_METATYPE() macro, and implement stream operators for it
		#The stream operators must then be registered with the qRegisterMetaTypeStreamOperators() function.
		#"""
		#res = super(QMimeData,self).setData(mimetype,data)
		#return res
	#----------------------------------------------------------------------
	def setHtml(self,html):
		"""
		setHtml(html)
			html=unicode

		Sets html as the HTML (MIME type text/html ) used to represent the data.
		"""
		res = super(QMimeData,self).setHtml(html)
		return res
	#----------------------------------------------------------------------
	def setImageData(self,image):
		"""
		setImageData(image)
			image=object

		Sets the data in the object to the given image .
		A PySide.QtCore.QVariant is used because PySide.QtCore.QMimeData belongs to the QtCore library, whereas PySide.QtGui.QImage belongs to QtGui
		The conversion from PySide.QtGui.QImage to PySide.QtCore.QVariant is implicit
		For example:
		"""
		res = super(QMimeData,self).setImageData(image)
		return res
	#----------------------------------------------------------------------
	def setText(self,text):
		"""
		setText(text)
			text=unicode

		Sets text as the plain text (MIME type text/plain ) used to represent the data.
		"""
		res = super(QMimeData,self).setText(text)
		return res
	#----------------------------------------------------------------------
	def setUrls(self,urls):
		"""
		setUrls(urls)
			urls=unKnown


		"""
		res = super(QMimeData,self).setUrls(urls)
		return res


class Drag_And_Drop_MimeData(QMimeData):
	def __init__(self, indexes, **kwargs):
		self.items            = kwargs.pop("items", [])
		self.data_model       = kwargs.pop("model")
		super(Drag_And_Drop_MimeData, self).__init__(**kwargs)
		self.indexes          = indexes
		if isinstance(self.data_model, QtGui.QStandardItemModel) and len(self.items) == 0:
			for index in indexes:
				self.items.append(self.data_model.itemFromIndex(index))
				
		self.drag_source      = None
		self.drop_destination = None
		
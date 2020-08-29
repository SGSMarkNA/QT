from PySide import QtGui, QtCore

class QGLShaderProgram(QtOpenGL.QGLShaderProgram):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGLShaderProgram,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def bind(self):
		"""
		Binds this shader program to the active PySide.QtOpenGL.QGLContext and makes it the current shader program
		Any previously bound shader program is released
		This is equivalent to calling glUseProgram() on PySide.QtOpenGL.QGLShaderProgram.programId()
		Returns true if the program was successfully bound; false otherwise
		If the shader program has not yet been linked, or it needs to be re-linked, this function will call PySide.QtOpenGL.QGLShaderProgram.link() .
		"""
		res = super(QGLShaderProgram,self).bind()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def geometryInputType(self):
		"""
		Returns the geometry shader input type, if active.
		This parameter takes effect the next time the program is linked.
		"""
		res = super(QGLShaderProgram,self).geometryInputType()
		return res
	#----------------------------------------------------------------------
	def geometryOutputType(self):
		"""
		Returns the geometry shader output type, if active.
		This parameter takes effect the next time the program is linked.
		"""
		res = super(QGLShaderProgram,self).geometryOutputType()
		return res
	#----------------------------------------------------------------------
	def geometryOutputVertexCount(self):
		"""
		Returns the maximum number of vertices the current geometry shader program will produce, if active.
		This parameter takes effect the ntext time the program is linked.
		"""
		res = super(QGLShaderProgram,self).geometryOutputVertexCount()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def init(self):
		"""

		"""
		res = super(QGLShaderProgram,self).init()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def isLinked(self):
		"""
		Returns true if this shader program has been linked; false otherwise.
		"""
		res = super(QGLShaderProgram,self).isLinked()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def link(self):
		"""
		Links together the shaders that were added to this program with PySide.QtOpenGL.QGLShaderProgram.addShader()
		Returns true if the link was successful or false otherwise
		If the link failed, the error messages can be retrieved with PySide.QtOpenGL.QGLShaderProgram.log() .
		Subclasses can override this function to initialize attributes and uniform variables for use in specific shader programs.
		If the shader program was already linked, calling this function again will force it to be re-linked.
		"""
		res = super(QGLShaderProgram,self).link()
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def log(self):
		"""
		Returns the errors and warnings that occurred during the last PySide.QtOpenGL.QGLShaderProgram.link() or PySide.QtOpenGL.QGLShaderProgram.addShader() with explicitly specified source code.
		"""
		res = super(QGLShaderProgram,self).log()
		return res
	#----------------------------------------------------------------------
	def maxGeometryOutputVertices(self):
		"""
		Returns the hardware limit for how many vertices a geometry shader can output.
		"""
		res = super(QGLShaderProgram,self).maxGeometryOutputVertices()
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def programId(self):
		"""
		Returns the OpenGL identifier associated with this shader program.
		"""
		res = super(QGLShaderProgram,self).programId()
		return res
	#----------------------------------------------------------------------
	def release(self):
		"""
		Releases the active shader program from the current PySide.QtOpenGL.QGLContext
		This is equivalent to calling glUseProgram(0) .
		"""
		res = super(QGLShaderProgram,self).release()
		return res
	#----------------------------------------------------------------------
	def removeAllShaders(self):
		"""
		Removes all of the shaders that were added to this program previously
		The PySide.QtOpenGL.QGLShader objects for the shaders will not be deleted if they were constructed externally
		PySide.QtOpenGL.QGLShader objects that are constructed internally by PySide.QtOpenGL.QGLShaderProgram will be deleted.
		"""
		res = super(QGLShaderProgram,self).removeAllShaders()
		return res
	#----------------------------------------------------------------------
	def shaders(self):
		"""
		Returns a list of all shaders that have been added to this shader program using PySide.QtOpenGL.QGLShaderProgram.addShader() .
		"""
		res = super(QGLShaderProgram,self).shaders()
		return res
	#----------------------------------------------------------------------
	def addShader(self,shader):
		"""
		addShader(shader)
			shader=QtOpenGL.QGLShader

		Adds a compiled shader to this shader program
		Returns true if the shader could be added, or false otherwise.
		Ownership of the shader object remains with the caller
		It will not be deleted when this PySide.QtOpenGL.QGLShaderProgram instance is deleted
		This allows the caller to add the same shader to multiple shader programs.
		"""
		res = super(QGLShaderProgram,self).addShader(shader)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def addShaderFromSourceCode(self,*args,**kwargs):
		"""
		addShaderFromSourceCode(type,source)
			type=QtOpenGL.QGLShader.ShaderType
			source=unicode

		addShaderFromSourceCode(type,source)
			type=QtOpenGL.QGLShader.ShaderType
			source=str

		addShaderFromSourceCode(type,source)
			type=QtOpenGL.QGLShader.ShaderType
			source=QtCore.QByteArray


		"""
		res = super(QGLShaderProgram,self).addShaderFromSourceCode(*args,**kwargs)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def addShaderFromSourceFile(self,type,fileName):
		"""
		addShaderFromSourceFile(type,fileName)
			type=QtOpenGL.QGLShader.ShaderType
			fileName=unicode


		"""
		res = super(QGLShaderProgram,self).addShaderFromSourceFile(type,fileName)
		isinstance(res,bool)
		return res
	#----------------------------------------------------------------------
	def attributeLocation(self,*args,**kwargs):
		"""
		attributeLocation(name)
			name=str

		attributeLocation(name)
			name=unicode

		attributeLocation(name)
			name=QtCore.QByteArray

		Returns the location of the attribute name within this shader programs parameter list
		Returns -1 if name is not a valid attribute for this shader program.
		"""
		res = super(QGLShaderProgram,self).attributeLocation(*args,**kwargs)
		isinstance(res,int)
		return res
	#----------------------------------------------------------------------
	def bindAttributeLocation(self,*args,**kwargs):
		"""
		bindAttributeLocation(name,location)
			name=str
			location=QtCore.int

		bindAttributeLocation(name,location)
			name=QtCore.QByteArray
			location=QtCore.int

		bindAttributeLocation(name,location)
			name=unicode
			location=QtCore.int

		Binds the attribute name to the specified location
		This function can be called before or after the program has been linked
		Any attributes that have not been explicitly bound when the program is linked will be assigned locations automatically.
		When this function is called after the program has been linked, the program will need to be relinked for the change to take effect.
		"""
		res = super(QGLShaderProgram,self).bindAttributeLocation(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def disableAttributeArray(self,*args,**kwargs):
		"""
		disableAttributeArray(location)
			location=QtCore.int

		disableAttributeArray(name)
			name=str

		Disables the vertex array at location in this shader program that was enabled by a previous call to PySide.QtOpenGL.QGLShaderProgram.enableAttributeArray() .
		"""
		res = super(QGLShaderProgram,self).disableAttributeArray(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def enableAttributeArray(self,*args,**kwargs):
		"""
		enableAttributeArray(location)
			location=QtCore.int

		enableAttributeArray(name)
			name=str

		Enables the vertex array at location in this shader program so that the value set by PySide.QtOpenGL.QGLShaderProgram.setAttributeArray() on location will be used by the shader program.
		"""
		res = super(QGLShaderProgram,self).enableAttributeArray(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def removeShader(self,shader):
		"""
		removeShader(shader)
			shader=QtOpenGL.QGLShader

		Removes shader from this shader program
		The object is not deleted.
		"""
		res = super(QGLShaderProgram,self).removeShader(shader)
		return res
	#----------------------------------------------------------------------
	def setAttributeArray(self,*args,**kwargs):
		"""
		setAttributeArray(name,values,tupleSize,stride=None)
			name=str
			values=QtCore.float
			tupleSize=QtCore.int
			stride=QtCore.int

		setAttributeArray(location,values,tupleSize,stride=None)
			location=QtCore.int
			values=QtCore.float
			tupleSize=QtCore.int
			stride=QtCore.int


		"""
		res = super(QGLShaderProgram,self).setAttributeArray(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setAttributeArray2D(self,*args,**kwargs):
		"""
		setAttributeArray2D(name,values,stride=None)
			name=str
			values=QtGui.QVector2D
			stride=QtCore.int

		setAttributeArray2D(location,values,stride=None)
			location=QtCore.int
			values=QtGui.QVector2D
			stride=QtCore.int

		This is an overloaded function.
		Sets an array of 2D vertex values on the attribute called name in this shader program
		The stride indicates the number of bytes between vertices
		A default stride value of zero indicates that the vertices are densely packed in values .
		The array will become active when PySide.QtOpenGL.QGLShaderProgram.enableAttributeArray() is called on name
		Otherwise the value specified with PySide.QtOpenGL.QGLShaderProgram.setAttributeValue() for name will be used.
		"""
		res = super(QGLShaderProgram,self).setAttributeArray2D(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setAttributeArray3D(self,*args,**kwargs):
		"""
		setAttributeArray3D(location,values,stride=None)
			location=QtCore.int
			values=QtGui.QVector3D
			stride=QtCore.int

		setAttributeArray3D(name,values,stride=None)
			name=str
			values=QtGui.QVector3D
			stride=QtCore.int

		Sets an array of 3D vertex values on the attribute at location in this shader program
		The stride indicates the number of bytes between vertices
		A default stride value of zero indicates that the vertices are densely packed in values .
		The array will become active when PySide.QtOpenGL.QGLShaderProgram.enableAttributeArray() is called on the location
		Otherwise the value specified with PySide.QtOpenGL.QGLShaderProgram.setAttributeValue() for location will be used.
		"""
		res = super(QGLShaderProgram,self).setAttributeArray3D(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setAttributeArray4D(self,*args,**kwargs):
		"""
		setAttributeArray4D(name,values,stride=None)
			name=str
			values=QtGui.QVector4D
			stride=QtCore.int

		setAttributeArray4D(location,values,stride=None)
			location=QtCore.int
			values=QtGui.QVector4D
			stride=QtCore.int

		This is an overloaded function.
		Sets an array of 4D vertex values on the attribute called name in this shader program
		The stride indicates the number of bytes between vertices
		A default stride value of zero indicates that the vertices are densely packed in values .
		The array will become active when PySide.QtOpenGL.QGLShaderProgram.enableAttributeArray() is called on name
		Otherwise the value specified with PySide.QtOpenGL.QGLShaderProgram.setAttributeValue() for name will be used.
		"""
		res = super(QGLShaderProgram,self).setAttributeArray4D(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setAttributeBuffer(self,*args,**kwargs):
		"""
		setAttributeBuffer(location,type,offset,tupleSize,stride=None)
			location=QtCore.int
			type=long
			offset=QtCore.int
			tupleSize=QtCore.int
			stride=QtCore.int

		setAttributeBuffer(name,type,offset,tupleSize,stride=None)
			name=str
			type=long
			offset=QtCore.int
			tupleSize=QtCore.int
			stride=QtCore.int


		"""
		res = super(QGLShaderProgram,self).setAttributeBuffer(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setAttributeValue(self,*args,**kwargs):
		"""
		setAttributeValue(location,value)
			location=QtCore.int
			value=QtGui.QVector4D

		setAttributeValue(location,value)
			location=QtCore.int
			value=QtGui.QVector2D

		setAttributeValue(location,value)
			location=QtCore.int
			value=QtGui.QVector3D

		setAttributeValue(location,value)
			location=QtCore.int
			value=QtCore.float

		setAttributeValue(location,value)
			location=QtCore.int
			value=QtGui.QColor

		setAttributeValue(location,x,y,z,w)
			location=QtCore.int
			x=QtCore.float
			y=QtCore.float
			z=QtCore.float
			w=QtCore.float

		setAttributeValue(location,x,y)
			location=QtCore.int
			x=QtCore.float
			y=QtCore.float

		setAttributeValue(location,x,y,z)
			location=QtCore.int
			x=QtCore.float
			y=QtCore.float
			z=QtCore.float

		setAttributeValue(name,x,y,z,w)
			name=str
			x=QtCore.float
			y=QtCore.float
			z=QtCore.float
			w=QtCore.float

		setAttributeValue(name,value)
			name=str
			value=QtGui.QColor

		setAttributeValue(name,value)
			name=str
			value=QtGui.QVector2D

		setAttributeValue(name,value)
			name=str
			value=QtGui.QVector4D

		setAttributeValue(name,value)
			name=str
			value=QtGui.QVector3D

		setAttributeValue(name,x,y)
			name=str
			x=QtCore.float
			y=QtCore.float

		setAttributeValue(name,x,y,z)
			name=str
			x=QtCore.float
			y=QtCore.float
			z=QtCore.float

		setAttributeValue(name,value)
			name=str
			value=QtCore.float

		Sets the attribute at location in the current context to value .
		"""
		res = super(QGLShaderProgram,self).setAttributeValue(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setGeometryInputType(self,inputType):
		"""
		setGeometryInputType(inputType)
			inputType=long


		"""
		res = super(QGLShaderProgram,self).setGeometryInputType(inputType)
		return res
	#----------------------------------------------------------------------
	def setGeometryOutputType(self,outputType):
		"""
		setGeometryOutputType(outputType)
			outputType=long


		"""
		res = super(QGLShaderProgram,self).setGeometryOutputType(outputType)
		return res
	#----------------------------------------------------------------------
	def setGeometryOutputVertexCount(self,count):
		"""
		setGeometryOutputVertexCount(count)
			count=QtCore.int

		Sets the maximum number of vertices the current geometry shader program will produce, if active, to count .
		This parameter takes effect the next time the program is linked.
		"""
		res = super(QGLShaderProgram,self).setGeometryOutputVertexCount(count)
		return res
	#----------------------------------------------------------------------
	def setUniformValue(self,*args,**kwargs):
		"""
		setUniformValue(location,value)
			location=QtCore.int
			value=QtGui.QMatrix3x3

		setUniformValue(location,value)
			location=QtCore.int
			value=QtGui.QMatrix3x4

		setUniformValue(location,value)
			location=QtCore.int
			value=QtGui.QMatrix4x2

		setUniformValue(location,value)
			location=QtCore.int
			value=QtGui.QMatrix4x3

		setUniformValue(location,value)
			location=QtCore.int
			value=QtGui.QMatrix3x2

		setUniformValue(location,value)
			location=QtCore.int
			value=QtGui.QMatrix2x3

		setUniformValue(location,value)
			location=QtCore.int
			value=QtGui.QMatrix2x4

		setUniformValue(location,value)
			location=QtCore.int
			value=QtGui.QMatrix2x2

		setUniformValue(location,value)
			location=QtCore.int
			value=QtGui.QMatrix4x4

		setUniformValue(location,color)
			location=QtCore.int
			color=QtGui.QColor

		setUniformValue(location,point)
			location=QtCore.int
			point=QtCore.QPointF

		setUniformValue(location,x,y)
			location=QtCore.int
			x=QtCore.float
			y=QtCore.float

		setUniformValue(location,point)
			location=QtCore.int
			point=QtCore.QPoint

		setUniformValue(location,x,y,z)
			location=QtCore.int
			x=QtCore.float
			y=QtCore.float
			z=QtCore.float

		setUniformValue(location,value)
			location=QtCore.int
			value=QtCore.int

		setUniformValue(location,value)
			location=QtCore.int
			value=long

		setUniformValue(location,x,y,z,w)
			location=QtCore.int
			x=QtCore.float
			y=QtCore.float
			z=QtCore.float
			w=QtCore.float

		setUniformValue(location,value)
			location=QtCore.int
			value=QtCore.float

		setUniformValue(location,value)
			location=QtCore.int
			value=QtGui.QVector4D

		setUniformValue(location,size)
			location=QtCore.int
			size=QtCore.QSize

		setUniformValue(location,value)
			location=QtCore.int
			value=QtGui.QTransform

		setUniformValue(location,value)
			location=QtCore.int
			value=QtGui.QVector3D

		setUniformValue(location,size)
			location=QtCore.int
			size=QtCore.QSizeF

		setUniformValue(location,value)
			location=QtCore.int
			value=QtGui.QVector2D

		setUniformValue(name,value)
			name=str
			value=QtGui.QMatrix3x2

		setUniformValue(name,value)
			name=str
			value=QtGui.QMatrix4x4

		setUniformValue(name,value)
			name=str
			value=QtGui.QMatrix3x3

		setUniformValue(name,value)
			name=str
			value=QtGui.QMatrix4x2

		setUniformValue(name,value)
			name=str
			value=QtGui.QMatrix4x3

		setUniformValue(name,value)
			name=str
			value=QtGui.QMatrix3x4

		setUniformValue(name,value)
			name=str
			value=QtGui.QMatrix2x4

		setUniformValue(name,value)
			name=str
			value=QtGui.QMatrix2x3

		setUniformValue(name,color)
			name=str
			color=QtGui.QColor

		setUniformValue(name,value)
			name=str
			value=QtGui.QMatrix2x2

		setUniformValue(name,value)
			name=str
			value=long

		setUniformValue(name,value)
			name=str
			value=QtCore.float

		setUniformValue(name,value)
			name=str
			value=QtGui.QVector4D

		setUniformValue(name,x,y)
			name=str
			x=QtCore.float
			y=QtCore.float

		setUniformValue(name,x,y,z,w)
			name=str
			x=QtCore.float
			y=QtCore.float
			z=QtCore.float
			w=QtCore.float

		setUniformValue(name,value)
			name=str
			value=QtCore.int

		setUniformValue(name,x,y,z)
			name=str
			x=QtCore.float
			y=QtCore.float
			z=QtCore.float

		setUniformValue(name,point)
			name=str
			point=QtCore.QPoint

		setUniformValue(name,point)
			name=str
			point=QtCore.QPointF

		setUniformValue(name,size)
			name=str
			size=QtCore.QSize

		setUniformValue(name,size)
			name=str
			size=QtCore.QSizeF

		setUniformValue(name,value)
			name=str
			value=QtGui.QVector3D

		setUniformValue(name,value)
			name=str
			value=QtGui.QTransform

		setUniformValue(name,value)
			name=str
			value=QtGui.QVector2D

		Sets the uniform variable at location in the current context to a 3x3 matrix value .
		"""
		res = super(QGLShaderProgram,self).setUniformValue(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setUniformValueArray(self,*args,**kwargs):
		"""
		setUniformValueArray(location,values,count,tupleSize)
			location=QtCore.int
			values=QtCore.float
			count=QtCore.int
			tupleSize=QtCore.int

		setUniformValueArray(name,values,count,tupleSize)
			name=str
			values=QtCore.float
			count=QtCore.int
			tupleSize=QtCore.int


		"""
		res = super(QGLShaderProgram,self).setUniformValueArray(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setUniformValueArray2D(self,*args,**kwargs):
		"""
		setUniformValueArray2D(location,values)
			location=QtCore.int
			values=QtGui.QVector2D

		setUniformValueArray2D(name,values)
			name=str
			values=QtGui.QVector2D

		Sets the uniform variable array at location in the current context to the count 2D vector elements of values .
		"""
		res = super(QGLShaderProgram,self).setUniformValueArray2D(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setUniformValueArray2x2(self,*args,**kwargs):
		"""
		setUniformValueArray2x2(location,values)
			location=QtCore.int
			values=QtGui.QMatrix2x2

		setUniformValueArray2x2(name,values)
			name=str
			values=QtGui.QMatrix2x2

		Sets the uniform variable array at location in the current context to the count 2x2 matrix elements of values .
		"""
		res = super(QGLShaderProgram,self).setUniformValueArray2x2(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setUniformValueArray2x3(self,*args,**kwargs):
		"""
		setUniformValueArray2x3(location,values)
			location=QtCore.int
			values=QtGui.QMatrix2x3

		setUniformValueArray2x3(name,values)
			name=str
			values=QtGui.QMatrix2x3

		Sets the uniform variable array at location in the current context to the count 2x3 matrix elements of values .
		"""
		res = super(QGLShaderProgram,self).setUniformValueArray2x3(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setUniformValueArray2x4(self,*args,**kwargs):
		"""
		setUniformValueArray2x4(location,values)
			location=QtCore.int
			values=QtGui.QMatrix2x4

		setUniformValueArray2x4(name,values)
			name=str
			values=QtGui.QMatrix2x4

		Sets the uniform variable array at location in the current context to the count 2x4 matrix elements of values .
		"""
		res = super(QGLShaderProgram,self).setUniformValueArray2x4(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setUniformValueArray3D(self,*args,**kwargs):
		"""
		setUniformValueArray3D(name,values)
			name=str
			values=QtGui.QVector3D

		setUniformValueArray3D(location,values)
			location=QtCore.int
			values=QtGui.QVector3D

		This is an overloaded function.
		Sets the uniform variable array called name in the current context to the count 3D vector elements of values .
		"""
		res = super(QGLShaderProgram,self).setUniformValueArray3D(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setUniformValueArray3x2(self,*args,**kwargs):
		"""
		setUniformValueArray3x2(location,values)
			location=QtCore.int
			values=QtGui.QMatrix3x2

		setUniformValueArray3x2(name,values)
			name=str
			values=QtGui.QMatrix3x2

		Sets the uniform variable array at location in the current context to the count 3x2 matrix elements of values .
		"""
		res = super(QGLShaderProgram,self).setUniformValueArray3x2(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setUniformValueArray3x3(self,*args,**kwargs):
		"""
		setUniformValueArray3x3(location,values)
			location=QtCore.int
			values=QtGui.QMatrix3x3

		setUniformValueArray3x3(name,values)
			name=str
			values=QtGui.QMatrix3x3

		Sets the uniform variable array at location in the current context to the count 3x3 matrix elements of values .
		"""
		res = super(QGLShaderProgram,self).setUniformValueArray3x3(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setUniformValueArray3x4(self,*args,**kwargs):
		"""
		setUniformValueArray3x4(location,values)
			location=QtCore.int
			values=QtGui.QMatrix3x4

		setUniformValueArray3x4(name,values)
			name=str
			values=QtGui.QMatrix3x4

		Sets the uniform variable array at location in the current context to the count 3x4 matrix elements of values .
		"""
		res = super(QGLShaderProgram,self).setUniformValueArray3x4(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setUniformValueArray4D(self,*args,**kwargs):
		"""
		setUniformValueArray4D(location,values)
			location=QtCore.int
			values=QtGui.QVector4D

		setUniformValueArray4D(name,values)
			name=str
			values=QtGui.QVector4D

		Sets the uniform variable array at location in the current context to the count 4D vector elements of values .
		"""
		res = super(QGLShaderProgram,self).setUniformValueArray4D(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setUniformValueArray4x2(self,*args,**kwargs):
		"""
		setUniformValueArray4x2(location,values)
			location=QtCore.int
			values=QtGui.QMatrix4x2

		setUniformValueArray4x2(name,values)
			name=str
			values=QtGui.QMatrix4x2

		Sets the uniform variable array at location in the current context to the count 4x2 matrix elements of values .
		"""
		res = super(QGLShaderProgram,self).setUniformValueArray4x2(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setUniformValueArray4x3(self,*args,**kwargs):
		"""
		setUniformValueArray4x3(name,values)
			name=str
			values=QtGui.QMatrix4x3

		setUniformValueArray4x3(location,values)
			location=QtCore.int
			values=QtGui.QMatrix4x3

		This is an overloaded function.
		Sets the uniform variable array called name in the current context to the count 4x3 matrix elements of values .
		"""
		res = super(QGLShaderProgram,self).setUniformValueArray4x3(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setUniformValueArray4x4(self,*args,**kwargs):
		"""
		setUniformValueArray4x4(location,values)
			location=QtCore.int
			values=QtGui.QMatrix4x4

		setUniformValueArray4x4(name,values)
			name=str
			values=QtGui.QMatrix4x4

		Sets the uniform variable array at location in the current context to the count 4x4 matrix elements of values .
		"""
		res = super(QGLShaderProgram,self).setUniformValueArray4x4(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setUniformValueArrayInt(self,*args,**kwargs):
		"""
		setUniformValueArrayInt(name,values)
			name=str
			values=QtCore.int

		setUniformValueArrayInt(location,values)
			location=QtCore.int
			values=QtCore.int


		"""
		res = super(QGLShaderProgram,self).setUniformValueArrayInt(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def setUniformValueArrayUint(self,*args,**kwargs):
		"""
		setUniformValueArrayUint(location,values)
			location=QtCore.int
			values=long

		setUniformValueArrayUint(name,values)
			name=str
			values=long


		"""
		res = super(QGLShaderProgram,self).setUniformValueArrayUint(*args,**kwargs)
		return res
	#----------------------------------------------------------------------
	def uniformLocation(self,*args,**kwargs):
		"""
		uniformLocation(name)
			name=str

		uniformLocation(name)
			name=unicode

		uniformLocation(name)
			name=QtCore.QByteArray

		Returns the location of the uniform variable name within this shader programs parameter list
		Returns -1 if name is not a valid uniform variable for this shader program.
		"""
		res = super(QGLShaderProgram,self).uniformLocation(*args,**kwargs)
		isinstance(res,int)
		return res

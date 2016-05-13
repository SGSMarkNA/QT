from PySide import QtGui, QtCore

class QGLShader(QtOpenGL.QGLShader):
	''''''
	def __init__(self,*args,**kwargs):
		''''''
		super(QGLShader,self).__init__(*args,**kwargs)
	#----------------------------------------------------------------------
	def isCompiled(self):
		"""
		Returns true if this shader has been compiled; false otherwise.
		"""
		res = super(QGLShader,self).isCompiled()
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def log(self):
		"""
		Returns the errors and warnings that occurred during the last compile.
		"""
		res = super(QGLShader,self).log()
		return res
	#----------------------------------------------------------------------
	def shaderId(self):
		"""
		Returns the OpenGL identifier associated with this shader.
		"""
		res = super(QGLShader,self).shaderId()
		return res
	#----------------------------------------------------------------------
	def shaderType(self):
		"""
		Returns the type of this shader.
		"""
		res = super(QGLShader,self).shaderType()
		isinstance(res,QtOpenGL.QGLShader.ShaderType)
		return res
	#----------------------------------------------------------------------
	def sourceCode(self):
		"""
		Returns the source code for this shader.
		"""
		res = super(QGLShader,self).sourceCode()
		isinstance(res,QtCore.QByteArray)
		return res
	#----------------------------------------------------------------------
	def compileSourceCode(self,*args,**kwargs):
		"""
		compileSourceCode(source)
			source=str

		compileSourceCode(source)
			source=QtCore.QByteArray

		compileSourceCode(source)
			source=unicode

		Sets the source code for this shader and compiles it
		Returns true if the source was successfully compiled, false otherwise.
		"""
		res = super(QGLShader,self).compileSourceCode(*args,**kwargs)
		isinstance(res,QtCore.bool)
		return res
	#----------------------------------------------------------------------
	def compileSourceFile(self,fileName):
		"""
		compileSourceFile(fileName)
			fileName=unicode

		Sets the source code for this shader to the contents of fileName and compiles it
		Returns true if the file could be opened and the source compiled, false otherwise.
		"""
		res = super(QGLShader,self).compileSourceFile(fileName)
		isinstance(res,QtCore.bool)
		return res

import os

if os.environ["QT_PACKAGE"] == "PySide":
	from PySide import QtCore,QtGui
	from Py_Side import pysideuic
	from cStringIO import StringIO
	import xml.etree.ElementTree as xml

elif os.environ["QT_PACKAGE"] == "PyQt4":
	from PyQt4 import QtCore,QtGui
	from PY_QT4 import uic
	
else:
	raise EnvironmentError("Could Not Determan The Proper Python Qt Package To Load set the env varible 'QT_PACKAGE' to eather PyQt4 or PySide")

def PyQt4_Reader(uiFile):
	form_class, base_class = uic.loadUiType(str(uiFile),from_imports=False)
	return form_class, base_class

def PySide_Reader(uiFile):
	parsed = xml.parse(uiFile)
	widget_class = parsed.find('widget').get('class')

	form_class = parsed.find('class').text
	with open(uiFile, 'r') as f:
		o = StringIO()
		frame = {}

		pysideuic.compileUi(f, o, indent=0)
		pyc = compile(o.getvalue(), '<string>', 'exec')
		exec pyc in frame

		#Fetch the base_class and form class based on their type in the xml from designer
		form_class = frame['Ui_%s'%form_class]
		base_class = eval('QtGui.%s'%widget_class)
	return form_class, base_class

def loadUiType(uiFile):
	"""
	Pyside "loadUiType" command like PyQt4 has one, so we have to convert the ui file to py code in-memory first    and then execute it in a special frame to retrieve the form_class.
	"""
	if os.environ["QT_PACKAGE"] == "PyQt4":
		if not os.path.exists(uiFile):
			uiFile.replace(".uic", ".ui")
		form_class, base_class  = PyQt4_Reader(uiFile)

	elif os.environ["QT_PACKAGE"] == "PySide":
		form_class, base_class = PySide_Reader(uiFile)

	return form_class, base_class
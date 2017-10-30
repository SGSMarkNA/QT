import os
import xml.etree.ElementTree as xml

QT_PACKAGE = os.environ.get("QT_PACKAGE")
try:
        import maya.cmds as cmds
	MAYA_VERSION    = int(cmds.about(version=True))
except:
	MAYA_VERSION = 2015

if QT_PACKAGE is None:
	if MAYA_VERSION >= 2017:
		QT_PACKAGE =  "PySide2"
		os.environ["QT_PACKAGE"] = "PySide2"
	elif MAYA_VERSION >= 2013:
		QT_PACKAGE =  "PySide"
		os.environ["QT_PACKAGE"] = "PySide"

if os.environ["QT_PACKAGE"] == "PySide2":
	from PySide2.QtCore import *
	from PySide2.QtGui import *
	from PySide2.QtWidgets import *
	import pyside2uic as pysideuic
	from cStringIO import StringIO

elif os.environ["QT_PACKAGE"] == "PySide":
	from PySide.QtCore import *
	from PySide.QtGui import *
	try:
		from Py_Side import pysideuic
	except Exception:
		pass
	from cStringIO import StringIO

elif os.environ["QT_PACKAGE"] == "PyQt4":
	from PyQt4.QtCore import *
	from PyQt4.QtGui import *
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
		base_class = eval('%s'%widget_class)
	return form_class, base_class

def loadUiType(uiFile):
	"""
	Pyside "loadUiType" command like PyQt4 has one, so we have to convert the ui file to py code in-memory first    and then execute it in a special frame to retrieve the form_class.
	"""
	if os.environ["QT_PACKAGE"] == "PyQt4":
		if not os.path.exists(uiFile):
			uiFile.replace(".uic", ".ui")
		form_class, base_class  = PyQt4_Reader(uiFile)

	elif os.environ["QT_PACKAGE"] == "PySide" or os.environ["QT_PACKAGE"] == "PySide2":
		form_class, base_class = PySide_Reader(uiFile)

	return form_class, base_class

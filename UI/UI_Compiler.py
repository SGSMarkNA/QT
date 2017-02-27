import os, glob, sys

def PySide_Generator(ui_folder, py_folder,ui_files=[]):
	try:
		from QT.UI.Py_Side import pysideuic
	except ImportError:
		import pyside2uic
		pysideuic = pyside2uic
	if len(ui_files):
		ui_file_names = ui_files
	else:
		ui_file_names = [os.path.basename(f).split(".")[0] for f in glob.glob(ui_folder+"\\*.ui")]
	
	for ui in ui_file_names:
	
		code_file = str(ui+".py")
		ui_file   = str(ui+".ui")
		code_path = os.path.join(py_folder,code_file)
		ui_path   = os.path.join(ui_folder,ui_file)
		py_file = file(code_path, "w")
		pysideuic.compileUi(ui_path, py_file, execute=True, indent=0, from_imports=False)
		
def PyQt4_Generator(ui_folder, py_folder,ui_files=[]):
	command_args   = " -x -i 0 "

	python_exe    = os.sys.executable
	uic_file      = os.path.join(os.path.dirname(__file__),"uic","pyuic.py")

	if len(ui_files):
		ui_file_names = ui_files
	else:
		ui_file_names = [os.path.basename(f).split(".")[0] for f in glob.glob(ui_folder+"\\*.ui")]

	for ui in ui_file_names:

		code_file = str(ui+".py")
		ui_file   = str(ui+".ui")

		code_path = os.path.join(py_folder,code_file)
		ui_path   = os.path.join(ui_folder,ui_file)
		cmd = python_exe + uic_file + command_args + " -o " + '"' + code_path + '"' + " " + '"' + ui_path + '"'
		print cmd
		print os.system(cmd)
		
def build_ui_files(ui_folder, py_folder, ui_files=[], from_imports=True, make_PySide=True, preview=False):
	if not os.path.exists(ui_folder):
		raise IOError("The Input UI Folder That Contains QtDesigner Files Does Not Exist\n%r" % ui_folder)
	if not os.path.exists(py_folder):
		raise IOError("The Input Python Code Output Folder Does Not Exist\n%r" % py_folder)
	if make_PySide:
		PySide_Generator(ui_folder, py_folder, ui_files)
	else:
		PyQt4_Generator(ui_folder, py_folder, ui_files)


#!C:/python27/python.exe
# -*- encoding:utf8 -*-
from distutils.core import setup
from py2exe.build_exe import py2exe

#windows
windows = ['run.py', ]

### options ###
# includes = ['sip','PyQt4.QtGui','PyQt4.QtCore',]
includes = ['sip',]
bundle_files = 1
excludes = [
    #"Tkconstants", "Tkinter", "tcl",
    #"_imagingtk", "PIL._imagingtk",
    #"ImageTk", "PIL.ImageTk", "FixTk", "kinterbasdb",
    #"MySQLdb", 'Numeric', 'OpenGL.GL', 'OpenGL.GLUT',
    #'dbGadfly', 'email.Generator',
    #'email.Iterators', 'email.Utils', 'kinterbasdb',
    #'numarray', 'pymssql', 'pysqlite2', 'wx.BitmapFromImage',
    ]
# dll_excludes = ['MSVCP90.dll','MSWSOCK.dll','mswsock.dll','powrprof.dll',]
dll_excludes = ['MSVCP90.dll',]

options = dict()
options['py2exe']=dict()
options['py2exe']['includes'] = includes
options['py2exe']['bundle_files'] = bundle_files
options['py2exe']['excludes'] = excludes
options['py2exe']['dll_excludes'] = dll_excludes

setup(
    windows = windows,
    options = options,
    zipfile=None,
    )

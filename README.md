Python based oneshot to purge saved crews from RescueNet ePCR.

Required additional libraries:
-pyodbc
-psutil

Install with:
pip3 install pyodbc psutil

Compile with:
pyinstaller --onefile purge_crews.py

OR, you can use the precompiled .exe

Usage:
purge_crews.exe --username fielddata --password [SQL Password]

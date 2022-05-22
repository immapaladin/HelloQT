# HelloQT
This is a standalone desktop app to upload survey data to a predefined folder structure.

## Technologies
* Python 3.10
* PySide6
* QT 6
* Nuitka 0.6.19

## Setup
To use this project, install the libraries using listed in the requirments.txt

```
 pip install -r requirements.txt
 
```
To convert the .ui file inot a py file:
```
pyside6-uic form.ui > form.py
 ```
To compile to a stand alone exe:
```
python -m nuitka --onefile --enable-plugin=pyside6 --windows-disable-console widget.py
```


# This Python file uses the following encoding: utf-8
import os
# from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog

"""
from PySide6.QtCore import QFile, Signal, Slot
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtGui, QtCore
"""
from form import Ui_Widget
import shutil
import pathlib


class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super(Widget, self).__init__()
        self.project = None
        self.note_name = None
        self.static_name = None
        self.img_name = None
        self.mjf_name = None
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.btn_upload.clicked.connect(
            lambda: self.make_survey_folders(self.ui.text_pnum.text(), self.ui.text_name.text(),
                                             self.ui.comboBox.currentText()))
        self.ui.btn_mjf.clicked.connect(lambda: self.mjf_file())
        self.ui.btn_static.clicked.connect(lambda: self.static_files())
        self.ui.btn_notes.clicked.connect(lambda: self.note_files())
        self.ui.btn_img.clicked.connect(lambda: self.images_files())
        self.ui.textBrowser.setText("Output:")

    def oops(self, msg):
        box = QMessageBox.critical(self, "error", msg)
        return box

    # functions for opening file dialogs

    def print_items(self, items):
        for file in items[0]:
            self.ui.textBrowser.append(os.path.basename(file))

    def mjf_file(self):
        """
        opens file dialog window and only accepts mjf files
        :return: a list of all selected files
        """
        self.mjf_name = QFileDialog.getOpenFileNames(self, 'Open file', 'c:\\', "MJF files (*.mjf)")
        self.ui.textBrowser.append("mjf files selected:")
        self.print_items(self.mjf_name)
        return

    def images_files(self):
        """
        opens file dialog window and only accepts pdf, jpg and png files
        :return: a list of all selected file
        """
        self.img_name = QFileDialog.getOpenFileNames(self, 'Open file', 'c:\\', "Image files (*.jpg *.jpeg *.png)")
        self.ui.textBrowser.append("Images files selected:")
        self.print_items(self.img_name)
        return

    def static_files(self):
        """
        opens file dialog window and only accepts tps files
        :return:  a list of all selected file
        """
        self.static_name = QFileDialog.getOpenFileNames(self, 'Open file', 'c:\\', "Static files (*.tps)")
        self.ui.textBrowser.append("Static files selected:")
        self.print_items(self.static_name)
        return

    def note_files(self):
        """
        opens file dialog window and only accepts jpg, pdf and png  files
        :return:a list of all selected fil
        """
        self.note_name = QFileDialog.getOpenFileNames(self, 'Open file', 'c:\\',
                                                      "Note files (*.jpg *.jpeg *.pdf *.png)")
        self.ui.textBrowser.append("Note files selected:")
        self.print_items(self.note_name)
        return

    def copy_files(self):
        """
            Copies files to their correct folder in the given survey name
            Skips if they already exist
        :return: Nothing
        """
        self.ui.textBrowser.setText("Output:")
        if self.mjf_name is None:
            print('Skipped MJF')
        else:
            for mjf in self.mjf_name[0]:
                file = os.path.basename(mjf)
                if os.path.exists(fr"{self.project}\{self.ui.text_name.text()}\RAW\RTK\{file}"):
                    self.exists_msg(file)
                else:
                    shutil.copy(mjf, fr"{self.project}\{self.ui.text_name.text()}\RAW\RTK")

        if self.img_name is None:
            print('Skipped Images')
        else:
            for img in self.img_name[0]:
                print(img)
                file = os.path.basename(img)
                if os.path.exists(fr"{self.project}\{self.ui.text_name.text()}\REPORT\{file}"):
                    self.exists_msg(file)
                else:
                    shutil.copy(img, fr"{self.project}\{self.ui.text_name.text()}\REPORT")

        if self.static_name is None:
            print('Skipped Static')
        else:
            for static in self.static_name[0]:
                file = os.path.basename(static)
                if os.path.exists(fr"{self.project}\{self.ui.text_name.text()}\RAW\STATIC\{file}"):
                    self.exists_msg(file)
                else:
                    shutil.copy(static, fr"{self.project}\{self.ui.text_name.text()}\RAW\STATIC")

        if self.note_name is None:
            print('Skipped notes')
        else:
            for note in self.note_name[0]:
                file = os.path.basename(note)
                if os.path.exists(fr"{self.project}\{self.ui.text_name.text()}\REPORT{file}"):
                    self.exists_msg(file)
                else:
                    shutil.copy(note, fr"{self.project}\{self.ui.text_name.text()}\REPORT")
        return

    # set variables to none
    def rest_files(self):
        """
        resets input files to None
        :return: Nothing
        """
        self.note_name = None
        self.static_name = None
        self.img_name = None
        self.mjf_name = None

    def exists_msg(self, a):
        self.ui.textBrowser.append(f"{a} skipped as it already exists")

    # main function to upload data

    def make_survey_folders(self, p_num, survey_name, depart):
        # checks if project and survey folder exist
        year = p_num[:2]
        print(depart)
        if len(survey_name) == 0 or len(p_num) == 0:
            result = "Survey name or Project number can't be empty "
            self.oops(result)
            return
        elif os.path.exists(fr"C:\Projects\20{year}\{p_num}\Design\{depart}\SURVEY"):
            self.project = fr"C:\Projects\20{year}\{p_num}\Design\{depart}\SURVEY"
        elif os.path.exists(fr"R:\Projects\20{year}\{p_num}\Design\{depart}\SURVEY"):
            self.project = fr"R:\Projects\20{year}\{p_num}\Design\{depart}\SURVEY"
        else:
            self.project = ""
        # if survey folder already exists, just copy files and do not create folders
        if os.path.exists(fr"{self.project}\{survey_name}"):
            parent_dir = fr"{self.project}\{survey_name}"
            self.copy_files()
            self.ui.textBrowser.append(f"{survey_name} now contains the following: ")
            for path in sorted(pathlib.Path(parent_dir).rglob('*')):
                depth = len(path.relative_to(parent_dir).parts)
                spacer = '    ' * depth
                self.ui.textBrowser.append(f'{spacer}+ {path.name}')
            self.rest_files()

        elif self.project != "" and survey_name != "":
            parent_dir = fr"{self.project}\{survey_name}"
            survey_folders = ["EXPORT", "IMPORT", "RAW", "REPORT"]
            export_folders = ["NAMENEZCODE", "SHP"]
            raw_folders = ["RTK", "STATIC"]

            for s_folders in survey_folders:
                os.makedirs(os.path.join(parent_dir, s_folders))

            for e_folders in export_folders:
                os.makedirs(os.path.join(parent_dir, survey_folders[0], e_folders))

            for r_folders in raw_folders:
                os.makedirs(os.path.join(parent_dir, survey_folders[2], r_folders))
            # checks if a file has been selected for each type.
            self.copy_files()
            # adds output message to text browser
            self.ui.textBrowser.append(f"The following files have been created: ")
            self.ui.textBrowser.append(f"+{survey_name}")
            for path in sorted(pathlib.Path(parent_dir).rglob('*')):
                depth = len(path.relative_to(parent_dir).parts)
                spacer = '    ' * depth
                self.ui.textBrowser.append(f'{spacer}+ {path.name}')
        else:
            result = f"Oh snap! Something went wrong \n Most likely you need to creat a folder outside of FMS"
            print('cows')
            self.oops(result)

        return


if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()
    sys.exit(app.exec())

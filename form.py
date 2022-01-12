

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTextBrowser, QTextEdit, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        Widget.setAutoFillBackground(False)
        Widget.setStyleSheet(u"color: rgb(221, 221, 221);\n"
"background-color: rgb(40, 44, 52);\n"
"")
        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(250, 80, 251, 101))
        self.frame.setCursor(QCursor(Qt.ArrowCursor))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lable_pnum = QLabel(self.frame)
        self.lable_pnum.setObjectName(u"lable_pnum")
        self.lable_pnum.setGeometry(QRect(10, 10, 91, 16))
        self.text_name = QLineEdit(self.frame)
        self.text_name.setObjectName(u"text_name")
        self.text_name.setGeometry(QRect(100, 60, 131, 24))
        self.text_pnum = QLineEdit(self.frame)
        self.text_pnum.setObjectName(u"text_pnum")
        self.text_pnum.setGeometry(QRect(100, 10, 131, 24))
        self.label_name = QLabel(self.frame)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(10, 60, 81, 16))
        self.line = QFrame(Widget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(210, 190, 341, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(Widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(207, 270, 351, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.btn_upload = QPushButton(Widget)
        self.btn_upload.setObjectName(u"btn_upload")
        self.btn_upload.setGeometry(QRect(330, 310, 101, 24))
        self.btn_upload.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_upload.setCheckable(False)
        self.btn_upload.setFlat(False)
        self.layoutWidget = QWidget(Widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(210, 220, 340, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_img = QPushButton(self.layoutWidget)
        self.btn_img.setObjectName(u"btn_img")
        self.btn_img.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_img)

        self.btn_notes = QPushButton(self.layoutWidget)
        self.btn_notes.setObjectName(u"btn_notes")
        self.btn_notes.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_notes)

        self.btn_static = QPushButton(self.layoutWidget)
        self.btn_static.setObjectName(u"btn_static")
        self.btn_static.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_static)

        self.btn_mjf = QPushButton(self.layoutWidget)
        self.btn_mjf.setObjectName(u"btn_mjf")
        self.btn_mjf.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_mjf)

        self.textBrowser = QTextBrowser(Widget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(210, 350, 331, 231))
        self.textBrowser.setStyleSheet(u"color: rgb(33, 37, 43);\n"
"background-color: rgba(221, 221, 221, 180);")
        self.textBrowser.setFrameShape(QFrame.StyledPanel)
        self.textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.textBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.textBrowser.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.textBrowser.setLineWrapMode(QTextEdit.WidgetWidth)
        self.textBrowser.setLineWrapColumnOrWidth(0)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Survey File  Up Loader", None))
        self.lable_pnum.setText(QCoreApplication.translate("Widget", u"Project Number", None))
#if QT_CONFIG(tooltip)
        self.text_name.setToolTip(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" color:#000000;\">Survey name, usually date and description</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.text_pnum.setToolTip(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" color:#000000;\">can be a R or P drive project</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.text_pnum.setInputMask(QCoreApplication.translate("Widget", u"99-9999-999", None))
        self.text_pnum.setText(QCoreApplication.translate("Widget", u"22-0000-000", None))
        self.label_name.setText(QCoreApplication.translate("Widget", u"Survey Name", None))
#if QT_CONFIG(tooltip)
        self.btn_upload.setToolTip(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" color:#000000;\">create folder and upload data. if folder exists just upload data</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_upload.setText(QCoreApplication.translate("Widget", u" Upload", None))
#if QT_CONFIG(tooltip)
        self.btn_img.setToolTip(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" color:#000000;\">select photos from survey</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_img.setText(QCoreApplication.translate("Widget", u"Images", None))
#if QT_CONFIG(tooltip)
        self.btn_notes.setToolTip(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" color:#000000;\">select survey notes</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_notes.setText(QCoreApplication.translate("Widget", u"Notes", None))
#if QT_CONFIG(tooltip)
        self.btn_static.setToolTip(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" color:#000000;\">select static files</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_static.setText(QCoreApplication.translate("Widget", u"Static", None))
#if QT_CONFIG(tooltip)
        self.btn_mjf.setToolTip(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" color:#000000;\">select survey job file</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_mjf.setText(QCoreApplication.translate("Widget", u"MJF", None))
    # retranslateUi


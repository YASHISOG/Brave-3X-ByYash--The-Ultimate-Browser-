#  Modules To Install

from PyQt5.QtCore import * # IMP   # pip install PyQt5
from PyQt5.QtWidgets import * #IMP
from PyQt5.QtGui import * #IMP
from PyQt5.QtWebEngineWidgets import *  # pip install PyQtWebEngine
from PyQt5.QtPrintSupport import * 
import os
import sys
 
 
 
                                # Hello
'''
Thanks This Is Yash "The One And Only Developer Of This Python Project
Credits:-
1st Thanks @Programming Hero For The GUI Of PyQt5
2nd Thanks To All Of The Creators Of Games And Other Stuff Like Music Player,Game, etc .. For Letting Me Use This
3rd All The Songs That Is Used In Music Player By [CWH] Credit Goers To Their Respective Singers.
================== Modified By {IF U DO ANY MODIFICATIONS WRITE YOUR NAME HERE } =========Thanks For Mod.
'''
# Don't Delete this Line This Is Just A Commnet If U Delete This Lines U Have No Longer Rights To Use This Project Anywhere
# Thank You!


# from hashlib import new
# import pickle
# import PyQt5
# from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets 
# from msilib.schema import SelfReg
# from PyQt5.QtCore import Qt
# from PIL.ImageQt import ImageQt # pip install pillow
# from PyQt5.QtWidgets import QApplication
# from PyQt5.QtGui import QPalette, QColor
# from PyQt5.QtWidgets import QInputDialog, QLineEdit, QDialog, QToolBar
'''
Thanks This Is Yash "The One And Only Developer Of This Python Project
Credits:-
1st Thanks @Programming Hero For The GUI Of PyQt5
2nd Thanks To All Of The Creators Of Games And Other Stuff Like Music Player,Game, etc .. For Letting Me Use This
3rd All The Songs That Is Used In Music Player By [CWH] Credit Goers To Their Respective Singers.
================== Modified By {IF U DO ANY MODIFICATIONS WRITE YOUR NAME HERE } =========Thanks For Mod.
'''
# Don't Delete this Line This Is Just A Commnet If U Delete This Lines U Have No Longer Rights To Use This Project Anywhere
# Thank You!
'''
class BookMarkToolBar(QtWidgets.QToolBar):
    bookmarkClicked = QtCore.pyqtSignal(QtCore.QUrl, str)

    def __init__(self, parent=None):
        super(BookMarkToolBar, self).__init__(parent)
        self.actionTriggered.connect(self.onActionTriggered)
        self.bookmark_list = []

    def setBoorkMarks(self, bookmarks):
        for bookmark in bookmarks:
            self.addBookMarkAction(bookmark["title"], bookmark["url"])

    def addBookMarkAction(self, title, url):
        bookmark = {"title": title, "url": url}
        fm = QtGui.QFontMetrics(self.font())
        if bookmark not in self.bookmark_list:
            text = fm.elidedText(title, QtCore.Qt.ElideRight, 150)
            action = self.addAction(text)
            action.setData(bookmark)
            self.bookmark_list.append(bookmark)

    @QtCore.pyqtSlot(QtWidgets.QAction)
    def onActionTriggered(self, action):
        bookmark = action.data()
        self.bookmarkClicked.emit(bookmark["url"], bookmark["title"])
'''
'''
Thanks This Is Yash "The One And Only Developer Of This Python Project
Credits:-
1st Thanks @Programming Hero For The GUI Of PyQt5
2nd Thanks To All Of The Creators Of Games And Other Stuff Like Music Player,Game, etc .. For Letting Me Use This
3rd All The Songs That Is Used In Music Player By [CWH] Credit Goers To Their Respective Singers.
================== Modified By {IF U DO ANY MODIFICATIONS WRITE YOUR NAME HERE } =========Thanks For Mod.
'''
# Don't Delete this Line This Is Just A Commnet If U Delete This Lines U Have No Longer Rights To Use This Project Anywhere
# Thank You!

class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        QBtn = QDialogButtonBox.Ok  # No cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        title = QLabel("Developer")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        layout.addWidget(title)

        logo = QLabel()
        logo.setPixmap(QPixmap(os.path.join('images', 'ma-icon-128.png')))
        layout.addWidget(logo)

        layout.addWidget(QLabel("Version 5.0"))
        layout.addWidget(QLabel("Copyright 2022 Yash Inclusive"))

        for i in range(0, layout.count()):
            layout.itemAt(i).setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)
'''
Thanks This Is Yash "The One And Only Developer Of This Python Project
Credits:-
1st Thanks @Programming Hero For The GUI Of PyQt5
2nd Thanks To All Of The Creators Of Games And Other Stuff Like Music Player,Game, etc .. For Letting Me Use This
3rd All The Songs That Is Used In Music Player By [CWH] Credit Goers To Their Respective Singers.
================== Modified By {IF U DO ANY MODIFICATIONS WRITE YOUR NAME HERE } =========Thanks For Mod.
'''
# Don't Delete this Line This Is Just A Commnet If U Delete This Lines U Have No Longer Rights To Use This Project Anywhere
# Thank You!

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
        self.tabs.currentChanged.connect(self.current_tab_changed)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)

        self.setCentralWidget(self.tabs)

        self.status = QStatusBar()
        self.setStatusBar(self.status)


        navtb = QToolBar("Navigation")
        navtb.setIconSize(QSize(16, 16))
        self.addToolBar(navtb)

        navbar2 = QToolBar()
        self.addToolBar(navbar2)

        back_btn = QAction('⬅', self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
        navtb.addAction(back_btn)

        next_btn = QAction('➡', self)
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
        navtb.addAction(next_btn)

        reload_btn = QAction(' 🔃 ', self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
        navtb.addAction(reload_btn)

        home_btn = QAction(' 📘 ', self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        navtb.addSeparator()

        self.httpsicon = QLabel()  # Yes, really!
        self.httpsicon.setPixmap(QPixmap(os.path.join('images', 'lock-nossl.png')))
        navtb.addWidget(self.httpsicon)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)

        stop_btn = QAction(QIcon(os.path.join('images', 'cross-circle.png')), "Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
        navtb.addAction(stop_btn)
        credits = "Credits To Developer Yash"

        # Uncomment to disable native menubar on Mac
        # self.menuBar().setNativeMenuBar(False)

        file_menu = self.menuBar().addMenu("&File")

        new_tab_action = QAction(QIcon(os.path.join('images', 'ui-tab--plus.png')), "New Tab", self)
        new_tab_action.setStatusTip("Open a new tab")
        new_tab_action.triggered.connect(lambda _: self.add_new_tab())
        file_menu.addAction(new_tab_action)

        open_file_action = QAction(QIcon(os.path.join('images', 'disk--arrow.png')), "Open file...", self)
        open_file_action.setStatusTip("Open from file")
        open_file_action.triggered.connect(self.open_file)
        file_menu.addAction(open_file_action)

        save_file_action = QAction(QIcon(os.path.join('images', 'disk--pencil.png')), "Save Page As...", self)
        save_file_action.setStatusTip("Save current page to file")
        save_file_action.triggered.connect(self.save_file)
        file_menu.addAction(save_file_action)

        print_action = QAction(QIcon(os.path.join('images', 'printer.png')), "Print...", self)
        print_action.setStatusTip("Print current page")
        print_action.triggered.connect(self.print_page)
        file_menu.addAction(print_action)

        help_menu = self.menuBar().addMenu("&Help")

        about_action = QAction(QIcon(os.path.join('images', 'question.png')), "About Our Team", self)
        about_action.setStatusTip("Find out more about Yash Here!")  # Hungry!
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

        navigate_mozarella_action = QAction(QIcon(os.path.join('images', 'lifebuoy.png')),
                                            "About Project", self)
        navigate_mozarella_action.setStatusTip("About Developer")
        navigate_mozarella_action.triggered.connect(self.navigate_mozarella)
        help_menu.addAction(navigate_mozarella_action)
# don't edit these we are watching you! ,As this browser Uses Internet So Be Alerted !!!!
# All Developing Credit Goes
# ============================================================================================

        self.add_new_tab(QUrl('https://www.bing.com/?toWww=1&redig=375257EAD25C4BF5AA82551D2405763A'), 'Homepage')
        if credits == "Credits To Developer Yash":
            print("\n==================================================================================\nDon't Edit This Line! This Line Is Reserved For The Developer Otherwise You May Need To Face Consequences As This Project Use Internet, We can Find You Easily So Don't Change These Lines.\n\n\n\n\n\n\n===============================================================\n")
        
            self.showMaximized()
            # self.bookmarks_load()


        self.setWindowTitle("A Simple Browser")
        self.setWindowIcon(QIcon(os.path.join('images', 'ma-icon-64.png')))
# NavBar 2 ==========================================================================================================

        new_tab_op = QAction('New Tab➕', self)
        new_tab_op.triggered.connect(lambda _: self.add_new_tab())
        navbar2.addAction(new_tab_op)
        tab2 = QAction('Incognito', self)
        tab2.triggered.connect(self.main_tab2)
        navbar2.addAction(tab2)
        tab1 = QAction('Google', self)
        tab1.triggered.connect(self.main_tab1)
        navbar2.addAction(tab1) 
        main4 = QAction('Yandex', self)
        main4.triggered.connect(self.main_tab4)
        navbar2.addAction(main4)
        main5 = QAction('Yahoo', self)
        main5.triggered.connect(self.main_tab5)
        navbar2.addAction(main5)
        new_btn = QAction('Brave', self)
        new_btn.triggered.connect(self.navigate_tab)
        navbar2.addAction(new_btn)



# =================================================================================================================
# nav bar 2 games and other stuffs
        
        snake_game = QAction('SnakeGame', self)
        snake_game.triggered.connect(self.snake_gameop)
        navbar2.addAction(snake_game)
        main3 = QAction('MusicPlayer', self)
        main3.triggered.connect(self.main_tab3)
        navbar2.addAction(main3)
        new_btn1 = QAction('TicTacToe', self)
        new_btn1.triggered.connect(self.navigate_tab1)
        navbar2.addAction(new_btn1)
        aboutproject1 = QAction('DrawingPad', self)
        aboutproject1.triggered.connect(self.aboutproject)
        navbar2.addAction(aboutproject1)
        ninjagame = QAction('Knife Master', self)
        ninjagame.triggered.connect(self.ninjagamebtn)
        navbar2.addAction(ninjagame)
        bullseye = QAction('Bow Master', self)
        bullseye.triggered.connect(self.bullseyef)
        navbar2.addAction(bullseye)
        flipgame = QAction('Flip Game', self)
        flipgame.triggered.connect(self.flipgamef)
        navbar2.addAction(flipgame)
        rimage = QAction('RandomImage', self)
        rimage.triggered.connect(self.randomimagef)
        navbar2.addAction(rimage)
        welcomepg = QAction('Wlcm. Pg.', self)
        welcomepg.triggered.connect(self.welcomepg)
        navbar2.addAction(welcomepg)
# ==============================================================================================================
    def add_new_tab(self, qurl=None, label="New Tab"):

        if qurl is None:
            qurl = QUrl('https://www.bing.com/?toWww=1&redig=375257EAD25C4BF5AA82551D2405763A')

        browser = QWebEngineView()
        browser.setUrl(qurl)
        browser.adjustSize()
        i = self.tabs.addTab(browser, label)

        self.tabs.setCurrentIndex(i)

        # More difficult! We only want to update the url when it's from the
        # correct tab
        browser.urlChanged.connect(lambda qurl, browser=browser:
                                   self.update_urlbar(qurl, browser))

        browser.loadFinished.connect(lambda _, i=i, browser=browser:
                                     self.tabs.setTabText(i, browser.page().title()))

    def tab_open_doubleclick(self, i):
        if i == -1:  # No tab under the click
            self.add_new_tab()

    def current_tab_changed(self, i):
        qurl = self.tabs.currentWidget().url()
        self.update_urlbar(qurl, self.tabs.currentWidget())
        self.update_title(self.tabs.currentWidget())

    def close_current_tab(self, i):
        if self.tabs.count() < 2:
            return

        self.tabs.removeTab(i)

    def update_title(self, browser):
        if browser != self.tabs.currentWidget():
            # If this signal is not from the current tab, ignore
            return

        title = self.tabs.currentWidget().page().title()
        self.setWindowTitle("%s - A Simple Browser" % title)

    def navigate_mozarella(self):
        self.tabs.currentWidget().setUrl(QUrl("https://yash.brizy.site/"))

    def about(self):
        dlg = AboutDialog()
        dlg.exec_()

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                  "Hypertext Markup Language (*.htm *.html);;"
                                                  "All files (*.*)")

        if filename:
            with open(filename, 'r') as f:
                html = f.read()

            self.tabs.currentWidget().setHtml(html)
            self.urlbar.setText(filename)

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save Page As", "",
                                                  "Hypertext Markup Language (*.htm *html);;"
                                                  "All files (*.*)")

        if filename:
            html = self.tabs.currentWidget().page().toHtml()
            with open(filename, 'w') as f:
                f.write(html.encode('utf8'))

    def print_page(self):
        dlg = QPrintPreviewDialog()
        dlg.paintRequested.connect(self.browser.print_)
        dlg.exec_()

    def navigate_home(self):
        self.tabs.currentWidget().setUrl(QUrl("https://www.bing.com/?toWww=1&redig=375257EAD25C4BF5AA82551D2405763A"))

    def navigate_to_url(self):  # Does not receive the Url
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("http")

        self.tabs.currentWidget().setUrl(q)

    def update_urlbar(self, q, browser=None):

        if browser != self.tabs.currentWidget():
            # If this signal is not from the current tab, ignore
            return

        if q.scheme() == 'https':
            # Secure padlock icon
            self.httpsicon.setPixmap(QPixmap(os.path.join('images', 'lock-ssl.png')))

        else:
            # Insecure padlock icon
            self.httpsicon.setPixmap(QPixmap(os.path.join('images', 'lock-nossl.png')))

        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)
# =================================================================================================================
# navbar2 functions ===============================================================================================
    def navigate_home(self):
        self.tabs.currentWidget().setUrl(QUrl('https://google.com'))
    def navigate_tab(self):
        self.tabs.currentWidget().setUrl(QUrl('https://search.brave.com'))
    def navigate_tab1(self):
        self.tabs.currentWidget().setUrl(QUrl('https://bit.ly/tictactoeop'))
    def main_tab1(self):
        self.tabs.currentWidget().setUrl(QUrl('https://google.com'))
    def main_tab2(self):
        self.tabs.currentWidget().setUrl(QUrl('https://duckduckgo.com'))
    def main_tab3(self):
        self.tabs.currentWidget().setUrl(QUrl('https://bit.ly/musicplayeropyash'))
    def main_tab4(self):
        self.tabs.currentWidget().setUrl(QUrl('https://yandex.com/'))
    def main_tab5(self):
        self.tabs.currentWidget().setUrl(QUrl('https://in.search.yahoo.com/?fr2=inr'))
    def aboutproject(self):
        self.tabs.currentWidget().setUrl(QUrl('https://bit.ly/drawingpadbyyash'))
    def ninjagamebtn(self):
        self.tabs.currentWidget().setUrl(QUrl('https://bit.ly/ninjagamebtn'))
    def bullseyef(self):
        self.tabs.currentWidget().setUrl(QUrl('https://bit.ly/bullseyegameop'))
    def flipgamef(self):
        self.tabs.currentWidget().setUrl(QUrl('https://bit.ly/flipgameop'))
    def randomimagef(self):
        self.tabs.currentWidget().setUrl(QUrl('https://bit.ly/randomimagebyyash'))
    def snake_gameop(self):
        self.tabs.currentWidget().setUrl(QUrl('https://bit.ly/snakegameopbyyash'))
    def welcomepg(self):
        self.tabs.currentWidget().setUrl(QUrl('https://bit.ly/bgwithclock'))






# =================================================================================================
''''
def print_image(image):
    
   # Initializes the QPainter and draws the pixmap onto it
    def drawImage(printer):
        painter = QPainter()
        painter.begin(printer)
        painter.setPen(Qt.red)
        painter.drawPixmap(0, 0, pil2pixmap(image))
        painter.end()
    
    # Shows the preview

def pil2pixmap(im):
    if im.mode == "RGB":
        r, g, b = im.split()
        im = IM.merge("RGB", (b, g, r))
    elif im.mode == "RGBA":
        r, g, b, a = im.split()
        im = IM.merge("RGBA", (b, g, r, a))
    elif im.mode == "L":
        im = im.convert("RGBA")
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_ARGB32)
    qim = qim.smoothScaled(int(2480 / 3.2), int(3508 / 3.2))
    pixmap = QtGui.QPixmap.fromImage(qim)
    return pixmap
'''
# =========================================================================================
'''
    def Bookmark(self):
        try:
            qurl = QUrl(self.urlbar.text())
            print('Here we are using the QUrl toString method: %s ---> Type: %s' %  (qurl.toString(), type(qurl)))
            url = qurl.toString()
            print('Here we are storing the new string to a new variable: %s ---> Type: %s' % (url, type(url)))
            b = open(os.path.join('bookmarks', 'bookmarks.txt'), "wb")
            self.bookmarks_write = pickle.dump(url, b)
            b.close()
        except:
            print("Crash - Bookmarks not stored")

        self.bookmark_btn.setText("★")
    
    def bookmarks_load(self):
        try:
            bookmarks_open = open(os.path.join('bookmarks', 'bookmarks.txt'), 'rb')
            self.bookmarks_write = pickle.load(bookmarks_open)
            bookmarks_open.close()
            self.create_bookmarks()
        
        except:
            bookmarks_open = open(os.path.join('bookmarks', 'bookmarks.txt'), 'wb')
            bookmarks = ''
            self.bookmarks_write = pickle.dump(bookmarks, bookmarks_open)
            bookmarks_open.close()
            self.create_bookmarks()
            print('Crash - Did not load bookmarks')
        

    def create_bookmarks(self):
        bookmark_list = []
        try:
            for book in self.bookmarks_write.split():
                print(book)
                bookmark_list.append(book)
                print(bookmark_list)
        except:
            print("Something went wrong with the list")

        try:
            button = QAction(QIcon(os.path.join('images', 'tab_icon.PNG')), 'Open bookmark', self)
            button.triggered.connect(self.add_new_tab(QUrl(bookmark_list[0]), 'New'))
            self.bookmark_bar.addAction(button)
        except:
            print('Button is causing the error')
'''
'''
Thanks This Is Yash "The One And Only Developer Of This Python Project
Credits:-
1st Thanks @Programming Hero For The GUI Of PyQt5
2nd Thanks To All Of The Creators Of Games And Other Stuff Like Music Player,Game, etc .. For Letting Me Use This
3rd All The Songs That Is Used In Music Player By [CWH] Credit Goers To Their Respective Singers.
================== Modified By {IF U DO ANY MODIFICATIONS WRITE YOUR NAME HERE } =========Thanks For Mod.
'''
# Don't Delete this Line This Is Just A Commnet If U Delete This Lines U Have No Longer Rights To Use This Project Anywhere
# Thank You!

# dark theme============================================
# Now use a palette to switch to dark colors:
palette = QPalette()
palette.setColor(QPalette.Window, QColor(53, 53, 53))
palette.setColor(QPalette.WindowText, Qt.white)
palette.setColor(QPalette.Base, QColor(25, 25, 25))
palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
palette.setColor(QPalette.ToolTipBase, Qt.black)
palette.setColor(QPalette.ToolTipText, Qt.white)
palette.setColor(QPalette.Text, Qt.white)
palette.setColor(QPalette.Button, QColor(53, 53, 53))
palette.setColor(QPalette.ButtonText, Qt.white)
palette.setColor(QPalette.BrightText, Qt.red)
palette.setColor(QPalette.Link, QColor(42, 130, 218))
palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
palette.setColor(QPalette.HighlightedText, Qt.black)
# For Dark Theme=======================================
app = QApplication(sys.argv)
app.setStyle("Fusion") #for dark theme
app.setPalette(palette) #for dark theme
app.setApplicationName("Browser For Coders")
app.setOrganizationName("Yash  IS OP")
app.setOrganizationDomain("https://yash.brizy.site/")



window = MainWindow()
# dlg = QPrintPreviewDialog()
# dlg.paintRequested.connect(drawImage)
# dlg.exec_()
app.exec_()

'''
Thanks This Is Yash "The One And Only Developer Of This Python Project
Credits:-
1st Thanks @Programming Hero For The GUI Of PyQt5
2nd Thanks To All Of The Creators Of Games And Other Stuff Like Music Player,Game, etc .. For Letting Me Use This
3rd All The Songs That Is Used In Music Player By [CWH] Credit Goers To Their Respective Singers.
================== Modified By {IF U DO ANY MODIFICATIONS WRITE YOUR NAME HERE } =========Thanks For Mod.
'''
# Don't Delete this Line This Is Just A Commnet If U Delete This Lines U Have No Longer Rights To Use This Project Anywhere
# Thank You!
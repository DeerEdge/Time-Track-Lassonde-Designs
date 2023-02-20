# Import PyQt5's widgets to be used throughout the program
import threading
import sys
import turtle
import tables
import colorama
from colorama import Fore
from PyQt5.QtCore import Qt, pyqtSignal, QDate, QRunnable, pyqtSlot, QThreadPool
from PyQt5.QtGui import QIcon, QPixmap, QTextCursor
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from datetime import time
from folium.plugins import MarkerCluster

# folium v0.12.1 - Used to display geographical data
import folium
import time
import io
import os
import sqlite3

# import class functions
import create_widget_functions

from create_widget_functions import VerticalTabWidget

class Main(object):
    def setup_window(self, main_window):
        main_window.setWindowTitle("Time Track")
        main_window.setObjectName("main_window")
        main_window.setFixedSize(800, 500)
        self.setup_login_screen(main_window)

    def setup_login_screen(self, main_window):
        self.login_central_widget = QtWidgets.QWidget(main_window)
        self.login_central_widget.resize(800, 500)
        self.login_screen_background = QtWidgets.QLabel(self.login_central_widget)
        self.login_screen_background.setFixedSize(800, 500)
        self.login_screen_background.setPixmap(QtGui.QPixmap("Application Pictures and Icons/Login Screen Background.png"))
        self.login_screen_background.setScaledContents(True)
        self.login_screen_background.show()
        self.login_widget_container = QtWidgets.QGroupBox(self.login_central_widget)
        self.login_widget_container.resize(800, 500)

        # Application Logo
        self.login_screen_logo = QtWidgets.QLabel(self.login_widget_container)
        self.login_screen_logo.setFixedSize(200, 200)
        self.login_screen_logo.move(-20, -75)
        self.login_screen_logo.setPixmap(QtGui.QPixmap("Application Pictures and Icons/Time Track Logo.png"))
        self.login_screen_logo.setScaledContents(True)
        self.login_screen_logo.show()

        # Student Login
        self.student_login_title = self.create_QLabel("login_widget_container", "login_titles", "Student Login", 145,80, 200, 50)
        self.student_username_label = self.create_QLabel("login_widget_container", "login_screen_labels", "Email ID", 80, 122, 200, 50)
        self.student_username = self.create_QLineEdit("login_widget_container", "login_screen_text_fields", False, 80,160, 240, 30)
        self.student_password_label = self.create_QLabel("login_widget_container", "login_screen_labels", "Password",80, 187, 200, 50)
        self.student_password = self.create_QLineEdit("login_widget_container", "login_screen_text_fields", False, 80,225, 240, 30)

        self.student_forgot_password = self.create_QPushButton("login_widget_container", "login_screen_forgot_password","Forgot password?", "None", 65, 255, 140, 30)
        self.student_incorrect_login = self.create_QLabel("login_widget_container", "incorrect_login", "Email ID and/or Password Icorrect. Please enter correct credentials.", 82, 275, 240, 50)
        self.student_incorrect_login.setWordWrap(True)
        self.student_incorrect_login.hide()
        self.student_login_button = self.create_QPushButton("login_widget_container", "student_login_button", "Login", "None", 80, 290, 240, 30)
        self.student_login_button.clicked.connect(self.setup_portal)
        self.student_or_label = self.create_QLabel("login_widget_container", "login_screen_labels", "or", 190, 310, 40,50)
        self.student_create_account = self.create_QPushButton("login_widget_container", "student_login_button", "Create a Student Account", "None", 80, 350, 240, 30)

        # Line divider between logins
        self.login_divider_line = self.create_QFrame("login_widget_container", "login_screen_elements", "VLine", 399, 40, 1, 410)

        # Administrator Login
        self.administrator_login_title = self.create_QLabel("login_widget_container", "login_titles", "Administrator Login", 525, 80, 200, 50)
        self.administrator_username_label = self.create_QLabel("login_widget_container", "login_screen_labels", "Email ID", 480, 122, 200, 50)
        self.administrator_username = self.create_QLineEdit("login_widget_container", "login_screen_text_fields", False, 480, 160, 240, 30)
        self.administrator_password_label = self.create_QLabel("login_widget_container", "login_screen_labels", "Password", 480, 187, 200, 50)
        self.administrator_password = self.create_QLineEdit("login_widget_container", "login_screen_text_fields", False, 480, 225, 240, 30)

        self.administrator_forgot_password = self.create_QPushButton("login_widget_container", "login_screen_forgot_password", "Forgot password?", "None", 465, 255, 140, 30)
        self.administrator_incorrect_login = self.create_QLabel("login_widget_container", "incorrect_login", "Email ID and/or Password Icorrect. Please enter correct credentials.", 482, 275, 240, 50)
        self.administrator_incorrect_login.setWordWrap(True)
        self.administrator_incorrect_login.hide()
        self.administrator_login_button = self.create_QPushButton("login_widget_container", "administrator_login_button", "Login", "None", 480, 290, 240, 30)
        self.administrator_login_button.clicked.connect(self.setup_portal)
        self.administrator_or_label = self.create_QLabel("login_widget_container", "login_screen_labels", "or", 590, 310, 40, 50)
        self.administrator_create_account = self.create_QPushButton("login_widget_container", "administrator_login_button", "Create an Administrator Account", "None", 480, 350, 240, 30)
        main_window.setStatusBar(None)

    def setup_portal(self):
        global username
        global password
        global user

        sending_button = self.login_widget_container.sender().objectName()

        if sending_button == "student_login_button":
            self.initialize_student_page()

            # self.student_login_button.move(80, 320)
            # self.student_or_label.move(190, 340)
            # self.student_create_account.move(80, 380)
            # self.student_incorrect_login.show()
        elif sending_button == "administrator_login_button":
            self.initialize_administrator_page()
            self.administrator_login_button.move(480, 320)
            self.administrator_or_label.move(590, 340)
            self.administrator_create_account.move(480, 380)
            self.administrator_incorrect_login.show()

    def initialize_student_page(self):
        self.login_central_widget.deleteLater()

        main_window.setFixedSize(1400, 800)
        qtRectangle = main_window.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        main_window.move(qtRectangle.topLeft())
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")
        self.central_widget.resize(1400, 800)

        self.app_logo = QtWidgets.QLabel(self.central_widget)
        self.app_logo.setFixedSize(140, 140)
        self.app_logo.move(20, 10)
        self.app_logo.setPixmap(QtGui.QPixmap("Application Pictures and Icons/Time Track Icon.png"))
        self.app_logo.setScaledContents(True)
        self.app_logo.show()

        self.log_out_button = self.create_QPushButton("central_widget", "log_out", "None",
                                                      "Application Pictures and Icons/Log Out.png", 1240, -50, 160, 160)
        self.log_out_button.setIconSize(QtCore.QSize(150, 150))
        self.log_out_button.setFlat(True)
        self.log_out_button.clicked.connect(self.return_to_login_screen)

        self.setup_student_page("Dheeraj", "Vislawath")
        main_window.setCentralWidget(self.central_widget)
        self.status_bar = QtWidgets.QStatusBar(main_window)
        main_window.setStatusBar(self.status_bar)

    def initialize_administrator_page(self):
        self.login_central_widget.deleteLater()

        main_window.setFixedSize(1400, 800)
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")
        self.central_widget.resize(1400, 800)

        self.app_logo = QtWidgets.QLabel(self.central_widget)
        self.app_logo.setFixedSize(140, 140)
        self.app_logo.move(20, 10)
        self.app_logo.setPixmap(QtGui.QPixmap("Application Pictures and Icons/Time Track Icon.png"))
        self.app_logo.setScaledContents(True)
        self.app_logo.show()

        self.log_out_button = self.create_QPushButton("central_widget", "log_out", "None",
                                                      "Application Pictures and Icons/Log Out.png", 1240, -50, 160, 160)
        self.log_out_button.setIconSize(QtCore.QSize(150, 150))
        self.log_out_button.setFlat(True)
        self.log_out_button.clicked.connect(self.return_to_login_screen)

        self.setup_student_page()
        main_window.setCentralWidget(self.central_widget)
        self.status_bar = QtWidgets.QStatusBar(main_window)
        main_window.setStatusBar(self.status_bar)

    def setup_student_page(self, first_name, last_name):
        global dashboard_slideshow
        global slideshow_title
        global slideshow_description
        global kill_thread_boolean
        global threadpool
        global map

        self.tab_widget = VerticalTabWidget(self.central_widget)
        self.tab_widget.setObjectName("tab_widget")
        self.tab_widget.resize(1405, 700)
        self.tab_widget.move(0, 55)

        self.dashboard_tab = QtWidgets.QWidget()
        self.upcoming_events_tab = QtWidgets.QWidget()
        self.maps_tab = QtWidgets.QWidget()
        self.points_tab = QtWidgets.QWidget()
        self.rewards_tab = QtWidgets.QWidget()
        self.community_tab = QtWidgets.QWidget()
        self.student_profile_tab = QtWidgets.QWidget()

        self.tab_widget.addTab(self.dashboard_tab, "Dashboard")
        self.tab_widget.addTab(self.upcoming_events_tab, "Upcoming Events")
        self.tab_widget.addTab(self.maps_tab, "Maps")
        self.tab_widget.addTab(self.points_tab, "Points")
        self.tab_widget.addTab(self.rewards_tab, "Rewards")
        self.tab_widget.addTab(self.student_profile_tab, "My Student Profile")

        # Dashboard Tab
        self.intro_label = self.create_QLabel("central_widget", "intro_label", "Signed in as " + first_name + " " + last_name, 200, 10, 600, 50)
        self.dashboard_label = self.create_QLabel("dashboard_tab", "dashboard_label", "Dashboard", 20, 20, 600, 50)
        self.dashboard_title_line = self.create_QFrame("dashboard_tab", "dashboard_title_line", "HLine", 10, 65, 600, 6)
        dashboard_slideshow = self.create_QLabel("dashboard_tab", "dashboard_slider_label", "filler", 20, 90, 840, 480)
        dashboard_slideshow.setScaledContents(True)
        slideshow_title = self.create_QLabel("dashboard_tab", "slideshow_title", "", 20, 580, 840, 20)
        slideshow_title.setWordWrap(True)
        slideshow_description = self.create_QLabel("dashboard_tab", "slideshow_description", "", 20, 600, 840, 100)
        slideshow_description.setWordWrap(True)
        slideshow_description.setAlignment(QtCore.Qt.AlignTop)
        self.dashboard_separator_line = self.create_QFrame("dashboard_tab", "dashboard_separator_line", "VLine", 875, 40, 6, 630)

        self.announcements = self.create_QLabel("dashboard_tab", "announcements", "Announcements", 900, 40, 300, 30)
        self.upcoming_events_objects = self.create_QScrollArea("dashboard_tab", "upcoming_events_QScrollArea",
                                                               "vertical_layout", 900, 110, 300, 560)
        self.upcoming_events = self.upcoming_events_objects[0]
        self.upcoming_events_layout = self.upcoming_events_objects[1]
        self.upcoming_events_scrollArea = self.upcoming_events_objects[2]



        # Upcoming Events Tab
        #
        #
        #
        self.upcoming_events_label = self.create_QLabel("upcoming_events_tab", "upcoming_events_label", "Upcoming Events", 20, 20, 600, 50)
        self.upcoming_events_title_line = self.create_QFrame("upcoming_events_tab", "upcoming_events_title_line", "HLine", 10, 65, 600, 6)
        self.student_calendar = self.create_QCalendar("upcoming_events_tab", 20, 80, 600, 600)
        self.student_calendar.selectionChanged.connect(self.student_upcoming_events_calendar)
        self.current_day = self.student_calendar.selectedDate().toString()
        self.day_events_label = self.create_QLabel("upcoming_events_tab", "day_event_label", "  Events on " + self.current_day, 705, 80, 430, 30)

        self.upcoming_events_tab_objects = self.create_QScrollArea("upcoming_events_tab", "upcoming_events_QScrollArea",
                                                               "vertical_layout", 705, 110, 430, 560)
        self.upcoming_tab_events = self.upcoming_events_tab_objects[0]
        self.upcoming_tab_events_layout = self.upcoming_events_tab_objects[1]
        self.upcoming_tab_events_scrollArea = self.upcoming_events_tab_objects[2]



        # Maps Tab
        #
        #
        #
        self.maps_label = self.create_QLabel("maps_tab", "maps_label", "Maps", 20, 20, 600, 50)
        self.maps_line = self.create_QFrame("maps_tab", "maps_line", "HLine", 10, 65, 600, 6)
        self.map_container = QtWidgets.QGroupBox(self.maps_tab)
        self.map_container.setGeometry(QtCore.QRect(20, 80, 800, 600))
        self.maps_objects = self.create_QScrollArea("maps_tab", "maps_QScrollArea", "vertical_layout", 835, 85, 360, 595)
        self.maps = self.maps_objects[0]
        self.maps_layout = self.maps_objects[1]
        self.maps_scrollArea = self.maps_objects[2]

        # The created QGroupBox container's layout is set to hold the web widget
        self.map_frame = QtWidgets.QVBoxLayout(self.map_container)
        coordinate = (40.617847198627, -111.86923371648)
        map = folium.Map(zoom_start=12, location=coordinate, control_scale=True)
        folium.Marker(location=coordinate, icon=folium.Icon(color="darkgreen", icon='user'),).add_to(map)
        data = io.BytesIO()
        map.save(data, close_file=False)
        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        self.map_frame.addWidget(webView)

        self.maps_scrollArea.setWidget(self.maps)
        self.maps_scrollArea.verticalScrollBar().setSliderPosition(0)

        # Points Tab
        #
        #
        #
        self.points_label = self.create_QLabel("points_tab", "points_label", "Points", 20, 20, 600, 50)
        self.points_title_line = self.create_QFrame("points_tab", "points_title_line", "HLine", 10, 65, 600, 6)

        self.points_leaderboard_objects = self.create_QScrollArea("points_tab", "points_leaderboard_QScrollArea",
                                                                  "vertical_layout", 750, 80, 450, 300)
        self.points_leaderboard = self.points_leaderboard_objects[0]
        self.points_leaderboard_layout = self.points_leaderboard_objects[1]
        self.points_leaderboard_scrollArea = self.points_leaderboard_objects[2]
        self.points_leaderboard_label = self.create_QLabel("points_tab", "points_leaderboard_label", "  Leaderboard: ", 750, 40, 450, 30)
        self.points_leaderboard_label  = self.create_QLabel("points_tab", " ", "Personal Points: 200", 900, 40, 300, 30)

        self.rewards_label = self.create_QLabel("rewards_tab", "rewards_label", "Rewards", 20, 20, 600, 50)
        self.rewards_title_line = self.create_QFrame("rewards_tab", "rewards_title_line", "HLine", 10, 65, 600, 6)
        self.rewards_my_points_label = self.create_QLabel("rewards_tab", "rewards_my_points_label", "  Your Points: 200", 950, 40, 300, 30)
        self.rewards_tab_objects = self.create_QScrollArea("rewards_tab", "rewards_QScrollArea", "grid_layout", 20, 120, 1180, 570)
        self.rewards_tab_objects = self.create_QScrollArea("rewards_tab", "rewards_QScrollArea", "grid_layout", 20, 120, 1180, 570)
        self.rewards = self.rewards_tab_objects[0]
        self.rewards_layout = self.rewards_tab_objects[1]
        self.rewards_events_scrollArea = self.rewards_tab_objects[2]

        index = 0
        self.rewards_events_scrollArea.setWidget(self.rewards)
        self.rewards_events_scrollArea.verticalScrollBar().setSliderPosition(0)

        # Student Profile Tab
        self.student_profile_label = self.create_QLabel("student_profile_tab", "student_profile_label", "My Profile", 20, 20, 600, 50)
        self.student_profile_title_line = self.create_QFrame("student_profile_tab", "student_profile_title_line", "HLine", 10, 65, 600, 6)
        self.student_profile_data = self.create_QTextEdit("student_profile_tab", "student_profile_data", True, 900, 50, 300, 300)
        self.student_profile_data_label = self.create_QLabel("student_profile_tab", "student_profile_data_label", "  User Data", 900, 20, 300, 30)
        self.student_purchases_label = self.create_QLabel("student_profile_tab", "student_purchases_label", "Past Purchases ", 20, 80, 300, 50)

        self.tab_widget.show()

    def setup_admin_page(self):
        self.intro_label = self.create_QLabel("central_widget", "intro_label", "Signed in as Dheeraj Vislawath", 200, 10, 600, 50)

        self.tab_widget = VerticalTabWidget(self.central_widget)
        self.tab_widget.setObjectName("tab_widget")
        self.tab_widget.resize(1000, 650)
        self.tab_widget.move(0, 55)

        # Administrator Login
        self.admin_dashboard_tab = QtWidgets.QWidget()
        self.admin_events_tab = QtWidgets.QWidget()
        self.admin_statistics_tab = QtWidgets.QWidget()
        self.admin_student_view_tab = QtWidgets.QWidget()

        self.tab_widget.addTab(self.admin_dashboard_tab, "Dashboard")
        self.tab_widget.addTab(self.admin_events_tab, "Events")
        self.tab_widget.addTab(self.admin_statistics_tab, "Statistics")
        self.tab_widget.addTab(self.admin_student_view_tab, "Student View")

        self.count = 0

        self.admin_dashboard_label = self.create_QLabel("admin_dashboard_tab", "admin_dashboard_label", "Dashboard", 20, 20, 600, 50)
        self.admin_dashboard_line = self.create_QFrame("admin_dashboard_tab", "admin_dashboard_line", "HLine", 10, 65, 600, 6)

        self.admin_events_label = self.create_QLabel("admin_events_tab", "admin_events_label", "Events", 20, 20, 600, 50)
        self.admin_events_line = self.create_QFrame("admin_events_tab", "admin_events_line", "HLine", 10, 65, 600, 6)
        self.admin_calendar = self.create_QCalendar("admin_events_tab", 20, 80, 350, 350)
        self.admin_calendar.selectionChanged.connect(self.admin_events_calendar)

        # setting selected date
        # self.admin_calendar.clicked.connect(lambda: self.admin_current_events.setText(text + str(self.count)))
        self.admin_events_title = self.create_QLabel("admin_events_tab", "admin_events_text", "Current Events", 400, 80, 400, 30)
        self.admin_current_events = self.create_QLineEdit("admin_events_tab", "admin_current_events", True, 400, 110, 400, 320)
        current_day = self.admin_calendar.selectedDate().toString()
        self.admin_current_events.setText("Events on " + current_day[4:] + ":")
        self.admin_current_events.setAlignment(Qt.AlignTop)

        self.admin_statistics_label = self.create_QLabel("admin_statistics_tab", "admin_statistics_label", "Statistics", 20, 20, 600, 50)
        self.admin_statistics_line = self.create_QFrame("admin_statistics_tab", "admin_statistics_line", "HLine", 10, 65, 600, 6)

        self.admin_student_view_label = self.create_QLabel("admin_student_view_tab", "admin_student_view_label", "Student View", 20, 20,600, 50)
        self.admin_student_view_line = self.create_QFrame("admin_student_view_tab", "admin_student_view_line", "HLine", 10, 65, 600, 6)

        self.tab_widget.show()

    def student_upcoming_events_calendar(self):
        selected_date = self.upcoming_events_tab.sender().selectedDate().toString()
        new_date = selected_date.split()
        self.check_events_on_day()

    def return_to_login_screen(self):
        global kill_thread_boolean
        kill_thread_boolean = True
        self.central_widget.deleteLater()
        main_window.setFixedSize(800, 500)
        self.setup_login_screen(main_window)
        main_window.setCentralWidget(self.login_central_widget)

    # def show_event_locations(self, user):
    #     if user == "student":
    #         for event in events:
    #             event_coordinate = (event[9], event[10])
    #             marker_cluster = MarkerCluster().add_to(map)
    #             folium.Marker(location=event_coordinate,
    #                           icon=folium.Icon(color="red", icon='circle', prefix='fa'),
    #                           popup=(folium.Popup(f'<h6><b>{event[1]}</b></h6>' + "\n" + f'<h6><b>{event[2]}</b></h6>', show=True, min_width=20)),).add_to(marker_cluster)
    #             self.event_object = QtWidgets.QGroupBox(self.maps)
    #             self.event_object.setFixedSize(325, 100)
    #             self.event_object.setLayout(QtWidgets.QVBoxLayout())
    #             self.title = self.create_QLabel("event", "title", (event[1] + "\n" + event[2]), 10, 10, 305, 60)
    #             self.title.setWordWrap(True)
    #             self.date = self.create_QLabel("event", "date", (str(event[7]) + "/" + str(event[8]) + "/" + str(event[6])), 240, 0, 80, 60)
    #             self.description = self.create_QLabel("event", "description", (event[3]), 10, 60, 305, 40)
    #             self.description.setWordWrap(True)
    #             self.maps_layout.addWidget(self.event_object)

    # Widget Creation Functions
    def create_QCheckBox(self, container, x_coordinate, y_coordinate, width, length):
        return create_widget_functions.create_QCheckBox.__init__(self, container, x_coordinate, y_coordinate, width, length)

    def create_QCalendar(self, container, x_coordinate, y_coordinate, width, length):
        return create_widget_functions.create_QCalendar.__init__(self, container, x_coordinate, y_coordinate, width, length)

    def create_QLabel(self, container, object_name, text, x_coordinate, y_coordinate, width, length):
        return create_widget_functions.create_QLabel.__init__(self, container, object_name, text, x_coordinate, y_coordinate, width, length)

    def create_QLineEdit(self, container, object_name, read_only, x_coordinate, y_coordinate, width, length):
        return create_widget_functions.create_QLineEdit.__init__(self, container, object_name, read_only, x_coordinate, y_coordinate, width, length)

    def create_QTextEdit(self, container, object_name, read_only, x_coordinate, y_coordinate, width, length):
        return create_widget_functions.create_QTextEdit.__init__(self, container, object_name, read_only, x_coordinate, y_coordinate, width, length)

    def create_QScrollArea(self, container, object_name, layout, x_coordinate, y_coordinate, fixed_width, min_length):
        return create_widget_functions.create_QScrollArea.__init__(self, container, object_name, layout, x_coordinate, y_coordinate, fixed_width, min_length)

    def create_QFrame(self, container, object_name, orientation, x_coordinate, y_coordinate, width, length):
        return create_widget_functions.create_QFrame.__init__(self, container, object_name, orientation, x_coordinate, y_coordinate, width, length)

    def create_QPushButton(self, container, object_name, text, icon, x_coordinate, y_coordinate, width, length):
        if container == "main_window":
            self.QPushButton = QtWidgets.QPushButton(main_window)
            if text != "None":
                self.QPushButton.setText(text)
            if icon != "None":
                self.QPushButton.setIcon(QIcon(icon))
            self.QPushButton.setFixedSize(width, length)
            self.QPushButton.move(x_coordinate, y_coordinate)

            return self.QPushButton
        else: return create_widget_functions.create_QPushButton.__init__(self, container, object_name, text, icon, x_coordinate, y_coordinate, width, length)

    def create_horizontal_QSlider(self, container, x_coordinate, y_coordinate, width, length):
        return create_widget_functions.create_horizontal_QSlider.__init__(self, container, x_coordinate, y_coordinate, width, length)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    with open("styling.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
    main_window = QtWidgets.QMainWindow()
    ui = Main()
    ui.setup_window(main_window)
    main_window.show()
    sys.exit(app.exec_())
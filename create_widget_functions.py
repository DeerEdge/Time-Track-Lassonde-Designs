from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QCheckBox, QTabWidget, QTabBar, QStylePainter, QStyleOptionTab, QStyle, QComboBox

class create_QComboBox:
    def __init__(self, container, x_coordinate, y_coordinate, width, length):
        # Creates and associates QComboBox to specified container
        if container == "points_tab":
            self.QComboBox = QtWidgets.QComboBox(self.points_tab)

        # Geometry of QComboBox is specified by the passed function parameters
        self.QComboBox.setGeometry(QtCore.QRect(x_coordinate, y_coordinate, width, length))
        return self.QComboBox

class create_QCheckBox():
    def __init__(self, container, x_coordinate, y_coordinate, width, length):
        if container == "dashboard_tab":
            self.QCheckBox = QtWidgets.QCheckBox(self.dashboard_tab)
        elif container == "upcoming_events_tab":
            self.QCheckBox = QtWidgets.QCheckBox(self.upcoming_events_tab)
        elif container == "event":
            self.QCheckBox = QtWidgets.QCheckBox(self.event_object)
        self.QCheckBox.resize(width, length)
        self.QCheckBox.move(x_coordinate, y_coordinate)
        return self.QCheckBox

class create_QCalendar():
    def __init__(self, container, x_coordinate, y_coordinate, width, length):
        if container == "upcoming_events_tab":
            self.QCalender = QtWidgets.QCalendarWidget(self.upcoming_events_tab)
        elif container == "admin_events_tab":
            self.QCalender = QtWidgets.QCalendarWidget(self.admin_events_tab)
        self.QCalender.setGeometry(x_coordinate, y_coordinate, width, length)
        return self.QCalender

class create_QLabel():
    def __init__(self, container, object_name, text, x_coordinate, y_coordinate, width, length):
        # Creates and associates QLabel to specified container
        if container == "login_widget_container":
            self.QLabel = QtWidgets.QLabel(self.login_widget_container)
        elif container == "central_widget":
            self.QLabel = QtWidgets.QLabel(self.central_widget)
        elif container == "dashboard_tab":
            self.QLabel = QtWidgets.QLabel(self.dashboard_tab)
        elif container == "upcoming_events_tab":
            self.QLabel = QtWidgets.QLabel(self.upcoming_events_tab)
        elif container == "points_tab":
            self.QLabel = QtWidgets.QLabel(self.points_tab)
        elif container == "rewards_tab":
            self.QLabel = QtWidgets.QLabel(self.rewards_tab)
        elif container == "student_profile_tab":
            self.QLabel = QtWidgets.QLabel(self.student_profile_tab)
        elif container == "event":
            self.QLabel = QtWidgets.QLabel(self.event_object)

        # Administrator
        elif container == "admin_dashboard_tab":
            self.QLabel = QtWidgets.QLabel(self.admin_dashboard_tab)
        elif container == "admin_events_tab":
            self.QLabel = QtWidgets.QLabel(self.admin_events_tab)
        elif container == "maps_tab":
            self.QLabel = QtWidgets.QLabel(self.maps_tab)
        elif container == "admin_statistics_tab":
            self.QLabel = QtWidgets.QLabel(self.admin_statistics_tab)
        elif container == "admin_student_view_tab":
            self.QLabel = QtWidgets.QLabel(self.admin_student_view_tab)
        self.QLabel.setWordWrap(True)
        self.QLabel.setObjectName(object_name)
        self.QLabel.setText(text)
        # Geometry of QLabel is specified by the passed function parameters
        self.QLabel.setGeometry(QtCore.QRect(x_coordinate, y_coordinate, width, length))
        return self.QLabel

class create_QLineEdit():
    def __init__(self, container, object_name, read_only, x_coordinate, y_coordinate, width, length):
        # Creates and associates QLabel to specified container
        if container == "login_widget_container":
            self.QLineEdit = QtWidgets.QLineEdit(self.login_widget_container)
        elif container == "dashboard_tab":
            self.QLineEdit = QtWidgets.QLineEdit(self.dashboard_tab)
        elif container == "admin_dashboard_tab":
            self.QLineEdit = QtWidgets.QLineEdit(self.admin_dashboard_tab)
        elif container == "upcoming_events_tab":
            self.QLineEdit = QtWidgets.QLineEdit(self.upcoming_events_tab)
        elif container == "points_tab":
            self.QLineEdit = QtWidgets.QLineEdit(self.points_tab)
        elif container == "rewards_tab":
            self.QLineEdit = QtWidgets.QLineEdit(self.rewards_tab)
        elif container == "student_profile_tab":
            self.QLineEdit = QtWidgets.QLineEdit(self.student_profile_tab)

            # Administrator
        elif container == "admin_dashboard_tab":
            self.QLineEdit = QtWidgets.QLineEdit(self.admin_dashboard_tab)
        elif container == "admin_events_tab":
            self.QLineEdit = QtWidgets.QLineEdit(self.admin_events_tab)
        elif container == "maps_tab":
            self.QLineEdit = QtWidgets.QLineEdit(self.maps_tab)
        elif container == "admin_statistics_tab":
            self.QLineEdit = QtWidgets.QLineEdit(self.admin_statistics_tab)
        elif container == "admin_student_view_tab":
            self.QLineEdit = QtWidgets.QLineEdit(self.admin_student_view_tab)
        self.QLineEdit.setObjectName(object_name)
        # user cannot type in the boxes
        self.QLineEdit.setReadOnly(read_only)
        # Geometry of QLineEdit is specified by the passed function parameters
        self.QLineEdit.setFixedSize(width, length)
        self.QLineEdit.move(x_coordinate, y_coordinate)

        return self.QLineEdit

class create_QTextEdit():
    def __init__(self, container, object_name, read_only, x_coordinate, y_coordinate, width, length):
        # Creates and associates QLabel to specified container
        if container == "login_widget_container":
            self.QTextEdit = QtWidgets.QTextEdit(self.login_widget_container)
        elif container == "dashboard_tab":
            self.QTextEdit = QtWidgets.QTextEdit(self.dashboard_tab)
        elif container == "admin_dashboard_tab":
            self.QTextEdit = QtWidgets.QTextEdit(self.admin_dashboard_tab)
        elif container == "upcoming_events_tab":
            self.QTextEdit = QtWidgets.QTextEdit(self.upcoming_events_tab)
        elif container == "points_tab":
            self.QTextEdit = QtWidgets.QTextEdit(self.points_tab)
        elif container == "rewards_tab":
            self.QTextEdit = QtWidgets.QTextEdit(self.rewards_tab)
        elif container == "student_profile_tab":
            self.QTextEdit = QtWidgets.QTextEdit(self.student_profile_tab)

            # Administrator
        elif container == "admin_dashboard_tab":
            self.QTextEdit = QtWidgets.QTextEdit(self.admin_dashboard_tab)
        elif container == "admin_events_tab":
            self.QTextEdit = QtWidgets.QTextEdit(self.admin_events_tab)
        elif container == "maps_tab":
            self.QTextEdit = QtWidgets.QTextEdit(self.maps_tab)
        elif container == "admin_statistics_tab":
            self.QTextEdit = QtWidgets.QTextEdit(self.admin_statistics_tab)
        elif container == "admin_student_view_tab":
            self.QTextEdit = QtWidgets.QTextEdit(self.admin_student_view_tab)
        self.QTextEdit.setObjectName(object_name)
        # user cannot type in the boxes
        self.QTextEdit.setReadOnly(read_only)
        # Geometry of QLineEdit is specified by the passed function parameters
        self.QTextEdit.setFixedSize(width, length)
        self.QTextEdit.move(x_coordinate, y_coordinate)
        self.QTextEdit.setWordWrapMode(True)

        return self.QTextEdit

class create_QScrollArea():
    def __init__(self, container, object_name, layout, x_coordinate, y_coordinate, fixed_width, min_length):
        self.scrollArea_object_container = QtWidgets.QWidget()
        if container == "upcoming_events_tab":
            self.QScrollArea = QtWidgets.QScrollArea(self.upcoming_events_tab)
        elif container == "dashboard_tab":
            self.QScrollArea = QtWidgets.QScrollArea(self.dashboard_tab)
        elif container == "maps_tab":
            self.QScrollArea = QtWidgets.QScrollArea(self.maps_tab)
        elif container == "points_tab":
            self.QScrollArea = QtWidgets.QScrollArea(self.points_tab)
        elif container == "rewards_tab":
            self.QScrollArea = QtWidgets.QScrollArea(self.rewards_tab)
        self.QScrollArea.setFixedWidth(fixed_width)
        self.QScrollArea.setFixedHeight(min_length)
        self.QScrollArea.move(x_coordinate, y_coordinate)
        self.QScrollArea.setWidgetResizable(True)
        self.QScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        if layout == "vertical_layout":
            self.scroll_vertical_layout = QtWidgets.QVBoxLayout(self.scrollArea_object_container)
            self.scrollArea_object_container.setLayout(self.scroll_vertical_layout)
            return [self.scrollArea_object_container, self.scroll_vertical_layout, self.QScrollArea]
        elif layout == "grid_layout":
            self.scroll_grid_layout = QtWidgets.QGridLayout(self.scrollArea_object_container)
            self.scrollArea_object_container.setLayout(self.scroll_grid_layout)
            self.QScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
            return [self.scrollArea_object_container, self.scroll_grid_layout, self.QScrollArea]

class create_QFrame():
    def __init__(self, container, object_name, orientation, x_coordinate, y_coordinate, width, length):
        if container == "login_widget_container":
            self.QFrame = QtWidgets.QFrame(self.login_widget_container)
        elif container == "dashboard_tab":
            self.QFrame = QtWidgets.QFrame(self.dashboard_tab)
        elif container == "admin_dashboard_tab":
            self.QFrame = QtWidgets.QFrame(self.admin_dashboard_tab)
        elif container == "upcoming_events_tab":
            self.QFrame = QtWidgets.QFrame(self.upcoming_events_tab)
        elif container == "points_tab":
            self.QFrame = QtWidgets.QFrame(self.points_tab)
        elif container == "rewards_tab":
            self.QFrame = QtWidgets.QFrame(self.rewards_tab)
        elif container == "student_profile_tab":
            self.QFrame = QtWidgets.QFrame(self.student_profile_tab)
            # Administrator
        elif container == "admin_dashboard_tab":
            self.QFrame = QtWidgets.QFrame(self.admin_dashboard_tab)
        elif container == "admin_events_tab":
            self.QFrame = QtWidgets.QFrame(self.admin_events_tab)
        elif container == "maps_tab":
            self.QFrame = QtWidgets.QFrame(self.maps_tab)
        elif container == "admin_statistics_tab":
            self.QFrame = QtWidgets.QFrame(self.admin_statistics_tab)
        elif container == "admin_student_view_tab":
            self.QFrame = QtWidgets.QFrame(self.admin_student_view_tab)
        self.QFrame.setObjectName(object_name)
        self.QFrame.setGeometry(QtCore.QRect(x_coordinate, y_coordinate, width, length))
        if orientation == "VLine":
            self.QFrame.setFrameShape(QtWidgets.QFrame.VLine)
        else:
            self.QFrame.setFrameShape(QtWidgets.QFrame.HLine)

class create_QPushButton():
    def __init__(self, container, object_name, text, icon, x_coordinate, y_coordinate, width, length):
        # Creates and associates QLabel to specified container
        if container == "login_widget_container":
            self.QPushButton = QtWidgets.QPushButton(self.login_widget_container)
        elif container == "central_widget":
            self.QPushButton = QtWidgets.QPushButton(self.central_widget)
        elif container == "student_profile_tab":
            self.QPushButton = QtWidgets.QPushButton(self.student_profile_tab)
        elif container == "rewards_tab":
            self.QPushButton = QtWidgets.QPushButton(self.rewards_tab)
        self.QPushButton.setObjectName(object_name)
        if text != "None":
            self.QPushButton.setText(text)
        if icon != "None":
            self.QPushButton.setIcon(QIcon(icon))
        # Geometry of QLineEdit is specified by the passed function parameters
        self.QPushButton.setFixedSize(width, length)
        self.QPushButton.move(x_coordinate, y_coordinate)

        return self.QPushButton

class create_horizontal_QSlider():
    def __init__(self, container, x_coordinate, y_coordinate, width, length):
        if container == "dashboard_tab":
            self.QSlider = QtWidgets.QSlider(Qt.Horizontal, self.dashboard_tab)
        self.QSlider.setGeometry(x_coordinate, y_coordinate, width, length)
        return self.QSlider

class TabBar(QTabBar):
    def tabSizeHint(self, index):
        self.setGeometry(0, 120, 180, 380)
        s = QTabBar.tabSizeHint(self, index)
        s.transpose()
        return s

    def paintEvent(self, event):
        painter = QStylePainter(self)
        opt = QStyleOptionTab()

        for i in range(self.count()):
            self.initStyleOption(opt, i)
            painter.drawControl(QStyle.CE_TabBarTabShape, opt)
            painter.save()

            s = opt.rect.size()
            s.transpose()
            r = QtCore.QRect(QtCore.QPoint(), s)
            r.moveCenter(opt.rect.center())
            opt.rect = r

            c = self.tabRect(i).center()
            painter.translate(c)
            painter.rotate(90)
            painter.translate(-c)
            painter.drawControl(QStyle.CE_TabBarTabLabel, opt)
            painter.restore()

class VerticalTabWidget(QTabWidget):
    def __init__(self, *args, **kwargs):
        QTabWidget.__init__(self, *args, **kwargs)
        self.setTabBar(TabBar())
        self.setTabPosition(QtWidgets.QTabWidget.West)
        self.setStyleSheet("QTabBar::tab { height: 180px; width: 50px;}")


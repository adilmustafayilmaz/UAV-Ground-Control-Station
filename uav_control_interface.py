import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QGridLayout, QLabel, QSlider, QPushButton, 
                            QGroupBox, QTabWidget, QComboBox, QFrame, QSplitter,
                            QProgressBar, QDial, QSpinBox)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QColor, QPalette, QPixmap

class UAVControlInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('UAV Control Interface')
        self.setGeometry(100, 100, 1200, 800)
        
        # Create central widget and main layout
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)
        
        # Add logo at the top
        logo_layout = QHBoxLayout()
        self.add_logo(logo_layout)
        main_layout.addLayout(logo_layout)
        
        # Create top status bar
        status_layout = QHBoxLayout()
        self.create_status_bar(status_layout)
        main_layout.addLayout(status_layout)
        
        # Create main content splitter
        content_splitter = QSplitter(Qt.Horizontal)
        
        # Left panel - Controls
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        self.create_control_panel(left_layout)
        content_splitter.addWidget(left_panel)
        
        # Right panel - Map/Camera View
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        self.create_visualization_panel(right_layout)
        content_splitter.addWidget(right_panel)
        
        # Set the splitter sizes
        content_splitter.setSizes([400, 800])
        main_layout.addWidget(content_splitter)
        
        # Bottom panel - Mission control & Emergency
        bottom_panel = QWidget()
        bottom_layout = QHBoxLayout(bottom_panel)
        self.create_mission_panel(bottom_layout)
        main_layout.addWidget(bottom_panel)
        
    def add_logo(self, layout):
        # Create logo container
        logo_container = QFrame()
        logo_container.setFrameShape(QFrame.NoFrame)
        logo_container_layout = QHBoxLayout(logo_container)
        
        # Create logo label
        logo_label = QLabel()
        # Try to load the actual logo
        logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "logo.png")
        
        if os.path.exists(logo_path):
            pixmap = QPixmap(logo_path)
            # Scale logo to appropriate size while maintaining aspect ratio
            pixmap = pixmap.scaled(200, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            logo_label.setPixmap(pixmap)
        else:
            # Create a placeholder text label if logo file doesn't exist
            logo_label.setText("UAV CONTROL SYSTEM")
            logo_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #003366;")
            logo_label.setMinimumWidth(200)
            logo_label.setMinimumHeight(80)
        
        logo_container_layout.addWidget(logo_label)
        logo_container_layout.addStretch(1)  # Push logo to left
        
        # Add company name or system name (optional)
        system_name = QLabel("Flight Control System")
        system_name.setStyleSheet("font-size: 18px; font-style: italic;")
        logo_container_layout.addWidget(system_name)
        
        layout.addWidget(logo_container)
        
    def create_status_bar(self, layout):
        # Connection status
        conn_group = QGroupBox("Connection")
        conn_layout = QHBoxLayout(conn_group)
        conn_status = QLabel("CONNECTED")
        conn_status.setStyleSheet("color: green; font-weight: bold;")
        conn_layout.addWidget(conn_status)
        layout.addWidget(conn_group)
        
        # Battery status
        battery_group = QGroupBox("Battery")
        battery_layout = QHBoxLayout(battery_group)
        battery_progress = QProgressBar()
        battery_progress.setValue(53)
        battery_progress.setStyleSheet("QProgressBar::chunk { background-color: green; }")
        battery_layout.addWidget(battery_progress)
        battery_layout.addWidget(QLabel("53%"))
        layout.addWidget(battery_group)
        
        # GPS status
        gps_group = QGroupBox("GPS")
        gps_layout = QHBoxLayout(gps_group)
        gps_layout.addWidget(QLabel("Satellites: 14"))
        gps_layout.addWidget(QLabel("Fix: 3D"))
        layout.addWidget(gps_group)
        
        # Flight mode
        mode_group = QGroupBox("Flight Mode")
        mode_layout = QHBoxLayout(mode_group)
        mode_combo = QComboBox()
        mode_combo.addItems(["Manual", "Stabilize", "Altitude Hold", "Loiter", "RTL", "Auto"])
        mode_layout.addWidget(mode_combo)
        layout.addWidget(mode_group)

    def create_control_panel(self, layout):
        # Flight parameters tab widget
        tabs = QTabWidget()
        
        # Primary controls tab
        primary_tab = QWidget()
        primary_layout = QGridLayout(primary_tab)
        
        # Throttle control
        throttle_group = QGroupBox("Throttle")
        throttle_layout = QVBoxLayout(throttle_group)
        self.throttle_slider = QSlider(Qt.Vertical)
        self.throttle_slider.setMinimum(0)
        self.throttle_slider.setMaximum(100)
        self.throttle_slider.setValue(0)
        self.throttle_label = QLabel("0%")
        throttle_layout.addWidget(self.throttle_slider, alignment=Qt.AlignHCenter)
        throttle_layout.addWidget(self.throttle_label, alignment=Qt.AlignHCenter)
        # Connect throttle slider to update function
        self.throttle_slider.valueChanged.connect(self.update_throttle_label)
        primary_layout.addWidget(throttle_group, 0, 0, 2, 1)
        
        # Attitude controls
        attitude_group = QGroupBox("Attitude Control")
        attitude_layout = QGridLayout(attitude_group)
        
        # Roll control
        self.roll_slider = QSlider(Qt.Vertical)
        self.roll_slider.setMinimum(-45)
        self.roll_slider.setMaximum(45)
        self.roll_slider.setValue(0)
        roll_label = QLabel("Roll")
        self.roll_value_label = QLabel("0°")


        # Pitch control
        pitch_label = QLabel("Pitch")
        self.pitch_slider = QSlider(Qt.Horizontal)
        self.pitch_slider.setMinimum(-45)
        self.pitch_slider.setMaximum(45)
        self.pitch_slider.setValue(0)
        self.pitch_value_label = QLabel("0°")
        attitude_layout.addWidget(pitch_label, 0, 1)
        attitude_layout.addWidget(self.pitch_slider, 1, 0, 1, 3)
        attitude_layout.addWidget(self.roll_value_label, 0, 2, alignment=Qt.AlignRight)
        # Connect pitch slider to update function
        self.pitch_slider.valueChanged.connect(self.update_pitch_label)
        
        
        
        # Modified positioning - Roll slider above, label below with value
        attitude_layout.addWidget(self.roll_slider, 0, 0, 1, 1)
        attitude_layout.addWidget(roll_label, 2, 0, 1, 1, Qt.AlignCenter)
        attitude_layout.addWidget(self.pitch_value_label, 3, 0, 1, 1, Qt.AlignCenter)
        # Connect roll slider to update function
        self.roll_slider.valueChanged.connect(self.update_roll_label)
        
        # Yaw control
        yaw_group = QGroupBox("Yaw")
        yaw_layout = QVBoxLayout(yaw_group)
        self.yaw_dial = QDial()
        self.yaw_dial.setMinimum(0)
        self.yaw_dial.setMaximum(359)
        self.yaw_dial.setValue(0)
        self.yaw_label = QLabel("0°")
        yaw_layout.addWidget(self.yaw_dial)
        yaw_layout.addWidget(self.yaw_label, alignment=Qt.AlignCenter)
        # Connect yaw dial to update function
        self.yaw_dial.valueChanged.connect(self.update_yaw_label)
        
        primary_layout.addWidget(attitude_group, 0, 1, 1, 1)
        primary_layout.addWidget(yaw_group, 1, 1, 1, 1)
        tabs.addTab(primary_tab, "Flight Controls")
        
        # Advanced parameters tab
        advanced_tab = QWidget()
        advanced_layout = QGridLayout(advanced_tab)
        parameters = [
            "Max Altitude", "Max Speed", "Return Altitude",
            "Loiter Radius", "Waypoint Radius", "Max Climb Rate"
        ]
        
        for i, param in enumerate(parameters):
            row, col = i // 2, i % 2
            param_group = QGroupBox(param)
            param_layout = QHBoxLayout(param_group)
            spin_box = QSpinBox()
            spin_box.setMinimum(0)
            spin_box.setMaximum(1000)
            param_layout.addWidget(spin_box)
            advanced_layout.addWidget(param_group, row, col)
            
        tabs.addTab(advanced_tab, "Advanced Parameters")
        
        # Add the tabs to the layout
        layout.addWidget(tabs)
        
        # Add telemetry display
        telemetry_group = QGroupBox("Telemetry")
        telemetry_layout = QGridLayout(telemetry_group)
        
        telemetry_items = [
            ("Altitude", "0 m"),
            ("Airspeed", "0 m/s"),
            ("Ground Speed", "0 m/s"),
            ("Distance", "0 m"),
            ("Vertical Speed", "0 m/s"),
            ("Heading", "0°"),
        ]
        
        for i, (label, value) in enumerate(telemetry_items):
            row, col = i // 3, i % 3
            telemetry_layout.addWidget(QLabel(label), row*2, col)
            value_label = QLabel(value)
            value_label.setStyleSheet("font-weight: bold; color: #0066cc;")
            telemetry_layout.addWidget(value_label, row*2+1, col)
        
        layout.addWidget(telemetry_group)
        
    def create_visualization_panel(self, layout):
        # Tab widget for map and camera views
        viz_tabs = QTabWidget()
        
        # Map view placeholder
        map_widget = QWidget()
        map_layout = QVBoxLayout(map_widget)
        map_placeholder = QLabel("Map View")
        map_placeholder.setAlignment(Qt.AlignCenter)
        map_placeholder.setStyleSheet("background-color: #e0e0e0; border: 1px solid #999;")
        map_placeholder.setMinimumHeight(400)
        map_layout.addWidget(map_placeholder)
        viz_tabs.addTab(map_widget, "Map View")
        
        # Camera feed placeholder
        camera_widget = QWidget()
        camera_layout = QVBoxLayout(camera_widget)
        camera_placeholder = QLabel("Camera Feed")
        camera_placeholder.setAlignment(Qt.AlignCenter)
        camera_placeholder.setStyleSheet("background-color: black; color: white; border: 1px solid #999;")
        camera_placeholder.setMinimumHeight(400)
        camera_layout.addWidget(camera_placeholder)
        viz_tabs.addTab(camera_widget, "Camera Feed")
        
        # Add the visualization tabs to the layout
        layout.addWidget(viz_tabs)
        
        # Add position information
        position_group = QGroupBox("Position Information")
        position_layout = QGridLayout(position_group)
        
        position_items = [
            ("Latitude", "0.000000° N"),
            ("Longitude", "0.000000° E"),
            ("Relative Altitude", "0 m"),
            ("Absolute Altitude", "0 m"),
        ]
        
        for i, (label, value) in enumerate(position_items):
            row, col = i // 2, i % 2
            position_layout.addWidget(QLabel(label), row, col*2)
            value_label = QLabel(value)
            value_label.setStyleSheet("font-weight: bold;")
            position_layout.addWidget(value_label, row, col*2+1)
        
        layout.addWidget(position_group)
        
    def create_mission_panel(self, layout):
        # Mission control
        mission_group = QGroupBox("Mission Control")
        mission_layout = QHBoxLayout(mission_group)
        
        mission_buttons = [
            "Load Mission", "Upload Mission", "Start Mission", 
            "Pause Mission", "Resume Mission", "Abort Mission"
        ]
        
        for button_text in mission_buttons:
            button = QPushButton(button_text)
            mission_layout.addWidget(button)
            
        layout.addWidget(mission_group)
        
        # Emergency controls
        emergency_group = QGroupBox("Emergency Controls")
        emergency_layout = QHBoxLayout(emergency_group)
        
        rtl_button = QPushButton("Return To Launch")
        rtl_button.setStyleSheet("background-color: orange;")
        emergency_layout.addWidget(rtl_button)
        
        land_button = QPushButton("Land Now")
        land_button.setStyleSheet("background-color: yellow;")
        emergency_layout.addWidget(land_button)
        
        emergency_button = QPushButton("EMERGENCY STOP")
        emergency_button.setStyleSheet("background-color: red; color: white; font-weight: bold;")
        emergency_layout.addWidget(emergency_button)
        
        layout.addWidget(emergency_group)

    # Add update functions for each control
    def update_throttle_label(self, value):
        self.throttle_label.setText(f"{value}%")
        
    def update_pitch_label(self, value):
        self.pitch_value_label.setText(f"{value}°")
        
    def update_roll_label(self, value):
        self.roll_value_label.setText(f"{value}°")
        
    def update_yaw_label(self, value):
        self.yaw_label.setText(f"{value}°")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = UAVControlInterface()
    window.show()
    sys.exit(app.exec_())

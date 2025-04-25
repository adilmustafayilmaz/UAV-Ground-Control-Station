import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QGridLayout, QLabel, QSlider, QPushButton, 
                            QGroupBox, QTabWidget, QComboBox, QFrame, QSplitter,
                            QProgressBar, QDial, QSpinBox, QLineEdit, QLayout)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QColor, QPalette, QPixmap

class UAVControlInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('UAV Control Interface')
        self.setGeometry(50, 50, 1600, 900)  # Pencere boyutunu artırıyorum, daha geniş ve yüksek
        self.showMaximized()  # Uygulamayı tam ekran modunda başlat
        
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
        
        # Left panel - Controls and Login
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        self.create_login_panel(left_layout)  # New login panel
        self.create_control_panel(left_layout)
        left_panel.setMinimumWidth(250)  # Set minimum width for control panel
        left_panel.setMaximumWidth(300)  # Set maximum width for control panel
        content_splitter.addWidget(left_panel)
        
        # Right panel - Map/Camera View
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        self.create_visualization_panel(right_layout)
        content_splitter.addWidget(right_panel)
        
        # Set the splitter sizes - give much more space to the right visualization panel
        content_splitter.setSizes([1, 5])  # 1:5 ratio
        main_layout.addWidget(content_splitter, 1)  # Add stretch factor of 1
        
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
        logo_container_layout.setContentsMargins(5, 2, 5, 2)  # Reduce vertical margins
        
        # Add stretch before logo to center it
        logo_container_layout.addStretch(1)
        
        # Create logo label
        logo_label = QLabel()
        # Try to load the actual logo
        logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "APEX_LOGO_3.png")
        
        if os.path.exists(logo_path):
            pixmap = QPixmap(logo_path)
            # Scale logo to appropriate size with increased width and reduced height
            pixmap = pixmap.scaled(300, 60, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            logo_label.setPixmap(pixmap)
        else:
            # Create a placeholder text label if logo file doesn't exist
            logo_label.setText("UAV CONTROL SYSTEM")
            logo_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #003366;")
            logo_label.setMinimumWidth(300)
            logo_label.setMaximumHeight(60)
        
        logo_container_layout.addWidget(logo_label, alignment=Qt.AlignCenter)
        
        # Add stretch after logo to center it
        logo_container_layout.addStretch(1)
        
        layout.addWidget(logo_container)
    
    def create_login_panel(self, layout):
        # Create login group box
        login_group = QGroupBox("Server Login")
        login_layout = QVBoxLayout(login_group)
        login_layout.setContentsMargins(3, 3, 3, 3)  # Reduce margins even more
        login_layout.setSpacing(2)  # Reduce spacing between elements
        
        # Username and password in a more compact layout
        credentials_layout = QGridLayout()
        credentials_layout.setSpacing(2)  # Reduce spacing
        
        username_label = QLabel("Username:")
        username_label.setMaximumHeight(20)  # Smaller label
        self.username_input = QLineEdit()
        self.username_input.setMaximumHeight(20)  # Even smaller height
        
        password_label = QLabel("Password:")
        password_label.setMaximumHeight(20)  # Smaller label
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)  # Hide password characters
        self.password_input.setMaximumHeight(20)  # Even smaller height
        
        credentials_layout.addWidget(username_label, 0, 0)
        credentials_layout.addWidget(self.username_input, 0, 1)
        credentials_layout.addWidget(password_label, 1, 0)
        credentials_layout.addWidget(self.password_input, 1, 1)
        
        login_layout.addLayout(credentials_layout)
        
        # Login button and status in one row
        login_button_layout = QHBoxLayout()
        login_button_layout.setSpacing(2)  # Reduced spacing
        
        login_button = QPushButton("Login")
        login_button.clicked.connect(self.handle_login)
        login_button.setMaximumWidth(70)  # Make button smaller
        login_button.setMaximumHeight(20)  # Make button shorter
        login_button_layout.addWidget(login_button)
        
        # Status label
        self.login_status = QLabel("")
        self.login_status.setMaximumHeight(15)  # Make label smaller
        login_button_layout.addWidget(self.login_status)
        login_button_layout.addStretch(1)  # Push everything to the left
        
        login_layout.addLayout(login_button_layout)
        
        layout.addWidget(login_group)
        
    def handle_login(self):
        # This is just the UI part, actual login logic would go here
        # For this demo, we'll just simulate a successful login
        self.login_status.setText("Successful")
        self.login_status.setStyleSheet("color: green; font-weight: bold;")
            
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
        
        # Flight mode - Sadece Autonomous ve Manual seçenekleri
        mode_group = QGroupBox("Flight Mode")
        mode_layout = QHBoxLayout(mode_group)
        mode_combo = QComboBox()
        mode_combo.addItems(["Manual", "Autonomous"])
        mode_layout.addWidget(mode_combo)
        layout.addWidget(mode_group)

    def create_control_panel(self, layout):
        # Add telemetry display
        telemetry_group = QGroupBox("Telemetry")
        telemetry_layout = QGridLayout(telemetry_group)
        telemetry_layout.setContentsMargins(5, 5, 5, 5)  # Biraz daha makul kenar boşlukları
        telemetry_layout.setVerticalSpacing(2)  # Dikey boşlukları biraz arttır
        telemetry_layout.setHorizontalSpacing(10)  # Yatay boşlukları arttır
        
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
            label_widget = QLabel(label)
            label_widget.setMaximumHeight(20)  # Daha okunabilir yükseklik
            # Font boyutunu varsayılana bırak
            
            telemetry_layout.addWidget(label_widget, row*2, col)
            
            value_label = QLabel(value)
            value_label.setMaximumHeight(20)  # Daha okunabilir yükseklik 
            value_label.setStyleSheet("font-weight: bold; color: #0066cc;")  # Normal font boyutu
            telemetry_layout.addWidget(value_label, row*2+1, col)
        
        layout.addWidget(telemetry_group)
        
    def create_visualization_panel(self, layout):
        # Main visualization container
        viz_container = QWidget()
        viz_layout = QVBoxLayout(viz_container)
        
        # Create a splitter for map and camera views (yatay olarak yan yana)
        views_splitter = QSplitter(Qt.Horizontal)
        
        # Map view placeholder
        map_group = QGroupBox("Map View")
        map_layout = QVBoxLayout(map_group)
        map_layout.setContentsMargins(5, 5, 5, 5)  # Kenarlık boşluklarını azalt
        map_placeholder = QLabel("Map View")
        map_placeholder.setAlignment(Qt.AlignCenter)
        map_placeholder.setStyleSheet("background-color: #e0e0e0; border: 1px solid #999;")
        # Increase minimum sizes for larger display
        map_placeholder.setMinimumHeight(400)  # Increased from 350
        map_placeholder.setMinimumWidth(450)   # Increased from 350
        map_layout.addWidget(map_placeholder)
        views_splitter.addWidget(map_group)
        
        # Camera feed placeholder
        camera_group = QGroupBox("Camera Feed")
        camera_layout = QVBoxLayout(camera_group)
        camera_layout.setContentsMargins(5, 5, 5, 5)  # Kenarlık boşluklarını azalt
        camera_placeholder = QLabel("Camera Feed")
        camera_placeholder.setAlignment(Qt.AlignCenter)
        camera_placeholder.setStyleSheet("background-color: black; color: white; border: 1px solid #999;")
        # Increase minimum sizes for larger display
        camera_placeholder.setMinimumHeight(400)  # Increased from 350
        camera_placeholder.setMinimumWidth(450)   # Increased from 350
        camera_layout.addWidget(camera_placeholder)
        views_splitter.addWidget(camera_group)
        
        # Set initial sizes for the views (equal distribution)
        views_splitter.setSizes([500, 500])  # Increased from 450, 450
        
        # Add the views splitter to the layout with stretch factor
        viz_layout.addWidget(views_splitter, 1)  # Add stretch factor of 1
        
        # Add position information (with reduced height)
        position_group = QGroupBox("Position Information")
        position_layout = QGridLayout(position_group)
        position_layout.setContentsMargins(5, 5, 5, 5)  # Kenarlık boşluklarını azalt
        
        position_items = [
            ("Latitude", "0.000000° N"),
            ("Longitude", "0.000000° E"),
            ("Relative Altitude", "0 m"),
            ("Absolute Altitude", "0 m"),
        ]
        
        for i, (label, value) in enumerate(position_items):
            row, col = i // 4, i % 4  # Her satırda 4 öğe olacak şekilde düzenle
            position_layout.addWidget(QLabel(label), row, col*2)
            value_label = QLabel(value)
            value_label.setStyleSheet("font-weight: bold;")
            position_layout.addWidget(value_label, row, col*2+1)
        
        # Add position group with fixed maximum height to give more space to map/camera
        position_group.setMaximumHeight(60)  # Limit height of position information
        viz_layout.addWidget(position_group, 0)  # No stretch factor
        
        # Add the visualization container to the main layout with increased stretch
        layout.addWidget(viz_container, 2)  # Increased stretch factor from 1 to 2
        
    def create_mission_panel(self, layout):
        # Create a tab widget for mission control
        mission_tabs = QTabWidget()
        
        # Combined Autonomous Flight and Target Tracking tab
        autonomous_tab = QWidget()
        autonomous_layout = QVBoxLayout(autonomous_tab)
        
        # Top section: Create a horizontal layout for the first row of groups
        top_section = QHBoxLayout()
        
        # Autonomous takeoff & landing (Left side)
        takeoff_landing_group = QGroupBox("Takeoff And Landing")
        takeoff_landing_layout = QGridLayout(takeoff_landing_group)
        
        # Autonomous takeoff
        auto_takeoff_button = QPushButton("Autonomous Takeoff")
        auto_takeoff_button.setStyleSheet("background-color: #66CC66; font-weight: bold;")
        takeoff_landing_layout.addWidget(auto_takeoff_button, 0, 0)
        
        # Manual takeoff
        manual_takeoff_button = QPushButton("Manual Takeoff")
        manual_takeoff_button.setStyleSheet("background-color: #CCFF99;")
        takeoff_landing_layout.addWidget(manual_takeoff_button, 0, 1)
        
        # Autonomous landing
        auto_landing_button = QPushButton("Autonomous Landing")
        auto_landing_button.setStyleSheet("background-color: #66CC66; font-weight: bold;")
        takeoff_landing_layout.addWidget(auto_landing_button, 1, 0)
        
        # Manual landing
        manual_landing_button = QPushButton("Manual Landing")
        manual_landing_button.setStyleSheet("background-color: #CCFF99;")
        takeoff_landing_layout.addWidget(manual_landing_button, 1, 1)
        
        top_section.addWidget(takeoff_landing_group)
        autonomous_layout.addLayout(top_section)
        
        # Bottom section: Create a horizontal layout for the second row of groups
        bottom_section = QHBoxLayout()
        
        # Route following (Left side)
        route_group = QGroupBox("Route Following")
        route_layout = QGridLayout(route_group)
        
        # Start route following
        start_route_button = QPushButton("Start Route Following")
        start_route_button.setStyleSheet("background-color: #66CCFF; font-weight: bold;")
        route_layout.addWidget(start_route_button, 0, 0)
        
        # Pause route
        pause_route_button = QPushButton("Pause Route")
        route_layout.addWidget(pause_route_button, 0, 1)
        
        # Resume route
        resume_route_button = QPushButton("Resume Route")
        route_layout.addWidget(resume_route_button, 1, 0)
        
        # Cancel route
        cancel_route_button = QPushButton("Cancel Route")
        route_layout.addWidget(cancel_route_button, 1, 1)
        
        bottom_section.addWidget(route_group)
        
        autonomous_layout.addLayout(bottom_section)
        
        mission_tabs.addTab(autonomous_tab, "Autonomous Flight Control")
        
        # Add the mission tabs to the layout
        layout.addWidget(mission_tabs, 3)
        
        # Enemy Aircraft Selection Menu (Bottom right corner)
        enemy_aircraft_group = QGroupBox("Enemy Aircraft Selection")
        enemy_aircraft_layout = QVBoxLayout(enemy_aircraft_group)
        
        # Information label
        info_label = QLabel("Select an aircraft to target:")
        enemy_aircraft_layout.addWidget(info_label)
        
        # Sample aircraft data - in a real application, this would be populated from server data
        aircraft_data = [
            {"team_id": 1, "altitude": 1200, "speed": 80},
            {"team_id": 2, "altitude": 950, "speed": 75},
            {"team_id": 3, "altitude": 1500, "speed": 90},
            {"team_id": 4, "altitude": 1100, "speed": 85}
        ]
        
        # Create buttons for each aircraft (one aircraft, one button)
        self.aircraft_buttons = []
        for aircraft in aircraft_data:
            aircraft_button = QPushButton(f"Team ID: {aircraft['team_id']} - Alt: {aircraft['altitude']}m - Speed: {aircraft['speed']}km/h")
            aircraft_button.setCheckable(True)  # Make the button checkable
            aircraft_button.setStyleSheet("text-align: left; padding-left: 10px;")
            aircraft_button.clicked.connect(lambda checked, btn=aircraft_button: self.select_aircraft(btn))
            self.aircraft_buttons.append(aircraft_button)
            enemy_aircraft_layout.addWidget(aircraft_button)
        
        # Auto-select the first aircraft
        if self.aircraft_buttons:
            self.aircraft_buttons[0].setChecked(True)
            self.current_aircraft = self.aircraft_buttons[0]
        
        # Submit button to lock onto selected aircraft
        submit_button = QPushButton("LOCK TARGET")
        submit_button.setStyleSheet("background-color: #FF9933; color: black; font-weight: bold; font-size: 13px;")
        submit_button.setMinimumHeight(35)
        enemy_aircraft_layout.addWidget(submit_button)
        
        # Add to layout (with smaller proportion than mission tabs)
        layout.addWidget(enemy_aircraft_group, 1)
        
        # Emergency controls
        emergency_group = QGroupBox("Emergency Controls")
        emergency_layout = QVBoxLayout(emergency_group)  # Changed to vertical layout
        
        rtl_button = QPushButton("Return To Launch")
        rtl_button.setStyleSheet("background-color: orange;")
        rtl_button.setMinimumHeight(60)  # Increased height
        emergency_layout.addWidget(rtl_button)
        
        kamikaze_button = QPushButton("KAMIKAZE")
        kamikaze_button.setStyleSheet("background-color: #8B0000; color: white; font-weight: bold;")
        kamikaze_button.setMinimumHeight(60)  # Increased height
        emergency_layout.addWidget(kamikaze_button)
        
        emergency_button = QPushButton("EMERGENCY STOP")
        emergency_button.setStyleSheet("background-color: red; color: white; font-weight: bold;")
        emergency_button.setMinimumHeight(60)  # Increased height
        emergency_layout.addWidget(emergency_button)
        
        layout.addWidget(emergency_group, 1)
        
    def select_aircraft(self, selected_button):
        # Uncheck all other buttons
        for button in self.aircraft_buttons:
            if button != selected_button:
                button.setChecked(False)
        
        # Store the currently selected aircraft
        self.current_aircraft = selected_button
        
        # Highlight the selected button
        selected_button.setStyleSheet("text-align: left; padding-left: 10px; background-color: #DDDDFF;")
        
        # Reset style for unselected buttons
        for button in self.aircraft_buttons:
            if button != selected_button:
                button.setStyleSheet("text-align: left; padding-left: 10px;")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = UAVControlInterface()
    window.show()
    sys.exit(app.exec_())
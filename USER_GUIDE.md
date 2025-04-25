# UAV Ground Control Station - User Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [User Interface Overview](#user-interface-overview)
4. [Top Status Bar](#top-status-bar)
5. [Left Control Panel](#left-control-panel)
   - [Server Login](#server-login)
   - [Telemetry Display](#telemetry-display)
6. [Visualization Panel](#visualization-panel)
   - [Map View](#map-view)
   - [Camera Feed](#camera-feed)
   - [Position Information](#position-information)
7. [Mission Control Panel](#mission-control-panel)
   - [Autonomous Flight Control](#autonomous-flight-control)
   - [Route Following](#route-following)
8. [Enemy Aircraft Selection](#enemy-aircraft-selection)
9. [Emergency Controls](#emergency-controls)
10. [Keyboard Shortcuts](#keyboard-shortcuts)
11. [Troubleshooting](#troubleshooting)

## Introduction

The UAV Ground Control Station is a sophisticated application designed for controlling and monitoring Unmanned Aerial Vehicles (UAVs) in real-time. This user guide provides detailed instructions on how to use each component of the interface effectively.

## Getting Started

### System Requirements
- Operating System: Windows, macOS, or Linux
- Minimum screen resolution: 1280 x 720 (1920 x 1080 recommended)
- Python 3.6 or higher with PyQt5 installed

### Installation
1. Ensure Python and PyQt5 are installed on your system
2. Clone or download the UAV-Ground-Control-Station repository
3. Install required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```
4. Launch the application by running:
   ```
   python updated_uav_control_interface.py
   ```

## User Interface Overview

The UAV Ground Control Station interface is divided into several key areas:

- **Top Bar**: Contains the logo and status indicators
- **Left Panel**: Includes login credentials and telemetry data
- **Center Panel**: Displays map view and camera feed
- **Bottom Panel**: Contains mission control options and emergency controls

The interface is designed to maximize visibility of critical visual information (map and camera) while providing easy access to control functions.

## Top Status Bar

### Connection Status
- **Location**: Top right of the screen
- **Description**: Indicates the connection status between the ground station and the UAV
- **States**:
  - "CONNECTED" (green): The system is successfully connected to the UAV
  - "DISCONNECTED" (red): No connection to the UAV is established
  - "CONNECTING" (yellow): Attempting to establish a connection

### Battery Status
- **Location**: Top right, next to Connection Status
- **Description**: Shows the current battery level of the UAV
- **Features**:
  - Progress bar showing visual representation of the battery percentage
  - Numerical percentage display
  - Color indicators: Green (>50%), Yellow (20-50%), Red (<20%)

### Flight Mode
- **Location**: Top right, next to Battery Status
- **Description**: Dropdown menu to select the flight control mode
- **Options**:
  - "Manual": User has direct control over the UAV
  - "Autonomous": UAV follows pre-programmed missions or algorithmic control

## Left Control Panel

### Server Login
- **Location**: Upper left corner of the application
- **Purpose**: Connect to the UAV control server for remote operation
- **Components**:
  - **Username field**: Enter your authorized username
  - **Password field**: Enter your secure password (displayed as dots for security)
  - **Login button**: Click to authenticate with the server
  - **Status indicator**: Shows "Successful" in green when login is complete

### Telemetry Display
- **Location**: Left panel, below login section
- **Purpose**: Real-time display of critical flight parameters
- **Displayed Information**:
  - **Altitude**: Current height of the UAV above ground level (in meters)
  - **Airspeed**: Speed of the UAV relative to the air (in meters per second)
  - **Ground Speed**: Speed of the UAV relative to the ground (in meters per second)
  - **Distance**: Distance traveled from the starting point (in meters)
  - **Vertical Speed**: Rate of climb or descent (in meters per second)
  - **Heading**: Direction the UAV is facing (in degrees, 0° = North)

## Visualization Panel

### Map View
- **Location**: Main central area, left side
- **Purpose**: Shows the UAV's location, flight path, and surrounding terrain
- **Features**:
  - Real-time position tracking
  - Route visualization
  - Waypoint markers
  - Scale indicator
  - Interactive elements (in the full implementation)

### Camera Feed
- **Location**: Main central area, right side
- **Purpose**: Live video feed from the UAV's onboard camera
- **Features**:
  - Real-time video stream
  - Target identification markers (when available)
  - Visual indicators for lock-on status

### Position Information
- **Location**: Below Map and Camera views
- **Purpose**: Precise location data of the UAV
- **Displayed Information**:
  - **Latitude**: Current north-south position (in degrees)
  - **Longitude**: Current east-west position (in degrees)
  - **Relative Altitude**: Height above the takeoff point (in meters)
  - **Absolute Altitude**: Height above sea level (in meters)

## Mission Control Panel

### Autonomous Flight Control
- **Location**: Bottom of the screen, left side
- **Purpose**: Controls for takeoff and landing operations
- **Buttons**:
  - **Autonomous Takeoff** (Green): Initiates autonomous takeoff sequence
  - **Manual Takeoff** (Light Green): Prepares for user-controlled takeoff
  - **Autonomous Landing** (Green): Initiates autonomous landing sequence
  - **Manual Landing** (Light Green): Prepares for user-controlled landing

### Route Following
- **Location**: Bottom of the screen, left side, below Takeoff & Landing
- **Purpose**: Controls for predefined route navigation
- **Buttons**:
  - **Start Route Following** (Blue): Begins navigation along the pre-planned route
  - **Pause Route**: Temporarily stops route following while maintaining position
  - **Resume Route**: Continues route following from the current position
  - **Cancel Route**: Aborts route following completely

## Enemy Aircraft Selection

- **Location**: Bottom right section
- **Purpose**: Identification and selection of target aircraft
- **Components**:
  - **Information label**: Instructs the user to select a target
  - **Aircraft list**: Shows detected aircraft with their Team ID, Altitude, and Speed
  - **Selection mechanism**: Click on an aircraft to select it (highlights in light blue)
  - **LOCK TARGET button** (Orange): Confirms selection and initiates tracking of the selected aircraft

## Emergency Controls

- **Location**: Bottom right corner
- **Purpose**: Quick access to critical safety functions
- **Buttons**:
  - **Return To Launch** (Orange): Commands the UAV to return to the takeoff location
  - **KAMIKAZE** (Dark Red): Initiates a directed impact sequence (use with extreme caution)
  - **EMERGENCY STOP** (Bright Red): Immediately cuts all motors for emergency situations
  
  > **WARNING**: The Emergency Stop function will cause the UAV to fall from its current position. Use only in extreme emergencies when the risk of continued flight exceeds the risk of an uncontrolled descent.

## Keyboard Shortcuts

| Function | Shortcut |
|----------|----------|
| Return To Launch | F1 |
| Emergency Stop | F12 |
| Toggle Map/Camera Fullscreen | F11 |
| Switch to Manual Mode | Ctrl+M |
| Switch to Autonomous Mode | Ctrl+A |

## Troubleshooting

### Connection Issues
- Ensure your network connection is stable
- Verify that the UAV is powered on and within communication range
- Check that the correct server address is configured in the settings

### Display Problems
- If map or camera feed appears frozen, click the refresh button in their respective panels
- For blank displays, verify that the data sources are properly connected
- Adjust the split view by dragging the divider between map and camera feeds

### Emergency Procedures
1. If the UAV becomes unresponsive, first try the "Return To Launch" function
2. If control cannot be regained, use the "EMERGENCY STOP" button as a last resort
3. Always maintain visual contact with the UAV when possible during emergency situations

---

For technical support, please contact your system administrator or refer to the technical documentation included with your UAV Ground Control Station package.
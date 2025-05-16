Weather Notification System - Observer Design Pattern

Overview:
This project demonstrates the Observer Design Pattern in Python through a weather monitoring system. Devices such as phone displays, LED panels, and alarm systems subscribe to a central weather station and receive automatic updates when the temperature changes.

Structure:
- interfaces.py: Contains the Observer and Subject abstract base classes.
- weather_station.py: Implements the WeatherStation class (the Subject).
- devices.py: Contains three observer classes: PhoneDisplay, LEDDisplay, and AlarmSystem.
- main.py: Sets up the system, registers observers, and simulates temperature updates.

How to Run:
1. Save all files in the same folder.
2. Open a terminal and navigate to the folder.
3. Run:

   python main.py

Expected Output:
Each observer will receive real-time updates when the weather station's temperature changes. The alarm system will trigger alerts for high temperatures.

Key Concept:
The Observer Design Pattern enables a one-to-many relationship between objects. When the subject (WeatherStation) changes state, all registered observers are notified automatically.

Author:
Isa Zeynalov
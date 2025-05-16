# 🌦️ Weather Notification System

This project demonstrates the **Observer Design Pattern** in Python by simulating a smart weather notification system. Multiple display devices receive real-time temperature updates from a central weather station.

---

## 🛠️ Technologies Used

- Python 3.x  
- Object-Oriented Programming  
- Observer Design Pattern

---

## 🧠 Design Pattern: Observer

The **Observer Pattern** defines a one-to-many dependency between objects so that when one object (the subject) changes state, all its dependents (observers) are notified and updated automatically.

---

## 📁 Project Structure

- `interfaces.py` – Abstract base classes for Subject and Observer  
- `weather_station.py` – Implements the Subject (WeatherStation)  
- `devices.py` – Implements Observers (PhoneDisplay, LEDDisplay, AlarmSystem)  
- `main.py` – Sets up the system and simulates temperature changes  
- `README.md` – Project documentation

---

## 🚀 Features

- Real-time temperature update simulation  
- Devices automatically receive updates when the weather changes  
- Observers can be dynamically added or removed at runtime  
- Clear and modular code structure

---

## 📌 Sample Output

```

\[WeatherStation] Temperature updated to 22.5°C
\[PhoneDisplay] New temperature: 22.5°C
\[LEDDisplay] Display updated with temperature: 22.5°C
\[AlarmSystem] Temperature is normal: 22.5°C

\[WeatherStation] Temperature updated to 35.0°C
\[PhoneDisplay] New temperature: 35.0°C
\[LEDDisplay] Display updated with temperature: 35.0°C
\[AlarmSystem] WARNING: High temperature alert! 35.0°C

````

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/weather-notification-system.git
cd weather-notification-system
````

2. Run the main script:

```bash
python main.py
```

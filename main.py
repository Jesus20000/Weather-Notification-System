from weather_station import WeatherStation
from devices import PhoneDisplay, LEDDisplay, AlarmSystem

def main():
    weather_station = WeatherStation()

    phone_display = PhoneDisplay()
    led_display = LEDDisplay()
    alarm_system = AlarmSystem()

    weather_station.register_observer(phone_display)
    weather_station.register_observer(led_display)
    weather_station.register_observer(alarm_system)

    # Simulate weather changes
    weather_station.set_temperature(22.5)
    weather_station.set_temperature(35.0)

    # Remove LEDDisplay from observers
    weather_station.remove_observer(led_display)

    # Another temperature update
    weather_station.set_temperature(18.0)

if __name__ == "__main__":
    main()
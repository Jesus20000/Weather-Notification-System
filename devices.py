from interfaces import Observer

class PhoneDisplay(Observer):
    def update(self, temperature: float):
        print(f"[PhoneDisplay] New temperature: {temperature}°C")

class LEDDisplay(Observer):
    def update(self, temperature: float):
        print(f"[LEDDisplay] Display updated with temperature: {temperature}°C")

class AlarmSystem(Observer):
    def update(self, temperature: float):
        if temperature > 30:
            print(f"[AlarmSystem] WARNING: High temperature alert! {temperature}°C")
        else:
            print(f"[AlarmSystem] Temperature is normal: {temperature}°C")
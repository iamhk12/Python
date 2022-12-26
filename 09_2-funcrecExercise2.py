#WAP to convert celcius to farheineit in python using functions

# (0°C × 9/5) + 32 = 32°F

def celToFar(temperature):
    return (temperature * 9/5) + 32 



temp = int(input("Enter your temperature in celcius : "))

print(f"The temperature is {celToFar(temp)}")
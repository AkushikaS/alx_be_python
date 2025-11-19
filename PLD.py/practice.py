temperature_c = int(input("Input temperature in celsius: "))
temperature_F =temperature_c * 9/5 + 32

if temperature_c < 0:
    message = "It's freezing outside!"

elif 0<= temperature_c <=20:
    message = "It's a bit chilly."

else :
    message = "Nice and warm today!"
print(message , temperature_F ,"F")



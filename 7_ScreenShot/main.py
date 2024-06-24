import pyscreenshot
import playsound
import time

for i in range (2,1,-1):
    print(f"THE image will be capture in {i} Second.")
    time.sleep(1)
image = pyscreenshot.grab()
playsound.playsound('Beep.mp3')
# image.show()
image_name = input("What is the name of the Image ?\n")
image_name = "".join([image_name,".png"])
image.save(image_name)

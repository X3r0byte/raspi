# raspibot

This is an old python file I created in 2015 for my raspi bot. The majority of the functionality should be in here, but it is fragmented as some of the files went missing :(. Links to the bot:

* Video of bot actually focusing on colored balls https://youtu.be/Agu-XnRrfR4
* Controlling color find with keystrokes https://youtu.be/FwwYg9Q_K1o
* Bot in action! https://youtu.be/tfZEHYMBBGw

Essentially, the bot uses two ultrasonic sensors to judge distances and proximity, and one servo attached camera to track colors. If the bot cannot find the tracked color, it uses a servo to turn the camera about until the color comes into view. If the bot senses the color/ball is close, it stops and celebrates with R2D2 sounds :)

Hardware:
* Raspberry Pi 3
* Adafruit motor and servo hats
* 2 DC motors
* 2 ultrasonic sensors
* 1 servo
* 1 sacrificed webcam

Software:
* Custom python scripting
* Adafruit libraries to run hats


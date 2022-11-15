# MPV-OSC
control MPV with Open Sound Control 

It's simple script to remote an MPV player on windows/OSX/ubuntu (minimal)
starts by blacking out desktop, usable for videoplayback or digital signage

It's used on Rpi's and odroid C4 to start this script on boot

osc commands are:
```
/command "brightness down"
/command "brightness up"
/command "speed up"
/command "speed down"
/command "info"               # gives video info on screen
/command "quit"               # quit this script
/command "force shutdown"     # you can use this to shutdown rpi/odroid/linux os's but you need to disable sudo on shutdown for it to work
/command "force reboot"       # you can use this to reboot rpi/odroid/linux os's but you need to disable sudo on shutdown for it to work

/volume "100"                 # use 0 to 100
/play "file.mp4"              # you can use file's in the directory from the mpv default profile file or use youtube or other video links
/stop
/pause
```

python3.9 - Dependencies:
```
mpv
pythonosc
```

import mpv
from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server

import subprocess

ip="192.168.178.255"
port=53035

mpv = mpv.MPV(ytdl=True, keep_open=True, input_default_bindings=True, loop=True, osd_level=0)

#blackout console:
mpv.play("black.png")


def command_handler(unused_addr, *args):

    if args[0] == "restart":
        mpv.play("black.png")
        print("mpv is runing again :)")

    if args[0] == "brightness down":
        mpv.keypress(3)
        print(args[0])
    if args[0] == "brightness up":
        mpv.keypress(4)
        print(args[0])

#    if args[0] == "zoom in":
#        mpv.keypress('e')
#        print(args[0])
#    if args[0] == "zoom out":
#        mpv.keypress('w')
#        print(args[0])
    if args[0] == "speed up":
        mpv.keypress(']')
        print(args[0])
    if args[0] == "speed down":
        mpv.keypress('[')
        print(args[0])

    if args[0] == "osd":
        mpv.toggle_osd()
        print(args[0])

    if args[0] == "stop hold":
        mpv.keypress("Q")
        print(args[0])

    if args[0] == "info":
        mpv.keypress("i")
        print(args[0])

    if args[0] == "quit" or args[0] == "console":
        print("back to console! :)")
        subprocess.call(["pkill", "python"])

    if args[0] == "force reboot":
        mpv.stop()
        print("Rebooting, Bye :)")
        subprocess.call(["sudo", "reboot", "now"])

    if args[0] == "force shutdown":
        mpv.stop()
        print("Shutting down, Bye :)")
        subprocess.call(["sudo", "shutdown", "now"])


def volume_handler(unused_addr, args):
    arg = round(args,2)
    print(unused_addr, arg)
    mpv.volume = arg

def play_handler(unused_addr, args):
    args = str(args)
    print(unused_addr, args)
    mpv.play(args)
    mpv.wait_for_playback()

def stop_handler(unused_addr, *args):
    print(unused_addr, args)
    mpv.stop()
    mpv.play("black.png")

def pause_handler(unused_addr, *args):
    mpv.keypress('P')
    print('pause key pressed')

dispatcher = Dispatcher()
dispatcher.map("/command", command_handler)
dispatcher.map("/volume", volume_handler)
dispatcher.map("/play", play_handler)
dispatcher.map("/stop", stop_handler)
dispatcher.map("/pause", pause_handler)

server = osc_server.ThreadingOSCUDPServer(
    (ip, port), dispatcher)
print("Serving on {}".format(server.server_address))
server.serve_forever()


README - Session Idle Inhibit Indicator
=======================================

Inhibiting a session from turning idle typically prevents the monitor from going
to sleep and/or the screensaver from activating. This is desirable when watching
videos on your computer. Some applications capable of video playback don't do
this, and as a result your screensaver can activate during video playback.

This simple indicator app allows you to see the status of session idle
inhibiting, and also to manually inhibit the session from turning idle, thus
preventing your monitor from turning off. Inhibiting the session from being
marked idle effectively disables all screensaver and monitor power save
functions. It will also instantly show you when other applications are
inhibiting the session from turning idle, such as VLC and Totem during video
playback.


Requirements
------------ 

This small app is written for Ubuntu+Gnome3 environment, typically Gnome Shell 
based these days. It requires the Appindicator Gnome shell extension to be 
active. If you require something more advanced, then I recommend you check out 
the Caffeine project instead, which supports more environments and has much more 
features: https://launchpad.net/caffeine


Installation to /usr/local on Ubuntu
------------------------------------

    sudo apt install gir1.2-appindicator3-0.1 python3-xdg
    sudo python3 setup.py install

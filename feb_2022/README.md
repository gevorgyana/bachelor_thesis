1. Do the ALSA component investigation.
You need to check the core repositories (kernel API and C library)

2. Do the investigation of the wm (window manager).

High-level tasks
1) ALSA PCM listen to the sound cards on demand (
  - maybe use systemd udev, too.
  - maybe use device tree? most probably, this is not needed
)
2) Integrate with the window manager that claims to be only keyboard-aware.
3) Facebook Flashlight, remember this thing
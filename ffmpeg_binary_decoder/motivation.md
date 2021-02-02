When we type characters using a keyboard, we make use of a whole infrastructure that
makes sense of our moves. These moves are unique, but they translate to a series of
characters by a keyboard, device driver, operating system, cpu. The same must be done
with voice to get a stable and rigid system that we can use to interact with computers.
The first thing that should be tried is trying to differentiate between sound and
silence. This can be done using ffmpeg, ffplay. These tools provide graphs of the sound
that is being played, so that each time point is matched to a certain point on some
scale. Let's choose a threshold and say that everything below that is silence,
everything else is a sound. If we do that, we can now use binary encoding to enter
informaton to the computer.

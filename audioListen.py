import pyglet

file = pyglet.resource.media('audio/focus.wav')
print("before play")
file.play()
print("after play")


pyglet.app.run()

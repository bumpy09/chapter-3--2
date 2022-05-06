def on_button_pressed_a():
    music.change_tempo_by(50)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    music.stop_melody(MelodyStopOptions.ALL)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_melody_ended():
    basic.clear_screen()
music.on_event(MusicEvent.MELODY_ENDED, on_melody_ended)

def on_button_pressed_b():
    music.start_melody(music.built_in_melody(Melodies.ENTERTAINER),
        MelodyOptions.FOREVER)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_melody_started():
    basic.show_icon(IconNames.EIGTH_NOTE)
music.on_event(MusicEvent.MELODY_STARTED, on_melody_started)

music.set_tempo(120)
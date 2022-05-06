input.onButtonPressed(Button.A, function () {
    music.changeTempoBy(50)
})
input.onButtonPressed(Button.AB, function () {
    music.stopMelody(MelodyStopOptions.All)
})
music.onEvent(MusicEvent.MelodyEnded, function () {
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    music.startMelody(music.builtInMelody(Melodies.Entertainer), MelodyOptions.Forever)
})
music.onEvent(MusicEvent.MelodyStarted, function () {
    basic.showIcon(IconNames.EigthNote)
})
music.setTempo(120)

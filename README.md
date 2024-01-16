# Musician-AI
Using genetic algorithm from scratch and python package scamp to produce melodies with different instruments.
The user scores the melodies (*Which is really a tedious process*) and save them as MIDI files (*Not implemented yet*). 


## TODOs 
- [ ] Current algorithm uses duration and number of notes to be played. Change them to bars and notes per bar
- [ ] Implement number_of_bars, notes_per_bar, number_of_pitches_per_note (allow for 2 pitches or more per note) as the inputs
- [x] I know what pitch corresponds to conventional notes. For example 60 -> C4 and 72 -> C5.
- [ ] Saving a melody as a MIDI file from the code itself (It is possible to use "MuseScore 3" which scamp supports) 
- [ ] If the user enters a invalid input, program closes. It shouldn't do.
- [ ] Play metronome sound on top of the melody playing.
- [ ] If population size is odd, while generating the new generation, it makes the new generation size -> population size - 1 
- [ ] Create multiple MIDIs and put them together to make a AI-Music.

Inspired by [this video](https://youtu.be/aOsET8KapQQ?si=YWnSoHEe_7Fyb7yq)


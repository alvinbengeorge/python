from pygame import midi as m
import time
m.init()
print(m.get_count())
midi=m.Output(1)
midi.set_instrument(64,0)
midi.set_instrument(64,1)
midi.note_on(48,100)
for i in range(48,56):
    midi.note_on(i,100,1)
    time.sleep(0.8)
    midi.note_off(i,100,1)
midi.note_off(48,100,0)
time.sleep(10)
for i in range(0,127):
    midi.set_instrument(i,0)
    for j in range(48,72):
        midi.note_on(j,127)
        time.sleep(0.04)        
        midi.note_off(j,127)
    print(i)    
        
    

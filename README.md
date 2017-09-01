# PyEnigma

PyEnigma is an Enigma code machine emulator, written in Python. It is fully working, but not garunteed to be the most efficient implementation, as it is only for fun.

You can run PyEnigma as a normal Python script, or use it like an import library.

For example:
```
import PyEnigma

print(PyEnigma.enigChar("A"))
```

PyEnigma simulates every aspect of the Enigma machine, simulating rotors and their position, which changes as each key is pressed, as well as having full support for the Plugboard and different Reflectors. In theory, it is capable of simulating infinite ammounts of rotors, as well as the common setups such as the Luftwaffe/Wehrmacht 3 rotor setup, and Kreigsmarine 4 rotor machines.

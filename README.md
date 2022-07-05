# Trabajo Practico Final
In this repository you will find differents files which are part of a one big project oriented to the traduction of text files to wav audios and communication with an extern real instrument.
The repository has three big directories: Synthetizer, xylophone.
In Synthetizer directory you'll find the main files, the ones able to be run and the construction files (from classes to functions). The xylophone directory has all te files and extensions to work with the xylophone and the xilo_reader has specific files to correctly read music scores and filter the notes that the xylophone is able to receive.

In order to use this repository the user has to introduce in any console, a sample frequency, the instrument text, then the music score and finally the wav file where the audio is saved. 

```shell
python .\main.py -f <frequency> -i <instrument> -p <score> -o <audio.wav>
```

And for the xylophone the user has to write in the console -> the music score and the device. Remember that is a necessary condition to be inside the xylophone directory in order to be able to use this parser.

```shell
python -\main.py -p <score> -d <device>
```

## Installation

This is fairly straightforward as it can be installed with pip.
Execute the following steps:

1. Clone the repository.

```shell
$ git clone https://github.com/Zoevelazquez0430/Tp-final.git 
```

1. Install the dependencies.

```shell
$ pip install -r requirements.txt
```

1. Install it with pip

```shell
$ pip install .
```



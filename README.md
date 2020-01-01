# genus-suche
search for entries in a slob dictionary with grammatical gender

## Installation

For installing [slob](https://github.com/itkach/slob.git) you first need
to install its dependency PyICU, e.g. as follows on Debian or Ubuntu
(therefore PyICU is not part of the Pipfile):

```
sudo apt-get install python3-icu
```

If using Pipenv, you need to supply `--site-packages` to access to
PyICU (`--system-site-packages` for virtualenv):

```
pipenv --python 3 --site-packages
pipenv install
```

## Usage

The application expects the
[German-English FreeDict dictionary](https://freedict.org/downloads/#smartphones-and-tablets)
in the slob format. Please download it from https://download.freedict.org/dictionaries/deu-eng/0.3.5/freedict-deu-eng-0.3.5.slob
As of this writing, FreeDict dictionaries are
[licensed under GNU GPL 3.0](https://freedict.org/documentation/).
A newer version of this dictionary might also work, but please change
the file name in the script.

You can then run it like

```
python genus_suche.py
```

With version 0.3.5 of the dictionary, the output is:

```
Bettdecke (f)
Blutsverwandtschaft (f)
Geldautomat (m)
Kelle (f)
Lokalisierung (f)
Proband (m)
unglaublicher ( m)
Wärmflasche (f)
```

## Conclusion

It is unfortunate that the dictionary that contains 81624 words
(blob count) only provides gender information for those 8 words
(7 nouns and one
[conjugated adjective](http://www.dict.org/bin/Dict?Form=Dict2&Database=fd-deu-eng&Query=unglaublicher)).
Practical use of this result is therefore rather limited unless the
dictionary gets significantly improved in this aspect.

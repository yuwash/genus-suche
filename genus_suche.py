#!/usr/bin/env python
import itertools
from bs4 import BeautifulSoup
import slob


def iter_gen(keyditemdict):
    for i in range(len(keyditemdict)):
        item = keyditemdict.lst[i]  # slob.Blob
        soup = BeautifulSoup(item.content, 'html.parser')
        if soup.body is None:
            continue
        soup_gramgrp = soup.body.find(class_='gramGrp')
        if soup_gramgrp is None:
            continue
        soup_gen = soup_gramgrp.find(class_='gen')
        if soup_gen is None:
            continue
        yield item, soup_gen.string


def print_genus(keyditemdict, limit=50):
    """
    >>> import os.path
    >>> from tempfile import TemporaryDirectory
    >>> data = {'Erde': 'f', 'Planet': 'm', 'Gestein': 'n'}
    >>> content_template = (
    ...     '<html><head></head><body><div></div>'
    ...     '<div class="gramGrp"><div></div><div class="gen">{}</div></div>'
    ...     '</body></html>'
    ... )
    >>> with TemporaryDirectory() as dirname:
    ...     path = os.path.join(dirname, 'example.slob')
    ...     with slob.create(path) as w:
    ...         for word, gender in data.items():
    ...             w.add(
    ...                 content_template.format(gender).encode('utf-8'), word)
    ...     with slob.open(path) as r:
    ...         print_genus(r.as_dict())
    Erde (f)
    Gestein (n)
    Planet (m)
    """
    for item, gen in itertools.islice(iter_gen(keyditemdict), limit):
        print('{} ({})'.format(item.key, gen))


if __name__ == '__main__':
    # from https://download.freedict.org/dictionaries/deu-eng/0.3.5/freedict-deu-eng-0.3.5.slob
    with slob.open('freedict-deu-eng-0.3.5.slob') as r:
        d = r.as_dict()  # slob.KeydItemDict
        print_genus(d)

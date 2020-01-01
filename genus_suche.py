#!/usr/bin/env python
import itertools
from bs4 import BeautifulSoup
import slob


def iter_gen(keyditemdict):
    for i in range(len(keyditemdict)):
        item = d.lst[i]  # slob.Blob
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


if __name__ == '__main__':
    # from https://download.freedict.org/dictionaries/deu-eng/0.3.5/freedict-deu-eng-0.3.5.slob
    with slob.open('freedict-deu-eng-0.3.5.slob') as r:
        d = r.as_dict()  # slob.KeydItemDict
        for item, gen in itertools.islice(iter_gen(d), 50):
            print('{} ({})'.format(item.key, gen))

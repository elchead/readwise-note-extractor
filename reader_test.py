import pytest
import reader
from unittest.mock import patch, mock_open
import unittest.mock as mock


def open_mockfile(data):
    with patch("builtins.open", mock_open(read_data=data)) as mock_file:
        return open(mock_file)


def test_read_note():
    data = """---
categories: [Book-notes]
title: Hell Yeah or No - Derek Sivers
date: 2020-12-07
excerpt_separator: <!--more-->
resources:
- name: cover
  src: cover.jpeg
featuredImagePreview: cover.jpeg
---
## ☘️ How the Book Changed Me

How my life / behavior / thoughts / ideas have changed as a result of reading the book.

I've become more aware of my priorities and keeping enough time to engage in what is important to me.

I no longer define myself through my job achievements.

I believe that it is most valuable to follow your passion.

## 📒 Summary + Notes

### Doing

Actions, not words, reveal our real values.

"As an example, a friend was trying to decide whether to stick with his frustrating job or quit to start his own company. Options: build company outside of office hours and quit when its sustainable; show up at work and secretly work on your own company until they fire you; propose the idea to the boss and start it as a division..."

### Goals

Goals shape the present, not the future. If it was a great goal, you would have jumped into action already.

I've become more aware of my priorities and keeping enough time to engage in what is important to me."""

    read = reader.NoteReader(open_mockfile(data))
    notes = [
        "Actions, not words, reveal our real values.",
        '"As an example, a friend was trying to decide whether to stick with his frustrating job or quit to start his own company. Options: build company outside of office hours and quit when its sustainable; show up at work and secretly work on your own company until they fire you; propose the idea to the boss and start it as a division..."',
        "Goals shape the present, not the future. If it was a great goal, you would have jumped into action already.",
        "I've become more aware of my priorities and keeping enough time to engage in what is important to me.",
    ]
    for note in notes:
        assert read.get_note() == note


cases = [
    (
        """---
categories: [Book-notes]
title: Hell Yeah or No - Derek Sivers
date: 2020-12-07
excerpt_separator: <!--more-->
resources:
- name: cover
  src: cover.jpeg
featuredImagePreview: cover.jpeg
---""",
        "Derek Sivers",
        "Hell Yeah or No",
        "2020-12-07",
    ),
    (
        """---
categories: [Book-notes]
title: Never split the differences - Chris Voss
date: 2020-09-26
resources:
- name: cover
  src: cover.jpeg
featuredImagePreview: cover.jpeg
---
![cover.jpeg](./cover.jpeg)""",
        "Chris Voss",
        "Never split the differences",
        "2020-09-26",
    ),
    (
        """---
categories: [Book-notes]
title: The 4-Hour Work Week - Tim Ferris
date: 2021-03-10
excerpt_separator: <!--more-->
resources:
- name: cover
  src: cover.jpeg
featuredImagePreview: cover.jpeg
---
![cover.jpeg](./cover.jpg)
""",
        "Tim Ferris",
        "The 4-Hour Work Week",
        "2021-03-10",
    ),
]


@pytest.mark.parametrize("txt, author, title, date", cases)
def test_metadata(txt, author, title, date):

    for case in cases:
        metadata = reader.MetaReader(open_mockfile(txt))
        assert metadata.title == title
        assert metadata.author == author
        assert metadata.date == date

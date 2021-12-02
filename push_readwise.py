#!/usr/bin/env python
from reader import NoteReader, MetaReader
import reader, readwise


def push_highlights(filename):
    read = NoteReader(open(filename, "r"))
    meta = MetaReader(open(filename, "r"))
    notes = read.get_all_notes()
    highlights = readwise.create_book_highlights(notes, title=meta.title, author=meta.author, date=meta.date)
    print("Title:", meta.title)
    print("Author:", meta.author)
    print("Date:", meta.date)
    print("#Notes:", len(notes))
    resp = readwise.save_highlights(highlights)
    code = resp.status_code
    if code != 200:
        raise Exception(f"Request failed:{code}\nHighlights: {highlights}")


push_highlights("index.en.md")

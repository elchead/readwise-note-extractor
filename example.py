from reader import NoteReader, MetaReader
import reader, readwise


read = NoteReader(open("test.md", "r"))
meta = MetaReader(open("test.md", "r"))
highlights = readwise.create_book_highlights(read.get_all_notes(), title=meta.title, author=meta.author, date=meta.date)
print(readwise.save_highlights(highlights))

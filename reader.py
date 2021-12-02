import frontmatter


def is_headline(line):
    return line[:3] == "###"


def is_empty_line(line):
    return line == "\n" or ""


class MetaReader:
    def __init__(self, file):
        self.yaml = frontmatter.loads(file.read())

    def _title_author(self):
        entry = self.yaml["title"]
        title, author = entry.split(" - ")
        return title.strip(), author.strip()

    @property
    def author(self):
        _, author = self._title_author()
        return author

    @property
    def title(self):
        title, _ = self._title_author()
        return title

    @property
    def date(self):
        return str(self.yaml["date"])


class NoteReader:
    note_section = "## 📒 Summary + Notes\n"

    def __init__(self, file):
        self.file = file
        self._intro_skipped = False

    def _is_intro_skipped(self, line):
        if not self._intro_skipped:
            self._intro_skipped = line == self.note_section
        return self._intro_skipped

    def get_all_notes(self):
        notes = []
        for line in self.file:
            if self._is_note(line):
                notes.append(line.rstrip())
        return notes

    def get_note(self):
        for line in self.file:
            if self._is_note(line):
                return line.rstrip()

    def _is_note(self, line):
        return (
            self._is_intro_skipped(line)
            and line != self.note_section
            and not is_headline(line)
            and not is_empty_line(line)
        )

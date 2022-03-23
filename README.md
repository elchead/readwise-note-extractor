# 📝 Readwise Note Extractor

The script extracts highlights from a given (markdown) file and uploads them to Readwise.
The note reader is specific to my note formatting but can be easily adjusted.

## Format
I have initial metadata at the top of the file that I want to ignore. The ending of my metadata is detected through a specific text line (currently hardcoded).

A highlight is defined through linebreaks.
E.g.:
```
This is meta.
This line indicates end of meta.

This is a highlight.

This is another highlight.

...
```

## Installation

1. Create an `.env` file with your Readwise API token `TOKEN=...`.
2. To read the token, install:
   ```
   pip install python-decouple
   ```
3. Include in `PATH`. I created a symbolic link in a path included directory to directly run the script from anywhere.

   ```
   ln -s push_readwise.py ~/homebrew/bin
   ```

## Usage

Run `push_readwise.py` to upload the notes of the file (currently hardcoded to `index.en.md`)

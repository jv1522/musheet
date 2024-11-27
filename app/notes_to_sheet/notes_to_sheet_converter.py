import abjad
import os

from dotenv import load_dotenv

# Get the path to the directory this file is in
BASEDIR = os.path.abspath(os.path.dirname(__file__))
PARENTDIR = os.path.join(BASEDIR, os.pardir)
ENVDIR = os.path.join(PARENTDIR, os.pardir)

load_dotenv(os.path.join(ENVDIR, '.env'))
print(f"LILYPOND_PATH: {os.getenv('LILYPOND_PATH')}")

# os.environ['LILYPOND_PATH'] = os.getenv('LILYPOND_PATH')

music_notes = ['c', 'd', 'e', 'f', 'g', 'a', 'b']


def display_sheet_music(notes=""):
    if notes:
        # TODO: list(set([char for char in notes if char.isalpha()])) Check if every note in notes is in music_notes
        voice_1 = abjad.Voice(notes, name="Voice_1")
        staff_1 = abjad.Staff([voice_1], name="Staff_1")
        abjad.show(staff_1)


if __name__ == "__main__":
    sample_notes = "c'16 f' g' a' d' g' a' b' e' a' b' c'' f' b' c'' d''16"
    display_sheet_music(sample_notes)

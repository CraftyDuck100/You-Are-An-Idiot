from flask import Flask, render_template
from datetime import datetime
import random
app = Flask(__name__)


@app.route('/')
def home():
    now = datetime.now()
    current_year = now.year
    current_day = now.day
    current_now = now
    current_month = now.strftime("%B")
    return render_template("index.html", now=current_now, year=current_year, month=current_month, day=current_day)
SONGS = ["https://www.youtube.com/embed/2t1NMRse6aI", "https://www.youtube.com/embed/HOz-9FzIDf0", "https://www.youtube.com/embed/0iVlSNpq8i8", "https://www.youtube.com/embed/oUevY6uH4Qg", "https://www.youtube.com/embed/kbNdx0yqbZE"]
TITLES = ["Alien Alien", "Matoryoshka", "BIRDBRAIN", "Traffic Jam", "Monitoring"]
ARTIST = ["NayutalieN", "HACHI", "Jamie Paige", "煮ル果実", "DECO*27"]
@app.route('/vocaloid')
def vocaloid():
    index = random.randint(0, 4)
    return render_template("vocaloid.html", song=SONGS[index], song_name=TITLES[index], song_artist=ARTIST[index])
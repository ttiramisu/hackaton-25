from flask import Flask, render_template, send_file
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

# Animals

tiger = [
    [1900, 1910, 1920, 1930, 1940, 1950, 1960,
     1970, 1980, 1990, 2000, 2010, 2020],
    [100000, 90000, 80000, 70000, 50000, 40000,
     30000, 20000, 8000, 5000, 3500, 3200, 3900]
]

###############################
############ MAIN #############
###############################


@app.route('/')
def index():
    return render_template('index.html')

###############################
############ ANIMAL ############
###############################


@app.route('/animal=<chosen_animal>')
def animal(chosen_animal):
    if chosen_animal == 'lion':
        return render_template('lion.html')
    if chosen_animal == 'tiger':
        return render_template('tiger.html')
    if chosen_animal == 'rhino':
        return render_template('rhino.html')
    if chosen_animal == 'elephant':
        return render_template('elephant.html')

###############################
######## RUN TIME CODE ########
###############################


if __name__ == "__main__":
    app.run(debug=True)

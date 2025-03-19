from flask import Flask, render_template

app = Flask(__name__)

###############################
############ MAIN #############
###############################


@app.route('/')
def index():
    return render_template('index.html')

###############################
############ ANIMAL ###########
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

import Flask, render_template, Blueprint

index_page = Blueprint("index", __)



# index route
@app.route('/')
def index():
    return render_template('index.html')
from flask import Flask,render_template,url_for
ab=Flask(__name__)

@ab.route('/')
def index():
    return render_template('index.html')
@ab.route('/abc')
def main():
    return render_template('main.html')
@ab.route('/xyz')
def min():
    return render_template('new.html')    
ab.run()
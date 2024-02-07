import os
from flask import Flask, render_template, session, redirect, url_for, flash
import re
from RSS import SQL
from RSS_test import SQL_test
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class Serch(FlaskForm):
    keyword = StringField('検索したいキーワードを入力してください', validators=[DataRequired()])
    submit = SubmitField('検索')
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news')
def news():
    elems = SQL.elems
    return render_template('news.html', elems=elems)

@app.route('/test')
def test():
    f = SQL_test.search_zenn('機械学習') 
    f = f['entries'] 
    return render_template('test_2.html',f=f)

@app.route('/test_NLP')
def test_NLP():
    f = SQL_test.search_zenn('自然言語処理') 
    f = f['entries'] 
    return render_template('test_2.html',f=f)

@app.route('/serch_news',methods=['GET','POST'])
def serch_news():
    form = Serch()
    if form.validate_on_submit():
        session['keyword'] = form.keyword.data
        f_zenn = SQL_test.search_zenn(session['keyword']) 
        f_zenn = f_zenn['entries']   

        f_qiita = SQL_test.search_qiita(session['keyword']) 
        f_qiita = f_qiita['entries']   

        f = f_zenn + f_qiita

        return render_template('test_3.html',f=f)
    return render_template('serch.html', form=form)

@app.route('/serch_blog',methods=['GET','POST'])
def serch_blog():
    form = Serch()
    if form.validate_on_submit():
        session['keyword'] = form.keyword.data
        f_zenn = SQL_test.search_zenn(session['keyword']) 
        f_zenn = f_zenn['entries']   

        f_qiita = SQL_test.search_qiita(session['keyword']) 
        f_qiita = f_qiita['entries']   

        f = f_zenn + f_qiita

        return render_template('test_2.html',f=f)
    return render_template('serch.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
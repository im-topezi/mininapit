from flask import render_template, request
from db_helper import reset_db

from repositories.citation_repository import (
    get_citations,
    create_article,
    create_inproceedings,
    generate_bibtex,
    delete_citation_by_key,
)
from config import app, test_env

@app.get('/')
def index():
    citations = get_citations()
    return render_template('index.html', citations=citations)

@app.get('/new')
def new():
    return render_template('new.html')

@app.post('/article_new')
def article_new():
    key = request.form['key_article']
    author = request.form['author_article']
    title = request.form['title_article']
    journal = request.form['journal_article']
    year = request.form['year_article']
    volume = request.form.get('volume_article')
    pages = request.form.get('pages_article')

    create_article(key, author, title, journal, year, volume, pages)

    citations = get_citations()

    return render_template('index.html', citations=citations)

@app.post('/inproceedings_new')
def inproceedings_new():
    key = request.form['key_inproceedings']
    author = request.form['author_inproceedings']
    title = request.form['title_inproceedings']
    year = request.form['year_inproceedings']
    booktitle = request.form['booktitle_inproceedings']

    create_inproceedings(key, author, title, year, booktitle)
    
    citations = get_citations()

    return render_template('index.html', citations=citations)

@app.get('/toggle-bibtex')
def toggle_bibtex():
    citations = get_citations()
    bibtex_citations = generate_bibtex(citations)
    return render_template('index.html', citations=bibtex_citations, is_bibtex=True)

if test_env:
    @app.get('/reset_db')
    def reset_database():
        reset_db()
        return 'db reset'

    @app.get('/alive')
    def alive():
        return 'yes'

@app.post('/delete')
def delete_citation():
    key = request.form['key']
    delete_citation_by_key(key)
    citations = get_citations()
    return render_template('index.html', citations=citations)

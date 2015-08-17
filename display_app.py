from flask import Flask, render_template, request
import cPickle as pickle
from tipworthy_rec import tip_rec
import operator


app = Flask(__name__)
tipmodel = pickle.load(open( "tipmodel.p", "rb" ))
articles = pickle.load(open( "news_articles.p", "rb" ))
user1 = 'MarioLutherKingJr'
user2 = 'roadies'
user3 = 'mxisaac'
user4 = 'Thoranus'
user5 = 'rappercake'

@app.route('/', methods=['GET'])
def home():
	return render_template('resume.html')

@app.route('/tipworthy', methods=['GET', 'POST'])
def tipworthy():
	return render_template('base.html')

@app.route('/tipworthy/user1', methods=['GET','POST'])
def user_1():
	articlescore = {}
	for i in articles.keys():
		articlescore[i] = tipmodel.predict(articles[i], user1)[1]
	sorted_art = sorted(articlescore, key=articlescore.get)
	sorted_score = sorted(articlescore.values())
	resultval = []
	for i, val in enumerate(sorted_score):
		if val < .17:
			resultval.append(sorted_art[i])
	return render_template('predictions.html', user='User 1', result = resultval)

@app.route('/tipworthy/user2', methods=['GET','POST'])
def user_2():
	articlescore = {}
	for i in articles.keys():
		articlescore[i] = tipmodel.predict(articles[i], user2)[1]
	sorted_art = sorted(articlescore, key=articlescore.get)
	sorted_score = sorted(articlescore.values())
	resultval = []
	for i, val in enumerate(sorted_score):
		if val < .17:
			resultval.append(sorted_art[i])
	return render_template('predictions.html', user='User 2', result = resultval)

@app.route('/tipworthy/user3', methods=['GET','POST'])
def user_3():
	articlescore = {}
	for i in articles.keys():
		articlescore[i] = tipmodel.predict(articles[i], user3)[1]
	sorted_art = sorted(articlescore, key=articlescore.get)
	sorted_score = sorted(articlescore.values())
	resultval = []
	for i, val in enumerate(sorted_score):
		if val < .17:
			resultval.append(sorted_art[i])
	return render_template('predictions.html', user='User 3', result = resultval)

@app.route('/tipworthy/user4', methods=['GET','POST'])
def user_4():
	articlescore = {}
	for i in articles.keys():
		articlescore[i] = tipmodel.predict(articles[i], user4)[1]
	sorted_art = sorted(articlescore, key=articlescore.get)
	sorted_score = sorted(articlescore.values())
	resultval = []
	for i, val in enumerate(sorted_score):
		if val < .17:
			resultval.append(sorted_art[i])
	return render_template('predictions.html', user='User 4', result = resultval)

@app.route('/tipworthy/user5', methods=['GET','POST'])
def user_5():
	articlescore = {}
	for i in articles.keys():
		articlescore[i] = tipmodel.predict(articles[i], user5)[1]
	sorted_art = sorted(articlescore, key=articlescore.get)
	sorted_score = sorted(articlescore.values())
	resultval = []
	for i, val in enumerate(sorted_score):
		if val < .17:
			resultval.append(sorted_art[i])
	return render_template('predictions.html', user='User 5', result = resultval)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
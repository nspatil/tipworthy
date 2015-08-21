from flask import Flask, render_template, request
import cPickle as pickle
from tipworthy_rec import tip_rec
import operator


app = Flask(__name__)
tipmodel = pickle.load(open( "tipmodel.p", "rb" ))
articles = pickle.load(open( "news_articles2.p", "rb" ))
user1 = ****
user2 = ****
user3 = ****
user4 = ****
user5 = ****

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
	maybeval = []
	for i, val in enumerate(sorted_score):
		if val < .17:
			resultval.append((sorted_art[i], 1 - val))
		if val > .17 and val < .19:
			maybeval.append((sorted_art[i], 1 - val))

	return render_template('predictions.html', user='User 1', result = resultval, maybe = maybeval)

@app.route('/tipworthy/user2', methods=['GET','POST'])
def user_2():
	articlescore = {}
	for i in articles.keys():
		articlescore[i] = tipmodel.predict(articles[i], user2)[1]
	sorted_art = sorted(articlescore, key=articlescore.get)
	sorted_score = sorted(articlescore.values())
	resultval = []
	maybeval = []
	for i, val in enumerate(sorted_score):
		if val < .17:
			resultval.append((sorted_art[i], 1 - val))
		if val > .17 and val < .19:
			maybeval.append((sorted_art[i], 1 - val))
	return render_template('predictions.html', user='User 2', result = resultval, maybe = maybeval)

@app.route('/tipworthy/user3', methods=['GET','POST'])
def user_3():
	articlescore = {}
	for i in articles.keys():
		articlescore[i] = tipmodel.predict(articles[i], user3)[1]
	sorted_art = sorted(articlescore, key=articlescore.get)
	sorted_score = sorted(articlescore.values())
	resultval = []
	maybeval = []
	for i, val in enumerate(sorted_score):
		if val < .17:
			resultval.append((sorted_art[i], 1 - val))
		if val > .17 and val < .19:
			maybeval.append((sorted_art[i], 1 - val))
	return render_template('predictions.html', user='User 3', result = resultval, maybe = maybeval)

@app.route('/tipworthy/user4', methods=['GET','POST'])
def user_4():
	articlescore = {}
	for i in articles.keys():
		articlescore[i] = tipmodel.predict(articles[i], user4)[1]
	sorted_art = sorted(articlescore, key=articlescore.get)
	sorted_score = sorted(articlescore.values())
	resultval = []
	maybeval = []
	for i, val in enumerate(sorted_score):
		if val < .17:
			resultval.append((sorted_art[i], 1 - val))
		if val > .17 and val < .19:
			maybeval.append((sorted_art[i], 1 - val))
	return render_template('predictions.html', user='User 4', result = resultval, maybe = maybeval)

@app.route('/tipworthy/user5', methods=['GET','POST'])
def user_5():
	articlescore = {}
	for i in articles.keys():
		articlescore[i] = tipmodel.predict(articles[i], user5)[1]
	sorted_art = sorted(articlescore, key=articlescore.get)
	sorted_score = sorted(articlescore.values())
	resultval = []
	maybeval = []
	for i, val in enumerate(sorted_score):
		if val < .17:
			resultval.append((sorted_art[i], 1 - val))
		if val > .17 and val < .19:
			maybeval.append((sorted_art[i], 1 - val))
	return render_template('predictions.html', user='User 5', result = resultval, maybe = maybeval)

@app.route('/tipworthy/self_recommend', methods=['POST'])
def self_recommend():
	txt = request.form['usersub']
	articlescore = []
	userlist = [user1, user2, user3, user4, user5]
	aliaslist = ['User 1', 'User 2', 'User 3', 'User 4', 'User 5']
	for i, val in enumerate(userlist):
		articlescore.append(1 - tipmodel.predict(txt, val)[1])
	val = zip(articlescore, aliaslist)
	return render_template('recommend.html', result = val)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

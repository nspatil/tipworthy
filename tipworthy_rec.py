import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import CountVectorizer as CV
from string import digits
from gensim import matutils
from gensim.models import ldamulticore as LatentDA
from gensim.corpora.dictionary import Dictionary

class tip_rec:

	def __init__(self, num_topics = 15):
		self.numtopics = num_topics
		self.topic_dict = dict(enumerate(np.zeros(num_topics)))
		self.user_dict = {}
		self.model = None
		self.worddict = {}
		self.mydict = None


	def train(self, df):
		self.user_dict = {el:self.topic_dict.copy() for el in df.sender.unique()}
		cv = CV(stop_words='english')
		X = cv.fit_transform(df['context'])
		vocab = cv.vocabulary_.keys()
		self.worddict=dict([(i, s) for i, s in enumerate(vocab)])
		self.mydict = Dictionary()
		self.mydict = self.mydict.from_corpus(matutils.Sparse2Corpus(X, documents_columns=False), id2word=self.worddict)
		self.model = LatentDA.LdaModel(matutils.Sparse2Corpus(X, documents_columns=False), num_topics=self.numtopics, passes=20, id2word=self.worddict)
		for i in df.iterrows():
			if i[1]['context'] == '':
				continue
			else:
				values = new_model[mydict.doc2bow(i[1]['context'].split())]
				for val in values:
					if val[0] in user_dict[i[1].sender].keys():
						if i[1].amt == '':
							continue
						user_dict[i[1].sender][val[0]] += val[1] * float(i[1].amt)
						continue
					user_dict[i[1].sender][val[0]] = val[1]
		for i in user_dict.keys():
			norm_const = sum(user_dict[i].values())
			for j in user_dict[i].keys():
				user_dict[i][j] = user_dict[i][j]/norm_const

	def predict(self, text, username = ''):
		topics = self.model[self.mydict.doc2bow(text.split())]
		doc_aff = np.zeros(self.numtopics)
		for i in topics:
			doc_aff[i[0]] = i[1]
		if username == '':
			returndict = {}
			for user in self.user_dict.keys():
				user_aff = np.array(self.user_dict[user].values())    
				score = np.linalg.norm(user_aff - doc_aff)
				returndict[user] = score
			return returndict
		else:
			user_aff = np.array(self.user_dict[username].values())    
			score = np.linalg.norm(user_aff - doc_aff)
			return (username, score)









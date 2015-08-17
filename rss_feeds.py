import feedparser
import re
import cPickle as pickle

def pull_article(url, article_dict):
	d = feedparser.parse(url)
	for entry in d['entries']:
		article_text = re.sub('<[^<]+?>', '', entry['summary_detail']['value'])
		article_url = entry['link']
		article_dict[article_url] = article_text
	return article_dict

if __name__ == '__main__':
	rss_list = ['http://fulltextrssfeed.com/feeds.reuters.com/Reuters/domesticNews',
	'http://fulltextrssfeed.com/feeds.reuters.com/reuters/entertainment',
	'http://fulltextrssfeed.com/feeds.reuters.com/reuters/scienceNews',
	'http://fulltextrssfeed.com/feeds.reuters.com/reuters/sportsNews',
	'http://fulltextrssfeed.com/feeds.reuters.com/Reuters/worldNews']
	article_dict = {}
	for rss in rss_list:
		article_dict = pull_article(rss, article_dict)
	pickle.dump( article_dict, open( "news_articles.p", "wb" ) )
from bs4 import BeautifulSoup
import requests
from urllib2 import Request, urlopen
import requests.auth
from time import sleep
import pandas
import sys

def write_context(contexturl, myheaders, attemptnum = 1):
	if attemptnum > 3:
		return '404 context not found'
	sleep(2.1)
	try: 
		r = requests.get(contexturl, headers=myheaders)
		soup = BeautifulSoup(r.text)
		return soup.find_all('div', class_='md')[1]
	except:
		sleep(7)
		return write_context(contexturl, myheaders, attemptnum+1)

if __name__ == '__main__':
	if len(sys.argv) > 1:
		myheaders = {'User-agent': *********} # Insert your own user agent here
		for i in xrange(1, sys.argv):
			df = pd.read_csv(sys.argv[i])
			df['context'] = ""
			for index, row in df.iterrows():
				df.loc[index, 'context'] = str(write_context(row['context_url'], myheaders))
			with open('outfile{0}'.format(i), 'wb') as f:
				df.to_csv(f)
	else:
		print "File required to output context"




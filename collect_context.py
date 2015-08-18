from bs4 import BeautifulSoup
import requests
from urllib2 import Request, urlopen
import requests.auth
from time import sleep
import pandas
import sys

#########
# This is the data collection file. It assumes a csv file with a list of Reddit context
# URLs exist. It scrapes reddit, attempting to maintain the limit of 30 requests per minute
# and gathers the top comment or posting for each provided link. It outputs the result as a CSV.
#########
def write_context(contexturl, myheaders, attemptnum = 1): #for a given context url, write context will attempt to retrieve the context 3 times. If it fails
	if attemptnum > 3:                                    #it will return "404 context not found"
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
			df = pd.read_csv(sys.argv[i]) #Pass in the CSV files as command line arguments. This program takes an arbitrary number of files
			df['context'] = ""
			for index, row in df.iterrows():
				df.loc[index, 'context'] = str(write_context(row['context_url'], myheaders))
			with open('outfile{0}'.format(i), 'wb') as f:
				df.to_csv(f)
	else:
		print "File required to output context"




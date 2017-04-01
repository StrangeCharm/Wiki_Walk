
from bs4 import BeautifulSoup
import random
import urllib2

# Starting Link
link_list=["Leonhard_Euler"]


def agent(link,link_list):

	for item in link_list:
		link_list.remove(item)

	url = "http://en.wikipedia.org/wiki/"+link #there could be wikipidea pages without /wiki/ but I haven't fond any
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page.read(),"lxml")
	a_tags = soup.find_all("a")

	page_links=[]
	for x in a_tags:
		page_links.append(x.get('href'))

	clean_links = []
	for x in page_links:
		if x is None :
			pass
		elif "/wiki/" == x[:6] and ":" not in x and "Main_Page" not in x:
			clean_links.append(x[6:])
	
	links=sorted(list(set(clean_links))) # removes duplicets and sorts
	for item in links:
		link_list.append(item)


while len(link_list) != 0 :
	next1=random.choice(link_list)
	print next1
	agent(next1,link_list)

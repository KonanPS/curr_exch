
# from django.template.loader import get_template
# from django.template import Template, Context
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
import datetime

def cur_exchange ( request ):
	import urllib2
	from bs4 import BeautifulSoup  

	cur_date = datetime.datetime.now()

	banks_url = ["http://www.trustbank.by/", "http://www.priorbank.by/", "http://www.belinvestbank.by/"]

	# USD table header
	# print "USD"

	# print

	# print "Bank          | SELL  | BUY   | DELTA |"

	# print
	# USD table header
	# loop for each bank's url
	for url in banks_url:

		request = urllib2.urlopen(url)

		soup = BeautifulSoup (request.read())

		if url == "http://www.trustbank.by/":

			curs_table = soup.table
			trust_usd_sell = int(curs_table.find_all("tr")[2].find_all("td")[1].contents[0])
			trust_usd_buy = int(curs_table.find_all("tr")[1].find_all("td")[1].contents[0])
			trustbank_delta = trust_usd_sell - trust_usd_buy

			#print "Trustbank     | %s | %s | %s | " % (trust_usd_buy, trust_usd_sell, trustbank_delta)

		if url == "http://www.priorbank.by/":

			prior_curs_table = soup.find_all("div", id='cash_toolbox_rates_1')[0].table
			prior_usd_sell = int(prior_curs_table.find_all("tr")[0].find_all("td")[2].contents[0])
			prior_usd_buy = int(prior_curs_table.find_all("tr")[0].find_all("td")[1].contents[0])
			priorbank_delta = prior_usd_sell - prior_usd_buy
			
			#print "Priorbank     | %s | %s | %s | " % (prior_usd_buy, prior_usd_sell, priorbank_delta)

		if url == "http://www.belinvestbank.by/":

			belinvest_cur_table = soup.find_all("div", class_='courses_block')[1].table.tbody
			belinvest_usd_buy_str = (belinvest_cur_table.find_all("tr")[0].find_all("td")[1].contents[0])
			belinvest_usd_sell_str = (belinvest_cur_table.find_all("tr")[0].find_all("td")[2].contents[0])

			belinvest_usd_buy = int(belinvest_usd_buy_str.split(".")[0])
			belinvest_usd_sell = int(belinvest_usd_sell_str.split(".")[0])
			belinvest_delta = belinvest_usd_sell - belinvest_usd_buy

			#print "Belinvestbank | %s | %s | %s |" % (belinvest_usd_buy, belinvest_usd_sell, belinvest_delta)

	# ctx = Context (
	# 	# {

	# 	# 'trust_usd_sell': trust_usd_sell,
	# 	# 'trust_usd_buy': trust_usd_buy,
	# 	# 'trustbank_delta': trustbank_delta,
	# 	# 'prior_usd_sell': prior_usd_sell,
	# 	# 'prior_usd_buy': prior_usd_buy,
	# 	# 'priorbank_delta': priorbank_delta,
	# 	# 'belinvest_usd_buy': belinvest_usd_buy,
	# 	# 'belinvest_usd_sell': belinvest_usd_sell,
	# 	# 'belinvest_delta': belinvest_delta

	# 	# }
	# 	locals()
	# 	)
	return render_to_response ('cur_exch.html', locals())
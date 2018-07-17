
from bittrex.bittrex import *
import  urllib2, json, time, math, argparse, pprint, numpy, bittrex, csv

#my_bittrex = Bittrex("<my_api_key>", "<my_api_secret>", api_version="<API_V1_1> or <API_V2_0>")
my_bittrex = Bittrex(None,None)

pair = "USDT-XRP"
url='https://bittrex.com/api/v1.1/public/getorderbook?market=' + pair + '&type=both'    


def buyquantity():
	# Gets all thebuy orders and returns a list of their quantities
	q = []
	for i in range(len(rb)):
		q.append(rb[i]['Quantity'])	
	return q

def sellquantity():
	# Gets all the sell orders and returns a list of their quantities
	q = []
	for i in range(len(rs)):
		q.append(rs[i]['Quantity'])
	return q

def fter(quantities,limit1,limit2,limit3,limit4):
	# Get he list of quantities and filters out the small orders and returns the biggest in terms of wieghted mean multiples
	#limit = numpy.mean(quantities)
	g1 = list(filter(lambda x: x > limit1, quantities))
	g2 = list(filter(lambda x: x > limit2, quantities))
	g3 = list(filter(lambda x: x > limit3, quantities))
	g4 = list(filter(lambda x: x > limit4, quantities))
	return g1,g2,g3,g4
	

def sellorders(limitsize):
	# Returns the matching filtered quantity with its respective price 
	for i in range(len(rs)):
		if rs[i]['Quantity'] in fqs[limitsize]:
			print("Price: " + str(rs[i]['Rate']) +"                " + "Amount: " + str(rs[i]['Quantity']))
		#	print(r[i])



def buyorders(limitsize):
	# Returns the matching filtered quantity with its respective price
	for i in range(len(rb)):
		if rb[i]['Quantity'] in fqb[limitsize]:
			print("Price: " + str(rb[i]['Rate']) +"                " + "Amount: " + str(rb[i]['Quantity']))
		#	print(r[i])
			price = str(rb[i]['Rate'])
		        quantity = str(rb[i]['Quantity'])
			csvwriter(price, quantity)

def csvwriter(price, quantity):
		csv = open('bittrexdata.csv', 'a')
		#w.write('Price, Amount\n')
		row = price + "," + quantity  + "\n"
		csv.write(row)
		

def printLevels():

	print("\n")
	print("\n")
	print("\n")
	print("\n")
	print("\n")

	print("________________MOON___________________\n")

	sellorders(3)

	print("\n")
	print("LASTPRICE:" + str(my_bittrex.get_ticker(pair)['result']['Last']))
	print("\n")

	buyorders(3) # prints all the buy orders larger than the a4limit

	print("\n_______________FLOOR__________________")
	
def webhandle():
	webUrl = urllib2.urlopen(url)
	#error handling
	#print("result code: " + str(webUrl.getcode()))
	
	return webUrl.read()


while True:
	data = webhandle()
	pyData = json.loads(data)
	rb = pyData['result']['buy']
	rs = pyData['result']['sell']

	b1limit = numpy.mean(buyquantity())     #limitsize of 0
	b2limit = b1limit*2 			# limitsize of 1
	b3limit = b1limit*3 			#limit size of 2
	b4limit = b1limit*4 			#limit size of 3

	fqb = fter(buyquantity(),b1limit,b2limit,b3limit,b4limit)

	s1limit = numpy.mean(sellquantity())   	#limitsize of 0
	s2limit = s1limit*2			# limitsize of 1
	s3limit = s1limit*3 			#limit size of 2
	s4limit = s1limit*4 			#limit size of 3

	fqs = fter(sellquantity(),s1limit,s2limit,s3limit,s4limit)


	
	printLevels()
	time.sleep(5)

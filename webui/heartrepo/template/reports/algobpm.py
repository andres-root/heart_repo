import re

class algobpm:


	def __init__(self, data):
		self.masterdata = open(data, 'r')
		
	def prom(self):
                text = self.masterdata.readlines()
                sum_value=0
		regex = r'[0-9]+'
                for line in text:
			num = re.findall(regex,line)
			print(line)
                        sum_value += int(num[1])
                return (sum_value/len(text))


		

	def conteo(self):
		promedios = self.prom()
		text = self.masterdata.readlines()
                count=0
		regex = r'[0-9]+'
                for line in text:
			num = re.findall(regex,line)
			
			if(int(num[1])>=int(promedios)) or num[0]>0:
				count += 1
		print count
		return count
		

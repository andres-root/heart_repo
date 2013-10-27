import re

class panel:

	def __init__(self, url_text):
		self.list_main = open(url_text, 'r')


	def filtrar(self, mes):
		cont=0
		list_resume = {}
		info = self.list_main.readlines()
		salida = open('data_resume.txt', 'w')
		for i in info:
			regex = r'[0-9]+'
			exit = re.findall(regex,i)
			print exit[1]
			if int(exit[1]) == int(mes):
				
				list_resume[cont] =i
				salida.write(list_resume[cont])
				cont+=1


	def promedio_mes(self, mes):
		cont = 0
		filtrar(mes)
		item = open('data_resume','r')
		text = item.readlines()
		sum_value=0
		for line in text:
			regex = r'[0-9]+'
                        exit = re.findall(regex,i)
			sum_value += int(exit[6])
		return (sum_value/len(text))


	def prom_meses(self):
		dic_prom
		total_text = self.list_main.readlines()
		asign = 0
		for line in total_text:
			regex = r'[0-9]+'
                        exit = re.findall(regex,i)
			if(asign ==0) or (asign != int(exit[2]):
				asign = int(line[5:6])
				dic_prom[asign] = promedio_mes(asign)
		return dic_prom
		
			

		

			
			
									
	

#authored by jgam
"""
possible db variables!

"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#from lxml import html
#import requests
import csv
import os
#import pandas as pd
#from pandas import ExcelWriter
#from pandas import ExcelFile
#import numpy as np
import xlwt
from datetime import date



today = str(date.today())


def sel_suggest(keywords, file_name, work_book):
	#ff = csv.writer(open(result_dir+file_name, "a+"))
	file_name = file_name[:len(file_name)-4]
	driver = webdriver.Chrome('/Users/ascent/Downloads/chromedriver')
	driver.get('https://www.google.com/webhp?hl=ja&gl=jp')#/search?hl=ko&gl=kr')
	#here we should use a for loop
	columns = 0
	sheet_name = 'hong-sam'
	work_sheet = work_book.add_sheet(sheet_name)
	for keyword in keywords:
		suggest_list = []
		suggest_list.append(keyword)
		if keyword[-1] == '_':
			keyword = keyword.replace('_',' ')
		print(keyword)
		sheet_name =str(columns)
		search = driver.find_element_by_name('q')
		search.send_keys(keyword)
		print('time sleep')
		time.sleep(5)
		while_cond = True
		child_index = 1
		

		while while_cond:
			try:
				#print('should be here 8 times')
				added = driver.find_element(By.XPATH, '//*[@id="tsf"]/div[2]/div/div[2]/div[2]/ul/li['+str(child_index)+']/div[1]/div/span')
				added_word = added.text
				#print(added_word)
				suggest_list.append(added_word)
				child_index += 1
			except:
				print('end of child_index and done')
				while_cond = False
		
		#also erase the search keyword in a search keyword tab.
		search.clear()
		#this needs to be written in a column of excel
		
		
		

		for row, item in enumerate(suggest_list):
			work_sheet.write(row, columns, item)

		columns += 1
		
		print(suggest_list)
	return 0




#get the list of all the keywords.


files = [f for f in os.listdir('.') if os.path.isfile(f)]
#open the excel file here with bunch of tabs
work_book = xlwt.Workbook()


for file in files:
	if file[len(file)-4:len(file)] != '.csv':
		continue
	keywords = []
	unique_keywords = []
	real_keywords = []
	file_name = ''
	file_name = today + str(file)[:len(file)-4]+'_suggests_results.csv'
	with open(file) as f:
		reader = csv.reader(f)
		for i in reader:
			keywords.append(i[0])
	keywords = keywords[1:]
	for keyword in keywords:
		if keyword[-1] == '_':
			continue
		else:
			unique_keywords.append(keyword)

	for unique in unique_keywords:
		real_keywords.append(unique)
		real_keywords.append(unique+'_')
	print(real_keywords)
	sel_suggest(real_keywords, file_name, work_book)
	work_book.save(file_name)


	

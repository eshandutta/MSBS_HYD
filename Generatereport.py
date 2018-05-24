#Login Credentials:- 
#			email:- eshandutta@gmail.com
#		     password:- hkp4pxar3i123



import urllib2
from bs4 import BeautifulSoup

import csv

#***************************************************************************
#	ASSIGNING VARIOUS URLs -> CITY-> DALLAS				   *
#***************************************************************************
url1= 'https://gtmetrix.com/reports/www.datamintelligence.com/rdzmJKz2'
page1=urllib2.urlopen(url1)
soup1 = BeautifulSoup(page1, 'html.parser')

url2='https://gtmetrix.com/reports/www.datamintelligence.com/7uYgODx0'
page2=urllib2.urlopen(url2)
soup2 = BeautifulSoup(page2, 'html.parser')

url3='https://gtmetrix.com/reports/www.datamintelligence.com/V6GQyYdD'
page3=urllib2.urlopen(url3)
soup3 = BeautifulSoup(page3, 'html.parser')

#url4='https://www.datamintelligence.com/research-report/asia-compound-feed-market/'
#page4=urllib2.urlopen(url4)

url5='https://gtmetrix.com/reports/www.datamintelligence.com/dVQ7HM35'
page5=urllib2.urlopen(url5)
soup5 = BeautifulSoup(page5, 'html.parser')

url6='https://gtmetrix.com/reports/www.datamintelligence.com/GmZO0bpc'
page6=urllib2.urlopen(url6)
soup6 = BeautifulSoup(page6, 'html.parser')



#***********************************************************************************
#       EXTRACTING DATA FROM THE REPORTS OBTAINED FROM GTMETRIX	 for URL 1	   *
#***********************************************************************************

#*******************************************************************************************************
score_box_url1= soup1.find('span', attrs={'class': 'report-score-percent'})
score_url1=score_box_url1.text

#*******************************************************************************************************
grade_box_url1=soup1.find('i', attrs={'class': 'sprite-grade-B'})
grade_url1=grade_box_url1.text

#*******************************************************************************************************
fully_loaded_time_box_url1=soup1.find('span', attrs={'class': 'report-page-detail-value'})
loadedTime_url1=fully_loaded_time_box_url1.text

#*******************************************************************************************************

total_page_size_box_url1=soup1.find('span', attrs={'class': 'report-page-detail-value'})
pageSize_url1=total_page_size_box_url1.text

#*******************************************************************************************************
request_page_box_url1=soup1.find('span', attrs={'class': 'report-page-detail-value'})
requests_url1=request_page_box_url1.text

#*******************************************************************************************************

#***********************************************************************************
#		EXPORTING DATA OF URL 1 TO EXCEL (FOR DALLAS)                 *			   #									      *
#***********************************************************************************

with open('REPORT.csv', 'a') as csv_file:
 writer = csv.writer(csv_file)
 writer.writerow(['URL','Page Speed Score','Yslow Score','Fully Loaded Time','Total Page Size','Requests','PageSpeed Issues','YSlow Issues'])
 writer.writerow([url1,score_url1,grade_url1,loadedTime_url1,pageSize_url1,requests_url1])


#***********************************************************************************
#       EXTRACTING DATA FROM THE REPORTS OBTAINED FROM GTMETRIX	 for URL 2(FOR DALLAS)	   *
#***********************************************************************************

#*******************************************************************************************************
score_box_url2= soup2.find('span', attrs={'class': 'report-score-percent'})
score_url2=score_box_url2.text

#*******************************************************************************************************
grade_box_url2=soup2.find('i', attrs={'class': 'sprite-grade-B'})
grade_url2=grade_box_url2.text

#*******************************************************************************************************
fully_loaded_time_box_url2=soup2.find('span', attrs={'class': 'report-page-detail-value'})
loadedTime_url2=fully_loaded_time_box_url2.text

#*******************************************************************************************************

total_page_size_box_url2=soup2.find('span', attrs={'class': 'report-page-detail-value'})
pageSize_url2=total_page_size_box_url2.text

#*******************************************************************************************************
request_page_box_url2=soup2.find('span', attrs={'class': 'report-page-detail-value'})
requests_url2=request_page_box_url2.text

#*******************************************************************************************************

#***********************************************************************************
#		EXPORTING DATA OF URL 2 TO EXCEL (FOR DALLAS)                 *			   #									      *
#***********************************************************************************

with open('REPORT.csv', 'a') as csv_file:
 writer = csv.writer(csv_file)
 writer.writerow(['URL','Page Speed Score','Yslow Score','Fully Loaded Time','Total Page Size','Requests','PageSpeed Issues','YSlow Issues'])
 writer.writerow([url2,score_url2,grade_url2,loadedTime_url2,pageSize_url2,requests_url2])


#***********************************************************************************
#       EXTRACTING DATA FROM THE REPORTS OBTAINED FROM GTMETRIX	 for URL 3(FOR DALLAS)	   *
#***********************************************************************************

#*******************************************************************************************************
score_box_url3= soup3.find('span', attrs={'class': 'report-score-percent'})
score_url3=score_box_url3.text

#*******************************************************************************************************
grade_box_url3=soup3.find('i', attrs={'class': 'sprite-grade-B'})
grade_url3=grade_box_url3.text

#*******************************************************************************************************
fully_loaded_time_box_url3=soup3.find('span', attrs={'class': 'report-page-detail-value'})
loadedTime_url3=fully_loaded_time_box_url3.text

#*******************************************************************************************************

total_page_size_box_url3=soup3.find('span', attrs={'class': 'report-page-detail-value'})
pageSize_url3=total_page_size_box_url3.text

#*******************************************************************************************************
request_page_box_url3=soup3.find('span', attrs={'class': 'report-page-detail-value'})
requests_url3=request_page_box_url3.text

#*******************************************************************************************************

#***********************************************************************************
#		EXPORTING DATA OF URL 3 TO EXCEL (FOR DALLAS)                 *			   #									      *
#***********************************************************************************

with open('REPORT.csv', 'a') as csv_file:
 writer = csv.writer(csv_file)
 writer.writerow(['URL','Page Speed Score','Yslow Score','Fully Loaded Time','Total Page Size','Requests','PageSpeed Issues','YSlow Issues'])
 writer.writerow([url3,score_url3,grade_url3,loadedTime_url3,pageSize_url3,requests_url3])


#Similarly now adding  new worksheets for the cities London, Mumbai, Sydney, Sao Paulo

#sheet_London = csv_file.add_sheet('London')
 
#sheet1.write(1, 0, 'url1')
#sheet1.write(2, 0, 'score')
#sheet1.write(3, 0, 'grade')
#sheet1.write(4, 0, 'loadedTime')
#sheet1.write(5, 0, 'pageSize')
#sheet1.write(0, 1, 'requests')

 
#wb.save('xlwt REPORT.xls')







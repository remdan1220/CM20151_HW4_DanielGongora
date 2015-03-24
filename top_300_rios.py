import csv
import sys


txt_file = r"coastal-stns-byVol-updated-oct2007.txt"
csv_file = r"top_300_rios.csv"

in_txt = csv.reader(open(txt_file, "rb"), delimiter ='\t', quoting=csv.QUOTE_NONE)

out_csv = csv.writer(open(csv_file, 'wb'))


c = 0
for row in in_txt:
	
	if c<301:
		out_csv.writerow(row)
		c+=1

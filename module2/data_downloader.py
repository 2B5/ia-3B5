import os
import json
import urllib2

def get_data(work_dir, file):

	file_path = os.path.realpath(file)	
	json_file = open(os.path.basename(file_path), 'r')
	
	data = json.load(json_file)
	for site_key in data:
		#print site_key, data[site_key]
		for file_key in data[site_key]:
			print file_key
			if not os.path.isfile( os.path.join(work_dir, file_key) + '.aiml'):
				aiml_file = open( os.path.join(work_dir, file_key) + '.aiml', 'w')
				
				print 'Downloading: ', site_key + file_key + '.aiml'
				url = urllib2.urlopen(site_key + file_key + '.aiml')
				aiml_file.write(url.read())

				aiml_file.close()
	print '\n\nAll files accounted for'
	json_file.close()

if __name__ == '__main__':
	work_dir = './data'
	if not os.path.isdir(work_dir):
		os.mkdir(work_dir)
	get_data(work_dir, './download.json')
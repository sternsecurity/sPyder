
import csv, os, sys, subprocess, time

inputFile = open('<path_to_input>.csv')
csvFile = csv.reader(inputFile)

# Get for user input
user = raw_input("Domain User: ")
passw = raw_input("Password: ")
domain = raw_input("Domain: ")

# Function to create dir where the share will be mounted
def makedirs(path):
	try:  
		os.makedirs(path)
	except OSError as err:  
		print ("Creation of the directory %s failed. Share NOT mounted" % path)
		print ("Error: %s" % err)
	else:
		return 0

# Function to mount the share
def mount(lpath, rpath, user, passw, domain):
	try:
		result = subprocess.Popen("mount -t cifs " + rpath + " " + lpath + " -ousername=" + user + ",password=" + passw + ",domain=" + domain, shell = True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		try:
		    # Filter stdout
		    for line in iter(result.stdout.readline, ''):
			sys.stdout.flush()
			# Print status
			print(">>> " + line.rstrip())
			sys.stdout.flush()
		except:
		    sys.stdout.flush()

		# Wait until process terminates
		while result.poll() is None:
		    # Process hasn't exited yet, wait longer
		    time.sleep(0.5)

		# Get return code from process
		return_code = result.returncode
		#err_msg = line.rstrip()
		#print 'RETURN CODE', return_code, err_msg
		if return_code != 0:
			raise Exception("Return Code: " + str(return_code))# + ", Error Message: " + err_msg)
	except Exception as error:
		print ("Mount failed: " + str(error))
		return return_code
	else:
		print ("Mount sucessfully created in: %s" % lpath)
		return 0

# Loop CSV file and mount share
for row in csvFile:
	
	col1_ip = row[0]
	col2_hostname = row[1]
	col3_share = row[2]
	wd = "/mnt/" + col2_hostname + "/"
	lpath = "/mnt/" + col2_hostname + "/" + col3_share
	rpath = "//" + col1_ip + "/" + col3_share + "/"	
	makedirsresult = makedirs(lpath)
	if makedirsresult == 0:
		mountresult = mount(lpath, rpath, user, passw, domain)
		if mountresult == 1:
			try:	
				time.sleep(0.5)
				os.chdir(wd)		
				os.rmdir(col3_share)
			except OSError as err:
				print ("Error: %s" % err)
				

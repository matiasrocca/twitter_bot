import twint


def download(username, output, limit):
	# Configure
	c = twint.Config()
	c.Username = username
	c.Store_json = True
	c.Output = output
	c.Retweets = True
	c.Limit = limit

	# Run
	twint.run.Profile(c)

def main():

	# input user
	username = # ''

	# structure of the files and maximum number of downloads
	filename = username + '.data'
	limit = 3200

	username_2 = # ""
	filename_2 = username_2 + ".data"

	# Download raw data
	download(username, filename, limit)
	download(username_2,filename_2,limit)


if __name__ == '__main__':
	main()
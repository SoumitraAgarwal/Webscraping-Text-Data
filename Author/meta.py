import time

def initialize_millis():
	millis = int(round(time.time() * 1000))
	return millis

def initialize_train():
	train = "../Train/" 
	return train

def initialize_docs():
	doc = range(4)
	return doc
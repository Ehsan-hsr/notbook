#!/usr/bin/python


import sys
import getopt
import json


dataset = {}


def readf():
	global dataset
	with open("data.txt") as infile:
		dataset = json.load(infile)

def writef():
	with open("data.txt", "w+") as outfile:
		json.dump(dataset, outfile)


def get(index):
	global dataset
	
	if index in dataset:
		print("{} is {}".format(index, dataset[index]))


def print_all():
	for row in dataset:
			print("{} {}".format(row, dataset[row]))


def set(index, value):
	global dataset
	dataset[index] = value
	print("insert {}={}".format(index, value))


def main(argv):
	readf()
	try:
		opts, args = getopt.getopt(argv, "as:g:", ["get=", "set="])
	except getopt.GetoptError:
		print("[-g][--get] for return value and [-s][--set] for set new value")
	

	for opt ,arg in opts:
		if opt in ["-g", "--get"]:
			return get(arg.strip())
		elif opt in ["-s", "--set"]:
			key, value = arg.split('=')
			key = key.strip()
			value = value.strip()
			return set(key, value)
		elif opt == "-a":
			print_all()
		
	print("please input data in correct format")




if __name__ == "__main__":
	main(sys.argv[1:])
	writef()

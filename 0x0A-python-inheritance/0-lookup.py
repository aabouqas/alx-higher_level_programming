#!/usr/bin/python3

def lookup(obj):
	return [attr for attr in dir(obj) if attr.startswith('__') and attr.endswith('__')]
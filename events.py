events = {}

def subscribe(key, operation):
	events[key][] = operation

def invoke(key):
	for operation in events[key]:
		operation()



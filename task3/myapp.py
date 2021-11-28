from datetime import datetime
import json

def app(env, start_response):
	# logic
	my_time = datetime.now()
	data = {
		'time': str(my_time),
		'url': env['HTTP_HOST']
	}
	json_str = json.dumps(data)
	json_data = bytes(json_str, encoding='utf8')
	start_response("200 OK", [("Content-type", "application/json"),
				("Content-Length", str(len(json_data)))])
	return iter([json_data])

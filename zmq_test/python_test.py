import requests
s = requests.Session()
a = requests.adapters.ZMQAdapter()
a.pattern='req_rep'
s.mount('tcp://', a)
x = s.get("tcp://127.0.0.1:5678",data='check the code!',timeout=1)
print x.status_code
print x.content

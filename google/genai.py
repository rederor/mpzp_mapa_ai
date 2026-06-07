import os,requests as r
class X:pass
class C:
 def __init__(s,temperature=.2,**k):s.temperature=temperature
class types:GenerateContentConfig=C
class Client:
 def __init__(s,api_key):s.models=s;s.k=os.getenv('DEEPSEEK_API_KEY')or api_key
 def generate_content(s,model,contents,config=None):
  j=r.post('https://api.deepseek.com/chat/completions',headers={'Authorization':'Bearer '+s.k},json={'model':'deepseek-chat','messages':[
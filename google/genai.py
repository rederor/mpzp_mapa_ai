import requests as r
class types:
 class GenerateContentConfig:
  def __init__(s,**k):pass
class Client:
 def __init__(s,api_key):s.models=s;s.k=api_key
 def generate_content(s,model,contents,config=None):
  x=r.post('https://api.deepseek.com/chat/completions',headers={'Authorization':'Bearer '+s.k},json={'model':'deepseek-chat','messages':[{'role':'user','content':contents}]}).json()
  return type('R',(),{'text':x['choices
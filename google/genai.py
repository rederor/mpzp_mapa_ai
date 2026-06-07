from .ds import q
class types:
 class GenerateContentConfig:
  def __init__(s,**k):pass
class Client:
 def __init__(s,api_key):s.models=s;s.k=api_key
 def generate_content(s,model,contents,config=None):return type('R',(),{'text':q(s.k,contents)})()

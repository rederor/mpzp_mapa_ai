import os, requests
U='https://api.deepseek.com/chat/completions'
M='deepseek-chat'
def q(k,c,config=None):
    key=k if k and k!='...' else os.getenv('DEEPSEEK_API_KEY')
    if not key: raise RuntimeError('Brak klucza DeepSeek: ustaw DEEPSEEK_API_KEY albo API_KEY.')
    t=getattr(config,'temperature',0.2) if config else 0.2
    r=requests.post(U,headers={'Authorization':'Bearer '+key,'Content-Type':'application/json'},json={'model':M,'messages':[{'role':'user','content':c}
from requests import post as p
U='https://api.deepseek.com/chat/completions'
M='deepseek-chat'
def q(k,c):
 return p(U,headers={'Authorization':'Bearer '+k},json={'model':M,'messages':[{'role':'user','content':c}]}).json()['choices'][0]['message']['content']

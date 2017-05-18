import requests
import pya3rt
from bs4 import BeautifulSoup
from pprint import pprint

apikey = "<YOUR_APIKEY>"
print ("URLを入力してください")
url = input()

client = pya3rt.ProofreadingClient(apikey)
res = requests.get(url)

soup = BeautifulSoup(res.content, 'html.parser')
records = soup.select('任意のタグ・クラス等')

for record in records:
  	arrays = record.get_text().split('\n')
while arrays.count('') > 0:
	arrays.remove('')
	
for array in arrays:
	new_array = client.proofreading(array)
	if new_array['status'] == 0:
		continue
	elif new_array['alerts'][0]['alertCode'] == 2:
		pprint(new_array['alerts'][0])
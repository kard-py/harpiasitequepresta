import requests
from requests.structures import CaseInsensitiveDict
import json
import time
url = "https://apirw.interm.com.br/categories"

headers = CaseInsensitiveDict()
headers["Authorization"] = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY0OGIyMDk5NDNjYjlkYWZhMDU2ZDZjMiIsInVzZXJuYW1lIjoiaGFycGlhZGV2In0.QqP9jvdsRXfcS3xLeT9dwTVMY-rd4kivyG0KMERGLeU"
headers["Content-Type"] = "application/json"


categorias = [
["acao_social", "Ação Social", ""],
["agronegocio", "Agronegocio", ""],
["arquitetura", "Arquitetura", ""],
["automotivo", "Automotivo", ""],
["beleza", "Beleza", ""],
["bem_estar", "Bem Estar", ""],
["construcao", "Construção", ""],
["direito", "Direito", ""],
["editorial", "Editoria", ""],
["educacao", "Educação", ""],
["emprendedorismo", "Emprendedorismo", ""],
["esporte", "Esporte", ""],
["financas", "Finanças", ""],
["imobiliario", "Imobiliario", ""],
["moda", "Moda", ""],
["motociclismo", "Motociclismo", ""],
["personalidades", "Personalidades", ""],
["saude,", "Saude", ""],
["segurança", "Segurança", ""],
["social", "Social", ""],
["sorriso35anos", "Sorriso 35 Anos", ""],
["sorriso36anos", "Sorriso 36 Anos", ""],
["sustentabilidade", "Sustentabilidade", ""],
["turismo", "Turismo", ""]
]



for i in range(0, len(categorias)):
    titulo = categorias[i][1]
    url_text = categorias[i][0]
    data = '{"images": [{"title":"","data":""}],"title":"'+titulo+'","url": "'+url_text+'"}'
    print(data)
    resp = requests.post(url, headers=headers, data=data)
    if resp.status_code == 400:
        print(resp.text)

    time.sleep(3)

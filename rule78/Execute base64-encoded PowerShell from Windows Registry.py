from elasticsearch import Elasticsearch

es = Elasticsearch('10.25.23.161:9200')

doc = {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "must": [
            {
              "match_phrase": {
                "event_id": "13"
              }
            },
            {
              "wildcard": {
                "registry_key_path.keyword": "*\\\\Software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Debug*"
              }
            }
          ]
        }
      }
    }
  }
}



res = es.search(index="logs-endpoint-winevent-*",body=doc)

count = res['hits']['total']['value']
tactic = "Defense Evasion"
technique = "Obfuscated Files or Information"
procedure = "Execute base64-encoded PowerShell from Windows Registry"
tech_code = "T1027"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 76)

print('Execute base64-encoded PowerShell from Windows Registry.py '+ str(count))
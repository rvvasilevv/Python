playlist={"ime":"uchene hehe",
          "avtor":"radkobatko",
          "pesni": [
              {"ime na pesen":"dqlkam bqlo","pevec":"krisko", "produljitelnost":2.45},
              {"ime na pesen":"mladi bulki","pevec":"100kila", "produljitelnost":2.45},
              {"ime na pesen":"otlichen 6","pevec":"Tonkata Storaro", "produljitelnost":2.45}
          ]
        }
produljitelnost = 0
for pesen in playlist["pesni"]:
    produljitelnost += pesen["produljitelnost"]
print(produljitelnost)

import json
x = {"name":"antony",
     "age":"24"}
# covert dictionary into a json
y = json.dumps(x)
print(y)
l=open("sample.json", "w")
l.write(y)
print(l)
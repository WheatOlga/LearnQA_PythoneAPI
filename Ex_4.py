import json

text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},' \
'{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'

data = json.loads(text)
secondLine = data["messages"][1]["message"]
print(secondLine)


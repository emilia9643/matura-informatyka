import platform
import json
x=platform.system()
print(x)

print(dir(platform))


x =  '{ "name":"John", "age":30, "city":"New York"}'
y=json.loads(x)
print(y["age"])


x={
    "name":"John",
    "age":30,
    "city":"New York"
}
print(json.dumps(x))🗿🗿🗿🗿🗿🗿🗿🗿🗿
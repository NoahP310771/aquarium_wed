import html
f = open('/var/www/html/aquarium/aquarium.html','w')

message = """
<h1>Aquarium temperature</h1>
"""

f.write(message)
f.close()
print("finished")

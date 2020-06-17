import requests
import html
import datetime
r = requests.get('https://api.particle.io/v1/devices/33003b000b47373336373936/temperature?access_token=1c476acb47bd0b944a031e2859ef7160e4b72a66')
temp = ("%.2f" % r.json()["result"])
r = requests.get('https://api.particle.io/v1/devices/33003b000b47373336373936/conductivity?access_token=1c476acb47bd0b944a031e2859ef7160e4b72a66')
cond = ("%.2f" % r.json()["result"])
r = requests.get('https://api.particle.io/v1/devices/33003b000b47373336373936/ph?access_token=1c476acb47bd0b944a031e2859ef7160e4b72a66')
ph = ("%.2f" % r.json()["result"])

#print(r)
#print(r.json())
#print("temperature result")
#print(r.json()["result"])
#temp = ("%.2f" % r.json()['result'])

now = datetime.datetime.now()
date_stamp = now.strftime("%Y-%b-%d %H:%M")
#print(date_stamp)

f = open('/var/www/html/aquarium/aquarium.csv','a')
f.write(date_stamp + ',' + temp + "," + cond + ',' + ph + '\n')
f.close()

f = open('/var/www/html/aquarium/aquarium.html','w')

message = """
<h1>Aquarium temperature</h1>
<p>The temperature of the aquarium is %s</p>
<p>The conductivity in the aquarium is %s</p>
<p>The pH in the aquarium is %s</p>
<p>this reading was last updated at %s</p>
""" % (html.escape(temp), html.escape(cond), html.escape(ph), html.escape(date_stamp))
f.write(message)
f.close()
print("finished")




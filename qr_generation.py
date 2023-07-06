!pip install segno
import segno

url = 'https://www.linkedin.com/in/marianna-ohanyan/?originalSubdomain=am'
qrcode = segno.make(url)
qrcode.save('qr.png', scale=10) 

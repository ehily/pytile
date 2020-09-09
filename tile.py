import requests

class Tile:
	def __init__(self, email, password):
		self.email = email;
		self.password = password;
		self.session = requests.session();
		self.headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0"
		}
		self.login();
	def login(self):
		r1 = self.session.get(
			url="https://web.thetileapp.com/login",
			headers=self.headers
		);
		r2 = self.session.post(
			url="https://web.thetileapp.com/api/v1/login",
			headers=self.headers,
			json={
				"email": self.email,
				"password": self.password
			}
		);
	def get_tiles(self):
		r1 = self.session.get(
			url="https://web.thetileapp.com/api/v1/devices",
			headers=self.headers
		);
		return r1.json();
	def ring_tile(self, uuid_device):
		r1 = self.session.post(
			url="https://web.thetileapp.com/api/v1/ring-state/%s" % uuid_device,
			headers=self.headers,
			json={
				"state": "start"
			}
		);
#Login to your account
t = Tile("<EMAIL>", "<PASSWORD>");
#Get all Tile devices
t.get_tiles();
#Ringing the Tile unit with its uuid
t.ring_tile("<UUID>");
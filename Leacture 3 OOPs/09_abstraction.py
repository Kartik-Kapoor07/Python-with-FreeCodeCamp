# Abstraction means:
# Hide internal details, show only what is necessary.

class EmailService:
    
    def _connect(self):
        print("Connecting to email server")
        
    def _authenticate(self):
        print("Authenticate")
        
    def send_email(self):
        self._connect()
        self._authenticate
        print("Sending email...")
        self._disconnect()
        
    def _disconnect(self):
        print("Disconnecting  from email server")

email = EmailService()
email.send_email()

# without using abstaction we need to write like this
# email._connect()
# email._authenticate()
# email.send_email()
# email._disconnect()

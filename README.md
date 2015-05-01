# emailer

An easy to use email wrapper for python and gmail.

All you need to do is:

* Sign into gmail
* go to [https://www.google.com/settings/security/lesssecureapps](https://www.google.com/settings/security/lesssecureapps) and change the setting to turn on.

Then you are ready to start sending email!!!

Example:

from mailer import Emailer
crds =json.load(open("creds.json","r"))
mailer = Emailer(addr=crds["addr"],pw=crds["pw"],receiver='ericschles@gmail.com',subject='Hi there')

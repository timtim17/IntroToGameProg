# Austin Jenchi
# 01/29/2015
# 8th Period
# Gmail

import httplib2
import re

from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run

def _callback(matches):
    id = matches.group(1)
    try:
        return unichr(int(id))
    except:
        return id

def decode_unicode_references(data):
    return re.sub("&#(\d+)(;|(?=\s))", _callback, data)


CLIENT_SECRET_FILE = 'client_secret.json'

# Location of the credentials storage file
STORAGE = Storage('gmail.storage')

# Start the OAuth flow to retrieve credentials
flow = flow_from_clientsecrets(CLIENT_SECRET_FILE, scope = 'https://www.googleapis.com/auth/gmail.modify')

credentials = STORAGE.get()

if credentials == None or credentials.invalid:
    credentials = run(flow, STORAGE)

# Authorize the httplib2.Http object with our credentials
http = httplib2.Http()
http = credentials.authorize(http)

# Build the Gmail service from discovery
gmail_service = build('gmail', 'v1', http = http)

# Retrieve a page of threads
messages = gmail_service.users().messages().list(userId = 'me', maxResults = 5).execute()
id = 0

# message = gmail_service.users().messages().get(userId = 'me', id = message["id"], format = 'full').execute()

while True:
    message = gmail_service.users().messages().get(userId = 'me', id = messages['messages'][id]['id'], format = 'full').execute()

    print message['payload']['headers'][13]['value']
    print
    print message['payload']['parts'][1]['data']
    # print decode_unicode_references(message['payload']['parts']['body']['data'])

    choice = raw_input('''Please choose an option:
    N: Next Email
    B: Previous Email
    A: Archive
    D: Delete
    P: Print
    E: Exit

    and press enter.

    ==> ''').upper()

    print

    if choice == 'N':
        print "NEXT EMAIL"
    elif choice == 'B':
        print "PREVIOUS EMAIL"
    elif choice == 'A':
        print "ARCHIVE EMAIL"
    elif choice == 'D':
        while True:
            choice = raw_input("ARE YOU SURE? Y/N ==> ").upper()
            if choice == "Y" or choice == "N":
                break
            else:
                print "That isn't Y(es) or N(o)!"

        if choice == "Y":
            print "EMAIL DELETED"
    elif choice == 'P':
        print "PRINT EMAIL"
    elif choice == 'E':
        print "Exiting..."
        break
    else:
        print "INVALID CHARACTER"
    print
import os
import json

from yattag import Doc



"""
##        #######     ###    ########
##       ##     ##   ## ##   ##     ##
##       ##     ##  ##   ##  ##     ##
##       ##     ## ##     ## ##     ##
##       ##     ## ######### ##     ##
##       ##     ## ##     ## ##     ##
########  #######  ##     ## ########
"""

def load_user_info():
	# find all dirs of format `@user`
	dirs = list(filter(
		lambda p: p.startswith('@'),
		os.listdir("../"),
	))

	# get json files from those dirs
	user_data = {}

	for usr in dirs:
		with open("../" + usr + "/info.json", 'r') as f:
			user_data[usr] = json.load(f)

	return user_data





"""
##     ## ######## ##     ## ##       ####  ######  ########
###   ### ##       ###   ### ##        ##  ##    ##    ##
#### #### ##       #### #### ##        ##  ##          ##
## ### ## ######   ## ### ## ##        ##   ######     ##
##     ## ##       ##     ## ##        ##        ##    ##
##     ## ##       ##     ## ##        ##  ##    ##    ##
##     ## ######## ##     ## ######## ####  ######     ##
"""

def gen_member_card(data):
	doc,tag,text = Doc().tagtext()

	with tag('li'):
		with tag('center'):
			with tag('b'):
				text(data['name'] + ' - ' + data['knc_id'])
			text('<br>')
			text(data['role'])
			text('<br>')
			with tag('a', href=data['email']):
				text(data['email'])
			text('<br>')
	
		
		with tag('h1'):
			text(data['name'])
		with tag('h2'):
			with tag('a', href=data['email']):
				text(data['email'])
		with tag('h2'):
			text(data['role'])
	
	links_list = ['github','website','CV']

	if any( (x in data) for x in links_list):
		with tag('h2'):
			text('Links:')
		with tag('ul'):
			for x in links_list:
				if x in data:
					with tag('li'):
						with tag('a', href=data[x]):
							text(x)

	return doc.getvalue()




def gen_members_page(user_data):

	# generate list of member cards
	MEMBERS_HEADER = None
	with open('members_header.txt') as f:
		MEMBERS_HEADER = f.read()
	MEMBERS_FOOTER = "</ul></div> </body> </html>"

	memlist = []

	for id in user_data:
		memlist.append(gen_member_card(user_data[id]))

	return (
		MEMBERS_HEADER
		+ '\n'.join(memlist)
		+ MEMBERS_FOOTER
	)




"""
##     ##  ######  ########  ########     ###     ######   ########
##     ## ##    ## ##     ## ##     ##   ## ##   ##    ##  ##
##     ## ##       ##     ## ##     ##  ##   ##  ##        ##
##     ##  ######  ########  ########  ##     ## ##   #### ######
##     ##       ## ##   ##   ##        ######### ##    ##  ##
##     ## ##    ## ##    ##  ##        ##     ## ##    ##  ##
 #######   ######  ##     ## ##        ##     ##  ######   ########
"""

def gen_personal_html(data):

	PERSONAL_TEMPLATE = f'''
	<!DOCTYPE html>
	<html>
	<meta charset="UTF-8">
	<head>
		<title>KNC -- {knc_id}</title>
	<link rel="stylesheet" href="../style.css">
	</head>
	<body style="padding-left: 20%;padding-right: 20%">
	<a href="../index.html">KNC Home</a>
	
	{everything_else}
	</body>
	</html>
	'''

	doc,tag,text = Doc().tagtext()

	with tag('center'):
		with tag('h1'):
			text(data['name'])
		with tag('h2'):
			with tag('a', href=data['email']):
				text(data['email'])
		with tag('h2'):
			text(data['role'])
	
	if 'bio' in data:
		with tag('p'):
			text(data['bio'])

	links_list = ['github','website','CV']

	if any( (x in data) for x in links_list):
		with tag('h2'):
			text('Links:')
		with tag('ul'):
			for x in links_list:
				if x in data:
					with tag('li'):
						with tag('a', href=data[x]):
							text(x)

	if 'proj_blurb' in data:
		with tag('h2'):
			text('Projects:')
		with tag('p'):
			text(data['proj_blurb'])

	
	return PERSONAL_TEMPLATE.format(
		knc_id = data['knc_id'],
		everything_else = doc.getvalue(),
	)


if __name__ == "__main__":
	print('dont run me')
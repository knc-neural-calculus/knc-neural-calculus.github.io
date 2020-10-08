import os
import json

from yattag import Doc,indent



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
			if user_data[usr]['knc_id'] != usr:
				raise ValueError('knc id in json does not match dirname!')

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
			with tag('b', id="memid"):
				text(data['name'])
			# if 'pronouns' in data:
			# 	text('  (%s)' % data['pronouns'])
			# else:
			# 	text('  (they/them)')
			doc._append("<br/>")

			with tag('a', id="memid", href=data['knc_id']):
				text(data['knc_id'])
			doc._append("<br/>")

			text(data['role'])
			doc._append("<br/>")

			with tag('a', href=data['email']):
				text(data['email'])
			doc._append("<br/>")
		
		links_list = ['github','website','CV']

		if any( (x in data) for x in links_list):
			with tag('center'):
				for x in links_list:
					if x in data:
						with tag('a', href=data[x]):
							text(x)
						doc._append("<br/>")

		if 'interests' in data:
			with tag('center'):
				with tag('p'):
					with tag('u'):
						text('Interests:')
					text('   ')
					text(data['interests'])

	return indent(doc.getvalue(), indent_text = False)




def gen_members_page(user_data):

	# generate list of member cards
	MEMBERS_HEADER = None
	with open('members_header.txt') as f:
		MEMBERS_HEADER = f.read()
	MEMBERS_FOOTER = '''
	</ul></div> </body> </html>

	<script>
		var ul = document.querySelector('ul#members');
		for (var i = ul.children.length; i >= 0; i--) {
			ul.appendChild(ul.children[Math.random() * i | 0]);
		}
	</script>
	'''

	memlist = []

	for id in user_data:
		memlist.append(gen_member_card(user_data[id]))

	return (
		MEMBERS_HEADER
		+ indent('\n'.join(memlist), indent_text = False)
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

	PERSONAL_TEMPLATE = '''
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

	if 'interests' in data:
		with tag('h2'):
			text('Interests:')
		with tag('p'):
			text(data['interests'])

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
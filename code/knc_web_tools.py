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


def load_proj_info():
	# find all dirs
	dirs = list(os.listdir("../projects/"))

	# get json files from those dirs
	proj_data = {}

	for proj_id in dirs:
		print('\t> loading project info:\t%s' % proj_id)
		with open("../projects/" + proj_id + "/info.json", 'r') as f:
			proj_data[proj_id] = json.load(f)
			if proj_data[proj_id]['proj_id'] != proj_id:
				raise ValueError('proj_id in json does not match dirname!')

	return proj_data




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

			with tag('a', href='mailto:'+data['email']):
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
		var ul = document.querySelector('ul#memlist');
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
		{header_stuff}
	</head>
	<body style="padding-left: 20%;padding-right: 20%">
	<a href="../index.html">KNC Home</a>
	
	{everything_else}
	</body>
	</html>
	'''

	doc,tag,text = Doc().tagtext()

	# if they want a webpage redirect
	if (
			'redirect_page_to_website' in data
			and 'website' in data
			and data['redirect_page_to_website']
		):

		# do the redirect
		redirect_header = (
			'<meta http-equiv="refresh" content="0; URL=%s" />' 
			% data['website']
		)

		# print a link also
		with tag('p'):
			text('redirecting to:')
			doc._append("<br/>")
			with tag('a', href=data['website']):
				text(data['website'])

		return PERSONAL_TEMPLATE.format(
			knc_id = data['knc_id'],
			everything_else = doc.getvalue(),
			header_stuff = redirect_header,
		)

	with tag('center'):
		with tag('h1'):
			text(data['name'])
		with tag('h2'):
			with tag('a', href='mailto:'+data['email']):
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
		header_stuff = '',
	)








"""
########  ########   #######        ## ########     ###     ######   ########
##     ## ##     ## ##     ##       ## ##     ##   ## ##   ##    ##  ##
##     ## ##     ## ##     ##       ## ##     ##  ##   ##  ##        ##
########  ########  ##     ##       ## ########  ##     ## ##   #### ######
##        ##   ##   ##     ## ##    ## ##        ######### ##    ##  ##
##        ##    ##  ##     ## ##    ## ##        ##     ## ##    ##  ##
##        ##     ##  #######   ######  ##        ##     ##  ######   ########
"""

def gen_proj_page(data):
	user_info = load_user_info()

	PERSONAL_TEMPLATE = '''
	<!DOCTYPE html>
	<html>
	<meta charset="UTF-8">
	<head>
		<title>KNC -- {projname}</title>
	<link rel="stylesheet" href="../../style.css">
	</head>
	<body style="padding-left: 20%;padding-right: 20%">
	<a href="../../index.html">KNC Home</a>
	
	{everything_else}
	</body>
	</html>
	'''

	doc,tag,text = Doc().tagtext()

	with tag('center'):
		with tag('h1'):
			text(data['projname'])
		doc._append("<br/>")
		
	with tag('center'):
		with tag('ul', id="nav", style="list-style-type: none; margin: 0; padding: 0"):
			for link in data['links']:
				with tag('a', href=data['links'][link]):
					with tag('li'):
						text(link)
		doc._append("<br/>")

	with tag('center'):
		with tag('h2'):
			with tag('b'):
				text('Contributors:  ')

			u_idx = 0
			for user in data['contributors']:
				if user[0] == '@':
					with tag('a', href='../../'+user):
						text(user_info[user]['name'])
				else:
					text(user)
				u_idx += 1
				if u_idx < len(data['contributors']):	
					text(', ')
		doc._append("<br/>")

	text(data['long_desc'])

	doc._append("<br/>\n\n")

	if 'images' in data:
		for img in data['images']:
			doc._append('<img src="%s" style="width: 25vw;">\n' % img)

	doc._append("<br/>\n\n")
	
	return PERSONAL_TEMPLATE.format(
		projname = data['projname'],
		everything_else = doc.getvalue(),
	)




def gen_proj_card(data):
	user_info = load_user_info()
	
	doc,tag,text = Doc().tagtext()

	with tag('li'):
		with tag('a', id="proj_id", href='projects/'+data['proj_id']):
			text(data['projname'])
		doc._append("<br/>")

		with tag('b'):
			text('Contributors:  ')

		u_idx = 0
		for user in data['contributors']:
			if user[0] == '@':
				with tag('a', href = user):
					text(user_info[user]['name'])
			else:
				text(user)
			
			u_idx += 1
			if u_idx < len(data['contributors']):
				text(', ')

		doc._append("<br/>")

		text(data['short_desc'])

		if 'thumbnail' in data:
			doc._append('<img src="%s" style="width: 25vw;">' % data['thumbnail'])

		doc._append("<br/><br/><br/>")

	return indent(doc.getvalue(), indent_text = False)




def gen_proj_list(proj_data):

	# generate list of member cards
	PROJECTS_HEADER = None
	with open('projects_header.txt') as f:
		PROJECTS_HEADER = f.read()

	PROJECTS_FOOTER = '''
	</ul> </body> </html>
	'''

	projlist = []

	for proj in proj_data:
		projlist.append(gen_proj_card(proj_data[proj]))

	return (
		PROJECTS_HEADER
		+ indent('\n'.join(projlist), indent_text = False)
		+ PROJECTS_FOOTER
	)



if __name__ == "__main__":
	print('dont run me!')
	exit(1)
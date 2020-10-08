from knc_web_tools import *

def main():
	user_info = load_user_info()

	knc_id = input('which user to generate a new index.html for?\n')

	if knc_id not in user_info:
		print('user not found! avalible users:')
		for x in knc_id:
			print('\t' + x)
		raise KeyError('user not found')
		exit(1)
	
	user_page = gen_personal_html(user_info[knc_id])

	do_continue = input('WARNING: this will overwrite the old `../%s/index.html`, continue? (y/n)\n' % knc_id)

	if do_continue == 'n':
		exit()
	elif do_continue == 'y':
		with open("../%s/index.html" % knc_id, 'w') as f:
			print(user_page, file=f)

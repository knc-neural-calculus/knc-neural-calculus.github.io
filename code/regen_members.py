from knc_web_tools import *

def main():
	user_info = load_user_info()

	mempage = gen_members_page(user_info)

	do_continue = input('WARNING: this will overwrite the old `../members.html`, continue? (y/n)\n')

	if do_continue == 'n':
		print('exiting -- no files modified')
		exit()
	elif do_continue == 'y':
		with open("../members.html", 'w') as f:
			print(mempage, file=f)
		print('updated successfully')

if __name__ == "__main__":
	main()
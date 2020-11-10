from knc_web_tools import *

def main():
	proj_info = load_proj_info()

	proj_list_page = gen_proj_list(proj_info)

	do_continue = input('WARNING: this will overwrite the old `../projects.html`, continue? (y/n)\n')

	if do_continue == 'n':
		print('exiting -- no files modified')
		exit()
	elif do_continue == 'y':
		with open("../projects.html", 'w') as f:
			print(proj_list_page, file=f)
		print('updated successfully')

if __name__ == "__main__":
	main()
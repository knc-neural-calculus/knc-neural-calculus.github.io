from knc_web_tools import *

def main():
	proj_info = load_proj_info()

	proj_id = input('which project to generate a new index.html for?\n')

	if proj_id not in proj_info:
		print('proj not found! avalible proj:')
		for x in proj_info:
			print('\t' + x)
		raise KeyError('proj not found')
		exit(1)
	
	proj_page = gen_proj_page(proj_info[proj_id])

	do_continue = input('WARNING: this will overwrite the old `../projects/%s/index.html`, continue? (y/n)\n' % proj_id)

	if do_continue == 'n':
		print('exiting -- no files modified')
		exit()
	elif do_continue == 'y':
		with open("../projects/%s/index.html" % proj_id, 'w') as f:
			print(proj_page, file=f)
		print('updated successfully')

if __name__ == "__main__":
	main()
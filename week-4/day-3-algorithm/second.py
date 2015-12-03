filename = open('alma.txt')
filename_read = filename.read()

def wc(text):
	count = [0,0]
	count[0] = len(text.split('\n'))
	count[1] = len(text)
	filename.close()
	return count

print(wc(filename_read))

filename2 = open('korte.txt')
filename2_read = filename2.read()

print(wc(filename2_read))

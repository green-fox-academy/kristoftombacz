from reverse import reverse_list
import os

print(reverse_list([3,4,5]))
print(os.getpid())


alma_file = open('alma.txt', 'w')
alma_file.write('balozsak')
alma_file.close()

alma_file = open('alma.txt')
print(alma_file.read())

alma_file.close()

#coding=utf-8

def reverse(str):
	if len(str) == 1:
		return str
	return str[-1] + reverse(str[:-1])

if __name__ == "__main__":
	print(reverse("abcdefg"))
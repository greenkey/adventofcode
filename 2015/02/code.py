
paper = 0
ribbon = 0

with open("input", "r") as packages:
	for package in packages:
		(l,w,h) = map(lambda x: int(x),package.strip().split('x'))
		ribbon += l*w*h + 2*min(l+w, w+h, h+l)
		paper += 2*(l*w + w*h + h*l) + min(l*w, w*h, h*l)


print("Paper needed tot: {} square feet".format(paper))
print("Ribbon needed tot: {} feet".format(ribbon))
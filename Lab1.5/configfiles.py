import glob

addresslist = []

for file in glob.iglob ("/home/ag/cloud/Seafile/p4ne/p4ne_training/config_files/*.txt"):
    with open(file) as openedfile:
        for lineinfile in openedfile:
            if "ip address " in lineinfile and not "dhcp" in lineinfile:

                addresslist.append(" ".join(lineinfile.strip().split(" ")[2:4]))


print (sorted(list(set(addresslist))))

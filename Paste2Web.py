#Author : D4Vinci
import requests ,re ,base64 ,random ,string ,os

def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

def rand():
	word =""
	for i in range(30):
		word += random.choice(string.ascii_letters+string.digits)
	return word

#post messages to the website
def send(msgs):
	#As you can see msgs is a list :3
	word = rand()
	print("Today's word is",word)
	print("-"*10)
	n=0
	for msg in msgs:
		msg = msg.replace("\r","").replace("\n","<(!NeWLIne!)>")
		word = word[:30]+str(n)
		link = "https://cl1p.net/"+word
		a=requests.post(link,data={"content":base64.b64encode(msg.encode("utf-8"))})
		#print(" [ Message "+str(n)+"]> "+link)
		print(" [ Part "+str(n)+" Sent ]")
		n +=1
	print("-"*10)
	print("\nToday's key is",str(n**2**2))

#get messages from the website
def receive(word,key):
	print("Receiving..")
	print("-"*5+"Message"+"-"*5)
	regex = re.compile('tent">(.*)</')
	key = int(pow(pow(int(key),0.5),0.5))
	for i in range(key):
		word = word[:30]+str(i)
		link = "https://cl1p.net/"+word
		source = requests.get(link).text
		msg = regex.findall(source)[0]
		msg = base64.b64decode(msg.encode("utf-8"))
		msg = msg.decode("utf-8")
		msg = msg.replace("<(!NeWLIne!)>","\n")
		print(msg, end=" ")
	print("\r"+"-"*5+"Message"+"-"*5)

def main():
	clear()
	print('\n --  ---  ---WELCOME BACK---  --   --   -- -')
	print(" --Paste2web-  --   --  --Secret messages---")
	print(" - -Do you wanna to (S)end or (R)eceive ?- -")
	put = input("(S-R)>> ").lower()
	if  put =="s":
		print("Type <(Done)> alone in a line when you finish the message\n..\n")
		final_msg = ""
		while True:
			x = input()
			if x.lower() != "<(done)>":
				final_msg += x+"\n"
			else:
				print("\n..")
				break
		print("\nSending..")
		try:
			send(final_msg.split(" "))
			print("Sent!")
		except:
			print("!"*10+"-ERROR SENDING MESSAGE-"+"!"*10)
		exit(0)

	elif  put =="r":
		word = input("Today's word is ")
		key = input("Today's key is ")
		receive(word,key)
		exit(0)
	else:
		main()

if __name__ == '__main__':
	main()

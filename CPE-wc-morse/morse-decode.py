def decode(secret):
# Function that decodes your string
	morse_code_decode = {
	".-": "A",
	"-...": "B",
	"-.-.": "C",
	"-..": "D",
	".": "E",
	"..-.": "F",
	"--.": "G",
	"....": "H",
	"..": "I",
	".---": "J",
	"-.-": "K",
	".-..": "L",
	"--": "M",
	"-.": "N",
	"---": "O",
	".--.": "P",
	"--.-": "Q",
	".-.": "R",
	"...": "S",
	"-": "T",
	"..-": "U",
	"...-": "V",
	".--": "W",
	"-..-": "X",
	"-.--": "Y",
	"--..": "Z",
	"-----": "0",
	".----": "1",
	"..---": "2",
	"...--": "3",
	"....-": "4",
	".....": "5",
	"-....": "6",
	"--...": "7",
	"---..": "8",
	"----.": "9",
	"(space)": " "
	}
# Dictonary for decoding morse code

	secret = secret.split(" ")
# Splites the morse code at every space

	decoded_msg = ""
# Creates a empy string

	try:
		for x in secret:
			decoded_msg = decoded_msg + morse_code_decode[x]
	except KeyError:
		pass
# Takes the morse code from the dir and turns it into caracters or numbers

	decoded_msg = decoded_msg.title()
# Makes the decoded word display in title

	return decoded_msg
# Returns a decoded message

if __name__ == "__main__":
# Execute test-program if started from original file

	file = open(input("Enter file to decode: "), "r") 
	nosecret = decode(file.read())
	print("Morse code is decoded:"+nosecret)


file = open("morse encoded.txt","w+") 
def encode(message):
# Function that encodes your string
	morse_code = morse_code = {
	"A": ".-",
	"B": "-...",
	"C": "-.-.",
	"D": "-..",
	"E": ".",
	"F": "..-.",
	"G": "--.",
	"H": "....",
	"I": "..",
	"J": ".---",
	"K": "-.-",
	"L": ".-..",
	"M": "--",
	"N": "-.",
	"O": "---",
	"P": ".--.",
	"Q": "--.-",
	"R": ".-.",
	"S": "...",
	"T": "-",
	"U": "..-",
	"V": "...-",
	"W": ".--",
	"X": "-..-",
	"Y": "-.--",
	"Z": "--..",
	"0": "-----",
	"1": ".----",
	"2": "..---",
	"3": "...--",
	"4": "....-",
	"5": ".....",
	"6": "-....",
	"7": "--...",
	"8": "---..",
	"9": "----.",
	" ": "(space)"
	}
# Dictonary with all caracters/numbers to morse code

	message = message.upper()
	encoded_msg = ""
# Makes you massage in all CAPS, and creates an empy string
	try:
		for x in message:
			encoded_msg = encoded_msg + morse_code[x] + " "
	except KeyError:
		print(" Invalid caracters! ".center(51, "*").upper())
		encoded_msg = "fail!"
# Takes your message imput and turns it into morse code
	
	return encoded_msg
# Returns the morse code

if __name__ == "__main__":

# Execute test-program if started from original file
	secret = encode(input("Enter a code to encode: "))
	print("Morse code is encoded: "+secret)
	file.write(secret) 
	file.close() 
# Prints the morse code

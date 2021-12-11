import wx
import gui

mainframe = gui.mainFrame
caeframe = gui.caesarCipher
vigFrame = gui.viginereCipher

class cipherTest(mainframe):
	def __init__(self,parent):
		mainframe.__init__(self, parent)

	def caesar_button( self, event ):
		self.caes = caesar(None)
		self.Destroy()
		self.caes.Show()

	def viginere_button( self, event ):
		self.vigi = viginere(None)
		self.Destroy()
		self.vigi.Show()


# Caesar cipher
class caesar(caeframe):
	def __init__(self,parent):
		caeframe.__init__(self, parent)

	def lets_encrypt( self, event ):
		plaintext = str(self.original_or_cipher.GetValue().upper())
		key = int(self.the_key.GetValue())
		alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		ciphertext = ""

		for letter in plaintext:
			if letter in alpha:
				letter_index = (alpha.find(letter) + key) % len(alpha)
				ciphertext = ciphertext + alpha[letter_index]
			else:
				ciphertext = ciphertext + letter
		self.the_result.SetValue(ciphertext)

	def lets_decrypt( self, event ):
		ciphertext = str(self.original_or_cipher.GetValue().upper())
		key = int(self.the_key.GetValue())
		alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		plaintext = ""

		for letter in ciphertext:
			if letter in alpha:
				letter_index = (alpha.find(letter) - key) % len(alpha)
				plaintext = plaintext + alpha[letter_index]
			else:
				plaintext = plaintext + letter
		self.the_result.SetValue(plaintext)

	def comeback( self, event ):
		self.comeback = cipherTest(None)
		self.Destroy()
		self.comeback.Show()

# Vigenère cipher
class viginere(vigFrame):
	def __init__(self,parent):
		vigFrame.__init__(self, parent)

	def lets_encrypt( self, event ):
		plaintext = str(self.original_or_cipher.GetValue().upper().replace(' ',''))
		key = str(self.the_key.GetValue().upper().replace(' ',''))
		key_length = len(key)
		key_as_int = [ord(i) for i in key]
		plaintext_int = [ord(i) for i in plaintext]
		ciphertext = ''
		for i in range(len(plaintext_int)):
			value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
			ciphertext += chr(value + 65)
		self.the_result.SetValue(ciphertext)

	def lets_decrypt( self, event ):
		ciphertext = str(self.original_or_cipher.GetValue().upper().replace(' ',''))
		key = str(self.the_key.GetValue().upper().replace(' ',''))
		key_length = len(key)
		key_as_int = [ord(i) for i in key]
		ciphertext_int = [ord(i) for i in ciphertext]
		plaintext = ''
		for i in range(len(ciphertext_int)):
			value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
			plaintext += chr(value + 65)
		self.the_result.SetValue(plaintext)

	def comeback( self, event ):
		self.comeback = cipherTest(None)
		self.Destroy()
		self.comeback.Show()
import platform

if platform.system() in ('Linux', 'Darwin'):
	from crypt import crypt, METHOD_SHA512


	def encrypt(s):
		return crypt(s, salt=METHOD_SHA512)


else:
	from passlib.hash import sha512_crypt


	def encrypt(s):
		return sha512_crypt.encrypt(s, rounds=5000)
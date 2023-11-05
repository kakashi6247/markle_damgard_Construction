import hashlib

hash_obj = hashlib.sha256()
#after importing library, we created an hashlib object, for hash function

data = "Hello, World!".encode('utf-8')  #Converting the string  to be hashed to bytes first
hash_obj.update(data) #Updating the hashlib object with the data

hash_result = hash_obj.hexdigest()
#Retrieve the hash value as a hexadecimal string by hexdigest function

print("Hash:", hash_result)
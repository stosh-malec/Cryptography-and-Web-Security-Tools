import hmac

#Run this funtion to validate HMACs. Key and Message will be taken as input and a hash will be return

def runtime():
  msg_input=input("Please enter a ciphertext")
  key_input = input('Please enter HMAC key')
  t = gen_tag(msg_input,key_input)
  hm=hmac.new(key_input.encode())
  hm.update(msg_input.encode())
  print(msg_input + ':' + t)
  return hm.hexdigest()

#To contribute please add fuctions to be able to parse and add files to read through and return files after creating hash

#!/usr/bin/env python3

import hmac
 
def gen_tag(msg,key):
  hm=hmac.new(key.encode())
  hm.update(msg.encode())
  return hm.hexdigest()
msg_input=input("Please enter a message to validate against HMAC")
key_input = input('Please enter a HMAC key to validate against')
t = gen_tag(msg_input,key_input)
print(msg_input + ':' + t)

#dumps()-Encryption
#loads()-Decryption
'''
1.JSON
2.Pickle
--------------------------------------------
import json
file=open('file.txt','a+')
data={
    "fullname": "John",
    "userid": 358735730,
    "password": "******"
}
# print(f'Original data: {data}')
# print(f'Type of original data:{type(data)}')
# print()
enc_data = json.dumps(data)
file.write(enc_data)
file.seek(0)
enc_data=file.read()
print(type(enc_data))
ori_data=json.loads(enc_data)
print(ori_data, type(ori_data))
# print(f'Encrypted data: {enc_data}')
# print(f'type of encrypted data:{type(enc_data)}')
# decp_data=json.loads(enc_data)
# print(f'Decrypted data: {decp_data}')
# print(f'type of decrypted data:{type(decp_data)}')
file.close()
'''
import pickle
file=open('file.txt','ab+')
data={
    "fullname": "John",
    "userid": 358735730,
    "password": "******"
}
print(f'Original data: {data}')
print(f'Type of original data:{type(data)}')
print()
enc_data = pickle.dumps(data)
# file.write(enc_data)
# file.seek(0)
# enc_data=file.read()
# print(type(enc_data))
# ori_data=pickle.loads(enc_data)
# print(ori_data, type(ori_data))
print(f'Encrypted data: {enc_data}')
print(f'Type of encrypted data:{type(enc_data)}')
decp_data=pickle.loads(enc_data)
print(f'Decrypted data: {decp_data}')
print(f'Type of decrypted data:{type(decp_data)}')
file.close()

'''
package architecture-
1.library:collection of packages
2.package:collection of files/module
3.module:files
'''
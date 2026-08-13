from scripts.validate import validate_ip

print(validate_ip("hello.1.1.2"))
print(validate_ip("192.0.0.2"))
print(validate_ip("192.168.1.1"))
print(validate_ip("256.168.1.1"))
print(validate_ip("192.abc.1.1"))
print(validate_ip("192.168.1"))
print(validate_ip("192.999.999.999")) 
from faker import Faker

fake = Faker()

print("Name: ",fake.name())
print("Address: ",fake.address())
print("E-mail: ",fake.email())
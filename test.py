import os

print("Here is the env var for this env")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
if AWS_ACCESS_KEY_ID:
  print(AWS_ACCESS_KEY_ID[7:])
print(os.environ.get("AWS_ACCESS_KEY_ID"))
print("That was the env var ")

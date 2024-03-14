text = """
dnspython==2.1.0
ecdsa==0.17.0
email-validator==1.1.3
fastapi==0.68.0
graphene==2.1.9
graphql-core==2.3.2
graphql-relay==2.0.1
greenlet==1.1.1
h11==0.12.0
httptools==0.3.0
idna==3.2
itsdangerous==1.1.0
Jinja2==2.11.3
Mako==1.1.5
MarkupSafe==2.0.1
"""


packages = filter(None, text.split("\n"))


# Prepend 'pip install ' to each package name

commands = ["pip install " + package for package in packages]


# Join the commands back into a single string separated by newlines

output_text = "\n".join(commands)

print(output_text)

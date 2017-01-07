import aiml

kernel = aiml.Kernel()
kernel.learn("startup.xml")
kernel.respond("load aiml")

while True:
    print(kernel.respond(raw_input("Message >>")))
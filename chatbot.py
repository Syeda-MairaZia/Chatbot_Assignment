import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("affirmative_to_interrogative02.aiml")

# Press CTRL-C to break this loop
while True:
    print (kernel.respond(input("Enter your message >> ")))
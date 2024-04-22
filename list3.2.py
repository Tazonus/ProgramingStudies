import sys
input_p = sys.argv[1]
output_p = "switched_" + input_p

input = open(input_p, 'r')
output = open(output_p, 'w')

takes = "\n"
leaves = "\r\n"
try:
    if sys.argv[2] == "unix":
        takes = "\r\n"
        leaves = "\n"
    elif sys.argv[2] == "win":
        takes = "\n"
        leaves = "\r\n"
except:
    guess = [0,0] # guesses is it unix/windows
    for line in input:
        if line.find("\r\n"):
            guess[1] += 1
        elif line.find("\n"):
            guess[0] += 1
            
    if guess[0] < guess[1]:
        takes = "\r\n"
        leaves = "\n"
        print("Guessed, you wanted to switch from windows to unix")
    else:
        takes = "\n"
        leaves = "\r\n"
        print("Guessed, you wanted to switch from unix to windows")

print(f"{takes},{leaves}")
for line in input:
    line = line.replace('\n', '\r\n')
    output.write(line)

input.close()
output.close()
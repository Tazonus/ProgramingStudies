import sys

def main():
    input_p = sys.argv[1]
    output_p = "switched_" + input_p

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
        guess_unix    = 0
        guess_windows = 0
        # guesses is it unix/windows
        input = open(input_p, 'r')
        for line in input:
            if  line.find("\r\n") != -1:
                guess_windows += 1
            elif line.find("\n") != -1:
                guess_unix += 1
        input.close()

        if guess_windows > guess_unix:
            takes = "\r\n"
            leaves = "\n"
            print("Guessed, you wanted to switch from windows to unix")
        else:
            takes = "\n"
            leaves = "\r\n"
            print("Guessed, you wanted to switch from unix to windows")

    input = open(input_p, 'r')
    output = open(output_p, 'w')
    for line in input:
        line = line.replace(takes, leaves)
        output.write(line)
    input.close()
    output.close()

if __name__ == "__main__":
    main()
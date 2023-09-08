import sys

# This program should take two arguments, a command--either "encode" or "decode"--
# and then a string.

if len(sys.argv) != 3:
    print("Incorrect number of arguments.", file=sys.stderr)
    print(f"Usage: {sys.argv[0]} command string\n", file=sys.stderr)
    sys.exit(1)

command, x = sys.argv[1:3]

match command:
    case "encode":
        # Implement the encoding here
        encoding = ""
        encoding_list=[]
        for n in x:
            y= hex(ord(n))
            encoding_list.append(y)
            encoding ="".join(encoding_list)
        print(encoding)

    case "decode":
        # Implement the decoding here
        z=x.split("0x")
        ny_list = [item for item in z if item != ""]
        decoded_list=[]

        for list in ny_list:
           decoded_list.append(chr(int(list, base = 16)))
        decoding = "".join(decoded_list)
        print(decoding)

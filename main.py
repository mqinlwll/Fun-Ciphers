import argparse
import importlib

def main():
    parser = argparse.ArgumentParser(description="Cipher Encoder/Decoder")
    parser.add_argument("cipher", choices=["caesar", "a1z26", "reverse_entire", "reverse_words"], help="Cipher to use")
    parser.add_argument("mode", choices=["encode", "decode", "brute_force"], help="Mode: encode, decode, or brute_force")
    parser.add_argument("--input_file", help="Input text file")
    parser.add_argument("--output_file", help="Output text file")
    parser.add_argument("--content", help="Input text content")
    parser.add_argument("--shift", type=int, help="Shift value for Caesar cipher")
    args = parser.parse_args()

    # Determine input source
    if args.content is not None:
        text = args.content
        print_result = True
    elif args.input_file is not None:
        if args.output_file is None:
            parser.error("--output_file is required when --input_file is used")
        with open(args.input_file, 'r') as f:
            text = f.read()
        print_result = False
    else:
        parser.error("Either --content or --input_file must be provided")

    # Map cipher to module
    cipher_to_module = {
        "caesar": "modules.Caesar",
        "a1z26": "modules.A1Z26",
        "reverse_entire": "modules.ReverseEntire",
        "reverse_words": "modules.ReverseWords"
    }
    module_name = cipher_to_module.get(args.cipher)
    if module_name is None:
        parser.error(f"Cipher {args.cipher} not supported")

    try:
        module = importlib.import_module(module_name)
    except ImportError:
        parser.error(f"Module for cipher {args.cipher} not found")

    # Select function based on mode
    if args.mode == "encode":
        func = getattr(module, "encode", None)
    elif args.mode == "decode":
        func = getattr(module, "decode", None)
    elif args.mode == "brute_force":
        func = getattr(module, "brute_force_decode", None)
    else:
        parser.error(f"Mode {args.mode} not supported")

    if func is None:
        parser.error(f"Mode {args.mode} not supported for {args.cipher}")

    # Execute cipher function
    if args.cipher == "caesar":
        if args.mode in ["encode", "decode"]:
            if args.shift is None:
                parser.error("--shift is required for caesar encode and decode")
            result = func(text, args.shift)
        elif args.mode == "brute_force":
            result = func(text)
    else:
        result = func(text)

    # Handle output
    if print_result:
        if args.mode == "brute_force":
            for i, res in enumerate(result):
                print(f"---- Possibility {i} ----")
                print(res)
                print()
        else:
            print(result)
    else:
        if args.mode == "brute_force":
            with open(args.output_file, 'w') as f:
                for i, res in enumerate(result):
                    f.write(f"---- Possibility {i} ----\n")
                    f.write(res + '\n\n')
        else:
            with open(args.output_file, 'w') as f:
                f.write(result)

if __name__ == "__main__":
    main()

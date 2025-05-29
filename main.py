import argparse
import importlib

def main():
    parser = argparse.ArgumentParser(description="Cipher Encoder/Decoder")
    parser.add_argument("cipher", choices=["caesar", "a1z26"], help="Cipher to use")
    parser.add_argument("mode", choices=["encode", "decode", "brute_force"], help="Mode: encode, decode, or brute_force")
    parser.add_argument("input_file", help="Input text file")
    parser.add_argument("output_file", help="Output text file")
    parser.add_argument("--shift", type=int, help="Shift value for encode/decode")
    args = parser.parse_args()

    # Map cipher to module name
    cipher_to_module = {
        "caesar": "modules.Caesar",
        "a1z26": "modules.A1Z26",
    }
    module_name = cipher_to_module.get(args.cipher)
    if module_name is None:
        parser.error(f"Cipher {args.cipher} not supported")

    try:
        module = importlib.import_module(module_name)
    except ImportError:
        parser.error(f"Module for cipher {args.cipher} not found")

    # Get the function based on mode
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

    # Read input file
    with open(args.input_file, 'r') as f:
        text = f.read()

    # Call the function with appropriate arguments
    if args.cipher == "caesar":
        if args.mode in ["encode", "decode"]:
            if args.shift is None:
                parser.error("--shift is required for caesar encode and decode")
            result = func(text, args.shift)
        elif args.mode == "brute_force":
            result = func(text)
    elif args.cipher == "a1z26":
        if args.mode in ["encode", "decode"]:
            result = func(text)

    # Write to output file
    if args.mode == "brute_force":
        with open(args.output_file, 'w') as f:
            for i, res in enumerate(result):
                f.write(f"---- Decoded with shift {i} ----\n")
                f.write(res + '\n\n')
    else:
        with open(args.output_file, 'w') as f:
            f.write(result)

if __name__ == "__main__":
    main()

# Fun Ciphers

A command-line tool for encoding and decoding text using Caesar and A1Z26 ciphers. It also supports brute-force decoding for the Caesar cipher.

## Usage

To use the tool, run `main.py` with the following arguments:

```
python main.py <cipher> <mode> <input_file> <output_file> [--shift <shift_value>]
```

Where:

- `<cipher>`: The cipher to use, either "caesar" or "a1z26".
- `<mode>`: The operation to perform, either "encode", "decode", or "brute_force" (only for Caesar cipher).
- `<input_file>`: The path to the input text file.
- `<output_file>`: The path to the output text file.
- `--shift <shift_value>`: The shift value for Caesar cipher's encode and decode modes (required for those modes).

## Examples

1. **Encode a file using Caesar cipher with shift 3:**

   ```
   python main.py caesar encode input.txt output.txt --shift 3
   ```

2. **Decode a file using Caesar cipher with shift 3:**

   ```
   python main.py caesar decode encoded.txt decoded.txt --shift 3
   ```

3. **Brute-force decode a file using Caesar cipher:**

   ```
   python main.py caesar brute_force encoded.txt possibilities.txt
   ```

   This will generate all possible decodings with shifts from 0 to 25.

4. **Encode a file using A1Z26 cipher:**

   ```
   python main.py a1z26 encode input.txt output.txt
   ```

5. **Decode a file using A1Z26 cipher:**

   ```
   python main.py a1z26 decode encoded.txt decoded.txt
   ```

## Notes

- For the **A1Z26 cipher**, the `encode` function ignores non-alphabetic characters, and the `decode` function expects the input to be in the format of numbers separated by '-', with words separated by spaces (e.g., "1-2-3" for "ABC").
- For the **Caesar cipher**, non-alphabetic characters are preserved as is, and it handles both uppercase and lowercase letters, preserving their case.
- The tool assumes that the input text for A1Z26 `decode` is correctly formatted; otherwise, it might raise errors.

## Extending the Tool

To add a new cipher, create a new Python file in the `modules` directory (e.g., `NewCipher.py`) and define the necessary functions (`encode`, `decode`, etc.). Then, update the `cipher_to_module` dictionary in `main.py` to include the new cipher.

For example:

```
cipher_to_module = {
    "caesar": "modules.Caesar",
    "a1z26": "modules.A1Z26",
    "newcipher": "modules.NewCipher",
}
```

Ensure the new module has the required functions based on the modes you want to support.

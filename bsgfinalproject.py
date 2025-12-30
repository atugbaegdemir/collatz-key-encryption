import hashlib

# 1️ Collatz ile Bit Dizisi Üretimi
def collatz_bits(seed, bit_len):
    n = seed
    bits = ""

    while len(bits) < bit_len:
        if n % 2 == 0:
            bits += "0"
            n //= 2
        else:
            bits += "1"
            n = 3 * n + 1

    return bits


# 2️ Collatz → SHA-256 → Güçlü Key
def generate_key(seed, key_len=256):
    collatz_output = collatz_bits(seed, 1024)
    hash_bytes = hashlib.sha256(collatz_output.encode()).digest()
    key_bits = ''.join(format(b, '08b') for b in hash_bytes)
    return key_bits[:key_len]


# 3️ Metin ↔ Binary Dönüşümü
def text_to_bits(text):
    return ''.join(format(ord(c), '08b') for c in text)

def bits_to_text(bits):
    chars = [bits[i:i+8] for i in range(0, len(bits), 8)]
    return ''.join(chr(int(c, 2)) for c in chars)


# 4️ XOR Şifreleme / Deşifre
def xor_cipher(data_bits, key_bits):
    result = ""
    for i in range(len(data_bits)):
        result += str(int(data_bits[i]) ^ int(key_bits[i % len(key_bits)]))
    return result


# 5️ Ana Program
if __name__ == "__main__":
    seed = 73                # Gizli anahtar (seed)
    message = "MERHABA"      # Şifrelenecek mesaj

    print("Orijinal Mesaj:", message)

    # Key üret
    key = generate_key(seed)
    print("Üretilen Key (ilk 64 bit):", key[:64])

    # Şifreleme
    message_bits = text_to_bits(message)
    cipher_bits = xor_cipher(message_bits, key)
    print("Şifreli Mesaj (binary):", cipher_bits)

    # Deşifre
    decrypted_bits = xor_cipher(cipher_bits, key)
    decrypted_message = bits_to_text(decrypted_bits)
    print("Çözülen Mesaj:", decrypted_message)

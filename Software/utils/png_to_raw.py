from PIL import Image
im = Image.open("../images/Background.png").convert("RGB")
out = bytearray()
for r, g, b in im.getdata():
    out += ((r & 0xF8) << 8 | (g & 0xFC) << 3 | b >> 3).to_bytes(2, "big")
open("sprite.rgb565", "wb").write(out)
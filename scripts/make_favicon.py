import sys
from pathlib import Path

try:
    from PIL import Image
except Exception:
    print(
        "Pillow is required. Install with: python3 -m pip install pillow",
        file=sys.stderr,
    )
    sys.exit(1)

if len(sys.argv) != 2:
    print("Usage: make_favicon.py <image>", file=sys.stderr)
    sys.exit(2)

src = Path(sys.argv[1])
if not src.exists():
    print(f"Not found: {src}", file=sys.stderr)
    sys.exit(3)

sizes = [16, 24, 32, 48, 64, 72, 96, 128, 256]
out_path = Path("favicon.ico")

with Image.open(src) as img:
    img = img.convert("RGBA")
    icon_sizes = []
    for size in sizes:
        frame = img.copy()
        frame.thumbnail((size, size))
        icon_sizes.append(frame)
    icon_sizes[0].save(out_path, format="ICO", sizes=[(s, s) for s in sizes])

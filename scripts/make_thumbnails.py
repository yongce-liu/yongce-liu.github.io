import os
import sys

try:
    from PIL import Image
except Exception:
    print(
        "Pillow is required. Install with: python3 -m pip install pillow",
        file=sys.stderr,
    )
    sys.exit(1)


def make_thumbnails(src_root, dst_root):
    max_size = (160, 160)

    for root, _dirs, files in os.walk(src_root):
        for name in files:
            src_path = os.path.join(root, name)
            rel_path = os.path.relpath(src_path, src_root)
            dst_path = os.path.join(dst_root, rel_path)
            os.makedirs(os.path.dirname(dst_path), exist_ok=True)
            if os.path.exists(dst_path):
                continue
            try:
                with Image.open(src_path) as img:
                    img.thumbnail(max_size)
                    img.save(dst_path)
            except Exception as exc:
                print(f"skip {src_path}: {exc}", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: make_thumbnails.py <src_root>", file=sys.stderr)
        sys.exit(2)

    src_root = sys.argv[1]

    if not os.path.exists(src_root):
        print(f"Source root not found: {src_root}", file=sys.stderr)
        sys.exit(3)

    make_thumbnails(src_root, f"{src_root}/tns")

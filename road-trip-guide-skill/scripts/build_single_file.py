# -*- coding: utf-8 -*-
"""Embed assets/*.jpg into trip map HTML as a single shareable file."""
import base64
import re
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    Image = None


def build(src_html: str, out_html: str, assets_dir: str = "assets") -> None:
    html = Path(src_html).read_text(encoding="utf-8")
    refs = sorted(set(re.findall(r"assets/[A-Za-z0-9_/\-\.]+\.(?:jpg|jpeg|png)", html)))
    for ref in refs:
        p = Path(ref)
        if not p.exists():
            print("MISSING", ref)
            continue
        if Image is not None:
            im = Image.open(p).convert("RGB")
            w, h = im.size
            if w > 1280:
                im = im.resize((1280, int(h * 1280 / w)), Image.LANCZOS)
            tmp = p.with_suffix(".embed.jpg")
            im.save(tmp, "JPEG", quality=72, optimize=True)
            raw = tmp.read_bytes()
        else:
            raw = p.read_bytes()
        b64 = base64.b64encode(raw).decode("ascii")
        html = html.replace(ref, "data:image/jpeg;base64," + b64)
        print("embedded", ref, f"{len(raw)//1024}KB")
    Path(out_html).write_text(html, encoding="utf-8")
    print("wrote", out_html, Path(out_html).stat().st_size)


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("usage: build_single_file.py src.html out.html")
        raise SystemExit(2)
    build(sys.argv[1], sys.argv[2])

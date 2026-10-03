from hashlib import sha256
from pathlib import Path

root = Path(__file__).resolve().parent
parts_dir = root / "parts"
parts = []
for number in range(1, 19):
    prefix = f"ADHD_Ontology_Pack_v0.4_reviewed_strict.zip.part{number:03d}"
    if number == 11:
        parts.extend([parts_dir / (prefix + "a"), parts_dir / (prefix + "b")])
    else:
        parts.append(parts_dir / prefix)
missing = [part.name for part in parts if not part.is_file()]
if missing:
    raise SystemExit("Missing archive part(s): " + ", ".join(missing))
out = root / "ADHD_Ontology_Pack_v0.4_reviewed_strict.zip"
with out.open("wb") as target:
    for part in parts:
        target.write(part.read_bytes())
actual = sha256(out.read_bytes()).hexdigest().upper()
expected = "0B42EC748A14B084D9A8DD6401FB72F11253C3CE9CCB1830EED00B9487C3B73E"
if actual != expected:
    out.unlink(missing_ok=True)
    raise SystemExit(f"SHA-256 mismatch: {actual}")
print(f"Reassembled {len(parts)} parts; SHA-256 OK: {actual}")

from hashlib import sha256
from pathlib import Path

root = Path(__file__).resolve().parent
parts = sorted((root / "parts").glob("ADHD_Ontology_Pack_v0.4_reviewed_strict.zip.part*"))
if not parts:
    raise SystemExit("No archive parts found")
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

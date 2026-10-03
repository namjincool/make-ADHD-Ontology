# OpenCrab pack archive

The original v0.4 OpenCrab import ZIP is stored as numbered binary parts because the GitHub MCP transfer rejected the single-file payload. The pieces preserve the original bytes and can be joined without transformation. Part 011 is split into `part011a` and `part011b` to keep each transfer below the connector's size limit.

Run from the repository root:

```shell
python release/reassemble_pack.py
```

The script writes `release/ADHD_Ontology_Pack_v0.4_reviewed_strict.zip`, checks its SHA-256, and removes the output if the check fails. Expected SHA-256: `0B42EC748A14B084D9A8DD6401FB72F11253C3CE9CCB1830EED00B9487C3B73E`. Original size: 1134602 bytes.

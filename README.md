# ADHD Ontology Pack for GraphRAG

Evidence-first ontology pack for structuring ADHD characteristics, functional impacts, assessment, associated factors, interventions, outcomes, and their supporting sources. The canonical release is v0.4.

## Release contents

- `docs/`: the 12-section design specification, 9-space mapping, schema, 30 Golden Questions, and the non-diagnostic personal-observation layer specification.
- `ontology/`: seed ontology and clearly marked candidate claims.
- `qa/`: v0.4 pack QA and Golden QA inputs, source anchors, and run output.
- `provenance/`: selected-source manifest, local integrity report, and initial OpenCrab ingest receipt.
- `release/`: the original OpenCrab v0.4 ZIP as numbered binary parts, with a reassembly and SHA-256 check.
- `history/`: earlier schema and QA-run artifacts; these are retained for traceability and are not the canonical release.

## Verified release snapshot

The reviewed OpenCrab pack is `ADHD Ontology Evidence Pack v0.4 Reviewed` (package ID `543da82d-9db6-4390-a312-4df917204970`). The recorded QA was grade A / 100, with 58 documents, 484 evidence chunks, 916 nodes, and 4,420 edges. The graph includes all nine OpenCrab spaces. Six manually reviewed candidate Claims had Evidence-to-Claim `supports` links; the remaining evidence gaps are recorded in the QA report.

The Golden QA run found each of the 30 question cards and its provenance among the top six results (20 top-one matches); original source documents were direct top-six results for 3 of 30 questions. This is a retrieval/provenance check, not a medical answer-accuracy evaluation.

## Safety and publication

This repository is intended to remain **private** by default. The ADHD subject matter is sensitive, and the ZIP contains source-derived evidence excerpts. The repository includes source metadata and a compact pack export, not the full raw `source_pack` collection. Review source permissions before changing repository visibility. No real personal observation records are included: that layer document defines a separate exploratory schema and explicitly prohibits using observations for diagnosis. This pack is informational and does not diagnose or replace clinical evaluation.

There is no license file; no rights to third-party source material are granted by this repository.

## Markdown and design input

Markdown navigation follows a sectioned design-spec pattern and keeps `resource`, `evidence`, `claim`, and the other OpenCrab spaces visibly distinct. The layout review consulted the OpenCrab `designer_brand_creator_persona_ontology pack` (package ID `75698a5b-6d89-4495-88df-e2353e1df33d`). Its retrieved documentation was weak and plan-derived, so it was used only as an information-architecture reference. No design-pack claims were imported as ADHD evidence.

## Start here

1. Read `docs/ADHD_Ontology_Pack_v0.1_Design_Spec.md`.
2. Check the canonical class/relation definitions in `docs/ADHD_ontology_schema_v0.2.md` and `.json`.
3. Review `qa/ADHD_Pack_QA_v0.4.md` before interpreting retrieval results.
4. Run `python release/reassemble_pack.py`, verify its SHA-256 success message, then import the reconstructed ZIP into OpenCrab.

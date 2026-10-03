# ADHD 온톨로지 스키마 초안

상태: **설계 초안**. OpenCrab 노드·엣지 생성이나 Evidence 색인은 아직 수행하지 않았다.

클래스 31개, 관계 24개. 각 항목의 출처 ID는 `source_pack/manifest.json`에서 확인한다.

## 클래스

| 클래스 | OpenCrab 공간 | 상위 클래스 | 출처 |
|---|---|---|---|
| Person | subject | — | P03_NIMH_General, P05_NICE_NG87 |
| ADHD | concept | — | P03_NIMH_General, P05_NICE_NG87 |
| Symptom | concept | — | P03_NIMH_General, P05_NICE_NG87 |
| Inattention | concept | Symptom | P03_NIMH_General |
| Hyperactivity | concept | Symptom | P03_NIMH_General |
| Impulsivity | concept | Symptom | P03_NIMH_General |
| AttentionDifficulty | concept | Symptom | P03_NIMH_General, P07_AADPA_Cooccurring |
| ExecutiveFunction | concept | — | P03_NIMH_General, P11_CADDRA_4_1 |
| WorkingMemory | concept | ExecutiveFunction | P03_NIMH_General |
| TaskInitiation | concept | ExecutiveFunction | P11_CADDRA_4_1 |
| Planning | concept | ExecutiveFunction | P03_NIMH_General, P11_CADDRA_4_1 |
| TimeManagement | concept | ExecutiveFunction | P04_NIMH_Adults, P12_RCPsych_CR235 |
| InhibitoryControl | concept | ExecutiveFunction | P03_NIMH_General, PMC10755583 |
| FunctionalImpact | outcome | — | P03_NIMH_General, P05_NICE_NG87 |
| WorkImpact | outcome | FunctionalImpact | P04_NIMH_Adults, PMC9443814 |
| AcademicImpact | outcome | FunctionalImpact | P03_NIMH_General, PMC11151783 |
| RelationshipImpact | outcome | FunctionalImpact | P03_NIMH_General, P04_NIMH_Adults |
| Context | concept | — | P03_NIMH_General, P05_NICE_NG87 |
| Sleep | concept | — | P03_NIMH_General, PMC8534229 |
| Stress | concept | — | P03_NIMH_General |
| Environment | concept | — | P08_AADPA_CBT, P05_NICE_NG87 |
| AlternativeExplanation | concept | — | P03_NIMH_General, P07_AADPA_Cooccurring |
| CooccurringCondition | concept | — | P07_AADPA_Cooccurring, P05_NICE_NG87 |
| Assessment | concept | — | P05_NICE_NG87, P06_AADPA_Diagnosis |
| Observation | evidence | — | P03_NIMH_General, P05_NICE_NG87 |
| Intervention | lever | — | P02_CDC_Treatment, P05_NICE_NG87, P08_AADPA_CBT |
| Outcome | outcome | — | PMC12651917, P05_NICE_NG87 |
| Evidence | evidence | — | P05_NICE_NG87, PMC12651917 |
| Guideline | policy | — | P05_NICE_NG87, P11_CADDRA_4_1 |
| Study | resource | — | PMC6109107, PMC10359875 |
| Claim | claim | — | P05_NICE_NG87, PMC12651917 |

## 관계

| 관계 | 시작 → 끝 | OpenCrab 직접 매핑 | 출처 |
|---|---|---|---|
| HAS_OBSERVATION | Person → Observation | manifest 확인 필요 | P03_NIMH_General, P05_NICE_NG87 |
| OBSERVES | Observation → Symptom | manifest 확인 필요 | P03_NIMH_General, P05_NICE_NG87 |
| OCCURS_IN | Observation → Context | manifest 확인 필요 | P03_NIMH_General, P05_NICE_NG87 |
| CHARACTERIZED_BY | ADHD → Symptom | manifest 확인 필요 | P03_NIMH_General, P05_NICE_NG87 |
| HAS_DOMAIN | ExecutiveFunction → WorkingMemory/TaskInitiation/Planning/TimeManagement/InhibitoryControl | manifest 확인 필요 | P03_NIMH_General, P11_CADDRA_4_1, P12_RCPsych_CR235 |
| ASSOCIATED_WITH_IMPACT | Symptom → FunctionalImpact | associated_with | P03_NIMH_General, P05_NICE_NG87, PMC11151783 |
| ASSESSES | Assessment → Symptom | manifest 확인 필요 | P05_NICE_NG87, P06_AADPA_Diagnosis |
| EVALUATES | Assessment → FunctionalImpact | manifest 확인 필요 | P05_NICE_NG87, P06_AADPA_Diagnosis |
| CONSIDERS | Assessment → AlternativeExplanation | manifest 확인 필요 | P03_NIMH_General, P07_AADPA_Cooccurring |
| USES_OBSERVATION | Assessment → Observation | manifest 확인 필요 | P03_NIMH_General, P05_NICE_NG87 |
| MAY_MIMIC | Sleep/Stress/AlternativeExplanation → AttentionDifficulty | manifest 확인 필요 | P03_NIMH_General, P07_AADPA_Cooccurring |
| CO_OCCURS_WITH | ADHD → CooccurringCondition | associated_with | P07_AADPA_Cooccurring, P05_NICE_NG87 |
| ASSOCIATED_WITH | Sleep → ADHD | associated_with | PMC8534229, P04_NIMH_Adults |
| TARGETS_SYMPTOM | Intervention → Symptom | manifest 확인 필요 | P05_NICE_NG87, P08_AADPA_CBT, PMC12651917 |
| TARGETS_IMPACT | Intervention → FunctionalImpact | manifest 확인 필요 | P08_AADPA_CBT, PMC9443814 |
| ASSOCIATED_WITH_OUTCOME | Intervention → Outcome | associated_with | PMC6109107, PMC10359875, PMC12651917 |
| RECOMMENDS | Guideline → Intervention | manifest 확인 필요 | P05_NICE_NG87, P11_CADDRA_4_1 |
| STUDIES | Study → ADHD/Symptom/Intervention/Outcome | manifest 확인 필요 | PMC6109107, PMC10359875 |
| REPORTS | Study → Evidence | manifest 확인 필요 | PMC6109107, PMC10359875 |
| MEASURES | Study → Outcome | manifest 확인 필요 | PMC6109107, PMC10359875 |
| SUPPORTS | Evidence → Claim | supports | P05_NICE_NG87, PMC12651917 |
| CONTRADICTS | Evidence → Claim | contradicts | PMC12651917, PMC10755583 |
| ABOUT | Claim → ADHD/Symptom/ExecutiveFunction/FunctionalImpact/Intervention/Outcome/Context | manifest 확인 필요 | P05_NICE_NG87, PMC12651917 |
| DERIVED_FROM | Evidence → Study/Guideline | derived_from | P05_NICE_NG87, PMC6109107 |

## 설계 결정

- OpenCrab의 9개 정규 공간에 클래스별 위치를 매핑했다. `community` 공간은 현재 자료에서 필요한 개체가 없어 비워 둔다.
- `Evidence`는 출처 구절·연구 결과이고, `Observation`은 개인에 관한 관찰 기록이다. 문헌에서 개인 기록을 임의 생성하지 않는다.
- 증상과 기능 영향, 수면과 ADHD, 개입과 결과의 연결은 기본적으로 비인과적이다. `AFFECTS`와 `causes`는 이번 초안의 관계에서 제외했다.
- 사용자가 제안한 `Symptom OCCURS_IN Context`는 개념 자체보다 실제 관찰에 맥락을 붙이는 `Observation OCCURS_IN Context`로 정밀화했다.
- `Sleep ASSOCIATED_WITH AttentionDifficulty`는 직접 관계 근거가 부족해 채택하지 않았다. 수면 문제·스트레스가 유사 증상에 해당할 수 있다는 감별 관계와 수면–ADHD 연관은 구분했다.
- `CONTRADICTS`는 실제 상충 근거가 확인될 때만 만든다. 서로 다른 연령대, 결과척도, 추적기간은 즉시 모순으로 취급하지 않는다.
- OpenCrab 상태 응답에서 확인된 직접 관계 의미는 `supports`, `contradicts`, `derived_from`, `associated_with` 등이다. 나머지 도메인 관계는 실제 빌드 전에 manifest 허용 여부를 확인해야 한다.

## 근거 공백과 보류

- `TaskInitiation`은 CADDRA에서 실행기능 영역으로 기술되지만 성인 업무 시작 지연의 특정 원인이라는 연결은 보류했다.
- 연구 5건은 서지정보만 확보했다. 해당 본문을 읽은 것으로 간주하지 않는다.
- 직장 환경 조정 효과는 문맥별 직접 연구가 부족하므로 개입 유형에서 모든 결과로 향하는 포괄적 효능 엣지를 만들지 않는다.

## 다음 단계의 품질 조건

1. 실제 OpenCrab ontology manifest가 허용하는 공간·관계만 사용한다.
2. 원문 단위별 Evidence를 보존하고 각 Claim에 출처 위치와 해시를 연결한다.
3. 연령대, 연구 설계, 비교군, 결과척도, 추적기간을 확인한 후 관계 인스턴스를 만든다.

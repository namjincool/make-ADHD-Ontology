# ADHD Ontology Pack v0.1

> 문서 유형: **설계 명세**. 첫 인제스트 문서. 작성일: 2026-10-03. 기반: `ADHD_ontology_schema_v0.2.json`, `ADHD_Golden_Questions.md`, `source_pack/manifest.json`. 이 문서에 적힌 클래스·관계는 설계 정의이며, 실제 환자 사실이나 임상 근거가 인제스트되었다는 뜻은 아니다.

## 1. Purpose

ADHD의 특징, 기능상의 영향, 평가 과정, 관련 요인, 관리·개입 방법 및 근거를 구조화한다. GraphRAG는 질문에 대해 개념, 주장, 문헌의 근거 위치와 적용 대상 집단을 함께 찾아야 한다. 특히 주장을 독립 `Claim` 노드로 두어 지지·상충 근거를 추적한다.

## 2. Scope

- 성인 ADHD를 중심으로 아동·청소년과의 차이를 명시한다.
- 증상, 실행기능, 기능 영향, 평가, 관련 상태, 개입, 측정 결과, 지침 권고를 구분한다.
- OpenCrab의 canonical 9-Space `subject / resource / evidence / concept / claim / community / outcome / lever / policy`를 사용한다.
- 출처 원문을 확보한 자료만 임상 `Evidence`의 후보로 삼는다. 이번 첫 인제스트 대상은 **이 설계 명세 한 문서**다.
- 개인 자기기록은 별도 `personal_pattern` 계층의 탐색 자료로 다룬다.

## 3. Non-goals

- 개인의 ADHD 진단, 증상 점수만으로 하는 판정, 치료 지시를 수행하지 않는다.
- 수면·스트레스와 ADHD의 연관을 인과관계로 자동 변환하지 않는다.
- 문헌 원문이 없는 서지정보를 임상 Evidence로 사용하지 않는다.
- 개인 관찰 기록을 진단 기준 또는 출판물 근거로 승격하지 않는다.
- 효과가 측정되지 않은 `ImprovedTaskCompletion`, 출처 없는 Dataset, 검증되지 않은 community 인스턴스를 만들지 않는다.

## 4. Core Classes

| OpenCrab Space | 클래스 |
|---|---|
| subject | Person, Clinician, Researcher |
| resource | Guideline, Study, Paper, Dataset (보류) |
| evidence | Observation, Evidence, GuidelineSection, StudyResult |
| concept | ADHD, Symptom, Inattention, Hyperactivity, Impulsivity, AttentionDifficulty, ExecutiveFunction, WorkingMemory, TaskInitiation, Planning, TimeManagement, InhibitoryControl, Context, Sleep, Stress, Environment, AlternativeExplanation, CooccurringCondition, Assessment |
| claim | Claim |
| community | ADHDClinicalDomain (보류), ExecutiveFunctionCluster (보류) |
| outcome | FunctionalImpact, WorkImpact, AcademicImpact, RelationshipImpact, Outcome, ImprovedTaskCompletion (보류) |
| lever | Intervention, BehavioralIntervention, EnvironmentalModification |
| policy | ClinicalGuideline |

`Guideline`은 버전이 있는 원본 문서(resource), `ClinicalGuideline`은 그 문서의 위치가 특정된 권고 내용(policy)이다. `Paper`는 연구 문서, `Study`는 설계·대상 정보가 있는 하위 유형이다. `GuidelineSection`과 `StudyResult`는 원문 위치를 가리키는 Evidence다.

OpenCrab의 현행 formal ontology는 `data`를 9-Space와 직교하는 계층으로 둔다. 기존 초안의 `Dataset → resource` 표기는 설계상 문서 자원 분류였으며, 실제 데이터셋이 들어올 경우 현행 `data` 계층과 DCAT 매핑을 우선한다. 현재 Dataset 인스턴스는 없다.

## 5. Relations

아래 25개는 **도메인 설계 어휘**다. 실제 그래프 관계는 OpenCrab manifest가 허용하는 의미(`supports`, `contradicts`, `derived_from`, `associated_with` 등)에 맞춰 확인한 뒤 생성한다. 양 끝 노드와 출처가 없으면 관계 인스턴스를 만들지 않는다.

| # | 설계 관계 | From | To | OpenCrab 런타임 의미 |
|---:|---|---|---|---|
| 1 | HAS_OBSERVATION | Person | Observation | 설계 관계; 런타임 매핑 확인 필요 |
| 2 | OBSERVES | Observation | Symptom | 설계 관계; 런타임 매핑 확인 필요 |
| 3 | OCCURS_IN | Observation | Context | 설계 관계; 런타임 매핑 확인 필요 |
| 4 | CHARACTERIZED_BY | ADHD | Symptom | 설계 관계; 런타임 매핑 확인 필요 |
| 5 | HAS_DOMAIN | ExecutiveFunction | WorkingMemory / TaskInitiation / Planning / TimeManagement / InhibitoryControl | 설계 관계; 런타임 매핑 확인 필요 |
| 6 | ASSOCIATED_WITH_IMPACT | Symptom | FunctionalImpact | associated_with |
| 7 | ASSESSES | Assessment | Symptom | 설계 관계; 런타임 매핑 확인 필요 |
| 8 | EVALUATES | Assessment | FunctionalImpact | 설계 관계; 런타임 매핑 확인 필요 |
| 9 | CONSIDERS | Assessment | AlternativeExplanation | 설계 관계; 런타임 매핑 확인 필요 |
| 10 | USES_OBSERVATION | Assessment | Observation | 설계 관계; 런타임 매핑 확인 필요 |
| 11 | MAY_MIMIC | Sleep / Stress / AlternativeExplanation | AttentionDifficulty | 설계 관계; 런타임 매핑 확인 필요 |
| 12 | CO_OCCURS_WITH | ADHD | CooccurringCondition | associated_with |
| 13 | ASSOCIATED_WITH | Sleep | ADHD | associated_with |
| 14 | TARGETS_SYMPTOM | Intervention | Symptom | 설계 관계; 런타임 매핑 확인 필요 |
| 15 | TARGETS_IMPACT | Intervention | FunctionalImpact | 설계 관계; 런타임 매핑 확인 필요 |
| 16 | ASSOCIATED_WITH_OUTCOME | Intervention | Outcome | associated_with |
| 17 | RECOMMENDS | ClinicalGuideline | Intervention | 설계 관계; 런타임 매핑 확인 필요 |
| 18 | STUDIES | Study | ADHD / Symptom / Intervention / Outcome | 설계 관계; 런타임 매핑 확인 필요 |
| 19 | REPORTS | Study | Evidence | 설계 관계; 런타임 매핑 확인 필요 |
| 20 | MEASURES | Study | Outcome | 설계 관계; 런타임 매핑 확인 필요 |
| 21 | SUPPORTS | Evidence | Claim | supports |
| 22 | CONTRADICTS | Evidence | Claim | contradicts |
| 23 | ABOUT | Claim | ADHD / Symptom / ExecutiveFunction / FunctionalImpact / Intervention / Outcome / Context / Sleep | 설계 관계; 런타임 매핑 확인 필요 |
| 24 | DERIVED_FROM | Evidence | Study / Paper / Guideline | derived_from |
| 25 | BASED_ON | ClinicalGuideline | Guideline | derived_from |

## 6. Properties

- 공통: `node_id`(안정된 고유 ID), `label`, `space`, `type`, `status`.
- 출처 필수: `source_locator`, `source_hash_or_external_id`, `collected_at`, `derived_by`, `derivation_version`.
- Resource: `source_id`, `title`, `publisher`, `url`, `publication_date`, `version`, `availability`.
- Evidence: `source_id`, `source_locator`, 원문 `content`, 해당 문서의 해시, 추출 단위. 지침 권고와 연구 측정 결과의 `evidence_type`을 구별한다.
- Claim: `statement`, `population`, `context`, `relation_type`, `causal_status`, `lifecycle_status`, `source_evidence_ids`.
- Outcome: `measure`, `population`, `comparator`, `timepoint`, `result`이 확인된 경우만 생성한다.
- 개인 관찰: 가명 ID, 관찰 시각, 기록자, 맥락, 동의 범위. 임상 Evidence와 별도 저장한다.

## 7. Claims

`Claim`은 한 문장으로 검증 가능한 독립 노드다. 문헌의 위치 특정 근거는 `Evidence --SUPPORTS/CONTRADICTS--> Claim`으로, 명제의 주제는 `Claim --ABOUT--> Concept`으로 연결한다. 생명주기는 `candidate → validated → promoted` 또는 `rejected`다. 근거 문서가 여러 개라면 각각 별도 Evidence 노드를 둔다.

설계 예시: `claim:adult_adhd_sleep_cooccurrence:001` — “성인 ADHD와 수면 문제는 흔히 동반된다.” 상태 `candidate`, 관계 `associated_with`, 인과 상태 `association_only`. 출처 후보는 NIMH 성인 ADHD 자료 `P04_NIMH_Adults`, 로컬 위치 `primary/P04_NIMH_Adults.txt#line=30`; 해당 원문이 별도 Evidence로 반입·검토되기 전에는 검증 또는 승격하지 않는다.

## 8. Evidence Model

- 원본 문서(Resource)와 해당 문서의 구절·절·측정 결과(Evidence)를 분리한다.
- Evidence 노드의 `content`에는 출처의 원문 전체 해당 단위를 보존한다. 추출·요약문만으로 원문을 대체하지 않는다.
- 지침의 권고(`GuidelineSection`)와 연구의 측정 결과(`StudyResult`)를 분리한다.
- `Evidence → Claim → Concept` 경로가 추적 가능해야 한다. 상충 판단 전에는 대상 집단, 연구 설계, 결과 측정, 시점을 비교한다.
- 설계 명세의 인제스트는 **설계 문서 Evidence**일 뿐 임상 문헌의 원문 Evidence가 아니다.

## 9. Validation Rules

1. 모든 근거 주장에는 실제 원문, 출처 ID, 원문 위치, 해시 또는 외부 ID를 요구한다.
2. `metadata_only` 자료는 근거 노드로 만들지 않는다.
3. `causes`는 `study_design`, `estimand`, `method`, `validation_status`를 확인한 뒤 별도 검토한다. 기본은 연관 의미다.
4. 대상 집단(성인/아동·청소년), 환경, 개입, 비교군, 결과의 시점을 구분한다.
5. 관계 양 끝 노드가 존재하고 원문 근거가 있는지 확인한다. 끊어진 관계와 의도치 않은 고립 노드를 남기지 않는다.
6. 개인 관찰 계층에서 임상 Claim으로 `SUPPORTS`·`CONTRADICTS`를 연결하지 않는다.
7. 첫 문서는 설계 명세인지 확인한다. 후속 문헌은 원문 단위로 반입하고 출처 추적 품질 검사를 거친다.

## 10. Golden Questions

아래 질문은 답변 검증을 위한 범위 정의이며, 그 자체로 의학적 주장이 아니다.

| ID | 분류 | Golden Question |
|---|---|---|
| Q01 | 특징 | ADHD의 핵심 증상 영역은 무엇이며, 부주의·과잉행동·충동성은 각각 어떻게 나타나는가? |
| Q02 | 특징 | ADHD의 증상 양상은 아동기, 청소년기, 성인기에 어떻게 달라질 수 있는가? |
| Q03 | 특징 | 부주의 증상과 실행기능의 어려움은 개념과 관찰 방법에서 어떻게 구별되는가? |
| Q04 | 특징·기능 | 과제 또는 업무 시작 지연은 어떤 실행기능 요소와 관련되는가? |
| Q05 | 특징·기능 | 시간 추정, 우선순위 설정, 계획 실행의 어려움은 각각 어떤 기능 영역과 관련되는가? |
| Q06 | 기능 영향 | ADHD 관련 어려움은 학습과 과제 수행에 어떤 영향을 줄 수 있는가? |
| Q07 | 기능 영향 | ADHD 관련 어려움은 업무의 시작, 지속, 마감, 오류 관리에 어떤 영향을 줄 수 있는가? |
| Q08 | 기능 영향 | ADHD 관련 어려움은 가사, 약속, 재정 관리 등 일상생활에 어떤 영향을 줄 수 있는가? |
| Q09 | 기능 영향 | ADHD 관련 어려움은 대인관계와 의사소통에 어떤 영향을 줄 수 있는가? |
| Q10 | 기능 영향 | 증상 빈도와 기능 손상 정도는 왜 별도로 평가해야 하는가? |
| Q11 | 평가 | ADHD 평가에서는 증상의 발달 시기, 지속 기간, 여러 환경에서의 관찰, 기능 손상을 어떻게 확인하는가? |
| Q12 | 평가 | 성인 ADHD 평가에서 현재의 어려움과 아동기 발달력을 연결하기 위해 어떤 정보를 확인하는가? |
| Q13 | 평가 | 본인 진술, 가족·교사·동료 등의 관찰, 과거 기록은 평가에서 각각 어떤 역할을 하는가? |
| Q14 | 평가 | 증상 평정척도와 인지·신경심리 검사는 무엇을 보조하며, 단독 판단에는 어떤 한계가 있는가? |
| Q15 | 평가 | ADHD와 비슷한 증상을 보일 수 있는 수면 문제, 불안, 우울, 학습·신체 건강 문제는 어떻게 감별하는가? |
| Q16 | 평가 | ADHD와 함께 나타날 수 있는 상태는 무엇이며, 평가·관리 계획에 어떤 영향을 주는가? |
| Q17 | 평가 | 학교·직장·가정 등 서로 다른 환경의 기능 손상을 어떤 정보로 파악하는가? |
| Q18 | 관련 요인 | 수면의 양·질과 ADHD 증상 또는 기능 손상 사이에는 어떤 연관이 보고되며, 방향성과 근거의 한계는 무엇인가? |
| Q19 | 관련 요인 | 스트레스·불안·우울은 ADHD 증상과 어떻게 겹치거나 상호 영향을 줄 수 있는가? |
| Q20 | 관련 요인 | 유전적·신경발달적·환경적 요인에 대해 무엇이 알려져 있으며, 연관성과 인과성을 어떻게 구분하는가? |
| Q21 | 관련 요인 | ADHD와 물질 사용 문제 사이에는 어떤 연관이 보고되며, 교란 요인은 무엇인가? |
| Q22 | 관련 요인 | 성별·성별화된 기대에 따라 ADHD의 발견과 평가 과정에 어떤 차이가 보고되는가? |
| Q23 | 관리·개입 | 약물치료는 어떤 증상과 기능 결과를 목표로 하며, 연령대별 근거는 무엇인가? |
| Q24 | 관리·개입 | 약물치료의 효과와 이상반응을 추적할 때 어떤 지표와 상황을 확인하는가? |
| Q25 | 관리·개입 | 성인 대상 인지행동치료·행동적 개입은 어떤 실행기능과 일상 기능 개선을 목표로 하는가? |
| Q26 | 관리·개입 | 직장·학교의 환경 조정과 지원은 어떤 기능상의 어려움을 줄이도록 설계되는가? |
| Q27 | 관리·개입 | 아동·청소년의 부모 교육 및 학교 기반 개입은 어떤 결과를 목표로 하며 근거는 무엇인가? |
| Q28 | 관리·개입 | 수면 관리와 신체활동 등 생활 습관 개입의 효과는 어떤 결과에서 평가되며 근거의 한계는 무엇인가? |
| Q29 | 관리·개입 | 개입을 선택하고 조정할 때 연령, 기능 손상, 동반 상태, 선호도, 치료 반응을 어떻게 함께 고려하는가? |
| Q30 | 근거 추적 | 특정 ADHD 관련 주장에 대해 지지 근거와 상충 근거는 어떤 문서·연구에서 왔으며, 대상 집단·연구 설계·발행 시점은 무엇인가? |

## 11. Example Triples

다음은 **스키마 방향 예시**다. 실제 관계 인스턴스는 원문과 OpenCrab 관계 제약을 확인한 뒤 만든다.

```text
ADHD --CHARACTERIZED_BY--> Inattention
Assessment --ASSESSES--> Symptom
Assessment --EVALUATES--> FunctionalImpact
ClinicalGuideline --BASED_ON--> Guideline
Evidence --SUPPORTS--> Claim
Claim --ABOUT--> ADHD
```

`Inattention --mayAffect--> TaskCompletion`은 이 단계에서 인과 또는 결과 근거가 부족하므로 생성하지 않는다. 위 수면 Claim도 별도 원문 Evidence 반입 전에는 후보에 머문다.

## 12. Source Policy

- 로컬 Source Pack: `source_pack/manifest.json` (수집일 2026-09-29). 총 32건: CDC·NIMH·NICE 5건, 전문기관 자료 7건, 연구 20건.
- 원문 확보 27건만 향후 본문 Evidence 후보. 5건은 `metadata_only`라 서지정보로만 유지한다.
- 우선 출처: [CDC ADHD](https://www.cdc.gov/adhd/), [NIMH ADHD](https://www.nimh.nih.gov/health/topics/attention-deficit-hyperactivity-disorder-adhd), [NICE NG87](https://www.nice.org.uk/guidance/ng87).
- 출처 문서의 발행·갱신 시점과 수집 시점을 별도로 기록한다. 해당 자료의 대상 연령과 연구 설계를 Claim마다 보존한다.
- 후속 반입 순서: 지침·전문기관 원문을 먼저, 연구 원문을 이어서 의미 단위로 분할한다. 각 단위를 Evidence로 색인하고 출처 해시·위치를 대조한다.
- 개인 관찰 자료는 별도 접근 제어 계층에만 보관한다. 이 팩에는 실제 개인 기록이 없다.

# ADHD Ontology 9-Space 매핑 초안 v0.2

상태: **스키마 초안·미색인** (2026-09-29). [상세 JSON](ADHD_ontology_schema_v0.2.json)은 이전 v0.1 초안을 대체하는 설계안이다. Source Pack의 원문을 자동으로 OpenCrab에 반입하거나 Claim을 검증·승격하지 않았다.

## TypeSafe 작업 분류

- `task_kind = ontology_schema_mapping`
- `evidence_route = source_backed_candidate_claim`
- `personal_data_route = separate_non_diagnostic_pattern_layer`
- TypeSafe API 연결이 프록시 오류로 실패하여 실제 모델 판정과 확률은 없다. 위 값은 스킬의 typed choice 방식에 따른 규칙 기반 분류다.

## 9-Space 매핑

| Space | 활성 클래스 또는 보류된 후보 | 적용 규칙 |
|---|---|---|
| subject | Person, Clinician, Researcher | Public literature does not create patient instances. |
| resource | Guideline, Paper, Study, Dataset | Guideline is the source document; Dataset awaits a real source. |
| evidence | Evidence, GuidelineSection, StudyResult, Observation | Observation here means clinician-collected assessment material; personal tracking is outside this graph. |
| concept | ADHD, Symptom, Inattention, Hyperactivity, Impulsivity, AttentionDifficulty, ExecutiveFunction, WorkingMemory, TaskInitiation, Planning, TimeManagement, InhibitoryControl, Context, Sleep, Stress, Environment, AlternativeExplanation, CooccurringCondition, Assessment | 근거가 확인된 인스턴스만 생성 |
| claim | Claim | Claims are separate atomic nodes; source passages point to them via SUPPORTS or CONTRADICTS. |
| community | ADHDClinicalDomain, ExecutiveFunctionCluster | Derived graph groups; no instances before validation. |
| outcome | FunctionalImpact, WorkImpact, AcademicImpact, RelationshipImpact, Outcome, ImprovedTaskCompletion | ImprovedTaskCompletion is deferred until a measured source is found. |
| lever | Intervention, BehavioralIntervention, EnvironmentalModification | 근거가 확인된 인스턴스만 생성 |
| policy | ClinicalGuideline | ClinicalGuideline is recommendation content, distinct from the Guideline resource. |

`Guideline`은 원본 지침 **문서(resource)**, `ClinicalGuideline`은 위치와 버전이 특정된 **권고 내용(policy)**이다. `BASED_ON`으로 둘을 연결한다. `Paper`는 논문 문서, `Study`는 설계·대상 정보가 붙은 하위 유형이다. `GuidelineSection`과 `StudyResult`는 원본 문서에서 추출한 위치 특정 근거이며 문서 자체와 별도 노드다.

`Dataset`은 실제 데이터셋 출처가 없어 인스턴스 생성을 보류한다. `ADHDClinicalDomain`·`ExecutiveFunctionCluster`도 검증된 멤버십 또는 그래프 군집 결과가 생기기 전까지 인스턴스를 만들지 않는다. `ImprovedTaskCompletion`은 측정 도구·비교군·시점이 확인된 결과가 없어 **개선이 입증된 결과 노드로 만들지 않는다**.

## Claim은 독립 노드

`Claim`에는 단일 명제, 대상 집단, 범위, 관계 유형, 인과 상태, 생명주기 상태, 근거 ID를 기록한다. `Evidence → SUPPORTS/CONTRADICTS → Claim → ABOUT → Concept` 경로로 질의한다. 근거 문서와 위치, 해시, 수집일, 생성 방법, 버전을 추적한다. `candidate → validated → promoted` 또는 `rejected` 상태를 구별한다. 원문 한 구절과 Claim을 동일 노드나 속성 하나로 합치지 않는다.

[후보 Claim 예시](ADHD_claim_candidate_v0.2.json)는 “성인 ADHD와 수면 문제가 흔히 동반된다”는 **연관** 명제다. NIMH 성인 ADHD 문서의 `primary/P04_NIMH_Adults.txt` 30행에 연결했다. 인과 방향이나 개인 진단을 뜻하지 않는다. 현재 상태는 `candidate`이며 OpenCrab에 색인되지 않았다.

## 개인 관찰 데이터 계층

개인 자기기록은 `personal_pattern` 계층에만 둔다. 자세한 저장·질의 규칙은 [개인 관찰 계층 설계](ADHD_personal_observation_layer.md)에 정의했다. 기록은 개인 패턴 탐색용이며 **ADHD 진단 기준이나 임상 Claim의 근거가 아니다**. 임상 문헌의 `Evidence`와 구분하여 색인·접근한다.

## 관계와 근거 경계

관계 유형은 총 **25개**다. `associated_with`는 동반·연관에 사용한다. `causes`는 연구 설계, 추정 대상, 방법, 검증 상태가 확인된 후에만 검토한다. `RECOMMENDS`는 `ClinicalGuideline → Intervention`, `BASED_ON`은 `ClinicalGuideline → Guideline`이다. 관계 인스턴스는 출처 위치를 확인한 뒤 생성한다.

Source Pack 32건 중 원문 확보 27건, 서지정보만 있는 5건은 Evidence로 사용하지 않는다. 과제 완료 개선, 데이터셋, 검증된 군집에는 현재 근거 공백이 있다.

## 다음 빌드 전 점검

1. 원문과 추출문 위치·해시를 대조하고 Claim의 대상 집단과 문구를 검토한다.
2. 실제 OpenCrab ontology manifest에서 클래스·관계 및 9-Space 제약을 검증한다.
3. 개인 계층 접근 제어와 분리 질의 경로를 구현한 뒤 데이터가 있을 때만 수집한다.

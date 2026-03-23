# Trendshift 레포 정리 아카이브

이 문서는 정리일 기준으로 누적하는 방식으로 관리합니다.

## 정리일: 2026-03-23
- 출처: https://trendshift.io/ , https://trendshift.io/github-trending-repositories
- 기준: 오늘 기준 두 페이지 전체를 다시 수집한 뒤, 페이지 간 중복을 제거하고 기존 파일(2026-03-05 기준 50개)과 겹치는 레포를 제외함
- 결과: 오늘 수집된 고유 레포 47개 중 신규 레포 20개만 정리
- 비고: 신규 20개는 모두 `trendshift.io` 오늘 목록에서 확인된 레포였음

## AI 에이전트·자동화 플랫폼 (10개)
1. **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** [TS]
   - 요약: 샌드박스, 메모리, 도구, 스킬, 서브에이전트를 결합해 리서치부터 구현까지 장시간 작업을 처리하는 오픈소스 SuperAgent 하니스입니다.
   - 활용 예시: 신규 기능 제안서를 넣으면 경쟁사 조사, 아키텍처 초안, 코드 스캐폴딩까지 몇 시간 단위로 이어지는 장기 작업 파이프라인을 자동 실행하는 데 쓸 수 있습니다.
2. **[browser-use/browser-use](https://github.com/browser-use/browser-use)** [TS]
   - 요약: 웹사이트를 AI 에이전트가 다룰 수 있게 만들어 온라인 작업 자동화를 쉽게 해주는 브라우저 자동화 프로젝트입니다.
   - 활용 예시: 브라우저로만 가능한 백오피스 업무를 에이전트가 로그인 후 처리하도록 연결해 폼 입력, 리포트 다운로드, 상태 점검을 자동화할 수 있습니다.
3. **[Crosstalk-Solutions/project-nomad](https://github.com/Crosstalk-Solutions/project-nomad)** [TS]
   - 요약: 오프라인 환경에서도 중요한 도구, 지식, AI 기능을 활용할 수 있도록 설계된 자급형 생존형 컴퓨팅 프로젝트입니다.
   - 활용 예시: 인터넷이 불안정한 현장 대응팀용 노트북 이미지로 구성해 매뉴얼 검색, 오프라인 문서 조회, 로컬 AI 질의응답까지 한 번에 제공할 수 있습니다.
4. **[garrytan/gstack](https://github.com/garrytan/gstack)** [TS]
   - 요약: CEO, 디자이너, 엔지니어링 매니저, QA 등 역할별 관점을 도구화한 Claude Code 작업 셋업입니다.
   - 활용 예시: 제품 초기 검증 단계에서 하나의 이슈를 기획 검토, 디자인 피드백, 릴리스 체크리스트, QA 확인까지 역할별 관점으로 순차 평가하는 워크플로를 만들 수 있습니다.
5. **[jackwener/opencli](https://github.com/jackwener/opencli)** [TS]
   - 요약: 웹사이트, Electron 앱, 로컬 바이너리를 표준화된 CLI 인터페이스로 바꿔 AI 에이전트가 쉽게 호출하도록 만드는 런타임입니다.
   - 활용 예시: 내부 웹 콘솔만 제공되는 운영 도구를 CLI처럼 노출해, 에이전트가 배포 이력 조회나 설정 변경 같은 작업을 명령형으로 수행하게 만들 수 있습니다.
6. **[karpathy/autoresearch](https://github.com/karpathy/autoresearch)** [TS]
   - 요약: 단일 GPU 환경에서도 AI 에이전트가 자동으로 연구 작업을 돌릴 수 있게 하는 실험 자동화 프로젝트입니다.
   - 활용 예시: 작은 GPU 서버 한 대에서 논문 아이디어 검증용 실험을 자동 반복하게 해, 데이터 준비부터 학습/평가 리포트 생성까지 연구 루프를 줄일 수 있습니다.
7. **[supermemoryai/supermemory](https://github.com/supermemoryai/supermemory)** [TS]
   - 요약: 빠르고 확장 가능한 메모리 엔진과 API를 제공해 AI 시대의 장기 기억 계층으로 쓰기 좋은 프로젝트입니다.
   - 활용 예시: 고객 상담 봇과 세일즈 봇이 같은 고객 이력을 공유하도록 연결해, 이전 대화 맥락과 선호 정보를 여러 에이전트가 재사용하게 만들 수 있습니다.
8. **[affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code)** [TS]
   - 요약: Claude Code, Codex, Cursor 계열 에이전트의 성능 최적화, 메모리, 보안, 리서치 우선 개발 방식을 묶은 운영 시스템입니다.
   - 활용 예시: 팀 공용 에이전트 환경에 이 구조를 적용해 보안 규칙, 기억 전략, 조사 우선 절차를 표준화하고 프롬프트 편차를 줄일 수 있습니다.
9. **[Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything)** [TS]
   - 요약: 코드베이스를 인터랙티브 지식 그래프로 바꾸어 탐색, 검색, 질문응답이 가능하도록 하는 Claude Code 스킬 모음입니다.
   - 활용 예시: 대형 모노레포 온보딩 시 신규 개발자가 "이 서비스는 어디서 인증을 처리하나?" 같은 질문을 그래프 기반으로 바로 탐색하게 할 수 있습니다.
10. **[MiniMax-AI/skills](https://github.com/MiniMax-AI/skills)** [TS]
   - 요약: 프론트엔드, 풀스택, Android, iOS, 셰이더 개발까지 구조화된 가이드를 제공하는 AI 코딩 에이전트용 개발 스킬 모음입니다.
   - 활용 예시: Codex나 Cursor 환경에 이 스킬 세트를 붙여 모바일/웹 병행 프로젝트에서 출력 형식과 개발 절차를 일정하게 맞추는 데 활용할 수 있습니다.

## 에이전트 스킬·워크플로 리소스 (5개)
1. **[github/spec-kit](https://github.com/github/spec-kit)** [TS]
   - 요약: 명세 주도 개발(Spec-Driven Development)을 빠르게 시작할 수 있도록 돕는 툴킷입니다.
   - 활용 예시: 기능 요청을 바로 코딩하지 않고 명세 문서, 수용 기준, 구현 태스크를 먼저 만드는 팀 규칙을 정착시키는 템플릿으로 쓸 수 있습니다.
2. **[Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)** [TS]
   - 요약: 48개 AI 에이전트와 36개 워크플로 스킬을 활용해 Claude Code를 게임 스튜디오처럼 운영하도록 설계한 프로젝트입니다.
   - 활용 예시: 인디 게임 프로토타입 개발에서 기획, 레벨 디자인, UI, QA 역할을 분리해 멀티에이전트 방식으로 병렬 제작 흐름을 실험할 수 있습니다.
3. **[greensock/gsap-skills](https://github.com/greensock/gsap-skills)** [TS]
   - 요약: GSAP를 AI 코딩 에이전트가 올바르게 사용하도록 모범 패턴과 플러그인 사용법을 제공하는 공식 스킬 세트입니다.
   - 활용 예시: 랜딩페이지 모션 작업에서 에이전트가 잘못된 애니메이션 코드를 만들지 않도록 GSAP 표준 패턴을 강제하는 참조 계층으로 붙일 수 있습니다.
4. **[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** [TS]
   - 요약: Claude Code용 스킬, 훅, 슬래시 명령, 오케스트레이터, 플러그인을 모아놓은 큐레이션 저장소입니다.
   - 활용 예시: 팀에 맞는 훅과 slash command 조합을 고를 때 이 목록을 기준으로 후보를 비교하고 내부 표준 셋을 빠르게 추릴 수 있습니다.
5. **[pascalorg/editor](https://github.com/pascalorg/editor)** [TS]
   - 요약: 공개 설명은 비어 있었지만 Trendshift 상에서는 3D generation 맥락으로 노출된 편집기 프로젝트로 보이며, 시각적 편집 워크플로 성격의 도구로 추정됩니다.
   - 활용 예시: WebGPU나 3D 편집 워크플로를 검증할 때 경량 편집기 베이스로 가져와 씬 구성, 에셋 배치, 상호작용 UI 프로토타입을 실험하는 출발점으로 사용할 수 있습니다.

## 금융·트레이딩 (2개)
1. **[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)** [TS]
   - 요약: 다중 에이전트 LLM 기반 금융 트레이딩 프레임워크입니다.
   - 활용 예시: 뉴스 해석 에이전트, 리스크 점검 에이전트, 주문 전략 에이전트를 분리해 전략별 의사결정 과정을 시뮬레이션하는 연구 환경으로 사용할 수 있습니다.
2. **[hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN)** [TS]
   - 요약: 중국어 환경에 맞게 강화한 다중 에이전트 LLM 금융 거래 프레임워크입니다.
   - 활용 예시: 중국어 뉴스와 종목 데이터를 활용한 전략 검토를 할 때 현지 언어 문맥까지 포함한 멀티에이전트 백테스트 환경으로 적용할 수 있습니다.

## 보안·공격 자동화 (1개)
1. **[vxcontrol/pentagi](https://github.com/vxcontrol/pentagi)** [TS]
   - 요약: 복잡한 침투 테스트 작업을 수행할 수 있는 완전 자율형 AI 에이전트 기반 펜테스팅 시스템입니다.
   - 활용 예시: 스테이징 환경에서 정기 보안 점검을 자동 실행해 약한 인증, 노출 서비스, 취약한 경로를 우선순위 포함 리포트로 받아보는 데 적합합니다.

## 개발 인프라·로컬 환경 (1개)
1. **[hectorvent/floci](https://github.com/hectorvent/floci)** [TS]
   - 요약: 가볍고 무료로 사용할 수 있는 AWS 로컬 에뮬레이터 프로젝트입니다.
   - 활용 예시: 클라우드 비용을 쓰지 않고도 로컬 개발 환경에서 AWS 연동 로직을 재현해 S3, 큐, 이벤트 기반 흐름을 테스트하는 데 활용할 수 있습니다.

## 콘텐츠·크리에이티브 자동화 (1개)
1. **[FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2)** [TS]
   - 요약: 온라인 수익화 과정을 자동화하는 데 초점을 둔 프로젝트입니다.
   - 활용 예시: 숏폼 콘텐츠 제작, 게시, 성과 추적 같은 반복 작업을 자동화하는 실험용 파이프라인으로 구성해 마케팅 자동화 아이디어를 검증할 수 있습니다.


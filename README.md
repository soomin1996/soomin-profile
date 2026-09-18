# 개인 소개 페이지 & 프론트엔드·백엔드 연동

클라우드컴퓨팅실습 개인과제 — 서수민

레트로 OS 창 형태의 개인 소개 페이지입니다.
페이지 안의 `PROFILE.EXE` 창에서 버튼을 누르면 Render에 배포한 FastAPI 백엔드를
호출하고, 돌아온 JSON 응답을 화면에 출력합니다.
소개 페이지와 연동 실습을 **하나의 페이지**로 구성했습니다.

## 배포 주소

| 구분 | 주소 |
|---|---|
| GitHub 저장소 | https://github.com/soomin1996/soomin-profile |
| Vercel 배포 페이지 | https://soomin-profile.vercel.app |
| 백엔드 Swagger UI | https://soomin-profile.onrender.com/docs |

## 주요 구성

```
soomin-profile/
├── frontend/          # Vercel 배포
│   ├── index.html     # 개인 소개 + 백엔드 연동 (한 페이지)
│   ├── avatar.png     # 픽셀 아트 아바타
│   └── dooly.png      # 강아지 둘리
├── backend/           # Render 배포
│   ├── main.py        # FastAPI 앱
│   ├── requirements.txt
│   └── .python-version
└── README.md
```

### 프론트엔드 (Vercel)

빌드 도구 없이 `index.html` 한 장으로 만들었습니다.

- 모눈종이 배경 위에 창(window)을 배치한 레트로 OS 화면
- 제목표시줄을 끌어 창을 옮기고, `×` 로 닫을 수 있습니다
- `PROFILE.EXE` 창 — `fetch`로 백엔드 `/profile` 을 호출해 응답을 출력합니다
- 요청 상태를 표시등으로 보여줍니다 (대기 / 200 OK / 실패)
- 화면 폭이 좁아지면 흩뿌린 배치가 세로로 쌓입니다

### 백엔드 (Render)

| 메서드 | 경로 | 설명 |
|---|---|---|
| GET | `/health` | 서버 상태 확인 |
| GET | `/profile` | 소개 정보(이름·역할·소속·관심) 반환 |
| GET | `/docs` | Swagger UI (FastAPI 자동 생성) |

- 응답 형태는 Pydantic 모델 `Profile` 로 정의했습니다
- 브라우저의 CORS 정책 때문에, Vercel 주소를 환경변수 `FRONTEND_ORIGINS` 로
  등록해 허용 출처에 추가합니다

## 로컬에서 실행하기

**백엔드**

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload          # http://127.0.0.1:8000/docs
```

**프론트엔드**

```bash
cd frontend
python3 -m http.server 5500        # http://127.0.0.1:5500
```

`index.html` 은 열린 주소가 `localhost`/`127.0.0.1` 이면 로컬 백엔드를,
그 외(배포된 사이트)면 Render 주소를 호출하도록 되어 있습니다.

## 사용 기술

- 프론트엔드 — HTML / CSS / JavaScript (`fetch`), 픽셀 폰트 [Galmuri](https://github.com/quiple/galmuri)
- 백엔드 — Python, FastAPI, Pydantic, Uvicorn
- 배포 — Vercel(프론트엔드), Render(백엔드), GitHub(소스 관리)

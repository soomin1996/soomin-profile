"""클라우드컴퓨팅실습 개인과제 — FastAPI 백엔드.

프론트엔드(Vercel)에서 호출해 결과를 화면에 표시한다.
"""

import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Soomin Seo · Profile API")

# ── CORS ────────────────────────────────────────────────────────────
# 브라우저는 다른 출처로 보낸 요청의 응답을 기본 차단한다.
# Vercel 주소는 배포 후 환경변수 FRONTEND_ORIGINS에 넣는다.
origins = ["http://localhost:5500", "http://127.0.0.1:5500"]
origins += [o.strip() for o in os.getenv("FRONTEND_ORIGINS", "").split(",") if o.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Profile(BaseModel):
    """프론트엔드에 돌려줄 소개 정보의 모양."""

    name: str
    role: str
    affiliation: str
    interests: list[str]


@app.get("/health")
def health_check():
    """서버가 살아 있는지 확인한다."""
    return {"status": "ok"}


@app.get("/profile", response_model=Profile)
def get_profile():
    """프론트엔드가 호출해 화면에 표시할 소개 정보."""
    return Profile(
        name="서수민 (Soomin Seo)",
        role="Market Intelligence Analyst",
        affiliation="KMBA · Seoul",
        interests=["둘리", "소비자 인사이트", "OTT · 미디어", "데이터 분석"],
    )

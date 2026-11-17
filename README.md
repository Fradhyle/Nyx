# Nyx - Entertainment Organizer
Program to manage various entertainment files (Videos, Images, Audios, etc.)
---
Dev Ideas
1. 파일 자체에 입력할 수 있는 표준 태그를 이용해서 파일에 정보 저장 (DB 방식보다 나을 듯?) -> 파일 형식마다 태그가 다른 부분은 고민해야 함
2. 모든 ID는 UUIDv7로 ```uuid.uuid7()```
3. 모든 텍스트에 다국어 지원 필요. 선호 언어로 먼저 노출되게 하는 것도 필요.

# FastAPI on Cloudflare Workers
Install dependencies and start local development with uv:

```sh
uv sync
uv run pywrangler dev
```

Deploy the Worker with:

```sh
uv run pywrangler deploy
```


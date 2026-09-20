# README

ComfyUI 원격 서버와 

## [CatVTON](https://github.com/Zheng-Chong/CatVTON)

인물 사진과 옷 사진을 합성하는 모델입니다.


## 환경변수 설정하기

`.env` 파일을 만들어서 `COMFY_BASE_URL` 값을 설정합니다. ComfyUI를 로컬에서 실행 중이라면 아래와 같습니다.

```dotenv
COMFY_BASE_URL=http://127.0.0.1:8189
```

## 프록시 서버 실행하기

ComfyUI는 8188 등의 다른 포트를 통해서 웹브라우저로 접속할 수 있는 프론트엔드를 제공합니다. 하지만 ComfyUI SDK에서 제공하는 v2 API를 사용하려면 `comfy-api-proxy`를 통해서 프록시 서버를 별도로 실행해주어야 합니다. 이를 위해서는 `comfy-api-proxy` 패키지가 설치된 파이썬 환경에서 아래 명령어를 실행해주어야 합니다. ComfyUI가 실행되는 포트가 8188이 아니라면 아래 명령어에서 포트번호를 알맞게 설정해주어야 합니다.

```bash
comfy-api-proxy --comfyui http://127.0.0.1:8188 --port 8189
```

## 다른 이미지로 실험하기

필요에 따라 `input` 디렉토리에 있는 `original.png`와 `reference.png` 파일을 변경하면 됩니다. 
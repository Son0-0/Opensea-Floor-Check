# Opensea floor price check
## Description
- 디스코드 봇 명령어를 통해 바닥가 정보 수집
  - Opensea API를 활용하여 원하는 프로젝트 바닥가 측정
  - 빗썸 오픈 API를 통하여 "ETH/KLAY - KRW" 실시간 시세 반영

## Installation
1. 레포지토리 클론  
```git clone https://github.com/Son0-0/Opensea-Floor-Check.git```
2. 필요한 라이브러리 설치  
```pip3 install -r requirements.txt```
3. 디스코드 봇 [TOKEN](https://discord.com/developers/docs/intro) 발급

## How to run your Bot
1. floorcheck.py 파일 실행  
```python3 floorcheck.py``` or ```python floorcheck.py```  

    1-1. floorcheck.py 파일 내 디스코드 봇 토큰 입력  
2. 봇 토큰 입력  
<img width="776" alt="terminal" src="https://user-images.githubusercontent.com/97378861/148895817-e8f52cbc-b5c8-409e-bd42-8afe3532472c.png">  

- 서버 내 백그라운드 실행하고 싶은 경우 (봇 토큰 미리 입력 필수)  
```nohup python3 floorcheck.py &``` or ```nohup python floorcheck.py &```

## Command
- !floor 프로젝트명  
ex) ```!floor doodles```  
<img width="359" alt="스크린샷 2022-08-07 오전 3 42 23" src="https://user-images.githubusercontent.com/81317358/183261987-65e8c15b-d020-4c68-87be-f9a7e28d6a6e.png">

- !fadd 프로젝트명 프로젝트-공식-오픈씨주소  
ex) ```!fadd doodles https://opensea.io/collection/doodles-official```  
<img width="473" alt="스크린샷 2022-08-07 오전 3 42 02" src="https://user-images.githubusercontent.com/81317358/183261985-752c45b5-2fb1-4c1b-9e05-692c94adb18b.png">

## Site List
- opensea.json 파일을 참고
  -  원하는 프로젝트가 있을시 양식에 맞게 추가
- 현재 기본으로 등록된 리스트
> moonbirds   =>    [Moonbirds](https://opensea.io/collection/proof-moonbirds)  
> bayc   =>    [BoredApeYachtClub](https://opensea.io/collection/boredapeyachtclub)    

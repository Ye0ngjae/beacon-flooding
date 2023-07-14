# Beacon Flooding 웹 애플리케이션

이 마크다운 문서는 Flask를 사용하여 Beacon Flooding을 수행하는 웹 애플리케이션에 대한 사용법을 안내합니다.

## 개요

이 웹 애플리케이션은 사용자가 웹 페이지에서 SSID를 입력하고 Beacon Flooding을 시작할 수 있도록 합니다. Beacon Flooding은 가짜 AP Beacon 프레임을 생성하여 주변의 Wi-Fi 디바이스에게 가짜 AP가 존재하는 것처럼 보이게 하는 공격입니다. 이 웹 애플리케이션은 Flask 프레임워크를 사용하여 개발되었으며, Python과 Scapy 라이브러리를 사용하여 Beacon Flooding을 구현합니다.

## 사전 요구사항

- Python 3.x+
- Flask 및 Scapy 라이브러리 설치
  
## 사용법

1. 소스 코드 및 관련 파일 다운로드

   - [GitHub 저장소 링크](https://github.com/Ye0ngjae/beacon-flooding)에서 소스 코드 및 관련 파일을 다운로드합니다.
   - 압축을 해제한 후 원하는 디렉토리로 이동합니다.

2. 가상 환경 설정 (선택 사항)

   - 가상 환경을 사용하여 프로젝트를 실행하고자 하는 경우, 가상 환경을 생성하고 활성화합니다.

3. 종속성 설치

   - 명령 프롬프트 또는 터미널을 열고 프로젝트 디렉토리로 이동합니다.
   - `pip install -r requirements.txt` 명령을 실행하여 필요한 종속성을 설치합니다.

4. 인터페이스 이름 설정

   - `app.py` 파일을 편집합니다.
   - `flood_beacon()` 함수 내부의 `iface='인터페이스_이름'` 부분을 실제 사용 중인 무선 인터페이스의 이름으로 변경합니다.

5. 애플리케이션 실행

   - 명령 프롬프트 또는 터미널에서 다음 명령을 실행합니다:
     ```
     python app.py
     ```
   - Flask 애플리케이션이 실행되고 서버가 시작됩니다.
   - 기본적으로 `http://localhost:5000` 주소에서 웹 애플리케이션에 접속할 수 있습니다.

6. 웹 애플리케이션 사용

   - 웹 브라우저에서 `http://localhost:5000` 주소로 이동합니다.
   - 웹 페이지에서 SSID 입력 필드를 찾고 원하는 SSID를 입력합니다.
   - "Start Flooding" 버튼을 클릭하여 Beacon Flooding을 시작합니다.
   - 서버 콘솔에서 Beacon Flooding이 시작되었음을 확인할 수 있습니다.
   - 필요한 경우, 다른 SSID로 Beacon Flooding을 추가로 시작할 수 있습니다.

7. Beacon Flooding 중지

   - Beacon Flooding을 중지하려면 웹 애플리케이션 페이지에서 "Stop Flooding" 버튼을 클릭합니다.
   - Beacon Flooding이 중지되고 서버 콘솔에서 해당 메시지가 표시됩니다.

## 주의사항

- Beacon Flooding은 합법적인 용도로 사용되어야 합니다. 법적인 제한 사항을 준수하고, 다른 사람의 개인정보 및 네트워크 보안을 침해하지 않도록 주의해야 합니다.
- 웹 애플리케이션을 실행하는 컴퓨터에는 Wi-Fi 기능이 있어야 합니다.
- 웹 애플리케이션을 실행하는 컴퓨터의 네트워크 인터페이스는 Monitor-Mode를 지원해야 합니다.
- Wi-Fi 인터페이스의 이름을 올바르게 설정해야 합니다. 필요한 경우, `app.py` 파일에서 인터페이스 이름을 수정해야 합니다.

## 추가 정보

- [Flask 공식 문서](https://flask.palletsprojects.com/)
- [Scapy 공식 문서](https://scapy.net/)

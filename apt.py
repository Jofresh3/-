import requests
from xml.etree import ElementTree

# 예시 URL 및 서비스 키
base_url = "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev"
service_key = "여기에 서비스 키를 입력"

# 가정된 '도로명시군구' 코드 리스트 (실제 코드로 대체 필요)
lawd_cd_list = ["11110", "11140", ...]  # 예시 코드들

# 결과를 저장할 리스트
results = []

# 지정된 범위 내에서 반복
for year in range(2010, 2024):  # 년도 범위
    for month in range(1, 13):  # 월 범위
        for day in range(1, 32):  # 일 범위 (실제 존재하는 날짜만 고려해야 함)
            for lawd_cd in lawd_cd_list:  # '도로명시군구' 코드
                # API 요청 URL 구성
                request_url = f"{base_url}?serviceKey={service_key}&LAWD_CD={lawd_cd}&DEAL_YMD={year}{month:02d}{day:02d}"

                # API 요청 및 응답
                response = requests.get(request_url)
                if response.status_code == 200:
                    # XML 응답 파싱
                    root = ElementTree.fromstring(response.content)
                    for item in root.findall('.//item'):
                        # 모든 필드 추출
                        data = {child.tag: child.text for child in item}
                        results.append(data)

# 결과 출력 또는 저장
print(results)

#https://www.data.go.kr/data/15057511/openapi.do
#공공기관 데이터

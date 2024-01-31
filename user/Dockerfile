FROM python:3.10.12

# 컨테이너 내 프로젝트 root directory 설정
WORKDIR /usr/src/app

# 필요한 module 설치
COPY requirements.txt ./
#RUN pip install --upgrade pip
RUN pip install -r requirements.txt
#RUN yarn install --ignore-engines
# 프로젝트 코드 복사
COPY . .

## Run the application on the port 8080
EXPOSE 8000

# gunicorn 배포 명령어
# CMD ["gunicorn", "--bind", "허용하는 IP:열어줄 포트", "project.wsgi:application"]
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "stock.wsgi:application"]


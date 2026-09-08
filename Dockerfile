FROM python:3.10-slim

# Instalar FFmpeg (vital para que yt-dlp pueda procesar los audios)
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Puerto dinámico asignado por el entorno de la nube
ENV PORT=5000
EXPOSE 5000

CMD ["python", "app.py"]

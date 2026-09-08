import os
from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route('/get-audio', methods=['GET'])
def get_audio():
    video_url = request.args.get('url')
    if not video_url:
        return jsonify({'success': False, 'error': 'Falta la URL'}), 400

    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            audio_url = info.get('url')
            if audio_url:
                return jsonify({'success': True, 'audio_url': audio_url})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

    return jsonify({'success': False, 'error': 'No se pudo extraer'}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

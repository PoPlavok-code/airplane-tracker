import http.server
import socketserver
from urllib.parse import parse_qs

PORT = 8000


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Читаем HTML-файл
        with open("contacts.html", "r", encoding="utf-8") as file:
            html_content = file.read()

        # Отправляем ответ
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html_content.encode("utf-8"))

        print(f"GET-запрос на {self.path}")

    def do_POST(self):
        # Читаем данные от пользователя
        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length).decode("utf-8")
        parsed_data = parse_qs(post_data)

        # Печатаем в консоль
        print("=" * 50)
        print("Получен POST-запрос!")
        print(f"Путь: {self.path}")
        print("Данные от пользователя:")
        for key, value in parsed_data.items():
            print(f"  {key}: {value[0]}")
        print("=" * 50)

        # Отправляем ответ
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        response = "<h1>Спасибо! Сообщение отправлено.</h1>"
        self.wfile.write(response.encode("utf-8"))


# Запуск сервера
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Сервер запущен на http://localhost:{PORT}")
    httpd.serve_forever()
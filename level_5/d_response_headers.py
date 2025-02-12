"""
У нас есть класс BaseResponse, который только работает с контентом, но он не умеет генерировать headers.
Нужно создать свой кастомный класс ответа, который сможет это делать


Задания:
    1. Создайте класс CustomResponse, который будет наследником и от BaseResponse и от BaseHeadersMixin
    2. Переопределите в нем метод generate_headers, таким образом, чтобы в базовые headers
       еще добавлялся header Content-Length, значение у которого - байтовая длинна контента. Используйте super()
       для этого
    3. Создайте экземпляр класса CustomResponse и вызовите у него метод generate_headers, все ли хэдэры теперь на месте.
"""


class BaseResponse:
    def __init__(self, content: str) -> None:
        self.content = content

    def get_byte_content_length(self) -> int:
        return len(self.content.encode('utf-8'))


class BaseHeadersMixin:
    def generate_base_headers(self) -> dict[str, str]:
        return {
            'Content-Type': 'application/x-www-form-urlencoded',
            'user-agent': (
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
            ),
        }

    def generate_headers(self) -> dict[str, str]:
        return self.generate_base_headers()


class CustomResponse(BaseHeadersMixin, BaseResponse):
    def generate_headers(self) -> dict[str, int | str]:
        return super().generate_base_headers() | {
            'Content-Length': super().get_byte_content_length(),
        }


if __name__ == '__main__':
    custom_response = CustomResponse(content='qwerty123')
    print(custom_response.generate_headers())
    print(custom_response.generate_base_headers())
    print(custom_response.get_byte_content_length())
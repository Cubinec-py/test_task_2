class MessageMathCaptcha:
    def __init__(self, client):
        self.client = client

    async def message_math_captcha(self, callback_data, channel=None):
        if not self.client.is_connected():
            await self.client.connect()
        user = await self.client.get_me()
        if user.username:
            split_data = user.username
        else:
            split_data = user.first_name
        data = callback_data[0].message.message.split(split_data)[0]
        result = self.evaluate_expression(data)
        await self.client.send_message(channel, result)

    @staticmethod
    def evaluate_expression(expression):
        operators = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y,
        }

        def parse_number(token_list):
            return int(token_list.pop(0))

        def parse_term(token_list):
            left = parse_factor(token_list)

            while token_list and token_list[0] in ["*", "/"]:
                operator = token_list.pop(0)
                right = parse_factor(token_list)
                left = operators[operator](left, right)

            return left

        def parse_expression(token_list):
            left = parse_term(token_list)

            while token_list and token_list[0] in ["+", "-"]:
                operator = token_list.pop(0)
                right = parse_term(token_list)
                left = operators[operator](left, right)

            return left

        def parse_factor(token_list):
            if token_list[0] == "(":
                token_list.pop(0)  # Consume '('
                result = parse_expression(token_list)
                token_list.pop(0)  # Consume ')'
                return result
            else:
                return parse_number(token_list)

        tokens = []
        current_token = ""
        for char in expression:
            if char in ["+", "-", "*", "/"]:
                if current_token:
                    tokens.append(current_token)
                tokens.append(char)
                current_token = ""
            elif char == "(" or char == ")":
                if current_token:
                    tokens.append(current_token)
                tokens.append(char)
                current_token = ""
            else:
                current_token += char

        if current_token:
            tokens.append(current_token)

        return str(int(parse_expression(tokens)))

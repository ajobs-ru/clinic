import ast
import secrets


def password(length=8):
    alphabet = "abcdefghijkmnpqrstuvwxyzABCDEFGHLMNPQRSTUVWXYZ23456789"
    return "".join(secrets.choice(alphabet) for i in range(length))


def upper_string(length=8):
    alphabet = "ABCDEFGHLMNPQRSTUVWXYZ23456789"
    return "".join(secrets.choice(alphabet) for i in range(length))


def random_hex(length=16):
    return secrets.token_hex(length)


def auto_cast(value):
    lowered = str(value).strip().lower()
    if lowered == "none" or lowered == "null":
        return None
    if lowered == "true":
        return True
    if lowered == "false":
        return False

    try:
        return ast.literal_eval(value)
    except (ValueError, SyntaxError):
        pass

    return value

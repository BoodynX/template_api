class NotEmptyStr:
    def __call__(self, value: str) -> bool:
        return bool(value.strip())

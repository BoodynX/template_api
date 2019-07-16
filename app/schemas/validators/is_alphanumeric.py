class IsAlphanumeric:
    def __call__(self, value: str) -> bool:
        return bool(value.isalnum())

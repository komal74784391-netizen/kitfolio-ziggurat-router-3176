class Router:
    """Route prompts to the cheapest backend that meets the tier."""

    def __init__(self, backends):
        self.backends = backends

    def route(self, prompt, tier="auto"):
        raise NotImplementedError

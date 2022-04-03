


class ZeroDenominatorError(Exception):
    def __init__(self):
        super(ZeroDenominatorError, self).__init__('на ноль делить низя')
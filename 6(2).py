# Клас для виконання математичних операцій
class MathOperations:

    @staticmethod
    def add(x, y):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            return x + y
        elif isinstance(x, (list, tuple)) and isinstance(y, (list, tuple)):
            return [x_i + y_i for x_i, y_i in zip(x, y)]
        elif isinstance(x, (np.ndarray, torch.Tensor)) and isinstance(y, (np.ndarray, torch.Tensor)):
            return x + y
        else:
            raise TypeError("Невідома операція")

    @staticmethod
    def subtract(x, y):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            return x - y
        elif isinstance(x, (list, tuple)) and isinstance(y, (list, tuple)):
            return [x_i - y_i for x_i, y_i in zip(x, y)]
        elif isinstance(x, (np.ndarray, torch.Tensor)) and isinstance(y, (np.ndarray, torch.Tensor

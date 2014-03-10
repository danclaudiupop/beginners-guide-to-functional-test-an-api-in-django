class ModelFactory(object):

    def __init__(self, model, **fields):
        self._model = model
        self._fields = fields
        self._counter = 1

    def __call__(self, **kwargs):
        fields = dict(self._fields)
        fields.update(kwargs)
        f = {}
        for k, v in fields.items():
            if callable(v):
                new_v = v
            try:
                new_v = v % self._counter
            except TypeError:
                new_v = v
            f[k] = new_v
        self._counter += 1
        return self._model.objects.create(**f)

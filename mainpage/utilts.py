def upload_to_common(instance, filename):
    model_name = instance.__class__.__name__.lower()
    return f'{model_name}/{filename}'
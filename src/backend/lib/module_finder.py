def _get_module(package, target):
    return __import__(f'{package}.{target}', fromlist=[f'{target}'])


class ModuleFinder(object):
    def __init__(self, package):
        self.package = package or 'backend'

    def get_controller(self, name_or_object, **kwargs):
        package = 'backend'
        try:
            if isinstance(name_or_object, str):
                controller_module = _get_module(package, 'controller')
                return getattr(controller_module, name_or_object)(**kwargs)
            else:
                return name_or_object(**kwargs)

        except Exception as e:
            raise Exception(e)


def pre_init_hook(cr):
    raise NotImplementedError


def post_init_hook(cr, registry):
    raise NotImplementedError


def uninstall_hook(cr, registry):
    raise NotImplementedError


def post_load():
    raise NotImplementedError


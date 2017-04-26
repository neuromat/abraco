from django import template

register = template.Library()


@register.filter
def placeholder_has_video(article):
    content = article.content
    plugin_list = content.get_plugins_list()

    for plugin in plugin_list:
        get_class = plugin.get_plugin_class()
        name = get_class.name

        if name.__str__() == 'Video':
            return True

    return False

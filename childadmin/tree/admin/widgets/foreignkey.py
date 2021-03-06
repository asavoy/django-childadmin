"""
Contains widgets that can be used for admin models
with related items.
"""
from django import forms
from django.core import urlresolvers
from django.utils.html import escape
from django.utils.safestring import mark_safe


class RenderLink(forms.Widget):
    """
    Renders a link to an admin page based on the primary key
    value of the model.
    """
    input_type = None
    
    def _has_changed(self, initial, data):
        return False
    def id_for_label(self, id_):
        return "hmm geen idee"
        
    def render(self, name, value, attrs=None):
        
        modelname = self.attrs['modelname']
        app_label = self.attrs['app_label']
        label = self.attrs['label']
        url_pattern = '%s:%s_%s_change' % ('admin', app_label, modelname)
        url = urlresolvers.reverse(url_pattern, args=[value])

        return mark_safe(
            '<a href="%s">%s</a><br>' % (
            escape(url), escape(label)
            ))

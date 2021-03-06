from django.conf.urls import url

from ansible.forms import AnsibleForm1, AnsibleForm2
from ansible.views import (
    PlaybookDetailView, PlaybookListView, PlaybookDeleteView, PlaybookFileView,
    PlaybookFileCreateView, PlaybookFileEditView, PlaybookWizard
)


urlpatterns = [
    url(
        r'^create/$',
        PlaybookWizard.as_view([
            AnsibleForm1,
            AnsibleForm2
        ]),
        name='playbook-create'
    ),
    url(
        r'^$',
        PlaybookListView.as_view(),
        name='playbook-list'
    ),
    url(
        r'^(?P<pk>[-\w]+)/delete$',
        PlaybookDeleteView.as_view(),
        name='playbook-delete'
    ),
    url(
        r'^(?P<pk>[-\w]+)/$',
        PlaybookDetailView.as_view(),
        name='playbook-detail'
    ),
    url(
        r'^(?P<pk>[-\w]+)/new/$',
        PlaybookFileCreateView.as_view(),
        name='playbook-file-create'
    ),
    url(
        r'^(?P<pk>[-\w]+)/files/(?P<slug>[\w-]+)$',
        PlaybookFileView.as_view(),
        name='playbook-file-detail'
    ),
    url(
        r'^(?P<pk>[-\w]+)/files/(?P<slug>[\w-]+)/edit$',
        PlaybookFileEditView.as_view(),
        name='playbook-file-edit'
    ),
]

from __future__ import unicode_literals

from ..models import Tag

from .literals import (
    TEST_TAG_COLOR, TEST_TAG_COLOR_EDITED, TEST_TAG_LABEL, TEST_TAG_LABEL_2,
    TEST_TAG_LABEL_EDITED
)


class TagAPIViewTestMixin(object):
    def _request_test_tag_create_api_view(self):
        return self.post(
            viewname='rest_api:tag-list', data={
                'label': TEST_TAG_LABEL, 'color': TEST_TAG_COLOR
            }
        )

    def _request_test_tag_delete_api_view(self):
        return self.delete(
            viewname='rest_api:tag-detail', kwargs={'pk': self.test_tag.pk}
        )

    def _request_tag_edit_view(self, extra_data=None, verb='patch'):
        data = {
            'label': TEST_TAG_LABEL_EDITED,
            'color': TEST_TAG_COLOR_EDITED
        }

        if extra_data:
            data.update(extra_data)

        return getattr(self, verb)(
            viewname='rest_api:tag-detail', kwargs={'pk': self.test_tag.pk},
            data=data
        )

    def _request_test_tag_document_list_api_view(self):
        return self.get(
            viewname='rest_api:tag-document-list', kwargs={
                'pk': self.test_tag.pk
            }
        )

    def _request_test_document_attach_tag_api_view(self):
        return self.post(
            viewname='rest_api:document-tag-list', kwargs={
                'document_pk': self.test_document.pk
            }, data={'tag_pk': self.test_tag.pk}
        )

    def _request_test_document_tag_detail_api_view(self):
        return self.get(
            viewname='rest_api:document-tag-detail', kwargs={
                'document_pk': self.test_document.pk, 'pk': self.test_tag.pk
            }
        )

    def _request_test_document_tag_list_view(self):
        return self.get(
            viewname='rest_api:document-tag-list', kwargs={
                'document_pk': self.test_document.pk
            }
        )

    def _request_test_document_tag_remove_view(self):
        return self.delete(
            viewname='rest_api:document-tag-detail', kwargs={
                'document_pk': self.test_document.pk, 'pk': self.test_tag.pk
            }
        )


class TagTestMixin(object):
    def _create_test_tag(self):
        self.test_tag = Tag.objects.create(
            color=TEST_TAG_COLOR, label=TEST_TAG_LABEL
        )

    def _create_test_tag_2(self):
        self.test_tag_2 = Tag.objects.create(
            color=TEST_TAG_COLOR, label=TEST_TAG_LABEL_2
        )


class TagViewTestMixin(object):
    def _request_test_tag_create_view(self):
        return self.post(
            viewname='tags:tag_create', data={
                'label': TEST_TAG_LABEL,
                'color': TEST_TAG_COLOR
            }
        )

    def _request_test_tag_delete_view(self):
        return self.post(
            viewname='tags:tag_delete', kwargs={'pk': self.test_tag.pk}
        )

    def _request_test_tag_delete_multiple_view(self):
        return self.post(
            viewname='tags:tag_multiple_delete',
            data={'id_list': self.test_tag.pk},
        )

    def _request_test_tag_edit_view(self):
        return self.post(
            viewname='tags:tag_edit', kwargs={'pk': self.test_tag.pk}, data={
                'label': TEST_TAG_LABEL_EDITED, 'color': TEST_TAG_COLOR_EDITED
            }
        )

    def _request_test_tag_list_view(self):
        return self.get(viewname='tags:tag_list')

    def _request_test_tag_document_list_view(self):
        return self.get(
            viewname='tags:tag_document_list', kwargs={'pk': self.test_tag.pk}
        )

    def _request_test_document_tag_attach_view(self):
        return self.post(
            viewname='tags:tag_attach', kwargs={'pk': self.test_document.pk},
            data={
                'tags': self.test_tag.pk,
                'user': self._test_case_user.pk
            }
        )

    def _request_test_document_multiple_tag_multiple_attach_view(self):
        return self.post(
            viewname='tags:multiple_documents_tag_attach', data={
                'id_list': self.test_document.pk, 'tags': self.test_tag.pk,
                'user': self._test_case_user.pk
            }
        )

    def _request_test_document_tag_multiple_remove_view(self):
        return self.post(
            viewname='tags:single_document_multiple_tag_remove',
            kwargs={'pk': self.test_document.pk}, data={
                'tags': self.test_tag.pk,
            }
        )

    def _request_test_document_multiple_tag_remove_view(self):
        return self.post(
            viewname='tags:multiple_documents_selection_tag_remove',
            data={
                'id_list': self.test_document.pk,
                'tags': self.test_tag.pk,
            }
        )

    def _request_test_document_tag_list_view(self):
        return self.get(
            viewname='tags:document_tag_list', kwargs={
                'pk': self.test_document.pk
            }
        )

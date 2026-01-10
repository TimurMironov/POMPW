from pathlib import Path


class TestAddAttachments:

    ATTACHMENT_PATH = Path(__file__).parent / "test_image.jpg"

    def test_add_attachments(self, my_info_page, auth_via_cookie):
        my_info_page.open_page()
        my_info_page.is_opened()
        my_info_page.add_attachment(self.ATTACHMENT_PATH)
        my_info_page.save_attachments_click()
        my_info_page.check_save_attachments()


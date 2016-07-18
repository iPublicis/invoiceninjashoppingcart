from invoiceninja import invoiceNinja
import data
from mock import patch, Mock


class TestInvoiceNinja(object):

    """Class for testing the invoice ninja module."""

    @patch('invoiceninja.invoiceNinja.get_static_data', return_value=data.static)
    def test_invoice_ninja_setup(self, mock_data):
        """Test invoice ninja setup works."""
        iv = invoiceNinja(token='token')

        err_msg = "invoice ninja should have been created with static data."
        assert iv.static == data.static, err_msg
import os
from dana_python.api_client import ApiClient
from dana_python.v1.payment_gateway import PaymentGatewayApi
from dana_python.v1.payment_gateway.models import PaymentInfo, ConsultPayRequest
from dana_python.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana_python.rest import ApiException
from tests.fixtures.payment_gateway import consult_pay_request

class TestPaymentGatewayApi:
    
    @classmethod
    def setup_class(cls):
        cls.config = SnapConfiguration(api_key=AuthSettings(
             PRIVATE_KEY=os.environ.get("PRIVATE_KEY"),
             ORIGIN=os.environ.get("ORIGIN"),
             X_PARTNER_ID=os.environ.get("X_PARTNER_ID"),
             CHANNEL_ID=os.environ.get("CHANNEL_ID"),
             ENV=Env.SANDBOX
            ),
        )

    def test_consult_pay_with_str_private_key_success(self, consult_pay_request: ConsultPayRequest):
        """Should give success response code and message and correct mandatory fields"""
        
        with ApiClient(self.config) as api_client:
            api_instance = PaymentGatewayApi(api_client)
            api_response = api_instance.consult_pay(consult_pay_request)

        print(api_response)

        assert api_response.response_code == '2005700'
        assert api_response.response_message == 'Successful'

        assert all(isinstance(i, PaymentInfo) for i in api_response.payment_infos)
        assert all(hasattr(i, "pay_method") for i in api_response.payment_infos)

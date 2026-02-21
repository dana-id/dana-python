# Copyright 2025 PT Espay Debit Indonesia Koe
#
# SnapHeader / PEM and debug mode tests (same scenarios as Go, PHP, Node SDKs).
# Covers convert_to_pem CRLF normalization and X-Debug-Mode header behavior.

import os

from dana.utils.snap_header import SnapHeader, X_DEBUG

# Minimal valid 512-bit RSA PEM for tests that need a real key (e.g. get_snap_header).
VALID_TEST_PRIVATE_KEY = """-----BEGIN PRIVATE KEY-----
MIIBVAIBADANBgkqhkiG9w0BAQEFAASCAT4wggE6AgEAAkEA1l/prH9SjNVSRH1W
kPhIhdu76TiUFD7O4FSq+RTr6XgIcBESyaXQUOO+68ZFinCbNzQ6/6MKPAn3C13z
JUfAwQIDAQABAkAl95C0K0ycgr9yP9yQClkV1Afg01Nujn0nP/eT67+odnWZTsb3
OvtXwGjIdyT1cm76xF8bh3fZjpFILL3yCxZRAiEA/IHmO7C5meVZ5wXlzlKrjGzl
JSccEL3NCRlMbfTv+AUCIQDZVv1VWADHIhOXWAQ1ZAbcySHaGWb8SyuCUdVk1oJu
jQIhAI/YGCYs2K543ywiSfWtVpiaeDcf/nbzCNiEFuwUupdZAiBRokL1U2C3ay1A
o2axRyjstP9qFDCCgxmMkYA9p/TF4QIgb8RAqS7FDRrVXvBYXz0V/kCjv+9txP/4
NoTxiitW66g=
-----END PRIVATE KEY-----"""


class TestConvertToPem:
    """convert_to_pem CRLF and format normalization (same scenarios as Go/PHP/Node)."""

    def test_already_pem_with_lf(self):
        pem = "-----BEGIN PRIVATE KEY-----\nMIIE\n-----END PRIVATE KEY-----"
        converted = SnapHeader.convert_to_pem(pem, "PRIVATE")
        assert "-----BEGIN PRIVATE KEY-----" in converted
        assert "-----END PRIVATE KEY-----" in converted
        assert "MIIE" in converted
        assert "\r" not in converted

    def test_normalizes_windows_crlf(self):
        pem = "-----BEGIN PRIVATE KEY-----\r\nMIIE\r\n-----END PRIVATE KEY-----"
        converted = SnapHeader.convert_to_pem(pem, "PRIVATE")
        assert "-----BEGIN PRIVATE KEY-----" in converted
        assert "-----END PRIVATE KEY-----" in converted
        assert "MIIE" in converted
        assert "\r" not in converted

    def test_handles_escaped_newlines(self):
        pem = "-----BEGIN PRIVATE KEY-----\\nMIIE\\n-----END PRIVATE KEY-----"
        converted = SnapHeader.convert_to_pem(pem, "PRIVATE")
        assert "-----BEGIN PRIVATE KEY-----" in converted
        assert "-----END PRIVATE KEY-----" in converted
        assert "MIIE" in converted
        assert "\n" in converted
        assert "\\n" not in converted

    def test_raw_base64_with_crlf(self):
        raw = "MIIEuwIBADA\r\nNBgkqhkiG9w"
        converted = SnapHeader.convert_to_pem(raw, "PRIVATE")
        has_header = (
            "-----BEGIN PRIVATE KEY-----" in converted
            or "-----BEGIN RSA PRIVATE KEY-----" in converted
        )
        has_footer = (
            "-----END PRIVATE KEY-----" in converted
            or "-----END RSA PRIVATE KEY-----" in converted
        )
        assert has_header
        assert has_footer
        assert "MIIEuwIBADANBgkqhkiG9w" in converted
        assert "\r" not in converted


class TestSnapHeaderDebugMode:
    """X-Debug-Mode behavior: default on in sandbox, off when X_DEBUG=false, never in production."""

    def test_enables_debug_in_sandbox_by_default(self):
        # Unset X_DEBUG so sandbox default applies
        env_prev = os.environ.pop("X_DEBUG", None)
        env_prev_dana = os.environ.pop("DANA_ENV", None)
        os.environ["ENV"] = "sandbox"
        try:
            result = SnapHeader.get_snap_generated_auth(
                "POST",
                "/v1/test",
                "{}",
                private_key=VALID_TEST_PRIVATE_KEY,
                support_debug_mode=True,
            )
            assert X_DEBUG in result
            assert result[X_DEBUG]["value"] == 1
        finally:
            if env_prev is not None:
                os.environ["X_DEBUG"] = env_prev
            if env_prev_dana is not None:
                os.environ["DANA_ENV"] = env_prev_dana
            os.environ.pop("ENV", None)

    def test_disables_debug_when_x_debug_false(self):
        env_prev = os.environ.get("X_DEBUG")
        env_prev_dana = os.environ.pop("DANA_ENV", None)
        os.environ["X_DEBUG"] = "false"
        os.environ["ENV"] = "sandbox"
        try:
            result = SnapHeader.get_snap_generated_auth(
                "POST",
                "/v1/test",
                "{}",
                private_key=VALID_TEST_PRIVATE_KEY,
                support_debug_mode=True,
            )
            assert X_DEBUG in result
            assert result[X_DEBUG]["value"] != 1
        finally:
            if env_prev is not None:
                os.environ["X_DEBUG"] = env_prev
            else:
                os.environ.pop("X_DEBUG", None)
            if env_prev_dana is not None:
                os.environ["DANA_ENV"] = env_prev_dana
            os.environ.pop("ENV", None)

    def test_never_enables_debug_in_production(self):
        env_prev = os.environ.pop("X_DEBUG", None)
        env_prev_dana = os.environ.pop("DANA_ENV", None)
        env_prev_env = os.environ.pop("ENV", None)
        os.environ["ENV"] = "production"
        try:
            result = SnapHeader.get_snap_generated_auth(
                "POST",
                "/v1/test",
                "{}",
                private_key=VALID_TEST_PRIVATE_KEY,
                support_debug_mode=True,
            )
            assert X_DEBUG in result
            assert result[X_DEBUG]["value"] != 1
        finally:
            if env_prev is not None:
                os.environ["X_DEBUG"] = env_prev
            if env_prev_dana is not None:
                os.environ["DANA_ENV"] = env_prev_dana
            if env_prev_env is not None:
                os.environ["ENV"] = env_prev_env
            else:
                os.environ.pop("ENV", None)

# Copyright 2026 PT Espay Debit Indonesia Koe
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
from typing import Any, Callable, Tuple

from dana.exceptions import ApiException

CUSTOMER_NUMBERS = ("62811742234", "62817345544", "62817345545")


def is_forbidden_response_code(code: str | None) -> bool:
    return bool(code and (str(code).startswith("403") or str(code).startswith("404")))


def is_forbidden_api_exception(exc: ApiException) -> bool:
    if exc.status in (403, 404):
        return True
    body = exc.body
    if not body:
        return False
    try:
        parsed = json.loads(body) if isinstance(body, (str, bytes)) else body
        if isinstance(parsed, dict):
            code = parsed.get("responseCode") or parsed.get("response_code")
            return is_forbidden_response_code(code)
    except (json.JSONDecodeError, TypeError):
        pass
    body_str = str(body)
    return "403" in body_str or "404" in body_str


def response_code_from_model(response: Any) -> str | None:
    return getattr(response, "response_code", None)


def with_customer_number_retry(
    operation: Callable[[str], Any],
) -> Tuple[Any, str]:
    last_exc: Exception | None = None
    for customer_number in CUSTOMER_NUMBERS:
        try:
            result = operation(customer_number)
            code = response_code_from_model(result)
            if is_forbidden_response_code(code):
                last_exc = ApiException(status=403, reason=f"responseCode={code}")
                continue
            return result, customer_number
        except ApiException as exc:
            if is_forbidden_api_exception(exc):
                last_exc = exc
                continue
            raise
    if last_exc:
        raise last_exc
    raise RuntimeError(f"All customer numbers returned 403/404: {CUSTOMER_NUMBERS}")

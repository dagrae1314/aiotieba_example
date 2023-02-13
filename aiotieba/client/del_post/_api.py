import sys

import yarl

from .._core import HttpCore
from .._helper import log_exception, log_success, pack_form_request, parse_json, send_request
from ..const import APP_BASE_HOST, APP_SECURE_SCHEME
from ..exception import TiebaServerError


def parse_body(body: bytes) -> None:
    res_json = parse_json(body)
    if code := int(res_json['error_code']):
        raise TiebaServerError(code, res_json['error_msg'])


async def request(http_core: HttpCore, fid: int, pid: int) -> bool:
    data = [
        ('BDUSS', http_core.core._BDUSS),
        ('fid', fid),
        ('pid', pid),
        ('tbs', http_core.core._tbs),
        ('z', '6'),
    ]

    request = pack_form_request(
        http_core,
        yarl.URL.build(scheme=APP_SECURE_SCHEME, host=APP_BASE_HOST, path="/c/c/bawu/delpost"),
        data,
    )

    log_str = f"fid={fid} pid={pid}"
    frame = sys._getframe(1)

    try:
        body = await send_request(request, http_core.connector, read_bufsize=1024)
        parse_body(body)

    except Exception as err:
        log_exception(frame, err, log_str)
        return False

    log_success(frame, log_str)
    return True

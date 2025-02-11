"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_sym_db = _symbol_database.Default()


from . import Agree_pb2 as Agree__pb2
from . import Media_pb2 as Media__pb2
from . import PbContent_pb2 as PbContent__pb2
from . import PollInfo_pb2 as PollInfo__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x12PostInfoList.proto\x1a\x0bMedia.proto\x1a\x0ePollInfo.proto\x1a\x0fPbContent.proto\x1a\x0b\x41gree.proto\"\xc2\x04\n\x0cPostInfoList\x12\x10\n\x08\x66orum_id\x18\x01 \x01(\x04\x12\x11\n\tthread_id\x18\x02 \x01(\x04\x12\x0f\n\x07post_id\x18\x03 \x01(\x04\x12\x13\n\x0b\x63reate_time\x18\x05 \x01(\r\x12\x12\n\nforum_name\x18\x06 \x01(\t\x12\r\n\x05title\x18\x07 \x01(\t\x12.\n\x07\x63ontent\x18\x08 \x03(\x0b\x32\x1d.PostInfoList.PostInfoContent\x12\x11\n\tuser_name\x18\n \x01(\t\x12\x15\n\x05media\x18\x10 \x03(\x0b\x32\x06.Media\x12\x11\n\treply_num\x18\x11 \x01(\r\x12\x0f\n\x07user_id\x18\x12 \x01(\x03\x12\x15\n\ruser_portrait\x18\x13 \x01(\t\x12\x13\n\x0bthread_type\x18\x1a \x01(\x04\x12\x1c\n\tpoll_info\x18\x1c \x01(\x0b\x32\t.PollInfo\x12\x10\n\x08\x66req_num\x18! \x01(\x05\x12\x11\n\tname_show\x18# \x01(\t\x12\x11\n\tshare_num\x18\' \x01(\x05\x12\x15\n\x05\x61gree\x18( \x01(\x0b\x32\x06.Agree\x12\x17\n\x0fis_share_thread\x18, \x01(\x05\x12&\n\x12\x66irst_post_content\x18\x31 \x03(\x0b\x32\n.PbContent\x1al\n\x0fPostInfoContent\x12 \n\x0cpost_content\x18\x01 \x03(\x0b\x32\n.PbContent\x12\x13\n\x0b\x63reate_time\x18\x02 \x01(\x04\x12\x11\n\tpost_type\x18\x03 \x01(\x04\x12\x0f\n\x07post_id\x18\x04 \x01(\x04\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PostInfoList_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS is False:
    DESCRIPTOR._options = None
    _globals['_POSTINFOLIST']._serialized_start = 82
    _globals['_POSTINFOLIST']._serialized_end = 660
    _globals['_POSTINFOLIST_POSTINFOCONTENT']._serialized_start = 552
    _globals['_POSTINFOLIST_POSTINFOCONTENT']._serialized_end = 660

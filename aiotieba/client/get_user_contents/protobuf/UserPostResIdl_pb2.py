# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: UserPostResIdl.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...common.protobuf import Error_pb2 as Error__pb2
from ...common.protobuf import PbContent_pb2 as PbContent__pb2
from ...common.protobuf import PollInfo_pb2 as PollInfo__pb2
from ...common.protobuf import Agree_pb2 as Agree__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14UserPostResIdl.proto\x1a\x0b\x45rror.proto\x1a\x0fPbContent.proto\x1a\x0ePollInfo.proto\x1a\x0b\x41gree.proto\"\xb0\x05\n\x0eUserPostResIdl\x12\x15\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x06.Error\x12%\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x17.UserPostResIdl.DataRes\x1a\xdf\x04\n\x07\x44\x61taRes\x12\x37\n\tpost_list\x18\x01 \x03(\x0b\x32$.UserPostResIdl.DataRes.PostInfoList\x1a\x9a\x04\n\x0cPostInfoList\x12\x10\n\x08\x66orum_id\x18\x01 \x01(\x04\x12\x11\n\tthread_id\x18\x02 \x01(\x04\x12\x0f\n\x07post_id\x18\x03 \x01(\x04\x12\x13\n\x0b\x63reate_time\x18\x05 \x01(\r\x12\x12\n\nforum_name\x18\x06 \x01(\t\x12\r\n\x05title\x18\x07 \x01(\t\x12\x45\n\x07\x63ontent\x18\x08 \x03(\x0b\x32\x34.UserPostResIdl.DataRes.PostInfoList.PostInfoContent\x12\x11\n\tuser_name\x18\n \x01(\t\x12\x11\n\treply_num\x18\x11 \x01(\r\x12\x0f\n\x07user_id\x18\x12 \x01(\x03\x12\x15\n\ruser_portrait\x18\x13 \x01(\t\x12\x1c\n\tpoll_info\x18\x1c \x01(\x0b\x32\t.PollInfo\x12\x10\n\x08\x66req_num\x18! \x01(\x05\x12\x11\n\tname_show\x18# \x01(\t\x12\x11\n\tshare_num\x18\' \x01(\x05\x12\x15\n\x05\x61gree\x18( \x01(\x0b\x32\x06.Agree\x12\x17\n\x0fis_share_thread\x18, \x01(\x05\x12&\n\x12\x66irst_post_content\x18\x31 \x03(\x0b\x32\n.PbContent\x1aY\n\x0fPostInfoContent\x12 \n\x0cpost_content\x18\x01 \x03(\x0b\x32\n.PbContent\x12\x13\n\x0b\x63reate_time\x18\x02 \x01(\x04\x12\x0f\n\x07post_id\x18\x04 \x01(\x04\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'UserPostResIdl_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _USERPOSTRESIDL._serialized_start=84
  _USERPOSTRESIDL._serialized_end=772
  _USERPOSTRESIDL_DATARES._serialized_start=165
  _USERPOSTRESIDL_DATARES._serialized_end=772
  _USERPOSTRESIDL_DATARES_POSTINFOLIST._serialized_start=234
  _USERPOSTRESIDL_DATARES_POSTINFOLIST._serialized_end=772
  _USERPOSTRESIDL_DATARES_POSTINFOLIST_POSTINFOCONTENT._serialized_start=683
  _USERPOSTRESIDL_DATARES_POSTINFOLIST_POSTINFOCONTENT._serialized_end=772
# @@protoc_insertion_point(module_scope)

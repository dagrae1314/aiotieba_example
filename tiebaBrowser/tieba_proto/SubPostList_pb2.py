# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SubPostList.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import PbContent_pb2 as PbContent__pb2
from . import User_pb2 as User__pb2
from . import Agree_pb2 as Agree__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11SubPostList.proto\x1a\x0fPbContent.proto\x1a\nUser.proto\x1a\x0b\x41gree.proto\"\x90\x01\n\x0bSubPostList\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x1b\n\x07\x63ontent\x18\x02 \x03(\x0b\x32\n.PbContent\x12\x0c\n\x04time\x18\x03 \x01(\r\x12\r\n\x05title\x18\x05 \x01(\t\x12\r\n\x05\x66loor\x18\x06 \x01(\r\x12\x15\n\x06\x61uthor\x18\x07 \x01(\x0b\x32\x05.User\x12\x15\n\x05\x61gree\x18\t \x01(\x0b\x32\x06.Agreeb\x06proto3')



_SUBPOSTLIST = DESCRIPTOR.message_types_by_name['SubPostList']
SubPostList = _reflection.GeneratedProtocolMessageType('SubPostList', (_message.Message,), {
  'DESCRIPTOR' : _SUBPOSTLIST,
  '__module__' : 'SubPostList_pb2'
  # @@protoc_insertion_point(class_scope:SubPostList)
  })
_sym_db.RegisterMessage(SubPostList)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SUBPOSTLIST._serialized_start=64
  _SUBPOSTLIST._serialized_end=208
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GetUserByTiebaUidResIdl.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import User_pb2 as User__pb2
from . import Error_pb2 as Error__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dGetUserByTiebaUidResIdl.proto\x1a\nUser.proto\x1a\x0b\x45rror.proto\"\x80\x01\n\x17GetUserByTiebaUidResIdl\x12\x15\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x06.Error\x12.\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32 .GetUserByTiebaUidResIdl.DataRes\x1a\x1e\n\x07\x44\x61taRes\x12\x13\n\x04user\x18\x01 \x01(\x0b\x32\x05.Userb\x06proto3')



_GETUSERBYTIEBAUIDRESIDL = DESCRIPTOR.message_types_by_name['GetUserByTiebaUidResIdl']
_GETUSERBYTIEBAUIDRESIDL_DATARES = _GETUSERBYTIEBAUIDRESIDL.nested_types_by_name['DataRes']
GetUserByTiebaUidResIdl = _reflection.GeneratedProtocolMessageType('GetUserByTiebaUidResIdl', (_message.Message,), {

  'DataRes' : _reflection.GeneratedProtocolMessageType('DataRes', (_message.Message,), {
    'DESCRIPTOR' : _GETUSERBYTIEBAUIDRESIDL_DATARES,
    '__module__' : 'GetUserByTiebaUidResIdl_pb2'
    # @@protoc_insertion_point(class_scope:GetUserByTiebaUidResIdl.DataRes)
    })
  ,
  'DESCRIPTOR' : _GETUSERBYTIEBAUIDRESIDL,
  '__module__' : 'GetUserByTiebaUidResIdl_pb2'
  # @@protoc_insertion_point(class_scope:GetUserByTiebaUidResIdl)
  })
_sym_db.RegisterMessage(GetUserByTiebaUidResIdl)
_sym_db.RegisterMessage(GetUserByTiebaUidResIdl.DataRes)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETUSERBYTIEBAUIDRESIDL._serialized_start=59
  _GETUSERBYTIEBAUIDRESIDL._serialized_end=187
  _GETUSERBYTIEBAUIDRESIDL_DATARES._serialized_start=157
  _GETUSERBYTIEBAUIDRESIDL_DATARES._serialized_end=187
# @@protoc_insertion_point(module_scope)

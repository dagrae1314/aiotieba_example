# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PbContent.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fPbContent.proto\"\xd2\x04\n\tPbContent\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x0c\n\x04link\x18\x03 \x01(\t\x12\x0b\n\x03src\x18\x04 \x01(\t\x12\r\n\x05\x62size\x18\x05 \x01(\t\x12\x0f\n\x07\x62ig_src\x18\x06 \x01(\t\x12\x10\n\x08\x62ig_size\x18\x07 \x01(\t\x12\x0f\n\x07\x63\x64n_src\x18\x08 \x01(\t\x12\x13\n\x0b\x62ig_cdn_src\x18\t \x01(\t\x12\x0f\n\x07imgtype\x18\n \x01(\t\x12\x11\n\tvoice_md5\x18\x0c \x01(\t\x12\x0b\n\x03uid\x18\x0f \x01(\x03\x12\r\n\x05width\x18\x12 \x01(\r\x12\x0e\n\x06height\x18\x13 \x01(\r\x12\x13\n\x0bpacket_name\x18\x14 \x01(\t\x12\x11\n\tphonetype\x18\x15 \x01(\t\x12\x0e\n\x06\x65_type\x18\x18 \x01(\r\x12\x12\n\norigin_src\x18\x19 \x01(\t\x12\x13\n\x0borigin_size\x18\x1b \x01(\r\x12\x30\n\x0etiebaplus_info\x18( \x01(\x0b\x32\x18.PbContent.TiebaPlusInfo\x1a\xd2\x01\n\rTiebaPlusInfo\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\t\x12\x10\n\x08jump_url\x18\x03 \x01(\t\x12\x10\n\x08\x61pp_icon\x18\x06 \x01(\t\x12\x13\n\x0btarget_type\x18\x0c \x01(\x05\x12\x14\n\x0ch5_jump_type\x18\r \x01(\x05\x12\x16\n\x0eh5_jump_number\x18\x0e \x01(\t\x12\x15\n\rh5_jump_param\x18\x0f \x01(\t\x12\x11\n\tjump_type\x18\x10 \x01(\x05\x12\x13\n\x0b\x62utton_desc\x18\x17 \x01(\tb\x06proto3')



_PBCONTENT = DESCRIPTOR.message_types_by_name['PbContent']
_PBCONTENT_TIEBAPLUSINFO = _PBCONTENT.nested_types_by_name['TiebaPlusInfo']
PbContent = _reflection.GeneratedProtocolMessageType('PbContent', (_message.Message,), {

  'TiebaPlusInfo' : _reflection.GeneratedProtocolMessageType('TiebaPlusInfo', (_message.Message,), {
    'DESCRIPTOR' : _PBCONTENT_TIEBAPLUSINFO,
    '__module__' : 'PbContent_pb2'
    # @@protoc_insertion_point(class_scope:PbContent.TiebaPlusInfo)
    })
  ,
  'DESCRIPTOR' : _PBCONTENT,
  '__module__' : 'PbContent_pb2'
  # @@protoc_insertion_point(class_scope:PbContent)
  })
_sym_db.RegisterMessage(PbContent)
_sym_db.RegisterMessage(PbContent.TiebaPlusInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PBCONTENT._serialized_start=20
  _PBCONTENT._serialized_end=614
  _PBCONTENT_TIEBAPLUSINFO._serialized_start=404
  _PBCONTENT_TIEBAPLUSINFO._serialized_end=614
# @@protoc_insertion_point(module_scope)
